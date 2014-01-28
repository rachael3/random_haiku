import random

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

BASE_PATH='/home/rachael/haiku/haiku/'

def hello(request):
    haiku1 = random.choice(
        open(BASE_PATH+"haiku1.txt").readlines()
    )
    haiku2 = random.choice(
        open(BASE_PATH+"haiku2.txt").readlines()
    )
    haiku3 = random.choice(
        open(BASE_PATH+"haiku3.txt").readlines()
    )
    '''
    if request.session.has_key('counter'):
        request.session['counter'] += 1
    else:
        request.session['counter'] = 0
    '''
    return render_to_response(
        'haiku/test.html',
        locals(),
        context_instance=RequestContext(request)
    )
