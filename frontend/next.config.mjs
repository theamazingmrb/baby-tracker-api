/** @type {import('next').NextConfig} */
const nextConfig = {
  eslint: {
    // Warning: This allows production builds to successfully complete even if
    // your project has ESLint errors.
    ignoreDuringBuilds: true,
  },
  output: 'export',
  distDir: 'out',
  // Configure base path if not serving from root
  // basePath: '',
  images: {
    unoptimized: true,
  },
};

export default nextConfig;
