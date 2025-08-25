// Next.js components
import ApiSection from "@/components/ApiSection";
import SetupSection from "@/components/SetupSection";
import ContributeSection from "@/components/ContributeSection";
import DeploymentSection from "@/components/DeploymentSection";

export default function Home() {
  return (
    <div className="min-h-screen bg-background text-foreground">
      {/* Header/Navigation */}
      <header className="sticky top-0 z-50">
        <nav className="container-padded py-4 glass-strong backdrop-blur-md border-b border-border/50">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-gradient-primary rounded-2xl flex items-center justify-center text-white text-xl font-bold shadow-lg">
                👶
              </div>
              <span className="text-xl font-bold text-primary tracking-tight">Baby Tracker</span>
            </div>
            <div className="hidden lg:flex items-center gap-8 text-sm font-medium">
              <a href="#features" className="text-secondary hover:text-primary link-underline transition-all duration-300">Features</a>
              <a href="#tech-stack" className="text-secondary hover:text-primary link-underline transition-all duration-300">Tech Stack</a>
              <a href="#api" className="text-secondary hover:text-primary link-underline transition-all duration-300">API</a>
              <a href="#setup" className="text-secondary hover:text-primary link-underline transition-all duration-300">Setup</a>
              <a href="#contribute" className="text-secondary hover:text-primary link-underline transition-all duration-300">Contribute</a>
              <a href="#deployment" className="text-secondary hover:text-primary link-underline transition-all duration-300">Deployment</a>
            </div>
            <div className="flex items-center gap-2 sm:gap-3">
              <a href="/api/docs/" className="btn-primary whitespace-nowrap text-xs sm:text-sm px-3 sm:px-6 py-2 flex-shrink-0">
                <span className="hidden sm:inline">API Docs</span>
                <span className="sm:hidden">API</span>
              </a>
              {/* Mobile menu button - could be added later */}
              <button className="lg:hidden p-2 rounded-xl bg-surface border border-border flex-shrink-0">
                <svg className="w-5 h-5 text-secondary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                </svg>
              </button>
            </div>
          </div>
        </nav>
      </header>

      {/* Hero Section */}
      <section className="relative overflow-hidden">
        <div className="absolute inset-0 -z-10 bg-gradient-to-b from-indigo-50 to-white" />
        <div className="container-padded py-24 text-center">
          <h1 className="text-4xl md:text-6xl font-semibold tracking-tight mb-6 text-gray-900">
            Baby Tracker API
          </h1>
          <p className="text-lg md:text-2xl text-gray-800 mb-10 max-w-2xl mx-auto">
            A privacy-first, self-hostable solution for tracking your baby’s development.
          </p>
          <div className="flex flex-col sm:flex-row justify-center gap-3">
            <a href="#setup" className="btn-primary">Get Started</a>
            <a
              href="https://github.com/theamazingmrb/baby-tracker-backend"
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
                    <p className="text-gray-800">Your baby&#39;s data stays on your server, not in a corporate database.</p>
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
                    <p className="text-gray-800">Get recommendations for feeding times and sleep patterns based on historical data.</p>
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
                    <p className="text-gray-800">Fully customizable and extendable to meet your specific needs.</p>
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
                    <p className="text-gray-800">Complete tenant isolation ensures users can only access their own data.</p>
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
            <div className="bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-elevated border border-gray-200 hover:shadow-lg transition-shadow transition-transform hover:-translate-y-0.5 text-gray-900">
              <div className="text-indigo-600 mb-4 text-3xl">&#x1F37C;</div>
              <h3 className="text-xl font-bold mb-2 text-gray-900">Feeding Tracking</h3>
              <p className="text-gray-800">Track breastfeeding, bottle feeds, and solid food with detailed metrics like duration, amount, and side.</p>
            </div>
            
            {/* Feature 2 */}
            <div className="bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-elevated border border-gray-200 hover:shadow-lg transition-shadow transition-transform hover:-translate-y-0.5 text-gray-900">
              <div className="text-indigo-600 mb-4 text-3xl">😴</div>
              <h3 className="text-xl font-bold mb-2 text-gray-900">Sleep Monitoring</h3>
              <p className="text-gray-800">Record sleep sessions with start/end times and quality ratings to establish healthy sleep patterns.</p>
            </div>
            
            {/* Feature 3 */}
            <div className="bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-elevated border border-gray-200 hover:shadow-lg transition-shadow transition-transform hover:-translate-y-0.5 text-gray-900">
              <div className="text-indigo-600 mb-4 text-3xl">🧷</div>
              <h3 className="text-xl font-bold mb-2 text-gray-900">Diaper Changes</h3>
              <p className="text-gray-800">Log diaper changes with type and notes to monitor digestive health and patterns.</p>
            </div>
            
            {/* Feature 4 */}
            <div className="bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-elevated border border-gray-200 hover:shadow-lg transition-shadow transition-transform hover:-translate-y-0.5 text-gray-900">
              <div className="text-indigo-600 mb-4 text-3xl">📏</div>
              <h3 className="text-xl font-bold mb-2 text-gray-900">Growth Milestones</h3>
              <p className="text-gray-800">Record height, weight, and other growth metrics to track development over time.</p>
            </div>
            
            {/* Feature 5 */}
            <div className="bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-elevated border border-gray-200 hover:shadow-lg transition-shadow transition-transform hover:-translate-y-0.5 text-gray-900">
              <div className="text-indigo-600 mb-4 text-3xl">👨‍⚕️</div>
              <h3 className="text-xl font-bold mb-2 text-gray-900">Doctor Appointments</h3>
              <p className="text-gray-800">Manage medical visits with notes, vaccinations, and follow-up information.</p>
            </div>
            
            {/* Feature 6 */}
            <div className="bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-elevated border border-gray-200 hover:shadow-lg transition-shadow transition-transform hover:-translate-y-0.5 text-gray-900">
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
                <div className="bg-white/80 backdrop-blur-md p-4 rounded-2xl shadow-elevated border border-gray-200 text-center hover:shadow-lg transition-shadow transition-transform hover:-translate-y-0.5">
                  <div className="text-indigo-600 text-3xl mb-2">🐍</div>
                  <h4 className="font-medium">Django</h4>
                </div>
                <div className="bg-white/80 backdrop-blur-md p-4 rounded-2xl shadow-elevated border border-gray-200 text-center hover:shadow-lg transition-shadow transition-transform hover:-translate-y-0.5">
                  <div className="text-indigo-600 text-3xl mb-2">🌐</div>
                  <h4 className="font-medium">Django REST</h4>
                </div>
                <div className="bg-white/80 backdrop-blur-md p-4 rounded-2xl shadow-elevated border border-gray-200 text-center hover:shadow-lg transition-shadow transition-transform hover:-translate-y-0.5">
                  <div className="text-indigo-600 text-3xl mb-2">🐘</div>
                  <h4 className="font-medium">PostgreSQL</h4>
                </div>
                <div className="bg-white/80 backdrop-blur-md p-4 rounded-2xl shadow-elevated border border-gray-200 text-center hover:shadow-lg transition-shadow transition-transform hover:-translate-y-0.5">
                  <div className="text-indigo-600 text-3xl mb-2">🔑</div>
                  <h4 className="font-medium">JWT Auth</h4>
                </div>
                <div className="bg-white/80 backdrop-blur-md p-4 rounded-2xl shadow-elevated border border-gray-200 text-center hover:shadow-lg transition-shadow transition-transform hover:-translate-y-0.5">
                  <div className="text-indigo-600 text-3xl mb-2">📊</div>
                  <h4 className="font-medium">Pandas</h4>
                </div>
                <div className="bg-white/80 backdrop-blur-md p-4 rounded-2xl shadow-elevated border border-gray-200 text-center hover:shadow-lg transition-shadow transition-transform hover:-translate-y-0.5">
                  <div className="text-indigo-600 text-3xl mb-2">🐳</div>
                  <h4 className="font-medium">Docker</h4>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* API Documentation Section */}
      <ApiSection />

      {/* Developer Setup Section */}
      <SetupSection />

      {/* Contribution Guidelines Section */}
      <ContributeSection />

      {/* Deployment Section */}
      <DeploymentSection />

      {/* Footer */}
      <footer className="border-t border-border/50 py-20 mt-32">
        <div className="container-padded">
          <div className="flex flex-col md:flex-row justify-between mb-12">
            <div className="mb-12 md:mb-0">
              <div className="flex items-center space-x-3 mb-6">
                <div className="w-12 h-12 bg-gradient-primary rounded-2xl flex items-center justify-center text-white text-xl font-bold shadow-lg">
                  👶
                </div>
                <span className="font-bold text-2xl text-primary">Baby Tracker</span>
              </div>
              <p className="max-w-md text-secondary text-lg leading-relaxed">
                A privacy-first, self-hostable solution for tracking your baby&apos;s development.
              </p>
            </div>
            <div className="grid grid-cols-2 md:grid-cols-3 gap-12">
              <div>
                <h4 className="font-semibold mb-6 text-primary text-lg">Links</h4>
                <ul className="space-y-4">
                  <li><a href="#features" className="text-secondary hover:text-primary link-underline transition-all duration-300">Features</a></li>
                  <li><a href="#tech-stack" className="text-secondary hover:text-primary link-underline transition-all duration-300">Tech Stack</a></li>
                  <li><a href="#api" className="text-secondary hover:text-primary link-underline transition-all duration-300">API</a></li>
                </ul>
              </div>
              <div>
                <h4 className="font-semibold mb-6 text-primary text-lg">Resources</h4>
                <ul className="space-y-4">
                  <li><a href="#setup" className="text-secondary hover:text-primary link-underline transition-all duration-300">Setup Guide</a></li>
                  <li><a href="#contribute" className="text-secondary hover:text-primary link-underline transition-all duration-300">Contribute</a></li>
                  <li><a href="#deployment" className="text-secondary hover:text-primary link-underline transition-all duration-300">Deployment</a></li>
                </ul>
              </div>
              <div>
                <h4 className="font-semibold mb-6 text-primary text-lg">Connect</h4>
                <ul className="space-y-4">
                  <li>
                    <a 
                      href="https://github.com/theamazingmrb/baby-tracker-backend" 
                      className="text-secondary hover:text-primary transition-all duration-300 flex items-center space-x-3 group"
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      <div className="w-8 h-8 bg-surface border border-border rounded-xl flex items-center justify-center group-hover:bg-gradient-primary group-hover:border-accent transition-all duration-300">
                        <svg className="h-4 w-4 group-hover:text-white" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                          <path fillRule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clipRule="evenodd" />
                        </svg>
                      </div>
                      <span>GitHub</span>
                    </a>
                  </li>
                  <li>
                    <a 
                      href="/api/docs/" 
                      className="text-secondary hover:text-primary transition-all duration-300 flex items-center space-x-3 group"
                    >
                      <div className="w-8 h-8 bg-surface border border-border rounded-xl flex items-center justify-center group-hover:bg-gradient-primary group-hover:border-accent transition-all duration-300">
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 group-hover:text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                        </svg>
                      </div>
                      <span>API Docs</span>
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </div>
          <div className="border-t border-border/50 mt-12 pt-8 text-center">
            <p className="text-tertiary">© {new Date().getFullYear()} Baby Tracker. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}
