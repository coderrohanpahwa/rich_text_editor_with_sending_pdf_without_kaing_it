from django.contrib import admin
from .models import Post,Vendor,Client,NumberOfPhases,Match
# Register your models here.
from django.utils import html
admin.site.register(Post)
admin.site.register(NumberOfPhases)
admin.site.register(Vendor)
admin.site.register(Client)

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ['client','vendor','matched','set_phase']
    def set_phase(self,obj):
        print(obj.client.id,obj.vendor.id)
        url=f'/match/{obj.client.id}/{obj.vendor.id}/numberofphases'
        return html.format_html(f"<a href='{url}'>Guide Phase</a>")


