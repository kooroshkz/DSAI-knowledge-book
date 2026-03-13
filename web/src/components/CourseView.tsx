import { useState, useEffect } from 'react';
import { Link, useParams, useSearchParams } from 'react-router-dom';
import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import remarkGfm from 'remark-gfm';
import rehypeRaw from 'rehype-raw';
import { ChevronLeft, FileText, Menu, ChevronRight } from 'lucide-react';
import 'katex/dist/katex.min.css';

export default function CourseView({ data }: { data: any[] }) {
  const { semesterName, courseName } = useParams();
  const [searchParams, setSearchParams] = useSearchParams();
  const fileParam = searchParams.get('file');

  const semester = data.find(s => s.name === semesterName);
  const course = semester?.courses.find((c: any) => c.name === courseName);
  
  const files = course?.files || [];
  
  const [activeFile, setActiveFile] = useState<string>(fileParam || files[0] || '');
  const [markdownContent, setMarkdownContent] = useState<string>('');
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (fileParam && files.includes(fileParam)) {
      setActiveFile(fileParam);
    } else if (!fileParam && files.length > 0) {
      setActiveFile(files[0]);
      setSearchParams({ file: files[0] }, { replace: true });
    }
  }, [fileParam, files, setSearchParams]);

  useEffect(() => {
    if (!activeFile || !semesterName || !courseName) return;
    
    setLoading(true);
    
    const baseUrl = import.meta.env.BASE_URL || '/';
    const normalizedBaseUrl = baseUrl.endsWith('/') ? baseUrl : `${baseUrl}/`;
    
    // We let the browser handle implicit encoding of URL parts as fetch allows it, 
    // but encodeURIComponent works fine generally. If there's a comma in activeFile, 
    // it was giving a Vite SPA fallback.
    // replacing encodeURIComponent to native strings for activeFile usually solves static path 
    // resolution issues in dev mode for files containing commas.
    // Actually we just encode the segments and join them.
    const semesterEncoded = encodeURIComponent(semesterName);
    const courseEncoded = encodeURIComponent(courseName);
    
    // the file might have characters like space or comma.
    // we should encode it, but if encodeURIComponent(activeFile) fails the Vite serving, 
    // it's often due to Vite decoding issues with %2C. Let's send the path segments straight.
    let fileEncoded = encodeURIComponent(activeFile).replace(/%2C/g, ',');
    
    const fetchPath = `${normalizedBaseUrl}content/${semesterEncoded}/${courseEncoded}/${fileEncoded}`;

    fetch(fetchPath)
      .then(res => res.text())
      .then(text => {
        // If it starts with doctype, Vite couldn't find the file and returned the index.html
        if (text.trim().toLowerCase().startsWith('<!doctype html>')) {
          setMarkdownContent(`## Error\nCould not load content for **${activeFile}**. File not found.`);
        } else {
          setMarkdownContent(text);
        }
        setLoading(false);
      })
      .catch(() => {
        setMarkdownContent(`## Error\nCould not load content for ${activeFile}. It might have been moved or deleted.`);
        setLoading(false);
      });
      
    window.scrollTo(0, 0);
  }, [activeFile, semesterName, courseName]);

  const handleFileClick = (file: string) => {
    setActiveFile(file);
    setSearchParams({ file });
    setSidebarOpen(false);
  };

  if (!course) {
    return (
      <div className="text-center py-20">
        <h2 className="text-xl font-medium mb-4">Course not found</h2>
        <Link to={`/semester/${semesterName}`} className="apple-accent hover:underline">
          Back to Semester
        </Link>
      </div>
    );
  }

  const courseDisplayName = course.name.replace(/-/g, ' ');

  return (
    <div className="flex-grow flex w-full max-w-full relative h-[calc(100vh-56px)] overflow-hidden">
      {/* Mobile sidebar toggle overlay */}
      {sidebarOpen && (
        <div 
          className="fixed inset-0 bg-black/20 z-40 lg:hidden backdrop-blur-sm"
          onClick={() => setSidebarOpen(false)}
        />
      )}

      {/* Sidebar */}
      <aside className={`
        apple-sidebar absolute inset-y-0 left-0 z-50 w-72 transform transition-transform duration-200 ease-in-out lg:relative lg:translate-x-0
        ${sidebarOpen ? 'translate-x-0' : '-translate-x-full lg:translate-x-0'}
      `}>
        <div className="h-full flex flex-col pt-6 pb-6 overflow-y-auto">
          <div className="px-6 mb-6">
            <Link 
              to={`/semester/${semesterName}`}
              className="inline-flex items-center gap-1 text-[14px] opacity-60 hover:opacity-100 transition-opacity mb-2"
            >
              <ChevronLeft className="w-4 h-4 ml-[-4px]" /> Semester
            </Link>
            <h2 className="font-semibold text-lg leading-tight tracking-tight mt-2">
              {courseDisplayName}
            </h2>
          </div>
          
          <div className="flex-grow px-3">
            <div className="space-y-0.5">
              {files.map((file: string) => (
                <button
                  key={file}
                  onClick={() => handleFileClick(file)}
                  className={`w-full text-left px-3 py-2 rounded-lg text-[15px] transition-colors flex items-start gap-2.5
                    ${activeFile === file 
                      ? 'apple-active-item font-medium' 
                      : 'hover:bg-black/5 dark:hover:bg-white/5 opacity-80 hover:opacity-100'
                    }
                  `}
                >
                  <FileText className="w-4 h-4 mt-0.5 shrink-0" />
                  <span className="truncate">{file.replace('.md', '')}</span>
                </button>
              ))}
              {files.length === 0 && (
                <div className="px-3 py-2 text-sm opacity-50 italic">
                  No notes available.
                </div>
              )}
            </div>
          </div>
        </div>
      </aside>

      {/* Main Content Area */}
      <div className="flex-grow flex flex-col min-w-0 bg-transparent overflow-y-auto h-full relative">
        <div className="flex items-center border-b border-[#e6e4dd] dark:border-[#2a2a2a] px-4 py-3 lg:hidden bg-[#fdfbf7]/90 dark:bg-[#1e1e1e]/90 backdrop-blur sticky top-0 z-30">
          <button 
            onClick={() => setSidebarOpen(true)}
            className="p-1.5 -ml-1.5 opacity-70 hover:opacity-100 rounded-md"
          >
            <Menu className="w-5 h-5" />
          </button>
          <div className="ml-2 flex items-center text-sm opacity-60 truncate">
            <span className="truncate">{courseDisplayName}</span>
            <ChevronRight className="w-4 h-4 mx-1 flex-shrink-0" />
            <span className="font-medium opacity-100 text-inherit truncate">
              {activeFile.replace('.md', '')}
            </span>
          </div>
        </div>

        <div className="flex-grow p-6 lg:p-12 w-full mx-auto pb-32">
          {loading ? (
            <div className="flex justify-center items-center h-64 opacity-50">
              <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-current"></div>
            </div>
          ) : (
            <div className="markdown-body">
              <ReactMarkdown
                remarkPlugins={[remarkMath, remarkGfm]}
                rehypePlugins={[rehypeRaw, rehypeKatex]}
                components={{
                  img: ({ node, ...props }) => {
                    let src = props.src;
                    if (src && !src.startsWith('http') && !src.startsWith('data:')) {
                      const baseUrl = import.meta.env.BASE_URL || '/';
                      const normalizedBaseUrl = baseUrl.endsWith('/') ? baseUrl : `${baseUrl}/`;
                      const semesterEncoded = encodeURIComponent(semesterName || '');
                      const courseEncoded = encodeURIComponent(courseName || '');
                      
                      let pathParts = (activeFile || '').split('/');
                      pathParts.pop(); 
                      const dirPath = pathParts.length > 0 ? encodeURIComponent(pathParts.join('/')) + '/' : '';
                      
                      // Handle relative paths better
                      if (src.startsWith('./')) {
                        src = src.substring(2);
                      }
                      
                      src = `${normalizedBaseUrl}content/${semesterEncoded}/${courseEncoded}/${dirPath}${src}`;
                    }
                    return <img {...props} src={src} className="max-w-full h-auto rounded-lg shadow-sm my-4" />;
                  }
                }}
              >
                {markdownContent}
              </ReactMarkdown>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
