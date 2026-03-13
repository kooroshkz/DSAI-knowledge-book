import fs from 'fs';
import path from 'path';

const ROOT_DIR = path.resolve('..');
const PUBLIC_CONTENT_DIR = path.resolve('public', 'content');

if (fs.existsSync(PUBLIC_CONTENT_DIR)) {
  fs.rmSync(PUBLIC_CONTENT_DIR, { recursive: true, force: true });
}
fs.mkdirSync(PUBLIC_CONTENT_DIR, { recursive: true });

function getSemesters() {
  return fs.readdirSync(ROOT_DIR).filter(item => {
    return item.endsWith('-Semester') || item.toLowerCase().endsWith('-semester');
  });
}

const structure = [];

getSemesters().forEach(semester => {
  const semesterPath = path.join(ROOT_DIR, semester);
  if (!fs.statSync(semesterPath).isDirectory()) return;

  const courses = fs.readdirSync(semesterPath).filter(item => {
    return fs.statSync(path.join(semesterPath, item)).isDirectory() && !item.startsWith('.');
  });

  const semesterData = {
    name: semester,
    courses: []
  };

  courses.forEach(course => {
    const coursePath = path.join(semesterPath, course);
    const destCourseDir = path.join(PUBLIC_CONTENT_DIR, semester, course);
    fs.mkdirSync(destCourseDir, { recursive: true });

    const mdFiles = [];

    // Helper to recursively copy directories & collect MD files
    function processDir(currentPath, relativePath = '') {
      const items = fs.readdirSync(currentPath);
      items.forEach(item => {
        if (item.startsWith('.')) return; // Skip dotfiles like .DS_Store
        
        const fullPath = path.join(currentPath, item);
        const rel = relativePath ? path.join(relativePath, item) : item;
        const destPath = path.join(destCourseDir, rel);
        
        if (fs.statSync(fullPath).isDirectory()) {
          if (!fs.existsSync(destPath)) {
            fs.mkdirSync(destPath, { recursive: true });
          }
          processDir(fullPath, rel);
        } else {
          fs.copyFileSync(fullPath, destPath);
          if (item.endsWith('.md')) {
            // Keep standard slashes for web paths
            mdFiles.push(rel.replace(/\\/g, '/'));
          }
        }
      });
    }

    processDir(coursePath);

    if (mdFiles.length > 0) {
      semesterData.courses.push({
        name: course,
        files: mdFiles
      });
    }
  });

  if (semesterData.courses.length > 0) {
    structure.push(semesterData);
  }
});

// Copy the 'Files' directory if it exists
const filesDir = path.join(ROOT_DIR, 'Files');
if (fs.existsSync(filesDir) && fs.statSync(filesDir).isDirectory()) {
  const destFilesDir = path.join(PUBLIC_CONTENT_DIR, 'Files');
  fs.mkdirSync(destFilesDir, { recursive: true });
  
  function copyDirRecursive(src, dest) {
    const items = fs.readdirSync(src);
    items.forEach(item => {
      if (item.startsWith('.')) return;
      const srcPath = path.join(src, item);
      const destPath = path.join(dest, item);
      if (fs.statSync(srcPath).isDirectory()) {
        if (!fs.existsSync(destPath)) {
          fs.mkdirSync(destPath, { recursive: true });
        }
        copyDirRecursive(srcPath, destPath);
      } else {
        fs.copyFileSync(srcPath, destPath);
      }
    });
  }
  
  copyDirRecursive(filesDir, destFilesDir);
}

// Sort semesters based on the specified order
const semesterOrder = {
  "first-semester": 1,
  "second-semester": 2,
  "third-semester": 3,
  "fourth-semester": 4,
  "fifth-semester": 5,
  "sixth-semester": 6
};

structure.sort((a, b) => {
  const aName = a.name.toLowerCase();
  const bName = b.name.toLowerCase();
  const aIdx = semesterOrder[aName] || 99;
  const bIdx = semesterOrder[bName] || 99;
  return aIdx - bIdx;
});

fs.writeFileSync(
  path.join('src', 'content-index.json'), 
  JSON.stringify(structure, null, 2)
);

console.log('Images and nested files copied. Index generated.');
