from django.contrib import admin
from app01.models import UserInfo, Department


# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('id',)
    list_per_page = 10
    list_editable = ('title',)


admin.site.register([UserInfo])
admin.site.register(Department, DepartmentAdmin)
