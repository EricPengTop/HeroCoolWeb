from django.contrib import admin
from CoolApp.models import User, News, Article


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    fields = ['headline', 'content', 'pub_date', 'reporter']


class ArticleAdminSet(admin.ModelAdmin):
    fieldsets = [('headline', {'fields': ['headline']}), ('content', {'fields': ['content']}),
                 ('pub_date', {'fields': ['pub_date']}), ('reporter', {'fields': ['reporter']})]


admin.site.register(User)
admin.site.register(News)
admin.site.register(Article, ArticleAdmin)
