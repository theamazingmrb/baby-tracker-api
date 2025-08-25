# Baby Tracker - API Documentation Website

This is the documentation website for the Baby Tracker API, built with Next.js and Tailwind CSS. It provides comprehensive information about the Baby Tracker API endpoints, setup instructions, deployment guides, and contribution guidelines.

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ 
- npm or yarn

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/baby-tracker-backend.git
cd baby-tracker-backend/frontend
```

2. Install dependencies:
```bash
npm install
# or
yarn install
```

3. Run the development server:
```bash
npm run dev
# or
yarn dev
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

## 📖 What's Included

### API Documentation
- Complete endpoint reference with all Baby Tracker API routes
- Authentication examples using JWT tokens
- Request/response examples for all major operations
- Data model specifications

### Setup Guides
- Docker setup (recommended)
- Local development setup
- Environment variable configuration
- Database setup instructions

### Deployment Documentation  
- Production deployment with Docker
- Environment configuration for production
- SSL/HTTPS setup with Let's Encrypt
- Monitoring and maintenance guides

### Contributing Guidelines
- How to contribute code, documentation, and bug reports
- Development workflow and standards
- Code style guidelines
- Testing requirements

## 🛠 Development

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint

### Project Structure

```
frontend/
├── src/
│   ├── app/                 # Next.js app directory
│   │   ├── favicon.ico
│   │   ├── globals.css
│   │   ├── layout.tsx
│   │   └── page.tsx
│   └── components/          # React components
│       ├── ApiSection.tsx
│       ├── ContributeSection.tsx
│       ├── DeploymentSection.tsx
│       └── SetupSection.tsx
├── public/                  # Static files
├── package.json
├── tailwind.config.js
└── tsconfig.json
```

## 🎨 Customization

### Updating API Information
- Edit `src/components/ApiSection.tsx` to modify API endpoint documentation
- Update endpoint URLs, methods, and descriptions as needed

### Modifying Setup Instructions
- Update `src/components/SetupSection.tsx` for installation and setup guides
- Modify Docker commands, environment variables, and prerequisites

### Changing Deployment Info
- Edit `src/components/DeploymentSection.tsx` for deployment instructions
- Update production configuration and hosting information

### Updating Contributing Guidelines
- Modify `src/components/ContributeSection.tsx` for contribution information
- Update coding standards, workflow, and project-specific requirements

## 🔗 Links

All links in the documentation point to placeholder URLs that should be updated:

- GitHub repository URLs
- API documentation endpoints
- Issue tracking links
- Discussion forums

Update these links in the respective component files to point to your actual project resources.

## 📱 Responsive Design

The documentation website is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones

## 🌟 Features

- **Clean, Modern Design** - Professional documentation layout
- **Comprehensive API Coverage** - All endpoints documented with examples
- **Interactive Examples** - Code snippets for multiple programming languages
- **Copy-Friendly** - Code blocks optimized for easy copying
- **Mobile Responsive** - Works on all device sizes
- **Fast Loading** - Optimized with Next.js and Tailwind CSS

## 🤝 Contributing

This documentation website welcomes contributions! You can help by:

1. **Improving Documentation** - Fix typos, add clarity, update outdated information
2. **Adding Examples** - Contribute more code examples in different languages
3. **Enhancing Design** - Improve the UI/UX of the documentation
4. **Fixing Bugs** - Report and fix any issues you find

### Making Changes

1. Fork the repository
2. Make your changes to the appropriate component files
3. Test your changes locally with `npm run dev`
4. Submit a pull request with a clear description

## 📄 License

This documentation website is part of the Baby Tracker project. Please refer to the main project's license for terms and conditions.

## 🆘 Support

If you need help with the documentation website:

1. Check the main Baby Tracker project documentation
2. Open an issue in the GitHub repository
3. Join the community discussions

---

**Note**: This is the documentation website for the Baby Tracker API. For the actual API server code, see the parent directory of this project.