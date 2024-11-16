from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from myapp import views


urlpatterns = [
    path('',views.index, name='index'),
    path('service/',views.service,name='service'),
    path('starter/',views.starter, name='starter'),
    path('about/',views.about,name='about'),
    path('doctors/',views.doctors,name='docs'),
    path('myservice/',views.doc_ser,name='myservice'),
    path('appointment/',views.appointment,name='appoint'),
    path('show/',views.Show,name='show'),
    path('delete/<int:id>',views.Delete),
    path('delete_con/<int:id>',views.del_con,name='delete_con'),
    path('contact/',views.contact,name='contact')
]
