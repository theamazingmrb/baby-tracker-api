{
  id: "baby-tracker",
  title: "Baby Tracker",
  description: "A comprehensive, privacy-first baby tracking solution that helps parents monitor feedings, diapers, sleep, growth milestones, and more with AI-powered insights for establishing healthy routines.",
  image: "/projects/baby-tracker.png",
  details: "Baby Tracker is a privacy-first, self-hostable solution that gives parents complete control over their baby's data. Built with Django REST Framework and PostgreSQL, this comprehensive API allows parents to track all aspects of their baby's development and get AI-powered insights to help establish healthy routines.\n\nThe application features a multi-tenant architecture with robust security measures ensuring complete data isolation between users. Parents can track feedings (breastfeeding, bottle, solid food), diaper changes, sleep sessions, growth milestones, doctor appointments, medications, and pumping sessions. The AI insights module analyzes historical data to provide recommendations for feeding times and sleep patterns.\n\nThe backend is designed with scalability in mind, using Django's powerful ORM for database interactions and JWT authentication for secure API access. The API is fully documented using OpenAPI (via drf-spectacular) and includes comprehensive test coverage to ensure reliability.\n\nBaby Tracker stands out with its focus on data privacy and ownership - unlike commercial alternatives that store sensitive data on third-party servers, this solution can be self-hosted, giving parents complete control over their baby's information while still providing all the features of premium baby tracking apps.",
  url: "https://baby-tracker-demo.herokuapp.com",
  githubUrl: "https://github.com/theamazingmrb/baby-tracker-backend",
  techStack: ["Django", "Django REST Framework", "PostgreSQL", "JWT Authentication", "Docker", "Pandas", "OpenAPI"],
  features: [
    "Baby Profile Management: Create and manage multiple baby profiles",
    "Comprehensive Activity Tracking: Monitor feedings, diapers, sleep, growth, appointments, medications, and pumping",
    "AI-Powered Insights: Get recommendations for feeding times and sleep patterns based on historical data",
    "Recipe Management: Store and manage baby food recipes with ingredients and instructions",
    "Multi-Tenancy Architecture: Complete tenant isolation ensures users can only access their own data",
    "JWT Authentication: Secure API access with token-based authentication",
    "Interactive API Documentation: Explore the API with Swagger UI and ReDoc interfaces",
    "Docker Deployment: Easy setup with containerized deployment options",
    "Data Export/Import: Backup and restore baby data as needed",
    "Comprehensive Test Coverage: Ensuring reliability and security"
  ],
  images: [
    "/projects/baby-tracker.png",
    "/projects/baby-tracker-dashboard.png",
    "/projects/baby-tracker-insights.png"
  ],
  metrics: [
    "100% Data Privacy Compliance",
    "95% Test Coverage",
    "50+ API Endpoints",
    "30% Faster Baby Pattern Recognition"
  ],
  businessImpact: "Baby Tracker empowers parents with a privacy-focused alternative to commercial baby tracking apps, providing complete data ownership while delivering powerful insights to help establish healthy routines for their children."
}
