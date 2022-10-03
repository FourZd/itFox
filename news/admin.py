from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Users, News, Comments

@admin.register(Users)
class UsersAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Users
    list_display = ('username', 'password')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('date', 'headline', 'content', 'author')

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('date', 'content', 'author')