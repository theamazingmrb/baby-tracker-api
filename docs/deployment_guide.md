# Baby Tracker Deployment Guide

This guide provides detailed instructions for deploying the Baby Tracker application to production using AWS EC2 with Docker Compose. This approach is simple, cost-effective (~$5-6/month), and provides full control over your deployment.

## AWS EC2 Deployment

### 1. Launch an EC2 Instance

1. **Sign in to the AWS Management Console** and navigate to the EC2 Dashboard.

2. **Launch a new EC2 instance**:
   - Click "Launch Instance"
   - Name your instance (e.g., "baby-tracker")
   - Select Amazon Linux 2023 AMI or Ubuntu Server (latest LTS)
   - Choose t3.nano instance type (1 vCPU, 0.5 GiB memory) - sufficient for most personal use cases
   - Create or select an existing key pair for SSH access
   - Configure security group to allow:
     - SSH (port 22) from your IP address
     - HTTP (port 80) from anywhere
     - HTTPS (port 443) from anywhere
   - Configure storage (default 8GB is sufficient)
   - Click "Launch Instance"

### 2. Connect to Your EC2 Instance

Once your instance is running, connect to it via SSH:

```bash
ssh -i /path/to/your-key.pem ec2-user@your-instance-public-ip
```

For Ubuntu instances, use `ubuntu` instead of `ec2-user`:

```bash
ssh -i /path/to/your-key.pem ubuntu@your-instance-public-ip
```

### 3. Install Docker and Docker Compose

#### For Amazon Linux 2023:

```bash
# Update system packages
sudo yum update -y

# Install Docker
sudo yum install -y docker
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Log out and log back in for group changes to take effect
exit
```

Reconnect to your instance after logging out.

#### For Ubuntu:

```bash
# Update system packages
sudo apt update
sudo apt upgrade -y

# Install Docker
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Log out and log back in for group changes to take effect
exit
```

Reconnect to your instance after logging out.

### 4. Deploy the Baby Tracker Application

1. **Clone the repository**:

```bash
git clone https://github.com/theamazingmrb/baby-tracker-api.git
cd baby-tracker-api
```

2. **Create and configure environment variables**:

```bash
cp .env.example .env
```

Edit the `.env` file with your production settings:

```bash
# Use nano or vim to edit the file
nano .env
```

Important settings to configure:

```
# Environment
DJANGO_DEBUG=False

# Production settings
PRODUCTION_DOMAIN=your-domain.com
FRONTEND_DOMAIN=your-domain.com
CORS_ALLOWED_ORIGINS=http://your-domain.com,https://your-domain.com,http://www.your-domain.com,https://www.your-domain.com
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0,your-domain.com,www.your-domain.com

# Database settings
DATABASE_URL=postgresql://postgres:postgres@db:5432/baby_tracker

# Security settings
SECRET_KEY=generate-a-secure-random-key-here

# Email settings (if needed)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.your-provider.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password
```

Note: The `ALLOWED_HOSTS` setting is important for Django to accept requests from your domain and www subdomain. The application will automatically add your PRODUCTION_DOMAIN to ALLOWED_HOSTS, but explicitly setting it ensures both the root domain and www subdomain work properly.

3. **Start the application**:

```bash
docker-compose up -d
```

This command will:
- Build the Docker images if they don't exist
- Start the PostgreSQL database and web application containers
- Run database migrations
- Collect static files
- Start the Django application with Gunicorn

4. **Create a superuser** for admin access:

```bash
docker-compose exec web python manage.py createsuperuser
```

Follow the prompts to create your admin user.

5. **Verify the deployment**:

```bash
# Check if containers are running
docker-compose ps

# Check application logs
docker-compose logs web
```

6. **Access your application** at `http://your-instance-ip/` and the admin interface at `http://your-instance-ip/admin/`

## Setting Up a Custom Domain (Optional)

If you want to use a custom domain instead of the EC2 instance IP:

1. **Register a domain** or use an existing one.

2. **Configure DNS settings** to point to your EC2 instance IP:
   - Create an A record pointing to your EC2 instance IP
   - If using AWS Route 53, create a hosted zone for your domain and configure the appropriate records

3. **Update your environment variables** in the `.env` file:
   ```
   PRODUCTION_DOMAIN=your-domain.com
   FRONTEND_DOMAIN=your-domain.com
   CORS_ALLOWED_ORIGINS=https://your-domain.com,http://localhost:3000
   ```

4. **Restart the application** to apply changes:
   ```bash
   docker-compose down
   docker-compose up -d
   ```

## Setting Up HTTPS with Let's Encrypt (Recommended for Production)

For production environments, HTTPS is strongly recommended. The project now includes a dedicated Docker Compose configuration file (`docker-compose.https.yml`) that sets up Nginx as a reverse proxy and Certbot for automatic SSL certificate management.

### Option 1: Using the Integrated HTTPS Setup (Recommended)

1. **Create required directories**:

   ```bash
   mkdir -p nginx/conf nginx/certbot/conf nginx/certbot/www
   ```

