#from django.template.loader import get_template
#from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
#from mysite.models import Event,BlogEntry

#csv
import csv 
from django.http import HttpResponse 
# Number of unruly passengers each year 1995 - 2005. In a real application 
# this would likely come from a database or some other back-end data store. 
UNRULY_PASSENGERS = [146,184,235,200,226,251,299,273,281,304,203] 
def unruly_passengers_csv(request): 
    # Create the HttpResponse object with the appropriate CSV header. 
    response = HttpResponse(mimetype='text/csv') 
    response['Content-Disposition'] = 'attachment; filename=unruly.csv' 
    # Create the CSV writer using the HttpResponse as the "file." 
    writer = csv.writer(response) 
    writer.writerow(['Year', 'Unruly Airline Passengers']) 
    for (year, num) in zip(range(1995, 2006), UNRULY_PASSENGERS): 
        writer.writerow([year, num]) 
    return response

#pdf
from cStringIO import StringIO 
from reportlab.pdfgen import canvas 
from django.http import HttpResponse 
def hello_pdf(request): 
    # Create the HttpResponse object with the appropriate PDF headers. 
    response = HttpResponse(mimetype='application/pdf') 
    response['Content-Disposition'] = 'attachment; filename=hello.pdf' 
    temp = StringIO() 
    # Create the PDF object, using the StringIO object as its "file." 
    p = canvas.Canvas(temp) 
    # Draw things on the PDF. Here's where the PDF generation happens. 
    # See the ReportLab documentation for the full list of functionality. 
    p.drawString(100, 100, "Hello world.") 
    # Close the PDF object cleanly. 
    p.showPage() 
    p.save() 
    # Get the value of the StringIO buffer and write it to the response. 
    response.write(temp.getvalue()) 
    return response
    
def my_image(request):
    image_date=open("/Users/yuanjingyun/Pictures/Prettybeauty008.jpg","rb").read()
    return HttpResponse(image_date,mimetype="image/jpg")
def hello(request):
  return HttpResponse('hello world')

def hell(request):
    return HttpResponse('hello world')

def current_datetime(request):
  now=datetime.datetime.now()
  return render_to_response('current_datetime.html',{'current_date':now})
  #t=get_template('current_datetime.html')
  #html=t.render(Context({'current_date':now}))
  #return HttpResponse(html)

def search_form(request):
    return render_to_response('search_form.html')
def search(request):
    if 'q' in resquest.GET:
        message='You searched for:%r'% request.GET['q']
    else:
        message='You submitted an empty form.'
    return HttpResponse(message)

def event_list(request):
    obj_list=Event.object.all()
    return render_to_response('mysite/event_list.html',{'event_list':obj_list})

def entry_list(request):
    obj_list=BlogEntry.objects.all()
    return render_to_response('mysite/blogentry_list.html',{'evtry_list':obj_list})
    
