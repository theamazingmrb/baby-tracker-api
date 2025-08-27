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
                  <h3 className="text-lg font-bold">EC2 + Docker Compose (Recommended)</h3>
                </div>
                <p className="text-gray-900 text-sm flex-grow">
                  Simple, cost-effective deployment using AWS EC2 with Docker Compose. Complete containerized setup with PostgreSQL and all dependencies included.
                </p>
                <div className="mt-4 text-xs text-gray-900">
                  ✓ Low cost (~$5-6/month)<br />
                  ✓ Simple configuration<br />
                  ✓ Full control
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
                  <h3 className="text-lg font-bold">Local Docker Deployment</h3>
                </div>
                <p className="text-gray-900 text-sm flex-grow">
                  Run Baby Tracker on your own hardware using Docker Compose for local development or self-hosting.
                </p>
                <div className="mt-4 text-xs text-gray-900">
                  ✓ Complete privacy<br />
                  ✓ No cloud costs<br />
                  ✓ Simple setup
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
                  <h3 className="text-lg font-bold">Other Cloud Options</h3>
                </div>
                <p className="text-gray-900 text-sm flex-grow">
                  Deploy to other cloud providers like GCP, Azure, DigitalOcean, or platforms like Heroku, Render, or Railway.
                </p>
                <div className="mt-4 text-xs text-gray-900">
                  ✓ Alternative providers<br />
                  ✓ Platform-specific features<br />
                  ✓ Existing infrastructure
                </div>
              </div>
            </div>
          </div>
          
          <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden mb-8 transition-all hover:-translate-y-0.5 hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl font-bold mb-4">🚀 AWS EC2 Deployment with Docker Compose</h3>
              <p className="text-gray-800 mb-6">The simplest and most cost-effective way to deploy Baby Tracker to production. Choose between standard HTTP deployment or secure HTTPS deployment:</p>
              
              <div className="space-y-6">
                <div>
                  <h4 className="font-bold mb-2">1. Launch an EC2 Instance</h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl overflow-x-auto font-mono text-sm ring-1 ring-white/10">
                    <div className="text-gray-500"># Key settings for your EC2 instance:</div>
                    <div>- Instance type: t3.nano (~$5-6/month)</div>
                    <div>- OS: Amazon Linux 2023 or Ubuntu Server</div>
                    <div>- Security group: Allow ports 22 (SSH), 80 (HTTP), 443 (HTTPS)</div>
                    <div>- Storage: 8GB (default) is sufficient</div>
                    <br />
                    <div className="text-gray-500"># Connect to your instance</div>
                    <div>ssh -i your-key.pem ec2-user@your-instance-ip</div>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-bold mb-2">2. Install Docker and Docker Compose</h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl overflow-x-auto font-mono text-sm ring-1 ring-white/10">
                    <div className="text-gray-500"># For Amazon Linux 2023</div>
                    <div>sudo yum update -y</div>
                    <div>sudo yum install -y docker</div>
                    <div>sudo systemctl start docker</div>
                    <div>sudo systemctl enable docker</div>
                    <div>sudo usermod -aG docker $USER</div>
                    <br />
                    <div className="text-gray-500"># Install Docker Compose</div>
                    <div>sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose</div>
                    <div>sudo chmod +x /usr/local/bin/docker-compose</div>
                    <br />
                    <div className="text-yellow-400"># Log out and back in for group changes</div>
                    <div>exit</div>
                    <div># Then reconnect via SSH</div>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-bold mb-2">3. Deploy the Application</h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl overflow-x-auto font-mono text-sm ring-1 ring-white/10">
                    <div className="text-gray-500"># Clone the repository</div>
                    <div>git clone https://github.com/theamazingmrb/baby-tracker-api.git</div>
                    <div>cd baby-tracker-api</div>
                    <br />
                    <div className="text-gray-500"># Configure environment</div>
                    <div>cp .env.example .env</div>
                    <div>nano .env  # Edit with your production settings</div>
                    <br />
                    <div className="text-gray-500"># Option 1: Start with basic HTTP setup</div>
                    <div>docker-compose up -d</div>
                    <br />
                    <div className="text-gray-500"># OR Option 2: Start with HTTPS setup</div>
                    <div>mkdir -p nginx/conf nginx/certbot/conf nginx/certbot/www</div>
                    <div>docker-compose -f docker-compose.https.yml up -d</div>
                    <br />
                    <div className="text-gray-500"># Create admin user</div>
                    <div>docker-compose exec web python manage.py createsuperuser</div>
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
                      <td className="px-4 py-3 text-sm font-medium text-indigo-600">PRODUCTION_DOMAIN</td>
                      <td className="px-4 py-3 text-sm font-mono text-gray-800">api.yourdomain.com</td>
                      <td className="px-4 py-3 text-sm text-gray-800">Your API backend domain</td>
                    </tr>
                    <tr>
                      <td className="px-4 py-3 text-sm font-medium text-indigo-600">FRONTEND_DOMAIN</td>
                      <td className="px-4 py-3 text-sm font-mono text-gray-800">app.yourdomain.com</td>
                      <td className="px-4 py-3 text-sm text-gray-800">Your frontend application domain</td>
                    </tr>
                    <tr>
                      <td className="px-4 py-3 text-sm font-medium text-indigo-600">ALLOWED_HOSTS</td>
                      <td className="px-4 py-3 text-sm font-mono text-gray-800">yourdomain.com,www.yourdomain.com</td>
                      <td className="px-4 py-3 text-sm text-gray-800">Your domain and www subdomain</td>
                    </tr>
                    <tr>
                      <td className="px-4 py-3 text-sm font-medium text-indigo-600">DATABASE_URL</td>
                      <td className="px-4 py-3 text-sm font-mono text-gray-800">postgresql://...</td>
                      <td className="px-4 py-3 text-sm text-gray-800">Production database connection</td>
                    </tr>
                    <tr>
                      <td className="px-4 py-3 text-sm font-medium text-indigo-600">CORS_ALLOWED_ORIGINS</td>
                      <td className="px-4 py-3 text-sm font-mono text-gray-800">http://yourdomain.com,https://yourdomain.com,http://www.yourdomain.com,https://www.yourdomain.com</td>
                      <td className="px-4 py-3 text-sm text-gray-800">Both HTTP and HTTPS versions of your domains</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          
          <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden mb-8 transition-all hover:-translate-y-0.5 hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl font-bold mb-4">SSL/HTTPS Setup with Let's Encrypt</h3>
              <p className="mb-4 text-gray-800">Secure your EC2 deployment with free SSL certificates using our integrated HTTPS setup:</p>
              
              <div className="bg-slate-900 text-slate-100 p-4 rounded-xl overflow-x-auto font-mono text-sm ring-1 ring-white/10">
                <div className="text-gray-500"># Option 1: Using the Integrated HTTPS Setup (Recommended)</div>
                <div className="text-gray-500"># Create required directories</div>
                <div>mkdir -p nginx/conf nginx/certbot/conf nginx/certbot/www</div>
                <br />
                <div className="text-gray-500"># Create a basic Nginx configuration</div>
                <div>{`cat > nginx/conf/app.conf << 'EOL'`}</div>
                <div>{`server {`}</div>
                <div>{`    listen 80;`}</div>
                <div>{`    server_name yourdomain.com www.yourdomain.com;`}</div>
                <div>{`    `}</div>
                <div>{`    location /.well-known/acme-challenge/ {`}</div>
                <div>{`        root /var/www/certbot;`}</div>
                <div>{`    }`}</div>
                <div>{`    `}</div>
                <div>{`    location / {`}</div>
                <div>{`        return 301 https://$host$request_uri;`}</div>
                <div>{`    }`}</div>
                <div>{`}`}</div>
                <div>{`EOL`}</div>
                <br />
                <div className="text-gray-500"># Replace domain placeholders with your actual domain</div>
                <div>sed -i 's/yourdomain.com/example.com/g' nginx/conf/app.conf  # Replace example.com with your domain</div>
                <br />
                <div className="text-gray-500"># Start the application with HTTPS configuration</div>
                <div>docker-compose -f docker-compose.https.yml up -d</div>
                <br />
                <div className="text-gray-500"># Obtain SSL certificates (after DNS is properly configured)</div>
                <div>{`docker-compose -f docker-compose.https.yml exec certbot certbot certonly --webroot \
  -w /var/www/certbot -d yourdomain.com -d www.yourdomain.com \
  --email your-email@example.com --agree-tos --no-eff-email`}</div>
                <br />
                <div className="text-gray-500"># Reload Nginx to apply the certificates</div>
                <div>docker-compose -f docker-compose.https.yml exec nginx nginx -s reload</div>
              </div>
              
              <div className="mt-4 mb-4 text-gray-800">Alternative manual setup (if needed):</div>
              
              <div className="bg-slate-900 text-slate-100 p-4 rounded-xl overflow-x-auto font-mono text-sm ring-1 ring-white/10">
                <div className="text-gray-500"># Option 2: Manual HTTPS Setup</div>
                <div className="text-gray-500"># For Amazon Linux 2023</div>
                <div>sudo dnf install -y augeas-libs</div>
                <div>sudo python3 -m pip install certbot</div>
                <br />
                <div className="text-gray-500"># For Ubuntu</div>
                <div>sudo apt install -y certbot</div>
                <br />
                <div className="text-gray-500"># Stop Docker containers to free port 80</div>
                <div>docker-compose down</div>
                <br />
                <div className="text-gray-500"># Obtain SSL certificate for both domain and www subdomain</div>
                <div>sudo certbot certonly --standalone -d yourdomain.com -d www.yourdomain.com</div>
                <br />
                <div className="text-gray-500"># Set up Nginx as reverse proxy with SSL</div>
                <div>mkdir -p nginx/conf</div>
                <div>nano nginx/conf/app.conf  # Configure with SSL paths</div>
                <div>{`docker-compose -f docker-compose.https.yml up -d`}</div>
              </div>
            </div>
          </div>
          
          <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden transition-all hover:-translate-y-0.5 hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl font-bold mb-4 text-gray-900">Monitoring & Maintenance</h3>
              
              <div className="grid md:grid-cols-2 gap-6">
                <div>
                  <h4 className="font-bold mb-2 text-gray-900">📊 EC2 & Container Monitoring</h4>
                  <div className="bg-gray-50 p-3 rounded-xl text-sm border border-gray-200 text-gray-800">
                    <div className="mb-2">Check EC2 system status:</div>
                    <code className="text-xs text-gray-900">top</code>
                    <div className="mt-2 mb-2">Check container status (HTTP setup):</div>
                    <code className="text-xs text-gray-900">cd ~/baby-tracker-api && docker-compose ps</code>
                    <div className="mt-2 mb-2">Check container status (HTTPS setup):</div>
                    <code className="text-xs text-gray-900">cd ~/baby-tracker-api && docker-compose -f docker-compose.https.yml ps</code>
                    <div className="mt-2 mb-2">View application logs:</div>
                    <code className="text-xs text-gray-900">docker-compose logs -f web</code>
                    <div className="mt-2 mb-2">View HTTPS-related logs:</div>
                    <code className="text-xs text-gray-900">docker-compose -f docker-compose.https.yml logs -f nginx certbot</code>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-bold mb-2 text-gray-900">💾 Database Backups</h4>
                  <div className="bg-gray-50 p-3 rounded-xl text-sm border border-gray-200 text-gray-800">
                    <div className="mb-2">Create backup script:</div>
                    <code className="text-xs text-gray-900">nano ~/backup-db.sh</code>
                    <div className="mt-1 mb-1 text-xs text-gray-600">Add these lines to the script:</div>
                    <pre className="text-xs text-gray-900 bg-gray-100 p-1 rounded">
