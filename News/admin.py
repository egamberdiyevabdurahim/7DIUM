from django.contrib import admin


from .models import News, LikeNews, Haqida


admin.site.register(News)
admin.site.register(LikeNews)
admin.site.register(Haqida)