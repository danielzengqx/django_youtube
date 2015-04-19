from django.contrib import admin

# Register your models here.
from .models import Join

class JoinAdmin(admin.ModelAdmin):
	#Default is __unicode__ only
	list_display = ['__unicode__', 'email', 'friend', 'timestamp', 'updated']  
	class Meta:
			model = Join

admin.site.register(Join, JoinAdmin)
