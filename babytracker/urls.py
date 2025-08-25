"""
URL configuration for babytracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from .views import serve_nextjs, NextJSStaticView

urlpatterns = [
    # Django Admin
    path("admin/", admin.site.urls),
    
    # API endpoints - these take precedence over frontend routes
    path("api/tracker/", include("tracker.urls")),
    path("api/recipes/", include("recipes.urls")),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    # Serve Next.js static files with more specific patterns first
    re_path(r'^_next/static/chunks/(?P<path>.*)$', NextJSStaticView.as_view(), name='nextjs_chunks'),
    re_path(r'^_next/static/(?P<path>.*)$', NextJSStaticView.as_view(), name='nextjs_static_files'),
    re_path(r'^_next/(?P<path>.*)$', NextJSStaticView.as_view(), name='nextjs_static'),
    
    # Handle specific Next.js assets
    re_path(r'^(?P<path>favicon\.ico)$', NextJSStaticView.as_view(), name='nextjs_favicon'),
    re_path(r'^(?P<path>.*\.svg)$', NextJSStaticView.as_view(), name='nextjs_svg'),
    
    # Handle font files specifically
    re_path(r'^(?P<path>.*\.(woff|woff2|ttf|eot|otf))$', NextJSStaticView.as_view(), name='nextjs_fonts'),
    
    # Handle other static assets from Next.js
    re_path(r'^(?P<path>.*\.(js|css|png|jpg|jpeg|ico|json))$', NextJSStaticView.as_view(), name='nextjs_assets'),
    
    # Catch-all pattern for frontend routes - serves appropriate HTML files
    re_path(r'^(?P<path>.*)$', serve_nextjs, name='nextjs_app'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
