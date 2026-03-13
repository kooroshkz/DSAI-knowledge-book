import { useState, useEffect } from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import { Book, Moon, Sun } from 'lucide-react';
import contentData from './content-index.json';
import SemesterView from './components/SemesterView';
import CourseView from './components/CourseView';
import HomeView from './components/HomeView';

function App() {
  const [darkMode, setDarkMode] = useState(() => {
    // If not set, check system preference. Otherwise default to false (light cream)
    return localStorage.getItem('theme') === 'dark' || 
      (!localStorage.getItem('theme') && window.matchMedia('(prefers-color-scheme: dark)').matches);
  });

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    } else {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    }
  }, [darkMode]);

  return (
    <div className="min-h-screen flex flex-col font-sans transition-colors duration-200">
      {/* Header */}
      <header className="apple-header sticky top-0 z-50">
        <div className="max-w-screen-2xl mx-auto px-4 h-14 flex items-center justify-between">
          <Link to="/" className="flex items-center gap-2 text-inherit font-medium text-[17px] hover:opacity-80 transition-opacity">
            <Book className="w-5 h-5 apple-accent" />
            <span>Notes</span>
          </Link>
          
          <nav className="flex items-center">
            <button 
              onClick={() => setDarkMode(!darkMode)} 
              className="p-2 rounded-full hover:bg-black/5 dark:hover:bg-white/10 transition-colors"
              aria-label="Toggle dark mode"
            >
              {darkMode ? <Sun className="w-5 h-5 text-[#e8b975]" /> : <Moon className="w-5 h-5 text-[#907038]" />}
            </button>
          </nav>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-grow flex flex-col">
        <Routes>
          <Route path="/" element={<HomeView data={contentData} />} />
          <Route path="/semester/:semesterName" element={<SemesterView data={contentData} />} />
          <Route path="/semester/:semesterName/course/:courseName" element={<CourseView data={contentData} />} />
        </Routes>
      </main>

      {/* Footer */}
      <footer className="py-6 mt-auto">
      </footer>
    </div>
  );
}

export default App;
