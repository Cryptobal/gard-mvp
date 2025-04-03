import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './styles/globals.css'
import { Providers } from './providers'

const inter = Inter({ 
  subsets: ['latin'],
  variable: '--font-inter',
})

export const metadata: Metadata = {
  title: 'GARD MVP',
  description: 'Sistema MVP de GARD',
  icons: {
    icon: '/favicon.ico',
    shortcut: '/favicon.ico',
    apple: '/favicon.ico',
  },
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="es" suppressHydrationWarning>
      <head>
        <link rel="icon" href="/favicon.ico" sizes="any" />
        <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
      </head>
      <body className={`${inter.className} min-h-screen`}>
        <Providers>
          <header className="p-4 border-b dark:border-gray-800">
            <div className="container mx-auto flex justify-between items-center">
              <h1 className="text-xl font-bold">GARD MVP</h1>
              {/* El ThemeToggle se renderizará dentro de Providers */}
            </div>
          </header>
          <main className="container mx-auto p-4">
            {children}
          </main>
          <footer className="p-4 border-t dark:border-gray-800">
            <div className="container mx-auto text-center text-sm text-gray-500">
              © {new Date().getFullYear()} GARD MVP
            </div>
          </footer>
        </Providers>
      </body>
    </html>
  )
} 