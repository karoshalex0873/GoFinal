from django.contrib import admin # type: ignore
from myapp.models import Member, Product,Appointment,Contact
# Register your models here.
admin.site.register(Member)
admin.site.register(Product)
admin.site.register(Appointment)
admin.site.register(Contact)