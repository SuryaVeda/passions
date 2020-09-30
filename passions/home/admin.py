from django.contrib import admin
from .models import News, Category, Comment, Reply
# Register your models here.
admin.site.register(News)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Reply)