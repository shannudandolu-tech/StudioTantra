'use client'

export default function Home() {
  return (
    <main className="min-h-screen flex items-center justify-center p-4">
      <div className="max-w-md w-full text-center">
        <h1 className="text-3xl font-bold text-slate-900 mb-2">
          Studio <span className="text-blue-600">Tantra</span>
        </h1>
        <p className="text-slate-600 mb-6">
          AI-powered ad creative platform for Indian SMBs
        </p>
        <div className="card p-6">
          <p className="text-sm text-slate-500 mb-4">
            Frontend initializing... connecting to backend API
          </p>
          <div className="animate-pulse">
            <div className="h-8 bg-slate-200 rounded"></div>
          </div>
        </div>
      </div>
    </main>
  )
}
