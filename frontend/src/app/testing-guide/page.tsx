import React from 'react';
import Link from 'next/link';
import TestingGuideSection from '../../components/TestingGuideSection';

export default function TestingGuidePage() {
  return (
    <main className="min-h-screen bg-gradient-to-b from-blue-50 to-white">
      <div className="container mx-auto px-4 py-12">
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-center mb-2 text-gray-900">Baby Tracker Testing Guide</h1>
          <p className="text-center text-gray-600 max-w-3xl mx-auto">
            A comprehensive guide for testing the Baby Tracker application
          </p>
        </div>
        
        <TestingGuideSection />
        
        <div className="mt-12 text-center">
          <Link 
            href="/" 
            className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            ← Back to Home
          </Link>
        </div>
      </div>
    </main>
  );
}
