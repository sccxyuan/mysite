
from django.conf.urls.defaults import *
from mysite.views import hello,current_datetime,hell,my_image,unruly_passengers_csv,hello_pdf,jianli

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from mysite import views
import csv
from mysite.books import views
from mysite.books.views import about_pages
from mysite.books.models import Publisher
from django.views.generic import list_detail 
from django.views.generic.simple import direct_to_template
#from mysite.feeds import LatestEntries,LatestEntriesByCategory
def get_books():
    return Book.objects.all()
    
publisher_info={
    'queryset':Publisher.objects.all(),
    'template_name':'publisher_list_page.html',
    'te.plate_object_name':'publisher',
    'extra_context':{'book_list':get_books},
  }


urlpatterns = patterns('',
    ('^$', hell),
    (r'^pict/$',my_image),
    (r'^pdf/$',hello_pdf),
    (r'^pic/$',unruly_passengers_csv),
    (r'^about/$',direct_to_template, {'template': 'aboutno.html'}),
    (r'^about/(\w+$)',about_pages),
    ('^hello/$', hello),
    (r'^jianli/$',jianli),
    ('^time/$', current_datetime),
    #(r'^events/$',views.event_list),
    (r'^search-form/$',views.search_form),
    (r'^search/$',views.search),
    #(r'feeds/(?p<url>.*)/$','django.contrib.syndication.views.feed',
    #    {'feed_dict':feeds}),
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
   # (r'^admin/', include(admin.site.urls)),
    #(r'^publishers/$',list_detail.object_list,publisher_info)
    
)
