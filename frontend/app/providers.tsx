'use client'

import { ThemeProvider } from 'next-themes'
import { ThemeToggle } from './components/ThemeToggle'
import React from 'react'

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <ThemeProvider attribute="class" defaultTheme="system" enableSystem>
      <div className="absolute right-4 top-4">
        <ThemeToggle />
      </div>
      {children}
    </ThemeProvider>
  )
} 