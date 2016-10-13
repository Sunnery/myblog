from django.template import loader,Context
from django.http import HttpResponse

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x

class SimpleMiddleware(MiddlewareMixin):
    # print 000000000000000000000000000000000
    # def process_request(self, request):
    #     return None
    #
    # def process_response(self, request, response):
    #     print response
    #     print 2222222222222222222222222222222222
    #     # return response

    def process_exception(self, request, exception):
        posts = None
        t = loader.get_template('404.html')
        c = Context({'posts': posts})
        return HttpResponse(t.render(c))