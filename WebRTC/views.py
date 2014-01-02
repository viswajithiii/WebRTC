from django.shortcuts import render_to_response
from django.template import RequestContext
from hookup.models import NGO

def home(request):

    querydict = {}
    querydict["ngos"] = NGO.objects.all()

    return render_to_response ('home.html', querydict, context_instance = RequestContext(request) )
