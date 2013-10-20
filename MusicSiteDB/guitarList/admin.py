from django.contrib import admin
from guitarList.models import Email

class EmailAdmin(admin.ModelAdmin):
	fieldsets = [
        ('Person information', {'fields': ['name', 'email', 'source_type']}),
        ('Region information', {'fields': ['city', 'state', 'country']}),
    ]

	list_display = ('email_id', 'name', 'email', 'city', 'state', 'country', 'created_date')

admin.site.register(Email, EmailAdmin)
