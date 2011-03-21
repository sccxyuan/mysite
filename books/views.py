from django.shortcuts import render_to_response
from django.http import HttpResponse
from mysite.books.models import Book
from django.http import Http404 
from django.template import TemplateDoesNotExist 
import datetime
from django.views.generic.simple import direct_to_template 

def about_pages(request, page): 
    try: 
        return direct_to_template(request, template="about/%s.html" % page) 
    except TemplateDoesNotExist: 
        raise Http404()



def search_form(request):
      return render_to_response('search_form.html')
      

def search(request):
    errors=[]
    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            errors.append('Enter s search term.')
        elif len(q)>20:
            errors.append('please enter at most 20 characters.')
        else:
            books=Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                {'books':books,'query':q})
    return render_to_response('search_form.html',{'errors':errors}) 
# Create your views here.
