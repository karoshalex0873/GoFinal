from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from myapp import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('service/',views.service,name='service'),
    path('starter/',views.starter, name='starter'),
    path('about/',views.about,name='about'),
    path('doctors/',views.doctors,name='docs'),
    path('myservice/',views.doc_ser,name='myservice')
]
