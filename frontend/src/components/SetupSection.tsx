import React from 'react';

const SetupSection = () => {
  return (
    <section className="py-16" id="setup">
      <div className="container-padded">
        <div className="text-center mb-12">
          <h2 className="text-3xl font-bold mb-4 text-gray-900">Developer Setup</h2>
          <p className="text-xl text-gray-900 max-w-3xl mx-auto">
            Get up and running with Baby Tracker in minutes
          </p>
        </div>
        
        <div className="max-w-4xl mx-auto">
          <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden mb-8 transition-all hover:-translate-y-0.5 hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl font-bold mb-4 text-gray-900">Prerequisites</h3>
              <ul className="list-disc pl-5 space-y-2 text-gray-900">
                <li>Python 3.9+</li>
                <li>PostgreSQL 12+ (or use Docker)</li>
                <li>Git</li>
                <li>Docker & Docker Compose (optional, for containerized setup)</li>
              </ul>
            </div>
          </div>
          
          <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden mb-8 transition-all hover:-translate-y-0.5 hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl font-bold mb-4 text-gray-900">Quick Start with Docker (Recommended)</h3>
              <p className="mb-4 text-gray-900">
                The easiest way to get started is using Docker Compose, which includes PostgreSQL and all dependencies.
              </p>
              
              <div className="mb-6">
                <h4 className="font-bold mb-2 text-gray-900">1. Clone and start the application</h4>
                <div className="bg-slate-900 text-slate-100 p-4 rounded-xl overflow-x-auto font-mono text-sm ring-1 ring-white/10">
                  <div className="text-gray-400"># Clone the repository</div>
                  <div>git clone https://github.com/theamazingmrb/baby-tracker-api.git</div>
                  <div>cd baby-tracker-api</div>
                  <br />
                  <div className="text-gray-400"># Start all services</div>
                  <div>docker-compose up -d</div>
                </div>
              </div>
              
              <div className="mb-6">
                <h4 className="font-bold mb-2 text-gray-900">2. Initialize the database</h4>
                <div className="bg-slate-900 text-slate-100 p-4 rounded-xl overflow-x-auto font-mono text-sm ring-1 ring-white/10">
                  <div className="text-gray-400"># Run migrations</div>
                  <div>docker-compose exec web python manage.py migrate</div>
                  <br />
                  <div className="text-gray-400"># Create admin user</div>
                  <div>docker-compose exec web python manage.py createsuperuser</div>
                  <br />
                  <div className="text-gray-400"># Load demo data (optional)</div>
                  <div>docker-compose exec web python manage.py loaddata demo_data.json</div>
                </div>
              </div>
              
              <div className="bg-indigo-50 rounded-xl p-4 border border-indigo-100">
                <h4 className="font-semibold text-blue-900 mb-2">🎉 You're ready!</h4>
                <ul className="text-sm text-blue-900 space-y-2">
                  <li>• <a href="http://localhost:8000/api/tracker/" className="text-blue-800 hover:text-blue-600 hover:underline font-medium">http://localhost:8000/api/tracker/</a></li>
                  <li>• <a href="http://localhost:8000/admin/" className="text-blue-800 hover:text-blue-600 hover:underline font-medium">http://localhost:8000/admin/</a></li>
                  <li>• <a href="http://localhost:8000/api/docs/" className="text-blue-800 hover:text-blue-600 hover:underline font-medium">http://localhost:8000/api/docs/</a></li>
                  <li>• <a href="http://localhost:3000/" className="text-blue-800 hover:text-blue-600 hover:underline font-medium">http://localhost:3000/</a></li>
                </ul>
              </div>
            </div>
          </div>
          
          <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden mb-8 transition-all hover:-translate-y-0.5 hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl font-bold mb-4 text-gray-900">Local Development Setup</h3>
              <p className="mb-4 text-gray-900">
                For local development without Docker, follow these steps:
              </p>
              
              <div className="mb-6">
                <h4 className="font-bold mb-2 text-gray-900">1. Clone and setup Python environment</h4>
                <div className="bg-slate-900 text-slate-100 p-4 rounded-xl overflow-x-auto font-mono text-sm ring-1 ring-white/10">
                  <div>git clone https://github.com/theamazingmrb/baby-tracker-api.git</div>
                  <div>cd baby-tracker-api</div>
                  <br />
                  <div className="text-gray-400"># Create virtual environment</div>
                  <div>python -m venv venv</div>
                  <div>source venv/bin/activate  <span className="text-gray-400"># On Windows: venv\\Scripts\\activate</span></div>
                  <br />
                  <div className="text-gray-400"># Install dependencies</div>
                  <div>pip install -r requirements.txt</div>
                </div>
              </div>
              
              <div className="mb-6">
                <h4 className="font-bold mb-2 text-gray-900">2. Configure environment variables</h4>
                <div className="bg-slate-900 text-slate-100 p-4 rounded-xl overflow-x-auto font-mono text-sm ring-1 ring-white/10">
                  <div className="text-gray-400"># Copy environment template</div>
                  <div>cp .env.example .env</div>
                </div>
                <div className="mt-3 p-4 bg-yellow-50 border-l-4 border-yellow-400 rounded-xl">
                  <p className="text-sm text-yellow-900">
                    <strong>Important:</strong> Edit the <code>.env</code> file with your database credentials and other settings.
                  </p>
                </div>
              </div>
              
              <div className="mb-6">
                <h4 className="font-bold mb-2 text-gray-900">3. Setup PostgreSQL database</h4>
                <div className="bg-slate-900 text-slate-100 p-4 rounded-xl overflow-x-auto font-mono text-sm ring-1 ring-white/10">
                  <div className="text-gray-400"># Create database (adjust for your PostgreSQL setup)</div>
                  <div>createdb babytracker</div>
                  <br />
                  <div className="text-gray-400"># Run migrations</div>
                  <div>python manage.py migrate</div>
                  <br />
                  <div className="text-gray-400"># Create admin user</div>
                  <div>python manage.py createsuperuser</div>
                  <br />
                  <div className="text-gray-400"># Start development server</div>
                  <div>python manage.py runserver</div>
                </div>
              </div>
            </div>
          </div>
          
          <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden mb-8 transition-all hover:-translate-y-0.5 hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl font-bold mb-4 text-gray-900">Environment Variables</h3>
              <p className="mb-4 text-gray-900">
                Key environment variables you need to configure:
              </p>
              
              <div className="overflow-x-auto">
                <table className="min-w-full divide-y divide-gray-200 text-gray-900">
                  <thead className="bg-slate-900">
                    <tr>
                      <th className="px-4 py-3 text-left text-xs font-bold text-white uppercase">Variable</th>
                      <th className="px-4 py-3 text-left text-xs font-bold text-white uppercase">Description</th>
                      <th className="px-4 py-3 text-left text-xs font-bold text-white uppercase">Example</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-700 bg-slate-800">
                    <tr>
                      <td className="px-4 py-3 text-sm font-medium text-white">DATABASE_URL</td>
                      <td className="px-4 py-3 text-sm text-slate-300">PostgreSQL connection string</td>
                      <td className="px-4 py-3 text-sm font-mono text-yellow-400">postgresql://user:pass@localhost/babytracker</td>
                    </tr>
                    <tr>
                      <td className="px-4 py-3 text-sm font-medium text-white">SECRET_KEY</td>
                      <td className="px-4 py-3 text-sm text-slate-300">Django secret key</td>
                      <td className="px-4 py-3 text-sm font-mono text-yellow-400">your-secret-key-here</td>
                    </tr>
                    <tr>
                      <td className="px-4 py-3 text-sm font-medium text-white">DEBUG</td>
                      <td className="px-4 py-3 text-sm text-slate-300">Enable debug mode</td>
                      <td className="px-4 py-3 text-sm font-mono text-yellow-400">True</td>
                    </tr>
                    <tr>
                      <td className="px-4 py-3 text-sm font-medium text-white">ALLOWED_HOSTS</td>
                      <td className="px-4 py-3 text-sm text-slate-300">Allowed host names</td>
                      <td className="px-4 py-3 text-sm font-mono text-yellow-400">localhost,127.0.0.1</td>
                    </tr>
                    <tr>
                      <td className="px-4 py-3 text-sm font-medium text-white">CORS_ALLOWED_ORIGINS</td>
                      <td className="px-4 py-3 text-sm text-slate-300">CORS allowed origins</td>
                      <td className="px-4 py-3 text-sm font-mono text-yellow-400">http://localhost:3000</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          
          <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden transition-all hover:-translate-y-0.5 hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl font-bold mb-4 text-gray-900">Testing the API</h3>
              <p className="mb-4 text-gray-900">
                Once the server is running, you can test the API endpoints:
              </p>
              
              <div className="grid md:grid-cols-2 gap-6">
                <div>
                  <h4 className="font-semibold mb-2 text-gray-900">Using curl</h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl overflow-x-auto font-mono text-sm ring-1 ring-white/10">
                    <div className="text-gray-400"># Register a new user</div>
                    <div>curl -X POST http://localhost:8000/api/tracker/register/ \</div>
                    <div>  -H "Content-Type: application/json" \\\</div>
                    <div>  -d '{`{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123"
}`}'</div>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-semibold mb-2 text-gray-900">Using Python requests</h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl overflow-x-auto font-mono text-sm ring-1 ring-white/10">
                    <div className="text-blue-400">import</div> <div className="text-white">requests</div>
                    <br />
                    <div className="text-white">response = requests.post(</div>
                    <div className="text-yellow-400">  "http://localhost:8000/api/tracker/register/",</div>
                    <div className="text-white">  json={`{
    "username": "testuser",
    "email": "test@example.com", 
    "password": "testpass123"
}`}</div>
                    <div className="text-white">)</div>
                  </div>
                </div>
              </div>
              
              <div className="mt-6 p-4 bg-indigo-50 rounded-xl border border-indigo-100">
                <h4 className="font-semibold text-blue-900 mb-2">📚 Next Steps</h4>
                <ul className="text-sm text-blue-800 space-y-1">
                  <li>• Explore the <a href="#api" className="text-blue-600 hover:underline">API Documentation</a> section above</li>
                  <li>• Check out the interactive <a href="http://localhost:8000/api/docs/" className="text-blue-600 hover:underline">Swagger UI</a></li>
                  <li>• Review the <a href="#contribute" className="text-blue-600 hover:underline">Contributing Guidelines</a></li>
                  <li>• Join our community discussions on GitHub</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default SetupSection;