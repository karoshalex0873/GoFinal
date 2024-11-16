from django.shortcuts import render,redirect # type: ignore
from myapp.models import Appointment,Contact
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
def appointment(request):
  if request.method == 'POST':
    myappointments=Appointment(
      FullName =request.POST['name'],
      Email=request.POST['email'],
      Phone=request.POST['phone'],
      datetime=request.POST['date'],
      Department=request.POST['department'],
      Doctor=request.POST['doctor'],
      message=request.POST['message']
    )
    myappointments.save()

    return redirect('/appointment')
  else:
    return render(request,'APPOINTMENT.html')

def Show(request):
  all_appointments=Appointment.objects.all()
  return render(request,'show.html',{'appointment':all_appointments})

def Delete(request,id):
  del_appoint=Appointment.objects.get(id=id)
  del_appoint.delete()  
  return redirect('/show')

def contact(request):
  if request.method == 'POST':
    My_contacts=Contact(
      Name=request.POST['name'],
      Email=request.POST['email'],
      Subject=request.POST['subject'],
      Message=request.POST['message']
    )
    My_contacts.save()
    return redirect('/contact')
  else:
    return render(request,'contacts.html')

def Show(request):
  all_contacts=Contact.objects.all()
  return render(request,'show.html',{'contacts':all_contacts})

def del_con(request,id):
  del_contact=Contact.objects.get(id=id)
  del_contact.delete()  
  return redirect('/show')