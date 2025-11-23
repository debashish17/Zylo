import { fetchRequestHandler } from '@trpc/server/adapters/fetch'
import { type NextRequest } from 'next/server'
import { createTRPCContext, router, publicProcedure } from '@/lib/trpc/server'
import { z } from 'zod'

// Define your API routes here
const appRouter = router({
  // Health check
  health: publicProcedure.query(() => {
    return { status: 'ok', timestamp: new Date().toISOString() }
  }),

  // Creative routes (will expand these)
  creative: router({
    list: publicProcedure.query(async ({ ctx }) => {
      return ctx.prisma.creative.findMany({
        include: {
          compliance: true,
        },
        orderBy: {
          updatedAt: 'desc',
        },
        take: 20,
      })
    }),

    getById: publicProcedure
      .input(z.object({ id: z.string() }))
      .query(async ({ ctx, input }) => {
        return ctx.prisma.creative.findUnique({
          where: { id: input.id },
          include: {
            compliance: true,
            exports: true,
          },
        })
      }),

    create: publicProcedure
      .input(
        z.object({
          title: z.string(),
          format: z.enum(['SQUARE_1_1', 'PORTRAIT_4_5', 'STORIES_9_16']),
          userId: z.string(),
          canvasState: z.any(),
        })
      )
      .mutation(async ({ ctx, input }) => {
        return ctx.prisma.creative.create({
          data: {
            title: input.title,
            format: input.format,
            userId: input.userId,
            canvasState: input.canvasState,
          },
        })
      }),

    update: publicProcedure
      .input(
        z.object({
          id: z.string(),
          title: z.string().optional(),
          canvasState: z.any().optional(),
        })
      )
      .mutation(async ({ ctx, input }) => {
        return ctx.prisma.creative.update({
          where: { id: input.id },
          data: {
            title: input.title,
            canvasState: input.canvasState,
          },
        })
      }),

    delete: publicProcedure
      .input(z.object({ id: z.string() }))
      .mutation(async ({ ctx, input }) => {
        return ctx.prisma.creative.delete({
          where: { id: input.id },
        })
      }),
  }),
})

export type AppRouter = typeof appRouter

const handler = (req: NextRequest) =>
  fetchRequestHandler({
    endpoint: '/api/trpc',
    req,
    router: appRouter,
    createContext: createTRPCContext,
  })

export { handler as GET, handler as POST }
