from django.shortcuts import render
# Create your views here.
def index(request):
  return render(request,'index.html')
def service(request):
  return render(request,'service-details')
def starter(request):
  return render(request,'starter-page')
def about(request):
  return render(request,'about.html')
def doctors(request):
  return render(request,'doctors.html')
def doc_ser(request):
  return render(request,'services.html')