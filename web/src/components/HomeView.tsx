import { Link } from 'react-router-dom';
import { Folder } from 'lucide-react';

export default function HomeView({ data }: { data: any[] }) {
  const semesters = data;

  return (
    <div className="max-w-4xl mx-auto px-4 py-16 w-full">
      <div className="mb-10 lg:pl-4">
        <h1 className="text-3xl font-semibold mb-2">BSc Data Science and Artificial Intelligence</h1>
        <p className="opacity-60 text-[15px]">Course notes by Koorosh Komeili Zadeh - Leiden University</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        {semesters.map((semester) => (
          <Link
            key={semester.name}
            to={`/semester/${encodeURIComponent(semester.name)}`}
            className="flex items-center gap-4 p-4 rounded-xl hover:bg-black/5 dark:hover:bg-white/5 transition-colors border border-transparent hover:border-[#e6e4dd] dark:hover:border-[#333]"
          >
            <Folder className="w-10 h-10 apple-accent fill-current opacity-80" />
            <div>
              <h2 className="text-[17px] font-medium capitalize">
                {semester.name.replace('-', ' ')}
              </h2>
              <p className="text-[13px] opacity-60 mt-0.5">
                {semester.courses.length} Course{semester.courses.length !== 1 ? 's' : ''}
              </p>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}