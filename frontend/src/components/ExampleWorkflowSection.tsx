import React from 'react';

const ExampleWorkflowSection = () => {
  return (
    <section className="py-16 bg-gray-50 dark:bg-slate-900" id="workflow-examples">
      <div className="container-padded">
        <div className="text-center mb-12">
          <h2 className="text-3xl font-bold mb-4 text-primary">Complete API Workflow Examples</h2>
          <p className="text-xl text-gray-900 max-w-3xl mx-auto">
            Follow these step-by-step examples to understand how to use the Baby Tracker API for common workflows
          </p>
        </div>

        <div className="max-w-4xl mx-auto">
          <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden transition-shadow hover:shadow-lg mb-8">
            <div className="p-6">
              <h3 className="text-xl text-gray-900 font-bold mb-4">Complete User Journey</h3>
              <p className="mb-6 text-gray-900">
                This example demonstrates a complete workflow from user registration to tracking various baby activities.
              </p>

              <div className="space-y-8">
                {/* Step 1: Register a new user */}
                <div>
                  <h4 className="font-semibold mb-2 text-gray-900 flex items-center">
                    <span className="bg-primary text-black rounded-full w-6 h-6 inline-flex items-center justify-center mr-2">1</span>
                    Register a New User
                  </h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl text-sm font-mono overflow-x-auto ring-1 ring-white/10">
                    <div className="text-blue-400">POST /api/register/</div>
                    <div className="mt-2">{`{
  "username": "parent123",
  "email": "parent@example.com",
  "password": "securepassword123"
}`}</div>
                    <div className="mt-4 text-green-400">Response (201 Created):</div>
                    <div className="mt-2">{`{
  "message": "User created successfully",
  "tokens": {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
}`}</div>
                  </div>
                </div>

                {/* Step 2: Create a baby profile */}
                <div>
                  <h4 className="font-semibold mb-2 text-gray-900 flex items-center">
                    <span className="bg-primary text-black rounded-full w-6 h-6 inline-flex items-center justify-center mr-2">2</span>
                    Create a Baby Profile
                  </h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl text-sm font-mono overflow-x-auto ring-1 ring-white/10">
                    <div className="text-blue-400">POST /api/babies/</div>
                    <div className="text-yellow-400">Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...</div>
                    <div className="mt-2">{`{
  "name": "Emma Smith",
  "birth_date": "2024-01-15",
  "gender": "female"
}`}</div>
                    <div className="mt-4 text-green-400">Response (201 Created):</div>
                    <div className="mt-2">{`{
  "id": 1,
  "name": "Emma Smith",
  "birth_date": "2024-01-15",
  "gender": "female",
  "user": 1
}`}</div>
                  </div>
                </div>

                {/* Step 3: Log a feeding */}
                <div>
                  <h4 className="font-semibold mb-2 text-gray-900 flex items-center">
                    <span className="bg-primary text-black rounded-full w-6 h-6 inline-flex items-center justify-center mr-2">3</span>
                    Log a Feeding Session
                  </h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl text-sm font-mono overflow-x-auto ring-1 ring-white/10">
                    <div className="text-blue-400">POST /api/feedings/</div>
                    <div className="text-yellow-400">Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...</div>
                    <div className="mt-2">{`{
  "baby": 1,
  "feeding_type": "breastfeeding",
  "quantity": 4.0,
  "last_side": "left_feeding"
}`}</div>
                    <div className="mt-4 text-green-400">Response (201 Created):</div>
                    <div className="mt-2">{`{
  "id": 1,
  "baby": 1,
  "time": "2025-08-27T14:30:00Z",
  "feeding_type": "breastfeeding",
  "quantity": 4.0,
  "last_side": "left_feeding"
}`}</div>
                  </div>
                </div>

                {/* Step 4: Record a diaper change */}
                <div>
                  <h4 className="font-semibold mb-2 text-gray-900 flex items-center">
                    <span className="bg-primary text-black rounded-full w-6 h-6 inline-flex items-center justify-center mr-2">4</span>
                    Record a Diaper Change
                  </h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl text-sm font-mono overflow-x-auto ring-1 ring-white/10">
                    <div className="text-blue-400">POST /api/diaper-changes/</div>
                    <div className="text-yellow-400">Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...</div>
                    <div className="mt-2">{`{
  "baby": 1,
  "diaper_type": "wet"
}`}</div>
                    <div className="mt-4 text-green-400">Response (201 Created):</div>
                    <div className="mt-2">{`{
  "id": 1,
  "baby": 1,
  "time": "2025-08-27T15:05:23Z",
  "diaper_type": "wet"
}`}</div>
                  </div>
                </div>

                {/* Step 5: Add a developmental milestone */}
                <div>
                  <h4 className="font-semibold mb-2 text-gray-900 flex items-center">
                    <span className="bg-primary text-black rounded-full w-6 h-6 inline-flex items-center justify-center mr-2">5</span>
                    Add a Developmental Milestone
                  </h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl text-sm font-mono overflow-x-auto ring-1 ring-white/10">
                    <div className="text-blue-400">POST /api/babies/1/milestones/</div>
                    <div className="text-yellow-400">Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...</div>
                    <div className="mt-2">{`{
  "title": "First Smile",
  "category": "social",
  "date_achieved": "2024-02-20",
  "notes": "Emma smiled for the first time during morning feeding"
}`}</div>
                    <div className="mt-4 text-green-400">Response (201 Created):</div>
                    <div className="mt-2">{`{
  "id": 1,
  "baby": 1,
  "title": "First Smile",
  "category": "social",
  "date_achieved": "2024-02-20",
  "notes": "Emma smiled for the first time during morning feeding"
}`}</div>
                  </div>
                </div>

                {/* Step 6: Schedule a doctor appointment */}
                <div>
                  <h4 className="font-semibold mb-2 text-gray-900 flex items-center">
                    <span className="bg-primary text-black rounded-full w-6 h-6 inline-flex items-center justify-center mr-2">6</span>
                    Schedule a Doctor Appointment
                  </h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl text-sm font-mono overflow-x-auto ring-1 ring-white/10">
                    <div className="text-blue-400">POST /api/doctor-appointments/</div>
                    <div className="text-yellow-400">Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...</div>
                    <div className="mt-2">{`{
  "baby": 1,
  "doctor_name": "Dr. Johnson",
  "appointment_date": "2024-03-15T10:30:00Z",
  "notes": "2-month checkup and vaccinations"
}`}</div>
                    <div className="mt-4 text-green-400">Response (201 Created):</div>
                    <div className="mt-2">{`{
  "id": 1,
  "baby": 1,
  "doctor_name": "Dr. Johnson",
  "appointment_date": "2024-03-15T10:30:00Z",
  "notes": "2-month checkup and vaccinations"
}`}</div>
                  </div>
                </div>

                {/* Step 7: Update a milestone */}
                <div>
                  <h4 className="font-semibold mb-2 text-gray-900 flex items-center">
                    <span className="bg-primary text-black rounded-full w-6 h-6 inline-flex items-center justify-center mr-2">7</span>
                    Update a Milestone
                  </h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl text-sm font-mono overflow-x-auto ring-1 ring-white/10">
                    <div className="text-blue-400">PUT /api/babies/1/milestones/1/</div>
                    <div className="text-yellow-400">Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...</div>
                    <div className="mt-2">{`{
  "title": "First Smile",
  "category": "social",
  "date_achieved": "2024-02-18",
  "notes": "Emma smiled for the first time during morning feeding. Updated with correct date."
}`}</div>
                    <div className="mt-4 text-green-400">Response (200 OK):</div>
                    <div className="mt-2">{`{
  "id": 1,
  "baby": 1,
  "title": "First Smile",
  "category": "social",
  "date_achieved": "2024-02-18",
  "notes": "Emma smiled for the first time during morning feeding. Updated with correct date."
}`}</div>
                  </div>
                </div>

                {/* Step 8: Get AI insights */}
                <div>
                  <h4 className="font-semibold mb-2 text-gray-900 flex items-center">
                    <span className="bg-primary text-black rounded-full w-6 h-6 inline-flex items-center justify-center mr-2">8</span>
                    Get AI Insights
                  </h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl text-sm font-mono overflow-x-auto ring-1 ring-white/10">
                    <div className="text-blue-400">GET /api/babies/1/ai-insights/?type=comprehensive</div>
                    <div className="text-yellow-400">Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...</div>
                    <div className="mt-4 text-green-400">Response (200 OK):</div>
                    <div className="mt-2">{`{
  "insights": [
    {
      "type": "feeding",
      "content": "Emma is feeding well with an average of 4oz per feeding. Consider alternating between left and right sides for balanced feeding."
    },
    {
      "type": "development",
      "content": "Emma's first smile at 34 days is right on track with typical developmental milestones."
    },
    {
      "type": "health",
      "content": "Don't forget the upcoming doctor's appointment on March 15th for important vaccinations."
    }
  ]
}`}</div>
                  </div>
                </div>

                {/* Step 9: Delete a record */}
                <div>
                  <h4 className="font-semibold mb-2 text-gray-900 flex items-center">
                    <span className="bg-primary text-black rounded-full w-6 h-6 inline-flex items-center justify-center mr-2">9</span>
                    Delete a Record
                  </h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl text-sm font-mono overflow-x-auto ring-1 ring-white/10">
                    <div className="text-blue-400">DELETE /api/doctor-appointments/1/</div>
                    <div className="text-yellow-400">Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...</div>
                    <div className="mt-4 text-green-400">Response (204 No Content)</div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden transition-shadow hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl text-gray-900 font-bold mb-4">Batch Operations</h3>
              <p className="mb-6 text-secondary text-gray-900">
                For efficiency, you can retrieve multiple records at once using filtering parameters.
              </p>

              <div className="space-y-8">
                {/* Example 1: Get all feedings for a specific date range */}
                <div>
                  <h4 className="font-semibold mb-2 text-gray-900">Get All Feedings for a Date Range</h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl text-sm font-mono overflow-x-auto ring-1 ring-white/10">
                    <div className="text-blue-400">GET /api/feedings/?baby=1&start_date=2024-02-01&end_date=2024-02-07</div>
                    <div className="text-yellow-400">Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...</div>
                    <div className="mt-4 text-green-400">Response (200 OK):</div>
                    <div className="mt-2">{`{
  "count": 15,
  "next": "http://api.example.com/api/feedings/?baby=1&end_date=2024-02-07&page=2&start_date=2024-02-01",
  "previous": null,
  "results": [
    {
      "id": 42,
      "baby": 1,
      "time": "2024-02-01T08:30:00Z",
      "feeding_type": "breastfeeding",
      "quantity": 3.5,
      "last_side": "left_feeding"
    },
    {
      "id": 43,
      "baby": 1,
      "time": "2024-02-01T12:15:00Z",
      "feeding_type": "bottle",
      "quantity": 4.0,
      "last_side": null
    },
    // ... more results
  ]
}`}</div>
                  </div>
                </div>

                {/* Example 2: Get all milestones by category */}
                <div>
                  <h4 className="font-semibold mb-2 text-gray-900">Get All Milestones by Category</h4>
                  <div className="bg-slate-900 text-slate-100 p-4 rounded-xl text-sm font-mono overflow-x-auto ring-1 ring-white/10">
                    <div className="text-blue-400">GET /api/babies/1/milestones/?category=physical</div>
                    <div className="text-yellow-400">Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...</div>
                    <div className="mt-4 text-green-400">Response (200 OK):</div>
                    <div className="mt-2">{`{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 5,
      "baby": 1,
      "title": "Holds Head Up",
      "category": "physical",
      "date_achieved": "2024-03-10",
      "notes": "Emma can hold her head up during tummy time for about 30 seconds"
    },
    {
      "id": 8,
      "baby": 1,
      "title": "Rolls Over",
      "category": "physical",
      "date_achieved": "2024-04-15",
      "notes": "First rolled from back to tummy"
    },
    {
      "id": 12,
      "baby": 1,
      "title": "Sits Unassisted",
      "category": "physical",
      "date_achieved": "2024-06-20",
      "notes": "Can sit without support for about a minute"
    }
  ]
}`}</div>
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

export default ExampleWorkflowSection;
