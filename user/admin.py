from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'user_type', 'is_active', 'is_admin']

admin.site.register(User, UserAdmin)




# from django.contrib import admin
# from .models import User
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# class UserAdmin(BaseUserAdmin):
#     list_display = ('email', 'name', 'is_admin', 'is_active', 'education')
#     search_fields = ('email', 'name')
#     readonly_fields = ('id', 'membership_number')

#     fieldsets = (
#         (None, {'fields': ('email', 'name', 'password')}),
#         ('Personal info', {'fields': ('education', 'phone_number', 'address', 'image', 'membership_number')}),
#         ('Permissions', {'fields': ('is_admin', 'is_active')}),
#     )

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'name', 'password', 'password2'),
#         }),
#     )

#     ordering = ('email',)

# admin.site.register(User, UserAdmin)
