'use client'

import { createTRPCReact, httpBatchLink } from '@trpc/react-query'
import type { AppRouter } from '@/app/api/trpc/[trpc]/route'
import superjson from 'superjson'

export const trpc = createTRPCReact<AppRouter>()

function getBaseUrl() {
  if (typeof window !== 'undefined') return ''
  return `http://localhost:${process.env.PORT ?? 3000}`
}

export const trpcClient = trpc.createClient({
  transformer: superjson,
  links: [
    httpBatchLink({
      url: `${getBaseUrl()}/api/trpc`,
    }),
  ],
})
