import json
import os
import re
import sys
from pathlib import Path


def fix_latex_for_github(content):
    # Step 1: Convert inline math $ ... $ containing \begin{}\end{} to display math
    # and merge adjacent inline math blocks that should be combined
    result_parts = []
    remaining = content
    
    while True:
        # Find next $
        dollar_pos = remaining.find('$')
        if dollar_pos == -1:
            result_parts.append(remaining)
            break
        
        # Check if it's $$
        if remaining[dollar_pos:dollar_pos+2] == '$$':
            # It's display math, find the closing $$
            closing_pos = remaining.find('$$', dollar_pos + 2)
            if closing_pos == -1:
                result_parts.append(remaining)
                break
            
            # Add everything up to opening $$
            result_parts.append(remaining[:dollar_pos + 2])
            remaining = remaining[dollar_pos + 2:]
            continue
        
        # It's a single $, find the closing $
        closing_pos = dollar_pos + 1
        found_closing = False
        
        while closing_pos < len(remaining):
            if remaining[closing_pos] == '$':
                if closing_pos > 0 and remaining[closing_pos - 1] != '\\':
                    if closing_pos + 1 >= len(remaining) or remaining[closing_pos + 1] != '$':
                        found_closing = True
                        break
            closing_pos += 1
        
        if not found_closing:
            result_parts.append(remaining)
            break
        
        # Extract the inline math content
        inline_content = remaining[dollar_pos + 1:closing_pos]
        
        # Add the part before the $
        result_parts.append(remaining[:dollar_pos])
        
        # Check if it contains \begin{...}\end{...}
        if '\\begin{' in inline_content and '\\end{' in inline_content:
            # Convert to display math, keeping matrix row structure
            clean_content = inline_content.strip()
            # Remove blank lines within the math
            clean_content = re.sub(r'\n\s*\n', '\n', clean_content)
            # Keep newlines after \\ (matrix row breaks), but normalize spacing
            # Replace \\\n with \\\n (keep it)
            # Replace other newlines (not after \\) with spaces
            lines = clean_content.split('\n')
            processed_lines = []
            for i,line in enumerate(lines):
                line = line.strip()
                if line:
                    if i < len(lines) - 1 and line.endswith('\\\\'):
                        # This line ends with \\, keep the newline
                        processed_lines.append(line)
                    elif i == 0 or (i > 0 and not processed_lines[-1].endswith('\\\\')):
                        # Continuation of previous line, append with space
                        if processed_lines:
                            processed_lines[-1] += ' ' + line
                        else:
                            processed_lines.append(line)
                    else:
                        # New content after \\
                        processed_lines.append(line)
            
            clean_content = '\n'.join(processed_lines)
            # Clean up extra spaces
            clean_content = re.sub(r' +', ' ', clean_content)
            
            # Check if next character after closing $ is another inline math $ (adjacent math blocks)
            next_char_pos = closing_pos + 1
            # Skip whitespace
            while next_char_pos < len(remaining) and remaining[next_char_pos] in ' \t':
                next_char_pos += 1
            
            # If next char is $, it might be adjacent inline math to merge
            if next_char_pos < len(remaining) and remaining[next_char_pos] == '$':
                # Peek ahead to see if it's also inline math with matrices
                next_dollar = next_char_pos
                if remaining[next_dollar:next_dollar+2] != '$$':  # Not already display math
                    # Find the closing $
                    next_closing = next_dollar + 1
                    found_next = False
                    while next_closing < len(remaining):
                        if remaining[next_closing] == '$':
                            if remaining[next_closing - 1] != '\\':
                                if next_closing + 1 >= len(remaining) or remaining[next_closing + 1] != '$':
                                    found_next = True
                                    break
                        next_closing += 1
                    
                    if found_next:
                        next_content = remaining[next_dollar + 1:next_closing]
                        # If it also has matrices, merge them
                        if '\\begin{' in next_content and '\\end{' in next_content:
                            clean_next = next_content.strip()
                            # Process preserving matrix structure
                            clean_next = re.sub(r'\n\s*\n', '\n', clean_next)
                            lines = clean_next.split('\n')
                            processed = []
                            for i, line in enumerate(lines):
                                line = line.strip()
                                if line:
                                    if i < len(lines) - 1 and line.endswith('\\\\'):
                                        processed.append(line)
                                    elif i == 0 or (i > 0 and not processed[-1].endswith('\\\\')):
                                        if processed:
                                            processed[-1] += ' ' + line
                                        else:
                                            processed.append(line)
                                    else:
                                        processed.append(line)
                            clean_next = '\n'.join(processed)
                            clean_next = re.sub(r' +', ' ', clean_next)
                            # Merge with a space
                            clean_content = clean_content + ' ' + clean_next
                            # Skip past the second math block
                            remaining = remaining[next_closing + 1:]
                            result_parts.append(f'$${clean_content}$$')
                            continue
            
            result_parts.append(f'$${clean_content}$$')
        else:
            # Keep as inline math, collapse newlines
            clean_content = inline_content.replace('\n', ' ').strip()
            clean_content = re.sub(r'\s+', ' ', clean_content)
            result_parts.append(f'${clean_content}$')
        
        remaining = remaining[closing_pos + 1:]
    
    content = ''.join(result_parts)
    
    # Step 2: Collapse existing display math blocks while preserving matrix structure
    # This handles $$\n content \n$$ patterns from the original notebook
    def collapse_display_math(match):
        math_content = match.group(1)
        # Strip whitespace
        math_content = math_content.strip()
        # Remove blank lines
        math_content = re.sub(r'\n\s*\n', '\n', math_content)
        # Preserve newlines after \\ (matrix row breaks)
        lines = math_content.split('\n')
        processed_lines = []
        for i, line in enumerate(lines):
            line = line.strip()
            if line:
                if i < len(lines) - 1 and line.endswith('\\\\'):
                    # Line ends with \\, keep newline
                    processed_lines.append(line)
                elif i == 0 or (i > 0 and not processed_lines[-1].endswith('\\\\')):
                    # Continuation line, append to previous
                    if processed_lines:
                        processed_lines[-1] += ' ' + line
                    else:
                        processed_lines.append(line)
                else:
                    # New line after \\
                    processed_lines.append(line)
        math_content = '\n'.join(processed_lines)
        # Clean up multiple spaces
        math_content = re.sub(r' +', ' ', math_content)
        return f'$${math_content}$$'
    
    # Match $$ ... $$ blocks (including multi-line ones)
    content = re.sub(r'\$\$(.*?)\$\$', collapse_display_math, content, flags=re.DOTALL)
    
    # Step 3: Merge adjacent display math blocks ($$...$$  $$...$$) into one
    # Only merge if both blocks are relatively short (< 80 chars) to avoid creating overly long equations
    # This handles cases like sharpening filter with two matrices, but keeps separate conditions separate
    def merge_if_short(match):
        block1 = match.group(1)[2:-2]  # Remove $$ from both ends
        block2 = match.group(2)[2:-2]
        # Only merge if both blocks are short (e.g., parts of same equation like matrix subtraction)
        if len(block1) < 80 and len(block2) < 80:
            return f'$${block1} {block2}$$'
        else:
            # Keep separate with a line break between
            return f'{match.group(1)}\n\n{match.group(2)}'
    
    content = re.sub(r'(\$\$[^\$]+\$\$)\s+(\$\$[^\$]+\$\$)', merge_if_short, content)
    
    # Step 4: Move display math to their own lines with blank lines before/after
    # Use safer regex patterns that don't cause catastrophic backtracking
    # Ensure blank line before $$ (when preceded by non-newline)
    content = re.sub(r'([^\n])\s*\n?\s*(\$\$)', r'\1\n\n\2', content)
    # Ensure blank line after $$ (when followed by non-newline)
    content = re.sub(r'(\$\$)\s*\n?\s*([^\n\$])', r'\1\n\n\2', content)
    
    # Step 5: Clean up excessive empty lines
    content = re.sub(r'\n\n\n+', r'\n\n', content)
    
    return content


