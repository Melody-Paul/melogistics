# from django.contrib import admin
# from .models import User,CustomerProfile,RiderProfile,Order
# from django.contrib.auth.admin import UserAdmin
# from .forms import UserCreationForm,UserEditForm




# @admin.register(RiderProfile)
# class RiderProfileAdmin(admin.ModelAdmin):
#     # pass


# @admin.register(CustomerProfile)
# class CustomerProfileAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Order)
# class Order(admin.ModelAdmin):
#     pass

#  # or the name of your user model

# class CustomUserAdmin(UserAdmin):
#     add_form = UserCreationForm
#     form = UserCreationForm
#     model = User

#     list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
#     list_filter = ('is_staff', 'is_active', 'is_superuser')
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal Info', {'fields': ('first_name', 'last_name')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
# admin.site.register(User, CustomUserAdmin)
