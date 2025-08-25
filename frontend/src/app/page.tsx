// Next.js components
import ApiSection from "@/components/ApiSection";
import SetupSection from "@/components/SetupSection";
import ContributeSection from "@/components/ContributeSection";
import Link from "next/link";

export default function Home() {
  return (
    <div className="min-h-screen bg-background text-foreground">

      {/* Hero Section */}
      <section className="relative overflow-hidden">
        <div className="absolute inset-0 -z-10 bg-gradient-to-b from-indigo-50 to-white" />
        <div className="container-padded py-24 text-center">
          <h1 className="text-4xl md:text-6xl font-semibold tracking-tight mb-6">
            Baby Tracker API
          </h1>
          <p className="text-lg md:text-2xl mb-10 max-w-2xl mx-auto">
            A privacy-first, self-hostable solution for tracking your baby’s development.
          </p>
          <div className="flex flex-col sm:flex-row justify-center gap-3">
            <a href="#setup" className="btn-primary">Get Started</a>
            <a
              href="https://github.com/theamazingmrb/baby-tracker-api"
              className="btn-ghost"
              target="_blank"
              rel="noopener noreferrer"
            >
              View on GitHub
            </a>
          </div>
        </div>
      </section>

      {/* Project Overview */}
      <section className="py-20 md:py-32" id="overview">
        <div className="container-padded">
          <div className="flex flex-col lg:flex-row items-center gap-16">
            <div className="lg:w-1/2 animate-fade-in-up">
              <h2 className="text-large mb-8 text-primary">Why Baby Tracker?</h2>
              <p className="text-xl text-secondary mb-8 leading-relaxed">
                Baby Tracker is an open-source project that helps parents track their baby&#39;s daily activities, growth, and development with complete privacy control.
              </p>
              <p className="mb-6 text-secondary text-lg leading-relaxed">
                Unlike commercial alternatives that store sensitive data on third-party servers, Baby Tracker gives parents complete control over their baby&#39;s data with a self-hostable solution.
              </p>
              <p className="text-secondary text-lg leading-relaxed">
                Built with Django REST Framework and designed with privacy and security in mind, Baby Tracker provides all the features of premium baby tracking apps while keeping your data under your control.
              </p>
            </div>
            <div className="lg:w-1/2 card animate-fade-in-up stagger-2">
              <h3 className="text-2xl font-bold mb-8 text-primary">Key Benefits</h3>
              <ul className="space-y-4">
                <li className="flex items-start">
                  <div className="bg-indigo-50 p-2 rounded-md mr-4">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                    </svg>
                  </div>
                  <div>
                    <h4 className="font-medium text-primary">Complete Data Privacy</h4>
                    <p>Your baby&#39;s data stays on your server, not in a corporate database.</p>
                  </div>
                </li>
                <li className="flex items-start">
                  <div className="bg-indigo-50 p-2 rounded-md mr-4">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                    </svg>
                  </div>
                  <div>
                    <h4 className="font-medium text-primary">AI-Powered Insights</h4>
                    <p>Get recommendations for feeding times and sleep patterns based on historical data.</p>
                  </div>
                </li>
                <li className="flex items-start">
                  <div className="bg-indigo-50 p-2 rounded-md mr-4">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
                    </svg>
                  </div>
                  <div>
                    <h4 className="font-medium">Open Source</h4>
                    <p>Fully customizable and extendable to meet your specific needs.</p>
                  </div>
                </li>
                <li className="flex items-start">
                  <div className="bg-indigo-50 p-2 rounded-md mr-4">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 0 1 9.288 0M15 7a3 3 0 1 1-6 0 3 3 0 0 1 6 0zm6 3a2 2 0 1 1-4 0 2 2 0 0 1 4 0zM7 10a2 2 0 1 1-4 0 2 2 0 0 1 4 0z" />
                    </svg>
                  </div>
                  <div>
                    <h4 className="font-medium">Multi-Tenancy</h4>
                    <p>Complete tenant isolation ensures users can only access their own data.</p>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16 bg-gray-50" id="features">
        <div className="container-padded">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold mb-4 text-gray-900">Comprehensive Baby Tracking Features</h2>
            <p className="text-xl text-gray-800 max-w-3xl mx-auto">Everything you need to monitor your baby&#39;s development</p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {/* Feature 1 */}
            <div className="bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-elevated border border-gray-200 hover:shadow-lg transition duration-300 hover:-translate-y-0.5 text-gray-900">
              <div className="text-indigo-600 mb-4 text-3xl">&#x1F37C;</div>
              <h3 className="text-xl font-bold mb-2 text-gray-900">Feeding Tracking</h3>
              <p className="text-gray-800">Track breastfeeding, bottle feeds, and solid food with detailed metrics like duration, amount, and side.</p>
            </div>
            
            {/* Feature 2 */}
            <div className="bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-elevated border border-gray-200 hover:shadow-lg transition duration-300 hover:-translate-y-0.5 text-gray-900">
              <div className="text-indigo-600 mb-4 text-3xl">😴</div>
              <h3 className="text-xl font-bold mb-2 text-gray-900">Sleep Monitoring</h3>
              <p className="text-gray-800">Record sleep sessions with start/end times and quality ratings to establish healthy sleep patterns.</p>
            </div>
            
            {/* Feature 3 */}
            <div className="bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-elevated border border-gray-200 hover:shadow-lg transition duration-300 hover:-translate-y-0.5 text-gray-900">
              <div className="text-indigo-600 mb-4 text-3xl">🧷</div>
              <h3 className="text-xl font-bold mb-2 text-gray-900">Diaper Changes</h3>
              <p className="text-gray-800">Log diaper changes with type and notes to monitor digestive health and patterns.</p>
            </div>
            
            {/* Feature 4 */}
            <div className="bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-elevated border border-gray-200 hover:shadow-lg transition duration-300 hover:-translate-y-0.5 text-gray-900">
              <div className="text-indigo-600 mb-4 text-3xl">📏</div>
              <h3 className="text-xl font-bold mb-2 text-gray-900">Growth Milestones</h3>
              <p className="text-gray-800">Record height, weight, and other growth metrics to track development over time.</p>
            </div>
            
            {/* Feature 5 */}
            <div className="bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-elevated border border-gray-200 hover:shadow-lg transition duration-300 hover:-translate-y-0.5 text-gray-900">
              <div className="text-indigo-600 mb-4 text-3xl">👨‍⚕️</div>
              <h3 className="text-xl font-bold mb-2 text-gray-900">Doctor Appointments</h3>
              <p className="text-gray-800">Manage medical visits with notes, vaccinations, and follow-up information.</p>
            </div>
            
            {/* Feature 6 */}
            <div className="bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-elevated border border-gray-200 hover:shadow-lg transition duration-300 hover:-translate-y-0.5 text-gray-900">
              <div className="text-indigo-600 mb-4 text-3xl">💡</div>
              <h3 className="text-xl font-bold mb-2 text-gray-900">AI Insights</h3>
              <p className="text-gray-800">Get AI-powered recommendations for feeding times and sleep patterns based on historical data.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Tech Stack Section */}
      <section className="py-16" id="tech-stack">
        <div className="container-padded">
          <div className="flex flex-col md:flex-row items-center gap-12">
            <div className="md:w-1/2">
              <h2 className="text-3xl font-bold mb-6">Built with Modern Technologies</h2>
              <p className="text-lg mb-4">
                Baby Tracker is built with a robust tech stack designed for reliability, security, and performance.
              </p>
              <p className="mb-4">
                The backend is powered by Django and Django REST Framework, providing a solid foundation for API development with built-in security features and excellent ORM capabilities.
              </p>
              <p>
                PostgreSQL ensures data integrity and reliability, while JWT authentication provides secure access to the API endpoints.
              </p>
            </div>
            <div className="md:w-1/2">
              <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
                <div className="bg-white/80 backdrop-blur-md p-4 rounded-2xl shadow-elevated border border-gray-200 text-center hover:shadow-lg transition duration-300 hover:-translate-y-0.5">
                  <div className="text-indigo-600 text-3xl mb-2">🐍</div>
                  <h4 className="font-medium text-black">Django</h4>
                </div>
                <div className="bg-white/80 backdrop-blur-md p-4 rounded-2xl shadow-elevated border border-gray-200 text-center hover:shadow-lg transition duration-300 hover:-translate-y-0.5">
                  <div className="text-indigo-600 text-3xl mb-2">🌐</div>
                  <h4 className="font-medium text-black">Django REST</h4>
                </div>
                <div className="bg-white/80 backdrop-blur-md p-4 rounded-2xl shadow-elevated border border-gray-200 text-center hover:shadow-lg transition duration-300 hover:-translate-y-0.5">
                  <div className="text-indigo-600 text-3xl mb-2">🐘</div>
                  <h4 className="font-medium text-black">PostgreSQL</h4>
                </div>
                <div className="bg-white/80 backdrop-blur-md p-4 rounded-2xl shadow-elevated border border-gray-200 text-center hover:shadow-lg transition duration-300 hover:-translate-y-0.5">
                  <div className="text-indigo-600 text-3xl mb-2">🔑</div>
                  <h4 className="font-medium text-black">JWT Auth</h4>
                </div>
                <div className="bg-white/80 backdrop-blur-md p-4 rounded-2xl shadow-elevated border border-gray-200 text-center hover:shadow-lg transition duration-300 hover:-translate-y-0.5">
                  <div className="text-indigo-600 text-3xl mb-2">📊</div>
                  <h4 className="font-medium text-black">Pandas</h4>
                </div>
                <div className="bg-white/80 backdrop-blur-md p-4 rounded-2xl shadow-elevated border border-gray-200 text-center hover:shadow-lg transition duration-300 hover:-translate-y-0.5">
                  <div className="text-indigo-600 text-3xl mb-2">🐳</div>
                  <h4 className="font-medium text-black">Docker</h4>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Documentation Section */}
      <section className="py-16 bg-gray-50" id="documentation">
        <div className="container-padded">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold mb-4 text-gray-900">Documentation & Resources</h2>
            <p className="text-xl text-gray-800 max-w-3xl mx-auto">Everything you need to work with the Baby Tracker project</p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
            {/* API Documentation Card */}
            <Link href="/api-docs" className="block">
              <div className="bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-elevated border border-gray-200 hover:shadow-lg transition duration-300 hover:-translate-y-1 h-full">
                <div className="text-indigo-600 mb-4 text-3xl">📚</div>
                <h3 className="text-xl font-bold mb-2 text-gray-900">API Documentation</h3>
                <p className="text-gray-800 mb-4">Comprehensive documentation for all Baby Tracker API endpoints and models.</p>
                <div className="text-indigo-600 font-medium flex items-center">
                  View Documentation
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 ml-1" viewBox="0 0 20 20" fill="currentColor">
                    <path fillRule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clipRule="evenodd" />
                  </svg>
                </div>
              </div>
            </Link>
            
            {/* Setup Guide Card */}
            <Link href="/setup-guide" className="block">
              <div className="bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-elevated border border-gray-200 hover:shadow-lg transition duration-300 hover:-translate-y-1 h-full">
                <div className="text-indigo-600 mb-4 text-3xl">⚙️</div>
                <h3 className="text-xl font-bold mb-2 text-gray-900">Setup Guide</h3>
                <p className="text-gray-800 mb-4">Step-by-step instructions for setting up your development environment.</p>
                <div className="text-indigo-600 font-medium flex items-center">
                  View Setup Guide
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 ml-1" viewBox="0 0 20 20" fill="currentColor">
                    <path fillRule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clipRule="evenodd" />
                  </svg>
                </div>
              </div>
            </Link>
            
            {/* Contribution Guidelines Card */}
            <Link href="/contribute" className="block">
              <div className="bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-elevated border border-gray-200 hover:shadow-lg transition duration-300 hover:-translate-y-1 h-full">
                <div className="text-indigo-600 mb-4 text-3xl">👥</div>
                <h3 className="text-xl font-bold mb-2 text-gray-900">Contribution Guidelines</h3>
                <p className="text-gray-800 mb-4">Learn how to contribute to the Baby Tracker open source project.</p>
                <div className="text-indigo-600 font-medium flex items-center">
                  View Guidelines
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 ml-1" viewBox="0 0 20 20" fill="currentColor">
                    <path fillRule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clipRule="evenodd" />
                  </svg>
                </div>
              </div>
            </Link>
          </div>
          
          <h3 className="text-2xl font-bold mb-6 text-center text-gray-900">Guides</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {/* Deployment Guide Card */}
            <Link href="/deployment-guide" className="block">
              <div className="bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-elevated border border-gray-200 hover:shadow-lg transition duration-300 hover:-translate-y-1 h-full">
                <div className="text-indigo-600 mb-4 text-3xl">🚀</div>
                <h3 className="text-xl font-bold mb-2 text-gray-900">Deployment Guide</h3>
                <p className="text-gray-800 mb-4">Step-by-step instructions for deploying the Baby Tracker application using Docker or manual setup.</p>
                <div className="text-indigo-600 font-medium flex items-center">
                  View Guide
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 ml-1" viewBox="0 0 20 20" fill="currentColor">
                    <path fillRule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clipRule="evenodd" />
                  </svg>
                </div>
              </div>
            </Link>
            
            {/* Testing Guide Card */}
            <Link href="/testing-guide" className="block">
              <div className="bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-elevated border border-gray-200 hover:shadow-lg transition duration-300 hover:-translate-y-1 h-full">
                <div className="text-indigo-600 mb-4 text-3xl">🧪</div>
                <h3 className="text-xl font-bold mb-2 text-gray-900">Testing Guide</h3>
                <p className="text-gray-800 mb-4">Learn how to write effective tests for the Baby Tracker application, including examples and best practices.</p>
                <div className="text-indigo-600 font-medium flex items-center">
                  View Guide
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 ml-1" viewBox="0 0 20 20" fill="currentColor">
                    <path fillRule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clipRule="evenodd" />
                  </svg>
                </div>
              </div>
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
}
