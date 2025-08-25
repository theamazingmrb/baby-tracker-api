from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.http import HttpResponse
import os
import logging

logger = logging.getLogger(__name__)

# Serve Next.js app
@never_cache
def serve_nextjs(request):
    # Serve the Next.js app's index.html from the build output directory
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        index_path = os.path.join(base_dir, 'frontend', 'out', 'index.html')
        
        # Check if the Next.js build exists
        if os.path.exists(index_path):
            with open(index_path, 'rb') as f:
                content = f.read()
            return HttpResponse(content, content_type='text/html')
        else:
            logger.warning(f"Next.js build not found at {index_path}")
            # Fallback to the old template if Next.js build is not available
            return render(request, 'landing.html')
    except Exception as e:
        logger.error(f"Error serving Next.js app: {str(e)}")
        # Fallback to the old template if there's an error
        return render(request, 'index.html')

# Serve static Next.js files
class NextJSStaticView(TemplateView):
    """
    Serve static files from the Next.js build
    """
    def get(self, request, path):
        try:
            # Normalize the path to prevent directory traversal
            path = os.path.normpath(path).lstrip('/')
            
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            file_path = os.path.join(base_dir, 'frontend', 'out', path)
            logger.info(f"Looking for Next.js static file at: {file_path}")
            
            # Check if the file exists before trying to open it
            if not os.path.exists(file_path):
                logger.warning(f"Next.js static file not found at {file_path}")
                
                # Try various fallback paths
                fallback_paths = [
                    # Try in _next directory
                    os.path.join(base_dir, 'frontend', 'out', '_next', path),
                    # Try in static directory
                    os.path.join(base_dir, 'frontend', 'out', '_next', 'static', path),
                    # Try in chunks directory
                    os.path.join(base_dir, 'frontend', 'out', '_next', 'static', 'chunks', path),
                    # Try in css directory
                    os.path.join(base_dir, 'frontend', 'out', '_next', 'static', 'css', path),
                ]
                
                for fallback_path in fallback_paths:
                    if os.path.exists(fallback_path):
                        file_path = fallback_path
                        logger.info(f"Found file at fallback path: {fallback_path}")
                        break
                else:  # No fallback found
                    logger.error(f"File not found in any location: {path}")
                    return HttpResponse(status=404)
                
            with open(file_path, 'rb') as f:
                content_type = self._get_content_type(path)
                response = HttpResponse(f.read(), content_type=content_type)
                # Add cache headers for static assets
                response['Cache-Control'] = 'public, max-age=31536000'
                return response
        except Exception as e:
            logger.error(f"Error serving Next.js static file {path}: {str(e)}")
            return HttpResponse(status=404)
    
    def _get_content_type(self, path):
        """
        Determine content type based on file extension
        """
        if path.endswith('.html'):
            return 'text/html'
        elif path.endswith('.js'):
            return 'application/javascript'
        elif path.endswith('.css'):
            return 'text/css'
        elif path.endswith('.json'):
            return 'application/json'
        elif path.endswith('.png'):
            return 'image/png'
        elif path.endswith('.jpg') or path.endswith('.jpeg'):
            return 'image/jpeg'
        elif path.endswith('.svg'):
            return 'image/svg+xml'
        elif path.endswith('.ico'):
            return 'image/x-icon'
        elif path.endswith('.woff'):
            return 'font/woff'
        elif path.endswith('.woff2'):
            return 'font/woff2'
        elif path.endswith('.ttf'):
            return 'font/ttf'
        elif path.endswith('.eot'):
            return 'application/vnd.ms-fontobject'
        elif path.endswith('.otf'):
            return 'font/otf'
        else:
            return 'application/octet-stream'
