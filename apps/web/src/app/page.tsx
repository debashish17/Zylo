import Link from 'next/link'
import { Button } from '@/components/ui/button'

export default function HomePage() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div className="z-10 max-w-5xl w-full items-center justify-center font-mono text-sm">
        <div className="text-center space-y-8">
          <h1 className="text-6xl font-bold tracking-tight">
            <span className="text-primary">Zylo</span>
          </h1>

          <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
            AI-Powered Retail Media Creative Builder
          </p>

          <div className="flex gap-4 justify-center">
            <Button asChild size="lg">
              <Link href="/create">Create New Campaign</Link>
            </Button>

            <Button asChild variant="outline" size="lg">
              <Link href="/dashboard">My Creatives</Link>
            </Button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-16 text-left">
            <div className="p-6 border rounded-lg">
              <h3 className="font-semibold text-lg mb-2">🎨 AI-Powered Design</h3>
              <p className="text-sm text-muted-foreground">
                Generate professional creatives with intelligent layout suggestions and color palettes
              </p>
            </div>

            <div className="p-6 border rounded-lg">
              <h3 className="font-semibold text-lg mb-2">✅ Real-time Compliance</h3>
              <p className="text-sm text-muted-foreground">
                Automatic validation against Tesco guidelines with instant feedback
              </p>
            </div>

            <div className="p-6 border rounded-lg">
              <h3 className="font-semibold text-lg mb-2">⚡ Export Ready</h3>
              <p className="text-sm text-muted-foreground">
                Multi-format export optimized for Facebook, Instagram, and Stories
              </p>
            </div>
          </div>
        </div>
      </div>
    </main>
  )
}