def extract_markdown_from_notebook(notebook_path):
    """Extract all markdown cells from a Jupyter notebook."""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    markdown_cells = []
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'markdown':
            # Join the source lines (they're stored as a list)
            source = cell.get('source', [])
            if isinstance(source, list):
                markdown_content = ''.join(source)
            else:
                markdown_content = source
            
            markdown_content = fix_latex_for_github(markdown_content)
            
            markdown_cells.append(markdown_content)
    
    return markdown_cells


def save_markdown_to_file(markdown_cells, output_path):
    """Save markdown cells to a .md file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        for i, cell_content in enumerate(markdown_cells):
            f.write(cell_content)
            # Add spacing between cells (if not already ending with newline)
            if i < len(markdown_cells) - 1 and not cell_content.endswith('\n'):
                f.write('\n\n')


def process_directory(directory_path, remove_notebooks=True):
    """Process all .ipynb files in the directory.
    
    Args:
        directory_path: Path to the directory containing .ipynb files
        remove_notebooks: If True, delete .ipynb files after successful conversion
    """
    directory = Path(directory_path)
    
    if not directory.exists():
        print(f"Error: Directory '{directory_path}' does not exist")
        return False
    
    if not directory.is_dir():
        print(f"Error: '{directory_path}' is not a directory")
        return False
    
    # Find all .ipynb files
    notebook_files = sorted(directory.glob('*.ipynb'))
    
    if not notebook_files:
        print(f"No .ipynb files found in {directory_path}")
        return False
    
    print(f"Found {len(notebook_files)} notebook(s) to process")
    
    processed_files = []
    
    for notebook_path in notebook_files:
        print(f"\nProcessing: {notebook_path.name}")
        
        try:
            # Extract markdown cells
            markdown_cells = extract_markdown_from_notebook(notebook_path)
            
            if not markdown_cells:
                print(f"No markdown cells found")
                continue
            
            # Create output .md file with same name
            output_path = notebook_path.with_suffix('.md')
            
            # Save markdown content
            save_markdown_to_file(markdown_cells, output_path)
            
            print(f"  ✓ Created {output_path.name} with {len(markdown_cells)} markdown cell(s)")
            processed_files.append(notebook_path)
            
        except Exception as e:
            print(f"  ✗ Error processing {notebook_path.name}: {e}")
    
    # Remove .ipynb files if requested and processing was successful
    if remove_notebooks and processed_files:
        print(f"\n{'='*60}")
        print("Removing processed .ipynb files...")
        for notebook_path in processed_files:
            try:
                notebook_path.unlink()
                print(f"  ✓ Removed {notebook_path.name}")
            except Exception as e:
                print(f"  ✗ Error removing {notebook_path.name}: {e}")
    
    return True


if __name__ == '__main__':
    print("="*60)
    print("Jupyter Notebook Markdown Extractor")
    print("Fixes LaTeX for GitHub Markdown Compatibility")
    print("="*60)
    
    # Check if directory argument is provided
    if len(sys.argv) < 2:
        print("\nUsage: python extract_markdown.py <directory_path>")
        print("\nExample:")
        print("  python extract_markdown.py Fifth-Semester/Computer-Vision")
        print("  python extract_markdown.py ../relative/path/to/notebooks")
        sys.exit(1)
    
    target_directory = sys.argv[1]
    print(f"\nTarget directory: {target_directory}\n")
    
    success = process_directory(target_directory, remove_notebooks=True)
    
    print("\n" + "="*60)
    if success:
        print("Done!")
    else:
        print("Failed!")
    print("="*60)
    
    sys.exit(0 if success else 1)
