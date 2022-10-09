from django.contrib import admin
from .models import Invoice
from .models import InvoiceItem
from .models import Receipt

# Register your models here.
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
admin.site.register(Receipt)
