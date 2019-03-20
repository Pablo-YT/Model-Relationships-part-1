from django.contrib import admin
from .models import Customer,Order, role,play ,actor,director

#admin.site.register(Customer)
#admin.site.register(Order)

#-----------------------------
admin.site.register(role)
admin.site.register(actor)
admin.site.register(director)
admin.site.register(play)
#------------------------------