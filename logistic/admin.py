
from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from core.models import Order
from core.models import User,CustomerProfile,RiderProfile,Order
from django.contrib.auth.admin import UserAdmin
from core.forms import UserCreationForm,UserEditForm


class MainAdmin(admin.AdminSite):
    site_header = "Melody's Delivery Admin dashboard"
    site_title = "melody's Admin"
    index_title = "melody's Admin"
    site_url = None

class RidersAdmin(admin.AdminSite):
    site_header = "Melody's Delivery Riders dashboard"
    site_title = "Riders Dashboard"
    index_title = "Riders Dashboard"
    site_url = None



main_admin = MainAdmin(name = 'admin')

class RiderProfileAdmin(admin.ModelAdmin):
    pass
main_admin.register(RiderProfile,RiderProfileAdmin)


class CustomerProfileAdmin(admin.ModelAdmin):
    pass
main_admin.register(CustomerProfile,CustomerProfileAdmin)


class OrderAdmin(admin.ModelAdmin):
    pass

main_admin.register(Order,OrderAdmin)


 # or the name of your user model

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserCreationForm
    model = User

    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
main_admin.register(User, CustomUserAdmin)

class RiderOrderAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        qs = super().get_queryset(request)
        obj = request.user.rider_profile
        return qs.filter(driver = obj).all()
    
    def has_add_permission(self, request):
        return False

    # Disabling change permission
    def has_change_permission(self, request, obj=None):
        return False
    def has_view_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        # return super().has_view_permission(request, obj)
        return True
    # Making all fields read-only
    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in self.model._meta.get_fields()]
riders_admin = RidersAdmin(name = 'riders')

riders_admin.register(Order,RiderOrderAdmin)
