from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Specialty, Doctor, Patient, Service, Appoinment, MedicalRecord

# Configuration pour CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informations personnelles', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'address')}),
        ('Rôles et permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'role')}
        ),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

# Configuration pour Specialty
@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)

# Configuration pour Doctor
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialty', 'bio')
    search_fields = ('user__first_name', 'user__last_name', 'specialty__name')
    list_filter = ('specialty',)

# Configuration pour Patient
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'medical_history')
    search_fields = ('user__first_name', 'user__last_name', 'medical_history')
    list_filter = ('date_of_birth',)

# Configuration pour Service
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name',)
    ordering = ('name',)

# Configuration pour Appoinment
@admin.register(Appoinment)
class AppoinmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'service', 'date', 'time', 'status', 'author')
    search_fields = ('patient__user__first_name', 'patient__user__last_name', 'doctor__user__first_name', 'doctor__user__last_name')
    list_filter = ('status', 'date', 'service')
    ordering = ('date', 'time')

# Configuration pour MedicalRecord
@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'diagnosis', 'date', 'author')
    search_fields = ('patient__user__first_name', 'patient__user__last_name', 'doctor__user__first_name', 'doctor__user__last_name', 'diagnosis')
    list_filter = ('date',)
    ordering = ('date',)

# Enregistrement du modèle CustomUser
admin.site.register(CustomUser, CustomUserAdmin)
