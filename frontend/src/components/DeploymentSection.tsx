import React from 'react';

const DeploymentSection = () => {
  return (
    <section className="py-16 bg-gray-50 text-black" id="deployment">
      <div className="container-padded">
        <div className="text-center mb-12">
          <h2 className="text-3xl font-bold mb-4 text-gray-900">Deployment Options</h2>
          <p className="text-xl text-gray-900 max-w-3xl mx-auto">
            Deploy Baby Tracker to your preferred hosting environment with complete privacy and control
          </p>
        </div>
        
        <div className="max-w-4xl mx-auto">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
            <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden h-full transition-all hover:-translate-y-0.5 hover:shadow-lg">
              <div className="p-6 flex flex-col h-full">
                <div className="flex flex-col sm:flex-row sm:items-center mb-4">
                  <div className="bg-blue-100 p-3 rounded-md mr-3 mb-2 sm:mb-0">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-blue-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                    </svg>
                  </div>
                  <h3 className="text-lg font-bold">Docker (Recommended)</h3>
                </div>
                <p className="text-gray-900 text-sm flex-grow">
                  Complete containerized setup with PostgreSQL, Redis, and all dependencies included. Perfect for production deployments.
                </p>
                <div className="mt-4 text-xs text-gray-900">
                  ✓ One-command deployment<br />
                  ✓ All services included<br />
                  ✓ Easy scaling
                </div>
              </div>
            </div>
            
            <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden h-full transition-all hover:-translate-y-0.5 hover:shadow-lg">
              <div className="p-6 flex flex-col h-full">
                <div className="flex flex-col sm:flex-row sm:items-center mb-4">
                  <div className="bg-green-100 p-3 rounded-md mr-3 mb-2 sm:mb-0">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 12h14M5 12a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v4a2 2 0 01-2 2M5 12a2 2 0 00-2 2v4a2 2 0 002 2h14a2 2 0 002-2v-4a2 2 0 00-2-2m-2-4h.01M17 16h.01" />
                    </svg>
                  </div>
                  <h3 className="text-lg font-bold">Manual Setup</h3>
                </div>
                <p className="text-gray-900 text-sm flex-grow">
                  Traditional server deployment with manual configuration of PostgreSQL, Python environment, and web server.
                </p>
                <div className="mt-4 text-xs text-gray-900">
                  ✓ Full control<br />
                  ✓ Custom configuration<br />
                  ✓ Existing infrastructure
                </div>
              </div>
            </div>
            
            <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden h-full transition-all hover:-translate-y-0.5 hover:shadow-lg">
              <div className="p-6 flex flex-col h-full">
                <div className="flex flex-col sm:flex-row sm:items-center mb-4">
                  <div className="bg-purple-100 p-3 rounded-md mr-3 mb-2 sm:mb-0">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-purple-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M9 19l3 3m0 0l3-3m-3 3V10" />
                    </svg>
                  </div>
                  <h3 className="text-lg font-bold">Cloud Platforms</h3>
                </div>
                <p className="text-gray-900 text-sm flex-grow">
                  Deploy to AWS, Google Cloud, DigitalOcean, or other cloud providers using their container services or VM instances.
                </p>
                <div className="mt-4 text-xs text-gray-900">
                  ✓ Managed infrastructure<br />
                  ✓ Auto-scaling<br />
                  ✓ Global availability
                </div>
              </div>
            </div>
          </div>
          
          <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden mb-8 transition-all hover:-translate-y-0.5 hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl font-bold mb-4">🚀 Quick Docker Deployment</h3>
              <p className="text-gray-800 mb-6">The fastest way to get Baby Tracker running in production:</p>
              
              <div className="space-y-6">
                <div>
                  <h4 className="font-bold mb-2">1. Server Preparation</h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl overflow-x-auto font-mono text-sm ring-1 ring-white/10">
                    <div className="text-gray-500"># Update your server</div>
                    <div>sudo apt update && sudo apt upgrade -y</div>
                    <br />
                    <div className="text-gray-500"># Install Docker and Docker Compose</div>
                    <div>curl -fsSL https://get.docker.com -o get-docker.sh</div>
                    <div>sudo sh get-docker.sh</div>
                    <div>sudo apt install docker-compose -y</div>
                    <br />
                    <div className="text-gray-500"># Add user to docker group</div>
                    <div>sudo usermod -aG docker $USER</div>
                    <div className="text-yellow-400"># Log out and back in for group changes</div>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-bold mb-2">2. Application Deployment</h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl overflow-x-auto font-mono text-sm ring-1 ring-white/10">
                    <div className="text-gray-500"># Clone the repository</div>
                    <div>git clone https://github.com/theamazingmrb/baby-tracker-api.git</div>
                    <div>cd baby-tracker-api</div>
                    <br />
                    <div className="text-gray-500"># Configure production environment</div>
                    <div>cp .env.example .env</div>
                    <div className="text-yellow-400"># Edit .env with your production settings</div>
                    <div>nano .env</div>
                    <br />
                    <div className="text-gray-500"># Deploy with production compose file</div>
                    <div>docker-compose -f docker-compose.yml up -d</div>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-bold mb-2">3. Database Setup</h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl overflow-x-auto font-mono text-sm ring-1 ring-white/10">
                    <div className="text-gray-500"># Run database migrations</div>
                    <div>docker-compose exec web python manage.py migrate</div>
                    <br />
                    <div className="text-gray-500"># Create admin user</div>
                    <div>docker-compose exec web python manage.py createsuperuser</div>
                    <br />
                    <div className="text-gray-500"># Collect static files</div>
                    <div>docker-compose exec web python manage.py collectstatic --noinput</div>
                  </div>
                </div>
              </div>
              
              <div className="mt-6 p-4 bg-green-50 border border-green-100 rounded-xl">
                <h4 className="font-semibold text-green-900 mb-2">🎉 Deployment Complete!</h4>
                <p className="text-sm text-green-800">Your Baby Tracker instance is now running. Access it at your server's IP address or domain.</p>
              </div>
            </div>
          </div>
          
          <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden mb-8 transition-all hover:-translate-y-0.5 hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl font-bold mb-4">Production Environment Configuration</h3>
              <p className="mb-4 text-gray-800">Critical environment variables for production deployment:</p>
              
              <div className="overflow-x-auto">
                <table className="min-w-full divide-y divide-gray-200">
                  <thead className="bg-gray-50">
                    <tr>
                      <th className="px-4 py-3 text-left text-xs font-medium text-gray-900 uppercase">Variable</th>
                      <th className="px-4 py-3 text-left text-xs font-medium text-gray-900 uppercase">Production Value</th>
                      <th className="px-4 py-3 text-left text-xs font-medium text-gray-900 uppercase">Description</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-gray-200">
                    <tr>
                      <td className="px-4 py-3 text-sm font-medium text-red-600">DEBUG</td>
                      <td className="px-4 py-3 text-sm font-mono text-gray-800">False</td>
                      <td className="px-4 py-3 text-sm text-gray-800">MUST be False in production</td>
                    </tr>
                    <tr>
                      <td className="px-4 py-3 text-sm font-medium text-red-600">SECRET_KEY</td>
                      <td className="px-4 py-3 text-sm font-mono text-gray-800">random-50-char-string</td>
                      <td className="px-4 py-3 text-sm text-gray-800">Generate secure random key</td>
                    </tr>
                    <tr>
                      <td className="px-4 py-3 text-sm font-medium text-indigo-600">ALLOWED_HOSTS</td>
                      <td className="px-4 py-3 text-sm font-mono text-gray-800">yourdomain.com,www.yourdomain.com</td>
                      <td className="px-4 py-3 text-sm text-gray-800">Your domain names</td>
                    </tr>
                    <tr>
                      <td className="px-4 py-3 text-sm font-medium text-indigo-600">DATABASE_URL</td>
                      <td className="px-4 py-3 text-sm font-mono text-gray-800">postgresql://...</td>
                      <td className="px-4 py-3 text-sm text-gray-800">Production database connection</td>
                    </tr>
                    <tr>
                      <td className="px-4 py-3 text-sm font-medium text-indigo-600">CORS_ALLOWED_ORIGINS</td>
                      <td className="px-4 py-3 text-sm font-mono text-gray-800">https://yourdomain.com</td>
                      <td className="px-4 py-3 text-sm text-gray-800">Frontend domain with HTTPS</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          
          <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden mb-8 transition-all hover:-translate-y-0.5 hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl font-bold mb-4">SSL/HTTPS Setup with Let's Encrypt</h3>
              <p className="mb-4 text-gray-800">Secure your deployment with free SSL certificates:</p>
              
              <div className="bg-slate-900 text-slate-100 p-4 rounded-xl overflow-x-auto font-mono text-sm ring-1 ring-white/10">
                <div className="text-gray-500"># Install Certbot</div>
                <div>sudo apt install certbot python3-certbot-nginx -y</div>
                <br />
                <div className="text-gray-500"># Obtain SSL certificate</div>
                <div>sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com</div>
                <br />
                <div className="text-gray-500"># Auto-renewal (certificate expires in 90 days)</div>
                <div>sudo crontab -e</div>
                <div className="text-yellow-400"># Add: 0 12 * * * /usr/bin/certbot renew --quiet</div>
              </div>
            </div>
          </div>
          
          <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden transition-all hover:-translate-y-0.5 hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl font-bold mb-4 text-gray-900">Monitoring & Maintenance</h3>
              
              <div className="grid md:grid-cols-2 gap-6">
                <div>
                  <h4 className="font-bold mb-2 text-gray-900">📊 Health Monitoring</h4>
                  <div className="bg-gray-50 p-3 rounded-xl text-sm border border-gray-200 text-gray-800">
                    <div className="mb-2">Check container status:</div>
                    <code className="text-xs text-gray-900">docker-compose ps</code>
                    <div className="mt-2 mb-2">View logs:</div>
                    <code className="text-xs text-gray-900">docker-compose logs -f web</code>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-bold mb-2 text-gray-900">💾 Database Backups</h4>
                  <div className="bg-gray-50 p-3 rounded-xl text-sm border border-gray-200 text-gray-800">
                    <div className="mb-2">Create backup:</div>
                    <code className="text-xs text-gray-900">docker-compose exec db pg_dump -U postgres babytracker {'>'} backup.sql</code>
                    <div className="mt-2 mb-2">Restore backup:</div>
                    <code className="text-xs text-gray-900">docker-compose exec db psql -U postgres babytracker {'<'} backup.sql</code>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-bold mb-2 text-gray-900">🔄 Updates</h4>
                  <div className="bg-gray-50 p-3 rounded-xl text-sm border border-gray-200 text-gray-800">
                    <div className="mb-2">Update application:</div>
                    <code className="text-xs text-gray-900">git pull && docker-compose up -d --build</code>
                    <div className="mt-2 mb-2">Run migrations:</div>
                    <code className="text-xs text-gray-900">docker-compose exec web python manage.py migrate</code>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-bold mb-2 text-gray-900">🚨 Troubleshooting</h4>
                  <div className="bg-gray-50 p-3 rounded-xl text-sm border border-gray-200 text-gray-800">
                    <div className="mb-2">Restart services:</div>
                    <code className="text-xs text-gray-900">docker-compose restart</code>
                    <div className="mt-2 mb-2">Reset everything:</div>
                    <code className="text-xs text-gray-900">docker-compose down && docker-compose up -d</code>
                  </div>
                </div>
              </div>
            </div>
            
            <div className="bg-gray-50 px-6 py-4">
              <div className="flex flex-col sm:flex-row justify-between items-center">
                <p className="text-sm text-gray-800 mb-4 sm:mb-0">
                  Need help with deployment? Check our detailed guides and community support.
                </p>
                <div className="flex space-x-3 text-sm">
                  <a 
                    href="https://github.com/theamazingmrb/baby-tracker-api/blob/main/DEPLOYMENT.md" 
                    className="btn-primary"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    Deployment Guide
                  </a>
                  <a 
                    href="https://github.com/theamazingmrb/baby-tracker-api/issues" 
                    className="btn-ghost"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    Get Support
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default DeploymentSection;