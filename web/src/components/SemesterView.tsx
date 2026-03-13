import { Link, useParams } from 'react-router-dom';
import { ChevronLeft, BookOpen } from 'lucide-react';

export default function SemesterView({ data }: { data: any[] }) {
  const { semesterName } = useParams();
  const semester = data.find(s => s.name === semesterName);

  if (!semester) {
    return (
      <div className="text-center py-20">
        <h2 className="text-xl font-medium mb-4">Semester not found</h2>
        <Link to="/" className="apple-accent hover:underline">Go back</Link>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto px-4 py-12 w-full">
      <div className="lg:pl-4 mb-10">
        <Link to="/" className="inline-flex items-center gap-1 text-sm opacity-60 hover:opacity-100 transition-opacity mb-4">
          <ChevronLeft className="w-4 h-4 ml(-1)" /> Folders
        </Link>
        <h1 className="text-3xl font-semibold capitalize tracking-tight">
          {semester.name.replace('-', ' ')}
        </h1>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {semester.courses.map((course: any) => (
          <Link
            key={course.name}
            to={`/semester/${encodeURIComponent(semester.name)}/course/${encodeURIComponent(course.name)}`}
            className="flex items-center gap-4 p-4 rounded-xl hover:bg-black/5 dark:hover:bg-white/5 transition-colors border border-transparent hover:border-[#e6e4dd] dark:hover:border-[#333]"
          >
            <BookOpen className="w-8 h-8 apple-accent opacity-80" />
            <div className="min-w-0">
              <h2 className="text-[17px] font-medium truncate" title={course.name.replace(/-/g, ' ')}>
                {course.name.replace(/-/g, ' ')}
              </h2>
              <div className="text-[13px] opacity-60 mt-0.5">
                {course.files.length} Note{course.files.length !== 1 ? 's' : ''}
              </div>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}