2. **Create a basic Nginx configuration**:

   ```bash
   cat > nginx/conf/app.conf << 'EOL'
   server {
       listen 80;
       server_name your-domain.com www.your-domain.com;
       
       location /.well-known/acme-challenge/ {
           root /var/www/certbot;
       }
       
       location / {
           return 301 https://$host$request_uri;
       }
   }
   
   server {
       listen 443 ssl;
       server_name your-domain.com www.your-domain.com;
       
       ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
       ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;
       
       location / {
           proxy_pass http://web:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   EOL
   ```

3. **Replace domain placeholders** with your actual domain:

   ```bash
   sed -i 's/your-domain.com/example.com/g' nginx/conf/app.conf  # Replace example.com with your domain
   ```

4. **Start the application** with HTTPS configuration:

   ```bash
   docker-compose -f docker-compose.https.yml up -d
   ```

5. **Obtain SSL certificates** (after DNS is properly configured):

   ```bash
   docker-compose -f docker-compose.https.yml exec certbot certbot certonly --webroot -w /var/www/certbot \
     -d your-domain.com -d www.your-domain.com \
     --email your-email@example.com --agree-tos --no-eff-email
   ```

6. **Reload Nginx** to apply the certificates:

   ```bash
   docker-compose -f docker-compose.https.yml exec nginx nginx -s reload
   ```

### Option 2: Manual HTTPS Setup

If you prefer to set up HTTPS manually or have specific requirements:

1. **Install Certbot**:

   For Amazon Linux 2023:
   ```bash
   sudo dnf install -y augeas-libs
   sudo python3 -m pip install certbot
   ```

   For Ubuntu:
   ```bash
   sudo apt install -y certbot
   ```

2. **Obtain SSL certificate**:

   ```bash
   # Stop Docker containers temporarily to free up port 80
   docker-compose down
   
   # Get certificate for both domain and www subdomain
   sudo certbot certonly --standalone -d your-domain.com -d www.your-domain.com
   
   # Start containers again
   docker-compose up -d
   ```

