from django.http import HttpResponse

from django.template import loader

# Create your views here.

def trees(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())