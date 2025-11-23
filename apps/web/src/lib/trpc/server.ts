import { initTRPC } from '@trpc/server'
import { prisma } from '@/lib/prisma'
import superjson from 'superjson'

// Create context for tRPC
export const createTRPCContext = async (opts: { headers: Headers }) => {
  return {
    prisma,
    headers: opts.headers,
  }
}

const t = initTRPC.context<typeof createTRPCContext>().create({
  transformer: superjson,
})

export const router = t.router
export const publicProcedure = t.procedure
