"use client";

import React, { useState } from 'react';
import Link from 'next/link';

export default function Header() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  return (
    <header className="sticky top-0 z-50">
      <nav className="container-padded py-4 glass-strong backdrop-blur-md border-b border-border/50">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Link href="/">
              <div className="w-10 h-10 bg-gradient-primary rounded-2xl flex items-center justify-center text-white text-xl font-bold shadow-lg">
                👶
              </div>
            </Link>
            <Link href="/" className="text-xl font-bold text-primary tracking-tight">Baby Tracker</Link>
          </div>
          <div className="hidden lg:flex items-center gap-8 text-sm font-medium">
            <Link href="/#features" className="text-secondary hover:text-primary link-underline transition-all duration-300">Features</Link>
            <Link href="/#tech-stack" className="text-secondary hover:text-primary link-underline transition-all duration-300">Tech Stack</Link>
            <Link href="/api-docs" className="text-secondary hover:text-primary link-underline transition-all duration-300">API</Link>
            <Link href="/setup-guide" className="text-secondary hover:text-primary link-underline transition-all duration-300">Setup</Link>
            <Link href="/contribute" className="text-secondary hover:text-primary link-underline transition-all duration-300">Contribute</Link>
            <Link href="/testing-guide" className="text-secondary hover:text-primary link-underline transition-all duration-300">Testing Guide</Link>
            <Link href="/deployment-guide" className="text-secondary hover:text-primary link-underline transition-all duration-300">Deployment</Link>
          </div>
          <div className="flex items-center gap-2 sm:gap-3">
            <a href="/api/docs/" className="btn-primary whitespace-nowrap text-xs sm:text-sm px-3 sm:px-6 py-2 flex-shrink-0">
              <span className="hidden sm:inline">API Docs</span>
              <span className="sm:hidden">API</span>
            </a>
            {/* Mobile menu button */}
            <button 
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="lg:hidden p-2 rounded-xl bg-surface border border-border flex-shrink-0 hover:bg-gray-100 transition-colors"
              aria-label="Toggle mobile menu"
            >
              <svg className="w-5 h-5 text-secondary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                {mobileMenuOpen ? (
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                ) : (
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                )}
              </svg>
            </button>
          </div>
        </div>

        {/* Mobile menu dropdown */}
        {mobileMenuOpen && (
          <div className="lg:hidden mt-4 pb-2 border-t border-border/50 pt-4">
            <div className="flex flex-col space-y-4">
              <Link 
                href="/#features" 
                className="text-secondary hover:text-primary transition-all duration-300 px-2 py-1"
                onClick={() => setMobileMenuOpen(false)}
              >
                Features
              </Link>
              <Link 
                href="/#tech-stack" 
                className="text-secondary hover:text-primary transition-all duration-300 px-2 py-1"
                onClick={() => setMobileMenuOpen(false)}
              >
                Tech Stack
              </Link>
              <Link 
                href="/api-docs" 
                className="text-secondary hover:text-primary transition-all duration-300 px-2 py-1"
                onClick={() => setMobileMenuOpen(false)}
              >
                API
              </Link>
              <Link 
                href="/setup-guide" 
                className="text-secondary hover:text-primary transition-all duration-300 px-2 py-1"
                onClick={() => setMobileMenuOpen(false)}
              >
                Setup
              </Link>
              <Link 
                href="/contribute" 
                className="text-secondary hover:text-primary transition-all duration-300 px-2 py-1"
                onClick={() => setMobileMenuOpen(false)}
              >
                Contribute
              </Link>
              <Link 
                href="/testing-guide" 
                className="text-secondary hover:text-primary transition-all duration-300 px-2 py-1"
                onClick={() => setMobileMenuOpen(false)}
              >
                Testing Guide
              </Link>
              <Link 
                href="/deployment-guide" 
                className="text-secondary hover:text-primary transition-all duration-300 px-2 py-1"
                onClick={() => setMobileMenuOpen(false)}
              >
                Deployment
              </Link>
            </div>
          </div>
        )}
      </nav>
    </header>
  );
}
