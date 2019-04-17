from django.contrib import admin
from workers.models import Position,Workers,Country,City
# Register your models here.
class WorkersAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','fathername','image','position','date_birn','price']
    list_filter = ['position','date_created','price']
    search_fields = ['firstname','lastname','fathername']
    prepopulated_fields = {'slug':['lastname',]}
    raw_id_fields = ['position',]
    date_hierarchy = 'date_created'
    ordering =['date_created']
class PositionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ['name', ]}
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ['name', ]}
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','country']
    prepopulated_fields = {'slug': ['name', ]}
admin.site.register(Workers,WorkersAdmin)
admin.site.register(Position,PositionAdmin)
admin.site.register(Country,CountryAdmin)
admin.site.register(City,CityAdmin)
