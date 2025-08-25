import React from 'react';

const ApiSection = () => {
  return (
    <section className="py-16 bg-gray-50 dark:bg-slate-900" id="api">
      <div className="container-padded">
        <div className="text-center mb-12">
          <h2 className="text-3xl font-bold mb-4 text-primary">API Documentation</h2>
          <p className="text-xl text-gray-900 max-w-3xl mx-auto">
            Explore Baby Tracker&apos;s RESTful API endpoints for all your baby tracking needs
          </p>
        </div>
        
        <div className="max-w-4xl mx-auto">
          <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden transition-shadow hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl font-bold mb-4 text-primary">RESTful Endpoints</h3>
              <p className="mb-6 text-secondary">
                Baby Tracker provides a comprehensive set of RESTful endpoints for tracking all aspects of your baby&apos;s development.
                The API is fully documented with Swagger/OpenAPI and includes authentication, filtering, and pagination.
              </p>
              
              <div className="overflow-x-auto">
                <table className="min-w-full divide-y divide-gray-200">
                  <thead className="bg-slate-900">
                    <tr>
                      <th scope="col" className="px-6 py-3 text-left text-xs font-bold text-white uppercase tracking-wider">
                        Endpoint
                      </th>
                      <th scope="col" className="px-6 py-3 text-left text-xs font-bold text-white uppercase tracking-wider">
                        Description
                      </th>
                      <th scope="col" className="px-6 py-3 text-left text-xs font-bold text-white uppercase tracking-wider">
                        Methods
                      </th>
                    </tr>
                  </thead>
                  <tbody className="bg-slate-800 divide-y divide-slate-700">
                    <tr className="hover:bg-slate-700">
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-accent">
                        /api/register/
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white">
                        User registration with JWT token response
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white font-mono">
                        POST
                      </td>
                    </tr>
                    <tr className="hover:bg-slate-700">
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-accent">
                        /api/token/
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white">
                        Obtain JWT access and refresh tokens
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white font-mono">
                        POST
                      </td>
                    </tr>
                    <tr className="hover:bg-slate-700">
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-accent">
                        /api/babies/
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white">
                        Manage baby profiles (name, birth_date, gender)
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white font-mono">
                        GET, POST, PUT, DELETE
                      </td>
                    </tr>
                    <tr className="hover:bg-slate-700">
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-accent">
                        /api/feedings/
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white">
                        Track breastfeeding, bottle feeds, and solid foods
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white font-mono">
                        GET, POST, PUT, DELETE
                      </td>
                    </tr>
                    <tr className="hover:bg-slate-700">
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-accent">
                        /api/sleep/
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white">
                        Record sleep sessions with start/end times
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white font-mono">
                        GET, POST
                      </td>
                    </tr>
                    <tr className="hover:bg-slate-700">
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-accent">
                        /api/diaper-changes/
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white">
                        Log diaper changes (wet, dirty, mixed)
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white font-mono">
                        GET, POST
                      </td>
                    </tr>
                    <tr className="hover:bg-slate-700">
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-accent">
                        /api/growth-milestones/
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white">
                        Track height, weight, and head circumference
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white font-mono">
                        GET, POST
                      </td>
                    </tr>
                    <tr className="hover:bg-slate-700">
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-accent">
                        /api/doctor-appointments/
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white">
                        Schedule and track medical appointments
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white font-mono">
                        GET, POST, PUT, DELETE
                      </td>
                    </tr>
                    <tr className="hover:bg-slate-700">
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-accent">
                        /api/babies/{`{id}`}/milestones/
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white">
                        Development milestones by category
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white font-mono">
                        GET, POST, PUT, DELETE
                      </td>
                    </tr>
                    <tr className="hover:bg-slate-700">
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-accent">
                        /api/appointments/
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white">
                        Manage doctor appointments and medical visits
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white font-mono">
                        GET, POST, PUT, DELETE
                      </td>
                    </tr>
                    <tr className="hover:bg-slate-700">
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-accent">
                        /api/pumping-sessions/
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white">
                        Track breast pumping sessions
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white font-mono">
                        GET, POST, PUT, DELETE
                      </td>
                    </tr>
                    <tr className="hover:bg-slate-700">
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-accent">
                        /api/medications/
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white">
                        Track medications and dosages
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white font-mono">
                        GET, POST, PUT, DELETE
                      </td>
                    </tr>
                    <tr className="hover:bg-slate-700">
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-accent">
                        /api/reminders/
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white">
                        Set reminders for baby care tasks
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white font-mono">
                        GET, POST, PUT, DELETE
                      </td>
                    </tr>
                    <tr className="hover:bg-slate-700">
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-accent">
                        /api/babies/{`{id}`}/ai-insights/
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white">
                        Get AI-powered insights and recommendations
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white font-mono">
                        GET
                      </td>
                    </tr>
                    <tr className="hover:bg-slate-700">
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-accent">
                        /api/babies/{`{id}`}/visualizations/
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white">
                        Get visualization data for charts and graphs
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-white font-mono">
                        GET
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            
            <div className="bg-slate-900 px-6 py-4">
              <div className="flex flex-col sm:flex-row justify-between items-center">
                <p className="text-sm text-white mb-4 sm:mb-0">
                  Full API documentation available at <code className="bg-slate-800 px-2 py-1 rounded text-yellow-400">/api/docs/</code>
                </p>
                <a 
                  href="/api/docs/" 
                  className="btn-primary"
                >
                  View Full API Docs
                </a>
              </div>
            </div>
          </div>
          
          {/* Authentication Section */}
          <div className="mt-8 bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden transition-shadow hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl font-bold mb-4 text-primary">Authentication</h3>
              <p className="mb-4 text-secondary">Baby Tracker uses JWT (JSON Web Token) authentication. All endpoints except registration and token obtaining require authentication.</p>
              
              <div className="grid md:grid-cols-2 gap-6">
                <div>
                  <h4 className="font-semibold mb-2 text-primary">Register a new user</h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl text-sm font-mono overflow-x-auto ring-1 ring-white/10">
                    <div className="text-blue-400">POST</div>
                    <div className="text-white">/api/register/</div>
                    <div className="mt-2">{`{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepassword123"
}`}</div>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-semibold mb-2 text-primary">Obtain JWT token</h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl text-sm font-mono overflow-x-auto ring-1 ring-white/10">
                    <div className="text-blue-400">POST</div>
                    <div className="text-white">/api/token/</div>
                    <div className="mt-2">{`{
  "username": "john_doe",
  "password": "securepassword123"
}`}</div>
                  </div>
                </div>
              </div>
              
              <div className="mt-4 p-4 bg-slate-900 rounded-xl ring-1 ring-white/10">
                <p className="text-sm text-slate-100">
                  <strong className="text-white">Authentication Header:</strong> Include the access token in all requests:
                  <code className="bg-slate-800 px-2 py-1 rounded ml-2 text-yellow-400">Authorization: Bearer &lt;access_token&gt;</code>
                </p>
              </div>
            </div>
          </div>
          
          {/* Examples Section */}
          <div className="mt-8 bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden transition-shadow hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl font-bold mb-4 text-primary">API Examples</h3>
              
              <div className="space-y-6">
                <div>
                  <h4 className="font-semibold mb-2 text-primary">Create a Baby Profile</h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl text-sm font-mono overflow-x-auto ring-1 ring-white/10">
                    <div className="text-blue-400">POST</div>
                    <div className="text-white">/api/babies/</div>
                    <div className="text-yellow-400">Authorization: Bearer &lt;token&gt;</div>
                    <div className="mt-2">{`{
  "name": "Emma Smith",
  "birth_date": "2024-01-15",
  "gender": "female"
}`}</div>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-semibold mb-2 text-primary">Log a Feeding Session</h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl text-sm font-mono overflow-x-auto ring-1 ring-white/10">
                    <div className="text-blue-400">POST</div>
                    <div className="text-white">/api/feedings/</div>
                    <div className="text-yellow-400">Authorization: Bearer &lt;token&gt;</div>
                    <div className="mt-2">{`{
  "baby": 1,
  "feeding_type": "breastfeeding",
  "quantity": 4.0,
  "last_side": "left_feeding"
}`}</div>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-semibold mb-2 text-primary">Get AI Insights for a Baby</h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl text-sm font-mono overflow-x-auto ring-1 ring-white/10">
                    <div className="text-blue-400">GET</div>
                    <div className="text-white">/api/babies/1/ai-insights/?type=feeding</div>
                    <div className="text-yellow-400">Authorization: Bearer &lt;token&gt;</div>
                  </div>
                  <p className="text-sm text-secondary mt-2">
                    Available insight types: <code className="bg-slate-800 px-1 py-0.5 rounded text-yellow-400">feeding</code>, <code className="bg-slate-800 px-1 py-0.5 rounded text-yellow-400">sleep</code>, <code className="bg-slate-800 px-1 py-0.5 rounded text-yellow-400">growth</code>, <code className="bg-slate-800 px-1 py-0.5 rounded text-yellow-400">diaper</code>, <code className="bg-slate-800 px-1 py-0.5 rounded text-yellow-400">comprehensive</code>, <code className="bg-slate-800 px-1 py-0.5 rounded text-yellow-400">all</code>
                  </p>
                </div>

                <div>
                  <h4 className="font-semibold mb-2 text-primary">Update an Appointment</h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl text-sm font-mono overflow-x-auto ring-1 ring-white/10">
                    <div className="text-blue-400">PUT</div>
                    <div className="text-white">/api/appointments/1/</div>
                    <div className="text-yellow-400">Authorization: Bearer &lt;token&gt;</div>
                    <div className="mt-2">{`{
  "baby": 1,
  "doctor_name": "Dr. Smith",
  "appointment_date": "2025-09-15T14:30:00Z",
  "notes": "Updated 6-month checkup appointment"
}`}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          {/* Data Models Section */}
          <div className="mt-8 bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden transition-shadow hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl font-bold mb-4 text-primary">Data Models</h3>
              <p className="mb-6 text-secondary">Understanding the data structures used in Baby Tracker API:</p>
              
              <div className="grid md:grid-cols-2 gap-6">
                <div>
                  <h4 className="font-semibold mb-2 text-primary">Baby Model</h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl text-sm font-mono overflow-x-auto ring-1 ring-white/10">
                    <ul className="space-y-2">
                      <li><span className="text-white">id:</span> <span className="text-yellow-400">integer (read-only)</span></li>
                      <li><span className="text-white">name:</span> <span className="text-yellow-400">string (required)</span></li>
                      <li><span className="text-white">birth_date:</span> <span className="text-yellow-400">date (YYYY-MM-DD)</span></li>
                      <li><span className="text-white">gender:</span> <span className="text-yellow-400">string</span></li>
                      <li><span className="text-white">user:</span> <span className="text-yellow-400">integer (read-only)</span></li>
                    </ul>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-semibold mb-2 text-primary">Feeding Model</h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl text-sm font-mono overflow-x-auto ring-1 ring-white/10">
                    <ul className="space-y-2">
                      <li><span className="text-white">id:</span> <span className="text-yellow-400">integer (read-only)</span></li>
                      <li><span className="text-white">baby:</span> <span className="text-yellow-400">integer (required)</span></li>
                      <li><span className="text-white">time:</span> <span className="text-yellow-400">datetime (auto-generated)</span></li>
                      <li><span className="text-white">feeding_type:</span> <span className="text-yellow-400">breastfeeding | bottle | solid</span></li>
                      <li><span className="text-white">quantity:</span> <span className="text-yellow-400">float (ounces/ml)</span></li>
                      <li><span className="text-white">last_side:</span> <span className="text-yellow-400">left_feeding | right_feeding | both_feeding</span></li>
                    </ul>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-semibold mb-2 text-primary">Sleep Model</h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl text-sm font-mono overflow-x-auto ring-1 ring-white/10">
                    <ul className="space-y-2">
                      <li><span className="text-white">id:</span> <span className="text-yellow-400">integer (read-only)</span></li>
                      <li><span className="text-white">baby:</span> <span className="text-yellow-400">integer (required)</span></li>
                      <li><span className="text-white">start_time:</span> <span className="text-yellow-400">datetime (required)</span></li>
                      <li><span className="text-white">end_time:</span> <span className="text-yellow-400">datetime (optional)</span></li>
                    </ul>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-semibold mb-2 text-primary">Diaper Change Model</h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl text-sm font-mono overflow-x-auto ring-1 ring-white/10">
                    <ul className="space-y-2">
                      <li><span className="text-white">id:</span> <span className="text-yellow-400">integer (read-only)</span></li>
                      <li><span className="text-white">baby:</span> <span className="text-yellow-400">integer (required)</span></li>
                      <li><span className="text-white">time:</span> <span className="text-yellow-400">datetime (auto-generated)</span></li>
                      <li><span className="text-white">diaper_type:</span> <span className="text-yellow-400">wet | dirty | mixed</span></li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ApiSection;