/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  images: {
    unoptimized: true,
    domains: ['vercel.app'],
  },
  distDir: '.next',
  assetPrefix: process.env.NODE_ENV === 'production' ? '/' : '',
  webpack: (config) => {
    return config;
  },
}

module.exports = nextConfig 