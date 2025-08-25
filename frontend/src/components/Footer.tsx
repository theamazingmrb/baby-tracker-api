import React from 'react';
import Link from 'next/link';

export default function Footer() {
  return (
    <footer className="border-t border-border/50 py-20 mt-32">
      <div className="container-padded">
        <div className="flex flex-col md:flex-row justify-between mb-12">
          <div className="mb-12 md:mb-0">
            <div className="flex items-center space-x-3 mb-6">
              <Link href="/">
                <div className="w-12 h-12 bg-gradient-primary rounded-2xl flex items-center justify-center text-white text-xl font-bold shadow-lg">
                  👶
                </div>
              </Link>
              <Link href="/" className="font-bold text-2xl text-primary">Baby Tracker</Link>
            </div>
            <p className="max-w-md text-secondary text-lg leading-relaxed">
              A privacy-first, self-hostable solution for tracking your baby&apos;s development.
            </p>
          </div>
          <div className="grid grid-cols-2 md:grid-cols-3 gap-12">
            <div>
              <h4 className="font-semibold mb-6 text-primary text-lg">Links</h4>
              <ul className="space-y-4">
                <li><Link href="/#features" className="text-secondary hover:text-primary link-underline transition-all duration-300">Features</Link></li>
                <li><Link href="/#tech-stack" className="text-secondary hover:text-primary link-underline transition-all duration-300">Tech Stack</Link></li>
                <li><Link href="/api-docs" className="text-secondary hover:text-primary link-underline transition-all duration-300">API</Link></li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold mb-6 text-primary text-lg">Resources</h4>
              <ul className="space-y-4">
                <li><Link href="/setup-guide" className="text-secondary hover:text-primary link-underline transition-all duration-300">Setup Guide</Link></li>
                <li><Link href="/contribute" className="text-secondary hover:text-primary link-underline transition-all duration-300">Contribute</Link></li>
                <li><Link href="/testing-guide" className="text-secondary hover:text-primary link-underline transition-all duration-300">Testing Guide</Link></li>
                <li><Link href="/deployment-guide" className="text-secondary hover:text-primary link-underline transition-all duration-300">Deployment</Link></li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold mb-6 text-primary text-lg">Connect</h4>
              <ul className="space-y-4">
                <li>
                  <a 
                    href="https://github.com/theamazingmrb/baby-tracker-api" 
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
  );
}
