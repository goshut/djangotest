from django.contrib import admin
from .models import Book, Hero

# Register your models here.
# admin.site.register(Hero)
admin.site.site_header = 'DJ书城'
admin.site.site_title = 'DJ书城MIS'
admin.site.index_title = '欢迎使用DJ书城MIS'


class BookTabular(admin.TabularInline):
    model = Hero
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ['btitle', 'pub_date', 'bread', 'bcomment']
    inlines = [BookTabular]


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_per_page = 6
    list_filter = ['hbook', 'hgender']
    list_display = ['hname', 'hgender', 'hcomment', 'hbook', 'book_comment']
    search_fields = ['hname']
    # fields = ['hname', 'hgender']
