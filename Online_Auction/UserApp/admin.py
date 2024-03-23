from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Country, City, User, State
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['country_id', 'country_name', 'country_code']

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['state_id', 'state_name']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['city_id', 'city_name']

@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ['id', 'username', 'first_name', 'last_name', 'city', 'is_staff', 'is_active']

    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields':('email', 'password', 'first_name', 'last_name')}),
        ('permissions',{'fields':('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('extra fields', {'fields':('role', 'contact_no', 'aadhar_card', 'pan_card', 'passport_front', 'passport_back', 'address', 'city')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'password1', 'password2',
            )}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
