from django.contrib import admin
from ContactEnquiry.models import contactform

# Register your models here.
class contacts(admin.ModelAdmin):
    list_display=('Name','Contact','People','Message')

admin.site.register(contactform,contacts)