3. **Configure Nginx as a reverse proxy** with SSL:

   Create a new file named `nginx.conf`:
   ```bash
   mkdir -p nginx
   nano nginx/nginx.conf
   ```

   Add the following configuration:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com www.your-domain.com;
       return 301 https://$host$request_uri;
   }

   server {
       listen 443 ssl;
       server_name your-domain.com www.your-domain.com;

       ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
       ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;
       ssl_protocols TLSv1.2 TLSv1.3;
       ssl_prefer_server_ciphers on;

       location / {
           proxy_pass http://localhost:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

4. **Create a custom Nginx configuration**:

   ```bash
   mkdir -p nginx/conf
   nano nginx/conf/app.conf
   ```

   Add the following content (replace yourdomain.com with your actual domain):
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com www.yourdomain.com;
       return 301 https://$host$request_uri;
   }

   server {
       listen 443 ssl;
       server_name yourdomain.com www.yourdomain.com;

       ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
       ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
       ssl_protocols TLSv1.2 TLSv1.3;
       ssl_prefer_server_ciphers on;

       location / {
           proxy_pass http://web:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

5. **Start the application with HTTPS support**:

   ```bash
   docker-compose -f docker-compose.https.yml up -d
   ```

6. **Certificate renewal is handled automatically**:

   The Certbot container in the `docker-compose.https.yml` configuration will automatically attempt to renew certificates when needed. However, you can also manually trigger renewal:

   ```bash
   docker-compose -f docker-compose.https.yml exec certbot certbot renew
   docker-compose -f docker-compose.https.yml exec nginx nginx -s reload
   ```

   If you prefer a scheduled renewal script:
   ```bash
   # Create a renewal script
   nano renew-cert.sh
   ```

   Add the following content:
   ```bash
   #!/bin/bash
   docker-compose -f docker-compose.https.yml exec certbot certbot renew
   docker-compose -f docker-compose.https.yml exec nginx nginx -s reload
   ```

   Make it executable:
   ```bash
   chmod +x renew-cert.sh
   ```

   Add a cron job to run it monthly:
   ```bash
   (crontab -l 2>/dev/null; echo "0 0 1 * * $(pwd)/renew-cert.sh") | crontab -
   ```

## Database Backups

To set up regular database backups:

1. **Create a backup script**:

   ```bash
   nano backup-db.sh
   ```

   Add the following content:
   ```bash
   #!/bin/bash
   TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
   BACKUP_DIR="/home/ec2-user/backups"

   # Create backup directory if it doesn't exist
   mkdir -p $BACKUP_DIR

   # Backup the database
   docker-compose exec -T db pg_dump -U postgres baby_tracker > $BACKUP_DIR/baby_tracker_$TIMESTAMP.sql

   # Keep only the 7 most recent backups
   ls -tp $BACKUP_DIR/*.sql | grep -v '/$' | tail -n +8 | xargs -I {} rm -- {}
   ```

   Make it executable:
   ```bash
   chmod +x backup-db.sh
   ```

2. **Schedule daily backups with cron**:

   ```bash
   (crontab -l 2>/dev/null; echo "0 2 * * * /home/ec2-user/baby-tracker-api/backup-db.sh") | crontab -
   ```

   This will run the backup script every day at 2:00 AM.

## Updating the Application

To update your application when new code is available:

```bash
# Navigate to your project directory
cd baby-tracker-api

# Pull the latest code
git pull

# For basic HTTP deployment
docker-compose down
docker-compose up -d --build

# OR for HTTPS deployment
docker-compose -f docker-compose.https.yml down
docker-compose -f docker-compose.https.yml up -d --build
```

## Troubleshooting

### Common Issues and Solutions

1. **Container fails to start**:
   - Check logs: `docker-compose logs web` or `docker-compose -f docker-compose.https.yml logs web`
   - Verify environment variables in `.env`
   - Ensure database connection is working

2. **Database connection issues**:
   - Check if the database container is running: `docker-compose ps`
   - Verify DATABASE_URL in `.env`
   - Check database logs: `docker-compose logs db`

3. **Permission issues**:
   - Ensure proper file permissions: `chmod -R 755 .`
   - Check Docker permissions: `sudo usermod -aG docker $USER`

4. **Port conflicts**:
   - Check if another service is using port 80: `sudo lsof -i :80`
   - Modify port mapping in `.env` by setting `WEB_PORT=8080` (or another available port)

5. **SSL/HTTPS issues**:
   - Verify certificate paths in Nginx configuration
   - Check certificate validity: `docker-compose -f docker-compose.https.yml exec certbot certbot certificates`
   - Ensure DNS is properly configured for your domain
   - Check Nginx logs: `docker-compose -f docker-compose.https.yml logs nginx`

### Viewing Logs

```bash
# For basic HTTP deployment
# View all logs
docker-compose logs

# View specific service logs
docker-compose logs web
docker-compose logs db

# Follow logs in real-time
docker-compose logs -f web

# For HTTPS deployment
# View all logs
docker-compose -f docker-compose.https.yml logs

# View specific service logs
docker-compose -f docker-compose.https.yml logs web
docker-compose -f docker-compose.https.yml logs nginx
docker-compose -f docker-compose.https.yml logs certbot

# Follow logs in real-time
docker-compose -f docker-compose.https.yml logs -f web
```

## Monitoring (Optional)

For basic monitoring of your EC2 instance:

1. **Set up AWS CloudWatch** for monitoring CPU, memory, and disk usage.

2. **Install and configure a monitoring tool** like Prometheus with Grafana or a simpler solution like Netdata:

   ```bash
   # Install Netdata
   bash <(curl -Ss https://my-netdata.io/kickstart.sh)
   ```

   Access Netdata dashboard at `http://your-instance-ip:19999`

## Security Best Practices

1. **Keep your system updated**:
   ```bash
   sudo yum update -y  # Amazon Linux
   # or
   sudo apt update && sudo apt upgrade -y  # Ubuntu
   ```

2. **Use strong passwords** for database and admin users.

3. **Restrict SSH access** to specific IP addresses in your security group.

4. **Enable and configure a firewall**:
   ```bash
   # For Ubuntu
   sudo ufw allow ssh
   sudo ufw allow http
   sudo ufw allow https
   sudo ufw enable
   ```

5. **Regularly back up your database** as described in the Database Backups section.

6. **Monitor your instance** for unusual activity.

## Deployment Configuration Files

The project includes two Docker Compose configuration files to suit different deployment needs:

1. **docker-compose.yml**: Basic deployment without HTTPS
   - Suitable for development or when using an external HTTPS proxy
   - Exposes the web service directly on port 80 (or the port specified in `WEB_PORT`)
   - Simpler configuration with fewer containers

2. **docker-compose.https.yml**: Production deployment with HTTPS
   - Includes Nginx as a reverse proxy and Certbot for SSL certificates
   - Handles automatic HTTPS redirection and certificate renewal
   - Recommended for production deployments

## Environment Variables

The following environment variables can be configured in your `.env` file:

- `PRODUCTION_DOMAIN`: Your API backend domain (e.g., babytracker.xyz)
- `FRONTEND_DOMAIN`: Your frontend application domain (e.g., babytracker.xyz)
- `ALLOWED_HOSTS`: Comma-separated list of domains allowed to serve the application
- `CORS_ALLOWED_ORIGINS`: Comma-separated list of origins allowed to access the API
- `POSTGRES_USER`: PostgreSQL username (used by Docker)
- `POSTGRES_PASSWORD`: PostgreSQL password (used by Docker)
- `POSTGRES_DB`: PostgreSQL database name (used by Docker)
- `WEB_PORT`: Port to expose the web service on (default: 80)
- `NETWORK_HOST`: Host to bind the Django server to (default: 0.0.0.0)
- `NETWORK_PORT`: Port for the Django server (default: 8000)

## Conclusion

You now have a fully functional Baby Tracker application deployed on AWS EC2 using Docker Compose. This setup provides a cost-effective, flexible, and secure way to run your application in production.

The new deployment configuration with separate files for HTTP and HTTPS makes it easy to choose the right setup for your needs, while the environment variable-based configuration allows for easy customization without modifying the Docker Compose files directly.

For any questions or issues, please refer to the project's GitHub repository or create an issue for support.
