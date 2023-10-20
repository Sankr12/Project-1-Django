from django.contrib import admin
from News.models import news

# Register your models here.
class Newsadmin(admin.ModelAdmin):
    list_display=('news_title', 'news_desc', 'news_image')

admin.site.register(news,Newsadmin)