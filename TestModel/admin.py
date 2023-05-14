from django.contrib import admin
from TestModel.models import Test, Tag, Contact, People


# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    # fields = ('name', 'email')

    list_display = ('name', 'age', 'email')  # list
    search_fields = ('name',)

    inlines = [TagInline]
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('age',),
        }]
    )


class PeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'city', 'age')
    ordering = ('id', )



admin.site.register(Contact, ContactAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.register([Test])
