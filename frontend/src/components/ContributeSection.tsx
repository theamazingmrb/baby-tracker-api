import React from 'react';

const ContributeSection = () => {
  return (
    <section className="py-16" id="contribute">
      <div className="container-padded">
        <div className="text-center mb-12">
          <h2 className="text-3xl font-bold mb-4 text-gray-900">Contributing to Baby Tracker</h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Join our community and help make Baby Tracker better for everyone
          </p>
        </div>
        
        <div className="max-w-4xl mx-auto">
          <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden mb-8 transition-all hover:-translate-y-0.5 hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl font-bold mb-4 text-gray-900">Ways to Contribute</h3>
              
              <div className="grid md:grid-cols-2 gap-6">
                <div className="space-y-4">
                  <div className="flex items-start">
                    <div className="bg-green-100 p-2 rounded-md mr-3 mt-1">
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                      </svg>
                    </div>
                    <div>
                      <h4 className="font-bold text-gray-900">🐛 Report Bugs</h4>
                      <p className="text-gray-900 text-sm">Found an issue? Help us fix it by reporting detailed bug reports.</p>
                    </div>
                  </div>
                  
                  <div className="flex items-start">
                    <div className="bg-blue-100 p-2 rounded-md mr-3 mt-1">
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                      </svg>
                    </div>
                    <div>
                      <h4 className="font-bold text-gray-900">💡 Suggest Features</h4>
                      <p className="text-gray-900 text-sm">Have ideas for new features? Share them with the community.</p>
                    </div>
                  </div>
                  
                  <div className="flex items-start">
                    <div className="bg-purple-100 p-2 rounded-md mr-3 mt-1">
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-purple-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
                      </svg>
                    </div>
                    <div>
                      <h4 className="font-bold text-gray-900">🔧 Write Code</h4>
                      <p className="text-gray-900 text-sm">Contribute new features, fix bugs, or improve existing functionality.</p>
                    </div>
                  </div>
                </div>
                
                <div className="space-y-4">
                  <div className="flex items-start">
                    <div className="bg-yellow-100 p-2 rounded-md mr-3 mt-1">
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-yellow-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                      </svg>
                    </div>
                    <div>
                      <h4 className="font-bold text-gray-900">📚 Improve Documentation</h4>
                      <p className="text-gray-900 text-sm">Help others by improving docs, guides, and API references.</p>
                    </div>
                  </div>
                  
                  <div className="flex items-start">
                    <div className="bg-red-100 p-2 rounded-md mr-3 mt-1">
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                      </svg>
                    </div>
                    <div>
                      <h4 className="font-bold text-gray-900">🔒 Security Review</h4>
                      <p className="text-gray-900 text-sm">Help keep Baby Tracker secure by reviewing code and reporting vulnerabilities.</p>
                    </div>
                  </div>
                  
                  <div className="flex items-start">
                    <div className="bg-indigo-100 p-2 rounded-md mr-3 mt-1">
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                      </svg>
                    </div>
                    <div>
                      <h4 className="font-bold text-gray-900">🤝 Community Support</h4>
                      <p className="text-gray-900 text-sm">Help other users with questions and share your experience.</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden mb-8 transition-all hover:-translate-y-0.5 hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl font-bold mb-4">Getting Started with Development</h3>
              
              <div className="space-y-6">
                <div>
                  <h4 className="font-bold mb-2 flex items-center">
                    <span className="bg-indigo-100 text-indigo-600 w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">1</span>
                    Fork & Clone
                  </h4>
                  <div className="ml-11">
                    <p className="text-gray-800 mb-2">Fork the repository and clone your copy:</p>
                    <div className="bg-slate-900 text-slate-100 p-3 rounded-xl font-mono text-sm ring-1 ring-white/10">
                      <div>git clone https://github.com/YOUR-USERNAME/baby-tracker-api.git</div>
                      <div>cd baby-tracker-api</div>
                      <div>git remote add upstream https://github.com/theamazingmrb/baby-tracker-api.git</div>
                    </div>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-bold mb-2 flex items-center">
                    <span className="bg-indigo-100 text-indigo-600 w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">2</span>
                    Set Up Development Environment
                  </h4>
                  <div className="ml-11">
                    <p className="text-gray-800 mb-2">Follow the <a href="#setup" className="text-blue-600 hover:underline">setup instructions</a> above to get your development environment running.</p>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-bold mb-2 flex items-center">
                    <span className="bg-indigo-100 text-indigo-600 w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">3</span>
                    Create a Feature Branch
                  </h4>
                  <div className="ml-11">
                    <div className="bg-slate-900 text-slate-100 p-3 rounded-xl font-mono text-sm ring-1 ring-white/10">
                      <div className="text-gray-400"># Create a new branch for your work</div>
                      <div>git checkout -b feature/your-feature-name</div>
                      <br />
                      <div className="text-gray-400"># Or for bug fixes:</div>
                      <div>git checkout -b fix/issue-description</div>
                    </div>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-bold mb-2 flex items-center">
                    <span className="bg-indigo-100 text-indigo-600 w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">4</span>
                    Make Your Changes
                  </h4>
                  <div className="ml-11">
                    <p className="text-gray-800 mb-2">Implement your feature or fix following our coding standards:</p>
                    <ul className="list-disc list-inside text-sm text-gray-800 space-y-1">
                      <li>Follow PEP 8 for Python code style</li>
                      <li>Add type hints to new functions</li>
                      <li>Write docstrings for classes and functions</li>
                      <li>Add tests for new functionality</li>
                      <li>Update documentation if needed</li>
                    </ul>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-bold mb-2 flex items-center">
                    <span className="bg-indigo-100 text-indigo-600 w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">5</span>
                    Test Your Changes
                  </h4>
                  <div className="ml-11">
                    <div className="bg-slate-900 text-slate-100 p-3 rounded-xl font-mono text-sm ring-1 ring-white/10">
                      <div className="text-gray-400"># Run the test suite</div>
                      <div>python manage.py test</div>
                      <br />
                      <div className="text-gray-400"># Run specific tests</div>
                      <div>python manage.py test tracker.tests.test_your_feature</div>
                      <br />
                      <div className="text-gray-400"># Check code style</div>
                      <div>flake8 .</div>
                    </div>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-bold mb-2 flex items-center">
                    <span className="bg-indigo-100 text-indigo-600 w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm">6</span>
                    Submit Your Pull Request
                  </h4>
                  <div className="ml-11">
                    <div className="bg-slate-900 text-slate-100 p-3 rounded-xl font-mono text-sm mb-3 ring-1 ring-white/10">
                      <div className="text-gray-400"># Commit your changes</div>
                      <div>git add .</div>
                      <div>git commit -m "Add: descriptive commit message"</div>
                      <br />
                      <div className="text-gray-400"># Push to your fork</div>
                      <div>git push origin feature/your-feature-name</div>
                    </div>
                    <p className="text-gray-700 text-sm">Then create a pull request on GitHub with a clear description of your changes.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden mb-8 transition-all hover:-translate-y-0.5 hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl font-bold mb-4 text-gray-900">Code Style & Standards</h3>
              
              <div className="grid md:grid-cols-2 gap-6">
                <div>
                  <h4 className="font-bold mb-2 text-gray-900">Python Standards</h4>
                  <ul className="list-disc list-inside text-sm text-gray-700 space-y-1">
                    <li>Follow PEP 8 style guide</li>
                    <li>Use type hints for function parameters</li>
                    <li>Write descriptive docstrings</li>
                    <li>Keep functions under 50 lines when possible</li>
                    <li>Use meaningful variable names</li>
                  </ul>
                </div>
                
                <div>
                  <h4 className="font-bold mb-2 text-gray-900">Django Conventions</h4>
                  <ul className="list-disc list-inside text-sm text-gray-700 space-y-1">
                    <li>Follow Django naming conventions</li>
                    <li>Use Django's built-in features when possible</li>
                    <li>Write tests for all views and models</li>
                    <li>Use proper permission classes</li>
                    <li>Follow REST API best practices</li>
                  </ul>
                </div>
                
                <div>
                  <h4 className="font-bold mb-2 text-gray-900">Git Workflow</h4>
                  <ul className="list-disc list-inside text-sm text-gray-700 space-y-1">
                    <li>Use descriptive commit messages</li>
                    <li>One feature per pull request</li>
                    <li>Keep commits small and focused</li>
                    <li>Rebase before submitting PR</li>
                    <li>Reference issues in commit messages</li>
                  </ul>
                </div>
                
                <div>
                  <h4 className="font-bold mb-2 text-gray-900">Testing Requirements</h4>
                  <ul className="list-disc list-inside text-sm text-gray-700 space-y-1">
                    <li>Write tests for new features</li>
                    <li>Maintain high test coverage</li>
                    <li>Include edge case testing</li>
                    <li>Test both success and error paths</li>
                    <li>Use Django's TestCase class</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          
          <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden transition-all hover:-translate-y-0.5 hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl font-bold mb-4 text-gray-900">Issue Reporting & Feature Requests</h3>
              <p className="mb-4 text-gray-800">
                Help us improve Baby Tracker by reporting issues or suggesting new features:
              </p>
              
              <div className="grid md:grid-cols-2 gap-6">
                <div>
                  <h4 className="font-bold mb-2 text-gray-900">🐛 Bug Reports</h4>
                  <p className="text-sm text-gray-800 mb-2">Include the following information:</p>
                  <ul className="list-disc list-inside text-sm text-gray-700 space-y-1">
                    <li>Steps to reproduce the issue</li>
                    <li>Expected vs. actual behavior</li>
                    <li>Environment details (OS, Python version)</li>
                    <li>Error messages or logs</li>
                    <li>Screenshots if applicable</li>
                  </ul>
                </div>
                
                <div>
                  <h4 className="font-bold mb-2 text-gray-900">💡 Feature Requests</h4>
                  <p className="text-sm text-gray-800 mb-2">Help us understand your needs:</p>
                  <ul className="list-disc list-inside text-sm text-gray-700 space-y-1">
                    <li>Describe the feature clearly</li>
                    <li>Explain the use case and benefits</li>
                    <li>Provide examples if possible</li>
                    <li>Consider implementation complexity</li>
                    <li>Check if similar features exist</li>
                  </ul>
                </div>
              </div>
              
              <div className="mt-6 p-4 bg-indigo-50 rounded-xl border border-indigo-100">
                <h4 className="font-semibold text-blue-900 mb-2">📋 Issue Templates</h4>
                <p className="text-sm text-blue-800">We provide issue templates to help you include all necessary information. Choose the appropriate template when creating a new issue.</p>
              </div>
            </div>
            
            <div className="bg-gray-50 px-6 py-4">
              <div className="flex flex-col sm:flex-row justify-center items-center space-y-3 sm:space-y-0 sm:space-x-4">
                <a 
                  href="https://github.com/theamazingmrb/baby-tracker-api/issues/new?template=bug_report.md" 
                  className="btn-primary"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Report Bug
                </a>
                <a 
                  href="https://github.com/theamazingmrb/baby-tracker-api/issues/new?template=feature_request.md" 
                  className="btn-ghost"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Request Feature
                </a>
                <a 
                  href="https://github.com/theamazingmrb/baby-tracker-api/discussions" 
                  className="btn-ghost"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Ask Question
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ContributeSection;