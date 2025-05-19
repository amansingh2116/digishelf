# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser, Book, Cart, Genre, ContactMessage


# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         # Remove 'username' if it doesn't exist in your model
#         ('Personal info', {'fields': ('phone',)}),  # Removed 'username'
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_seller', 'groups', 'user_permissions')}),
#     )
#     list_display = ('email', 'is_staff', 'is_seller')  # Removed 'username'
#     ordering = ('email',)  # Add this line to fix the ordering issue
    
#     # Also add this to customize the add user form
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2'),
#         }),
#     )
# from .models import Book, SliderImage



from django.contrib import admin
from .models import Book, SliderImage, Genre, ContactMessage, Cart, CartItem, CustomUser

# Register your models here
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    list_filter = ('genres', 'seller')
    search_fields = ('title', 'author')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(SliderImage)
class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'display_order', 'is_active')
    list_editable = ('display_order', 'is_active')
    list_filter = ('is_active',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('created_at',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'added_at')


# admin.site.register(SliderImage)
# admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(Book)
# admin.site.register(Cart)
# admin.site.register(Genre)
# admin.site.register(ContactMessage)