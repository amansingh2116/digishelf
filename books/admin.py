from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book, Cart, Genre, ContactMessage


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # Remove 'username' if it doesn't exist in your model
        ('Personal info', {'fields': ('phone',)}),  # Removed 'username'
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_seller', 'groups', 'user_permissions')}),
    )
    list_display = ('email', 'is_staff', 'is_seller')  # Removed 'username'
    ordering = ('email',)  # Add this line to fix the ordering issue
    
    # Also add this to customize the add user form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)
admin.site.register(Cart)
admin.site.register(Genre)
admin.site.register(ContactMessage)