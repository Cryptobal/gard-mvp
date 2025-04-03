/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  output: 'export',
  images: {
    unoptimized: true,
  },
  distDir: '.next',
  trailingSlash: true,
  basePath: '',
  assetPrefix: ''
}

module.exports = nextConfig 