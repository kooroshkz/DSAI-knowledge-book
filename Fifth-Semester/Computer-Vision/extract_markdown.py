#!/usr/bin/env python3
"""
Script to extract markdown cells from Jupyter notebooks and save them as .md files.
Fixes LaTeX notation for GitHub markdown compatibility.
"""

import json
import os
import re
from pathlib import Path


def fix_latex_for_github(content):
    """Fix LaTeX notation to be compatible with GitHub markdown preview."""
    
    # Core strategy: Fix malformed inline math that spans multiple lines with LaTeX environments    
    # Convert: $ equation \n \begin{env}...\end{env} \n $ text
    # To: $$equation \begin{env}...\end{env}$$ text
    
    # Step 1: Find all potential inline math spans ($ to $)
    # that contain LaTeX environments or span multiple lines
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
            
            # Add everything including the display math as-is
            result_parts.append(remaining[:closing_pos + 2])
            remaining = remaining[closing_pos + 2:]
            continue
        
        # It's a single $, find the closing $
        closing_pos = dollar_pos + 1
        found_closing = False
        
        # Look for unescaped $ that closes this inline math
        while closing_pos < len(remaining):
            if remaining[closing_pos] == '$':
                # Check if it's escaped
                if closing_pos > 0 and remaining[closing_pos - 1] != '\\':
                    # Check if it's not $$
                    if closing_pos + 1 >= len(remaining) or remaining[closing_pos + 1] != '$':
                        found_closing = True
                        break
            closing_pos += 1
        
        if not found_closing:
            result_parts.append(remaining)
            break
        
        # Extract the inline math content
        inline_content = remaining[dollar_pos + 1:closing_pos]
        
        # Check if it contains \begin{...}\end{...} or spans multiple lines with significant content
        has_environment = '\\begin{' in inline_content and '\\end{' in inline_content
        has_multiple_lines = '\n' in inline_content and len(inline_content.strip().split('\n')) > 2
        
        # Add the part before the $
        result_parts.append(remaining[:dollar_pos])
        
        if has_environment or (has_multiple_lines and any(cmd in inline_content for cmd in ['\\frac', '\\begin', '\\sum', '\\int'])):
            # Convert to display math
            # Clean up the content
            clean_content = inline_content.strip()
            # Remove excessive blank lines
            clean_content = re.sub(r'\n\s*\n', r'\n', clean_content)
            result_parts.append(f'$$\n{clean_content}\n$$')
        else:
            # Keep as inline math but clean it up
            clean_content = inline_content.replace('\n', ' ').strip()
            result_parts.append(f'${clean_content}$')
        
        # Continue with the rest
        remaining = remaining[closing_pos + 1:]
    
    content = ''.join(result_parts)
    
    # Step 1.5: Ensure $$ are on their own lines for proper tracking in Step 2
    # GitHub requires blank lines around display math blocks for proper rendering
    content = re.sub(r'(.*?\S)\s*\$\$(\s|$)', r'\1\n\n$$\2', content)  # blank line before opening $$
    content = re.sub(r'(^|\s)\$\$\s*(\S.*?)', r'\1$$\n\n\2', content, flags=re.MULTILINE)  # blank line after closing $$
    
    # Step 2: Fix standalone \begin{...}\end{...} environments not in math mode
    lines = content.split('\n')
    result = []
    i = 0
    in_display_math = False
    
    while i < len(lines):
        line = lines[i]
        
        # Track if we're entering/exiting display math
        if line.strip() == '$$':
            in_display_math = not in_display_math
            result.append(line)
            i += 1
            continue
        
        # Check if line starts with \begin and contains no $ AND not already in display math
        if not in_display_math and line.strip().startswith('\\begin{') and '$' not in line:
            # Find the corresponding \end{
            env_lines = [line]
            j = i + 1
            
            while j < len(lines):
                env_lines.append(lines[j])
                if '\\end{' in lines[j]:
                    break
                j += 1
            
            # Wrap in display math
            result.append('$$')
            result.extend(env_lines)
            result.append('$$')
            i = j + 1
        else:
            result.append(line)
            i += 1
    
    content = '\n'.join(result)
    
    # Step 3: Ensure $$ are on their own lines (with some exceptions)
    # Split content into lines
    lines = content.split('\n')
    result = []
    
    for line in lines:
        # If line has $$ and other content
        if '$$' in line and line.strip() != '$$':
            # Check if it's opening or closing $$
            parts = line.split('$$')
            if len(parts) ==2:
                # One $$ in the line
                before, after = parts
                if before.strip() and after.strip():
                    # $$ in the middle: "text $$ text"
                    result.append(before.rstrip())
                    result.append('$$')
                    result.append(after.lstrip())
                elif before.strip():
                    # $$ at end: "text $$"
                    result.append(before.rstrip())
                    result.append('$$')
                elif after.strip():
                    # $$ at start: "$$ text"
                    result.append('$$')
                    result.append(after.lstrip())
                else:
                    result.append(line)
            else:
                # Multiple $$ - just add as-is for now
                result.append(line)
        else:
            result.append(line)
    
    content = '\n'.join(result)
    
    # Step 4: Clean up excessive empty lines
    content = re.sub(r'\n\n\n+', r'\n\n', content)
    
    # Step 5: Fix consecutive $$ (like $$ followed by $$)
    content = re.sub(r'\$\$\s*\n\s*\$\$\s*\n', r'', content)
    
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
            
            # Fix LaTeX for GitHub compatibility
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


def process_directory(directory_path):
    """Process all .ipynb files in the directory."""
    directory = Path(directory_path)
    
    # Find all .ipynb files
    notebook_files = sorted(directory.glob('*.ipynb'))
    
    if not notebook_files:
        print(f"No .ipynb files found in {directory_path}")
        return
    
    print(f"Found {len(notebook_files)} notebook(s) to process")
    
    for notebook_path in notebook_files:
        print(f"\nProcessing: {notebook_path.name}")
        
        try:
            # Extract markdown cells
            markdown_cells = extract_markdown_from_notebook(notebook_path)
            
            if not markdown_cells:
                print(f"  ⚠️  No markdown cells found")
                continue
            
            # Create output .md file with same name
            output_path = notebook_path.with_suffix('.md')
            
            # Save markdown content
            save_markdown_to_file(markdown_cells, output_path)
            
            print(f"  ✓ Created {output_path.name} with {len(markdown_cells)} markdown cell(s)")
            
        except Exception as e:
            print(f"  ✗ Error processing {notebook_path.name}: {e}")


if __name__ == '__main__':
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    
    print("=" * 60)
    print("Jupyter Notebook Markdown Extractor")
    print("Fixes LaTeX for GitHub Markdown Compatibility")
    print("=" * 60)
    
    process_directory(script_dir)
    
    print("\n" + "=" * 60)
    print("Done!")
    print("=" * 60)
