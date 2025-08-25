"use client";

import React from 'react';
import CodeBlock, { CodeLine } from './CodeBlock';

export default function TestingGuideSection() {
  return (
    <section id="testing-guide" className="py-16 bg-gray-50 text-black">
      <div className="container-padded">
        <div className="text-center mb-12">
          <h2 className="text-3xl font-bold mb-4 text-gray-900">Testing Guide</h2>
          <p className="text-xl text-gray-900 max-w-3xl mx-auto">
            Concrete examples and best practices for testing features in the Baby Tracker application
          </p>
        </div>

        <div className="grid md:grid-cols-2 gap-8 mb-12">
          <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden h-full transition-all hover:-translate-y-0.5 hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl font-bold mb-4 text-gray-900">Testing Framework</h3>
              <p className="text-gray-700 mb-4">
                Baby Tracker uses Django&apos;s built-in testing framework along with Django REST Framework&apos;s testing utilities:
              </p>
              <ul className="list-disc list-inside text-sm text-gray-700 space-y-2 mb-4">
                <li><code className="bg-gray-100 px-1 rounded">django.test.TestCase</code>: Base class for Django tests</li>
                <li><code className="bg-gray-100 px-1 rounded">rest_framework.test.APIClient</code>: Client for making API requests in tests</li>
                <li><code className="bg-gray-100 px-1 rounded">unittest.mock</code>: For mocking external dependencies</li>
              </ul>
            </div>
          </div>

          <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden h-full transition-all hover:-translate-y-0.5 hover:shadow-lg">
            <div className="p-6">
              <h3 className="text-xl font-bold mb-4 text-gray-900">Test Structure</h3>
              <p className="text-gray-700 mb-4">
                Tests are organized by feature/model and placed in the appropriate app&apos;s <code className="bg-gray-100 px-1 rounded">tests</code> directory:
              </p>
              <ul className="list-disc list-inside text-sm text-gray-700 space-y-2">
                <li><code className="bg-gray-100 px-1 rounded">tracker/tests/</code>: Tests for the tracker app</li>
                <li><code className="bg-gray-100 px-1 rounded">recipes/tests/</code>: Tests for the recipes app</li>
              </ul>
              <p className="text-gray-700 mt-4">
                Each test file focuses on a specific model or feature, with class names following the pattern <code className="bg-gray-100 px-1 rounded">{'{Feature}APITestCase'}</code>.
              </p>
            </div>
          </div>
        </div>

        <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden mb-8 transition-all hover:-translate-y-0.5 hover:shadow-lg">
          <div className="p-6">
            <h3 className="text-xl font-bold mb-4 text-gray-900">🧪 Example: Adding a New Feature with Tests</h3>
          
            <div className="mb-8">
              <h4 className="font-bold text-lg mb-2 text-gray-900">Step 1: Define the Model</h4>
              <CodeBlock language="python">
                <CodeLine comment highlight># tracker/models.py</CodeLine>
                <CodeLine>from django.db import models</CodeLine>
                <CodeLine>from django.conf import settings</CodeLine>
                <br />
                <CodeLine>class Medication(models.Model):</CodeLine>
                <CodeLine indent={1} comment highlight>"""Model for tracking baby medications."""</CodeLine>
                <CodeLine indent={1}>baby = models.ForeignKey('Baby', on_delete=models.CASCADE, related_name='medications')</CodeLine>
                <CodeLine indent={1}>user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)</CodeLine>
                <CodeLine indent={1}>name = models.CharField(max_length=100)</CodeLine>
                <CodeLine indent={1}>dosage = models.CharField(max_length=50)</CodeLine>
                <CodeLine indent={1}>time = models.DateTimeField()</CodeLine>
                <CodeLine indent={1}>notes = models.TextField(blank=True, null=True)</CodeLine>
                <br />
                <CodeLine indent={1}>def __str__(self):</CodeLine>
                <CodeLine indent={2}>return f"{'{'}self.name{'}'} - {'{'}self.dosage{'}'} - {'{'}self.time{'}'}"</CodeLine>
              </CodeBlock>
            </div>
          
            <div className="mb-8">
              <h4 className="font-bold text-lg mb-2 text-gray-900">Step 2: Create the Serializer</h4>
              <CodeBlock language="python">
                <CodeLine comment highlight># tracker/serializers.py</CodeLine>
                <CodeLine>from rest_framework import serializers</CodeLine>
                <CodeLine>from .models import Medication</CodeLine>
                <br />
                <CodeLine>class MedicationSerializer(serializers.ModelSerializer):</CodeLine>
                <CodeLine indent={1}>class Meta:</CodeLine>
                <CodeLine indent={2}>model = Medication</CodeLine>
                <CodeLine indent={2}>fields = ['id', 'baby', 'name', 'dosage', 'time', 'notes']</CodeLine>
                <CodeLine indent={2}>read_only_fields = ['user']</CodeLine>
              </CodeBlock>
            </div>
          
            <div className="mb-8">
              <h4 className="font-bold text-lg mb-2 text-gray-900">Step 3: Implement the View</h4>
              <CodeBlock language="python">
                <CodeLine comment highlight># tracker/views.py</CodeLine>
                <CodeLine>from rest_framework import generics</CodeLine>
                <CodeLine>from .models import Medication</CodeLine>
                <CodeLine>from .serializers import MedicationSerializer</CodeLine>
                <CodeLine>from .permissions import IsTenantUser</CodeLine>
                <br />
                <CodeLine>class MedicationListCreateView(generics.ListCreateAPIView):</CodeLine>
                <CodeLine indent={1}>serializer_class = MedicationSerializer</CodeLine>
                <CodeLine indent={1}>permission_classes = [IsTenantUser]</CodeLine>
                <br />
                <CodeLine indent={1}>def get_queryset(self):</CodeLine>
                <CodeLine indent={2}>return Medication.objects.filter(user=self.request.user)</CodeLine>
                <br />
                <CodeLine indent={1}>def perform_create(self, serializer):</CodeLine>
                <CodeLine indent={2}>serializer.save(user=self.request.user)</CodeLine>
              </CodeBlock>
            </div>
          
            <div className="mb-8">
              <h4 className="font-bold text-lg mb-2 text-gray-900">Step 4: Add URL Pattern</h4>
              <CodeBlock language="python">
                <CodeLine comment highlight># tracker/urls.py</CodeLine>
                <CodeLine>from django.urls import path</CodeLine>
                <CodeLine>from .views import MedicationListCreateView</CodeLine>
                <br />
                <CodeLine>urlpatterns = [</CodeLine>
                <CodeLine indent={1} comment highlight># ... other URL patterns</CodeLine>
                <CodeLine indent={1}>path('medications/', MedicationListCreateView.as_view(), name='medication-list'),</CodeLine>
                <CodeLine>]</CodeLine>
              </CodeBlock>
            </div>
          
            <div>
              <h4 className="font-bold text-lg mb-2 text-gray-900">Step 5: Write Tests</h4>
              <CodeBlock language="python">
                <CodeLine comment highlight># tracker/tests/test_medication_api.py</CodeLine>
                <CodeLine>from django.test import TestCase</CodeLine>
                <CodeLine>from django.contrib.auth import get_user_model</CodeLine>
                <CodeLine>from django.urls import reverse</CodeLine>
                <CodeLine>from rest_framework import status</CodeLine>
                <CodeLine>from rest_framework.test import APIClient</CodeLine>
                <CodeLine>from tracker.models import Baby, Medication</CodeLine>
                <CodeLine>from datetime import datetime</CodeLine>
                <br />
                <CodeLine>User = get_user_model()</CodeLine>
                <br />
                <CodeLine>class MedicationAPITestCase(TestCase):</CodeLine>
                <CodeLine indent={1}>def setUp(self):</CodeLine>
                <CodeLine indent={2} comment highlight># Create test users</CodeLine>
                <CodeLine indent={2}>self.user1 = User.objects.create_user(</CodeLine>
                <CodeLine indent={3}>username='testuser1',</CodeLine>
                <CodeLine indent={3}>email='test1@example.com',</CodeLine>
                <CodeLine indent={3}>password='testpassword1'</CodeLine>
                <CodeLine indent={2}>)</CodeLine>
                <br />
                <CodeLine indent={2} comment highlight># Create test babies</CodeLine>
                <CodeLine indent={2}>self.baby1 = Baby.objects.create(</CodeLine>
                <CodeLine indent={3}>name='Baby One',</CodeLine>
                <CodeLine indent={3}>birth_date='2023-01-01',</CodeLine>
                <CodeLine indent={3}>gender='Male',</CodeLine>
                <CodeLine indent={3}>user=self.user1</CodeLine>
                <CodeLine indent={2}>)</CodeLine>
                <br />
                <CodeLine indent={2} comment highlight># Setup API clients</CodeLine>
                <CodeLine indent={2}>self.client1 = APIClient()</CodeLine>
                <CodeLine indent={2}>self.client1.force_authenticate(user=self.user1)</CodeLine>
                <br />
                <CodeLine indent={1}>def test_list_medications(self):</CodeLine>
                <CodeLine indent={2} comment highlight>"""Test listing medications for authenticated user"""</CodeLine>
                <CodeLine indent={2}>url = reverse('medication-list')</CodeLine>
                <CodeLine indent={2}>response = self.client1.get(url)</CodeLine>
                <CodeLine indent={2}>self.assertEqual(response.status_code, status.HTTP_200_OK)</CodeLine>
                <br />
                <CodeLine indent={2} comment highlight># Test for proper permission handling</CodeLine>
                <CodeLine indent={2}>self.assertEqual(len(response.data), 1)</CodeLine>
                <CodeLine indent={2}>self.assertEqual(response.data[0]['name'], 'Tylenol')</CodeLine>
              </CodeBlock>
            </div>
          </div>
        </div>

        <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden mb-8 transition-all hover:-translate-y-0.5 hover:shadow-lg">
          <div className="p-6">
            <h3 className="text-xl font-bold mb-4">🤖 Testing Complex Features: AI Insights Example</h3>
          
            <p className="text-gray-700 mb-6">
              For complex features like AI insights, you&apos;ll need to test both the underlying logic and the API endpoints.
              Here&apos;s how we test the AI insights feature:
            </p>
          
            <div className="mb-8">
              <h4 className="font-bold text-lg mb-2 text-gray-900">Testing AI Insights API</h4>
              <CodeBlock language="python">
                <CodeLine comment highlight># tracker/tests/test_ai_insights_api.py</CodeLine>
                <CodeLine>from django.test import TestCase</CodeLine>
                <CodeLine>from django.contrib.auth import get_user_model</CodeLine>
                <CodeLine>from django.urls import reverse</CodeLine>
                <CodeLine>from rest_framework import status</CodeLine>
                <CodeLine>from rest_framework.test import APIClient</CodeLine>
                <CodeLine>from tracker.models import Baby, Feeding</CodeLine>
                <CodeLine>from datetime import datetime, timedelta</CodeLine>
                <br />
                <CodeLine>User = get_user_model()</CodeLine>
                <br />
                <CodeLine>class AIInsightsAPITestCase(TestCase):</CodeLine>
                <CodeLine indent={1}>def setUp(self):</CodeLine>
                <CodeLine indent={2} comment highlight># Create test users and babies</CodeLine>
                <CodeLine indent={2}>self.user1 = User.objects.create_user(</CodeLine>
                <CodeLine indent={3}>username='testuser1',</CodeLine>
                <CodeLine indent={3}>email='test1@example.com',</CodeLine>
                <CodeLine indent={3}>password='testpassword1'</CodeLine>
                <CodeLine indent={2}>)</CodeLine>
                <CodeLine indent={2}>self.baby1 = Baby.objects.create(</CodeLine>
                <CodeLine indent={3}>name='Baby One',</CodeLine>
                <CodeLine indent={3}>birth_date='2023-01-01',</CodeLine>
                <CodeLine indent={3}>gender='Male',</CodeLine>
                <CodeLine indent={3}>user=self.user1</CodeLine>
                <CodeLine indent={2}>)</CodeLine>
                <br />
                <CodeLine indent={2} comment highlight># Create test feeding data for AI analysis</CodeLine>
                <CodeLine indent={2}>base_time = datetime.now()</CodeLine>
                <CodeLine indent={2}>for i in range(10):</CodeLine>
                <CodeLine indent={3}>Feeding.objects.create(</CodeLine>
                <CodeLine indent={4}>baby=self.baby1,</CodeLine>
                <CodeLine indent={4}>user=self.user1,</CodeLine>
                <CodeLine indent={4}>start_time=base_time - timedelta(hours=i*3),</CodeLine>
                <CodeLine indent={4}>feeding_type='bottle',</CodeLine>
                <CodeLine indent={4}>quantity=120,</CodeLine>
                <CodeLine indent={4}>unit='ml'</CodeLine>
                <CodeLine indent={3}>)</CodeLine>
                <br />
                <CodeLine indent={1}>def test_feeding_insights_endpoint(self):</CodeLine>
                <CodeLine indent={2} comment highlight>"""Test feeding insights endpoint"""</CodeLine>
                <CodeLine indent={2}>url = reverse('baby-ai-insights', kwargs={'{'}'pk': self.baby1.id{'}'}) + '?type=feeding'</CodeLine>
                <CodeLine indent={2}>response = self.client1.get(url)</CodeLine>
                <CodeLine indent={2} comment highlight># Verify successful response and data structure</CodeLine>
                <CodeLine indent={2}>self.assertEqual(response.status_code, status.HTTP_200_OK)</CodeLine>
                <CodeLine indent={2}>self.assertIn('feeding_insights', response.data)</CodeLine>
              </CodeBlock>
            </div>
          
            <div>
              <h4 className="font-bold text-lg mb-2 text-gray-900">Common Testing Challenges & Solutions</h4>
              <div className="space-y-4">
                <div>
                  <h5 className="font-semibold text-gray-900">1. Timezone Issues in Tests</h5>
                  <p className="text-gray-700">
                    When working with datetime objects, timezone issues can cause test failures. Use UTC consistently and be aware of timezone conversions.
                  </p>
                  <div className="bg-gray-50 p-3 rounded-xl text-sm border border-gray-200 text-gray-800 mt-2">
                    <div className="mb-2">
                      <strong>Example Fix:</strong> When converting datetime objects to numpy arrays, use timestamps instead of np.datetime64 to avoid timezone warnings:
                    </div>
                    <CodeBlock language="python" className="p-2 mt-1 text-xs rounded-md">
                      <CodeLine comment highlight># When converting datetime objects to numpy arrays, use timestamps instead:</CodeLine>
                      <CodeLine>times = sorted(df["time"].tolist())</CodeLine>
                      <CodeLine>times_utc = [t.timestamp() for t in times]  <span className="text-yellow-500"># Convert to UTC timestamps</span></CodeLine>
                      <CodeLine>times_np = np.array(times_utc)  <span className="text-yellow-500"># Now use numpy array operations</span></CodeLine>
                    </CodeBlock>
                  </div>
                </div>
              
                <div>
                  <h5 className="font-semibold text-gray-900">2. Permission Testing</h5>
                  <p className="text-gray-700">
                    Ensure you test both successful access by owners and denied access by non-owners.
                  </p>
                  <div className="bg-gray-50 p-3 rounded-xl text-sm border border-gray-200 text-gray-800 mt-2">
                    <div className="mb-2">
                      <strong>Example Fix:</strong> Make sure your test assertions match the actual API behavior:
                    </div>
                    <CodeBlock language="python" className="p-2 mt-1 text-xs rounded-md">
                      <CodeLine comment highlight># If the API returns 400 BAD REQUEST for invalid data rather than 403 FORBIDDEN:</CodeLine>
                      <CodeLine>self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  <span className="text-yellow-500"># Not 403</span></CodeLine>
                    </CodeBlock>
                  </div>
                </div>
              
                <div>
                  <h5 className="font-semibold text-gray-900">3. URL Patterns in Tests</h5>
                  <p className="text-gray-700">
                    Always use Django&apos;s reverse() function to generate URLs instead of hardcoding them.
                  </p>
                  <div className="bg-gray-50 p-3 rounded-xl text-sm border border-gray-200 text-gray-800 mt-2">
                    <div className="mb-2">
                      <strong>Example Fix:</strong> Replace hardcoded URLs with reverse():
                    </div>
                    <CodeBlock language="python" className="p-2 mt-1 text-xs rounded-md">
                      <CodeLine comment highlight># Instead of:</CodeLine>
                      <CodeLine>url = f'/api/growth-milestones/{'{'}self.milestone1.id{'}'}/'</CodeLine>
                      <br />
                      <CodeLine comment highlight># Use:</CodeLine>
                      <CodeLine>url = reverse('growth-milestone-detail', kwargs={'{'}'pk': self.milestone1.id{'}'})</CodeLine>
                    </CodeBlock>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div className="bg-white/80 backdrop-blur-md rounded-2xl shadow-elevated border border-gray-200 overflow-hidden transition-all hover:-translate-y-0.5 hover:shadow-lg">
          <div className="p-6">
            <h3 className="text-xl font-bold mb-4 text-gray-900">Best Practices for Testing</h3>
          
            <div className="grid md:grid-cols-2 gap-8">
              <div>
                <h4 className="font-bold mb-2 text-gray-900">📋 Test Organization</h4>
                <div className="bg-gray-50 p-3 rounded-xl text-sm border border-gray-200 text-gray-800">
                  <ul className="list-disc list-inside text-sm space-y-2">
                    <li><strong>Isolation:</strong> Each test should be independent</li>
                    <li><strong>Realistic Data:</strong> Use realistic test data</li>
                    <li><strong>Comprehensive Coverage:</strong> Test both success and failure cases</li>
                    <li><strong>Clean Setup/Teardown:</strong> Properly set up and clean up test data</li>
                  </ul>
                </div>
              </div>
              
              <div>
                <h4 className="font-bold mb-2 text-gray-900">🏃‍♂️ Test Execution</h4>
                <div className="bg-gray-50 p-3 rounded-xl text-sm border border-gray-200 text-gray-800">
                  <ul className="list-disc list-inside text-sm space-y-2">
                    <li><strong>Run Specific Tests:</strong> <code className="bg-gray-100 px-1 rounded">python manage.py test tracker.tests.test_baby_api</code></li>
                    <li><strong>Run with Coverage:</strong> <code className="bg-gray-100 px-1 rounded">coverage run --source='.' manage.py test</code></li>
                    <li><strong>View Coverage Report:</strong> <code className="bg-gray-100 px-1 rounded">coverage report</code></li>
                    <li><strong>CI Integration:</strong> Tests run automatically on GitHub Actions</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
