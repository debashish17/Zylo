/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  transpilePackages: ['@tesco-create/ui', '@tesco-create/types'],
  images: {
    domains: [
      'localhost',
      // Add your Supabase storage domain
      // e.g., 'xxxxx.supabase.co'
    ],
  },
  experimental: {
    serverActions: {
      bodySizeLimit: '10mb',
    },
  },
}

module.exports = nextConfig
