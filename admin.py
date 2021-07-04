from django.contrib import admin

# Register your models here.
from .models import patients
from .models import test
from .models import vac
admin.site.register(test)
admin.site.register(vac)
class patientsAdmin(admin.ModelAdmin):
	#fields=(('name','address'))
	list_display=('name','age','gender','address','mobilenumber','wardnumber')
	ordering=('name',)
	search_fields=('name','age','gender','address','mobilenumber','wardnumber')
admin.site.register(patients,patientsAdmin)

# Register your models here.
