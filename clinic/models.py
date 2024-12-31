from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Modèle utilisateur personnalisé
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('doctor', 'Médecin'),
        ('patient', 'Patient'),
    ]
    role = models.CharField(
        max_length=10, 
        choices=ROLE_CHOICES, 
        default='patient',
        verbose_name="Rôle"
    )
    phone_number = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        verbose_name="Numéro de téléphone"
    )
    address = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Adresse"
    )

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",
        blank=True,
        verbose_name="Groupes"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set",
        blank=True,
        verbose_name="Permissions utilisateur"
    )

    def __str__(self):
        return f"{self.username} ({self.role})"


# Modèle pour les spécialités médicales
class Specialty(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom de la spécialité")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return self.name


# Modèle pour les médecins
class Doctor(models.Model):
    user = models.OneToOneField(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='doctor_profile', 
        verbose_name="Utilisateur"
    )
    specialty = models.ForeignKey(
        Specialty, 
        on_delete=models.SET_NULL, 
        null=True, 
        verbose_name="Spécialité"
    )
    bio = models.TextField(blank=True, null=True, verbose_name="Biographie")
    availability = models.TextField(blank=True, null=True, verbose_name="Disponibilité")

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name} - {self.specialty}"


# Modèle pour les patients
class Patient(models.Model):
    user = models.OneToOneField(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='patient_profile', 
        verbose_name="Utilisateur"
    )
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Date de naissance")
    medical_history = models.TextField(blank=True, null=True, verbose_name="Historique médical")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


# Modèle pour les services proposés par la clinic
class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom du service")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")

    def __str__(self):
        return self.name


# Modèle pour les rendez-vous
class Appoinment(models.Model):  # Correction du nom
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('confirmed', 'Confirmé'),
        ('cancelled', 'Annulé'),
    ]
    patient = models.ForeignKey(
        'clinic.Patient', 
        on_delete=models.CASCADE, 
        verbose_name="Patient"
    )
    doctor = models.ForeignKey(
        'clinic.Doctor', 
        on_delete=models.CASCADE, 
        verbose_name="Médecin"
    )
    service = models.ForeignKey(
        'clinic.Service', 
        on_delete=models.SET_NULL, 
        null=True, 
        verbose_name="Service"
    )
    date = models.DateField(verbose_name="Date du rendez-vous")
    time = models.TimeField(verbose_name="Heure du rendez-vous")
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='pending', 
        verbose_name="Statut"
    )
    author = models.ForeignKey(
        CustomUser, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        verbose_name="Créateur"
    )

    def __str__(self):
        return f"Rendez-vous: {self.patient} avec {self.doctor} le {self.date} à {self.time}"


# Modèle pour les dossiers médicaux
class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        'clinic.Patient', 
        on_delete=models.CASCADE, 
        verbose_name="Patient"
    )
    doctor = models.ForeignKey(
        'clinic.Doctor', 
        on_delete=models.SET_NULL, 
        null=True, 
        verbose_name="Médecin"
    )
    diagnosis = models.TextField(verbose_name="Diagnostic")
    treatment = models.TextField(verbose_name="Traitement")
    date = models.DateField(auto_now_add=True, verbose_name="Date du dossier")
    author = models.ForeignKey(
        CustomUser, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        verbose_name="Créateur"
    )

    def __str__(self):
        return f"Dossier médical de {self.patient} - {self.date}"
