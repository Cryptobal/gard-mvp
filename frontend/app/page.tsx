import Link from 'next/link'

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-[70vh] py-12">
      <h1 className="text-4xl font-bold mb-8 text-center">
        Bienvenido a GARD MVP
      </h1>
      <p className="text-xl mb-12 text-center max-w-2xl">
        Un proyecto fullstack optimizado para desarrollo rápido de MVPs.
      </p>
      <div className="flex flex-col sm:flex-row gap-4">
        <Link
          href="/login"
          className="px-6 py-3 rounded-md bg-blue-600 text-white hover:bg-blue-700 transition-colors"
        >
          Iniciar sesión
        </Link>
        <a
          href="https://github.com/username/gard-mvp"
          target="_blank"
          rel="noopener noreferrer"
          className="px-6 py-3 rounded-md border border-gray-300 dark:border-gray-700 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
        >
          Ver código fuente
        </a>
      </div>
    </div>
  )
} 