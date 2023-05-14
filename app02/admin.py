from django.contrib import admin

from app02.models import Publish, Book, AuthorDetail, Author


# Register your models here.


# class BookAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'price', 'pub_date', 'publish_id')
#     search_fields = ('title',)
#     list_per_page = 10
#     list_editable = ('title', 'price', 'pub_date')
#     date_hierarchy = None  # 按时间分层
#     ordering = ('id',)
#     fieldsets = (
#         ['Main', {
#             'fields': ('title', 'price'),
#         }],
#         ['Advance', {
#             'classes': ('collapse',),  # CSS
#             'fields': ('pub_date',),
#         }],
#
#     )


class AuthorDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender', 'tel', 'addr', 'birthday')
    search_fields = ('id',)
    list_per_page = 10
    list_editable = ('tel', 'addr', 'birthday')
    date_hierarchy = None  # 按时间分层
    ordering = ('id',)
    fieldsets = (
        ['Main', {
            'fields': ('gender', 'addr', 'birthday'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('tel',),
        }],

    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')
    search_fields = ('id',)
    list_per_page = 10
    list_editable = ('name', 'age')


class PublishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'email')
    search_fields = ('id',)
    ordering = ('id',)


#
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'pub_date', 'publish_id')
    search_fields = ('id',)
    ordering = ('id',)
    fieldsets = (
        ['Main', {
            'fields': ('title', 'price', 'pub_date', 'publish'),
        }],

    )


admin.site.register(Book, BookAdmin)
admin.site.register(AuthorDetail, AuthorDetailAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publish, PublishAdmin)
