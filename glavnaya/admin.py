from django.contrib import admin
from .models import New, Team, Kurs, Faq

class NewsAdmin(admin.ModelAdmin):
    list_display=["title","published"]
    list_display_links=["title"]
    list_filter=["published"]
    class Meta:
        model=New
admin.site.register(New,NewsAdmin)
admin.site.register(Team)
admin.site.register(Kurs)
admin.site.register(Faq)
#admin.site.register(Foto)
