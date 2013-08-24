from django.contrib import admin
from polls.models import Poll

class PollAdmin(admin.ModelAdmin):

	fieldsets=[
		('random Zuwa field', {'fields':['question']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]

	#fields = ['pub_date', 'question']

admin.site.register(Poll,PollAdmin)
