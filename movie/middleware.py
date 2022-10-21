

from django.utils.deprecation import MiddlewareMixin


count=0
class RequestCounterMiddleware(MiddlewareMixin):
    

    def process_request(self, request):
        current_user = request.user
        
        global count
        count=count+1
        return None
        
    def reset_request(self, request):
        
        global count
        return None
    