from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

def mcc(request):
  # request the context of the request.
  # the context contains information such as the client's machine details, for example
  context = RequestContext(request)

  # construct a dictionary to pass to the template engine as its context.
  content = {}

  return render_to_response('mcc/mcc.html', content, context)