#!/bin/bash
DATE=$(date +%Y-%m-%d)
BACKUP_DIR=~/backups
mkdir -p $BACKUP_DIR
cd ~/baby-tracker-api
docker-compose exec -T db pg_dump -U postgres postgres {'>'} $BACKUP_DIR/backup-$DATE.sql
                    </pre>
                    <div className="mt-2 mb-2">Schedule daily backups:</div>
                    <code className="text-xs text-gray-900">chmod +x ~/backup-db.sh && crontab -e</code>
                    <div className="mt-1 mb-1 text-xs text-gray-600">Add this line to crontab:</div>
                    <code className="text-xs text-gray-900">0 2 * * * ~/backup-db.sh</code>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-bold mb-2 text-gray-900">🔄 EC2 Application Updates</h4>
                  <div className="bg-gray-50 p-3 rounded-xl text-sm border border-gray-200 text-gray-800">
                    <div className="mb-2">Update application code:</div>
                    <code className="text-xs text-gray-900">cd ~/baby-tracker-api && git pull origin main</code>
                    <div className="mt-2 mb-2">Backup database before update:</div>
                    <code className="text-xs text-gray-900">./backup-db.sh</code>
                    <div className="mt-2 mb-2">Rebuild and restart containers (HTTP deployment):</div>
                    <code className="text-xs text-gray-900">docker-compose down && docker-compose up -d --build</code>
                    <div className="mt-2 mb-2">OR for HTTPS deployment:</div>
                    <code className="text-xs text-gray-900">docker-compose -f docker-compose.https.yml down && docker-compose -f docker-compose.https.yml up -d --build</code>
                    <div className="mt-2 mb-2">Run migrations:</div>
                    <code className="text-xs text-gray-900">docker-compose exec web python manage.py migrate</code>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-bold mb-2 text-gray-900">🚨 EC2 Troubleshooting</h4>
                  <div className="bg-gray-50 p-3 rounded-xl text-sm border border-gray-200 text-gray-800">
                    <div className="mb-2">Check EC2 disk space:</div>
                    <code className="text-xs text-gray-900">df -h</code>
                    <div className="mt-2 mb-2">Restart Docker service:</div>
                    <code className="text-xs text-gray-900">sudo systemctl restart docker</code>
                    <div className="mt-2 mb-2">Restart application containers (HTTP):</div>
                    <code className="text-xs text-gray-900">cd ~/baby-tracker-api && docker-compose restart</code>
                    <div className="mt-2 mb-2">Restart application containers (HTTPS):</div>
                    <code className="text-xs text-gray-900">cd ~/baby-tracker-api && docker-compose -f docker-compose.https.yml restart</code>
                    <div className="mt-2 mb-2">View detailed application errors:</div>
                    <code className="text-xs text-gray-900">docker-compose logs -f web</code>
                    <div className="mt-2 mb-2">View Nginx logs (HTTPS setup):</div>
                    <code className="text-xs text-gray-900">docker-compose -f docker-compose.https.yml logs -f nginx</code>
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
                    href="https://github.com/theamazingmrb/baby-tracker-api/blob/main/docs/deployment_guide.md" 
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