# This imports Django's model tools, which let us create database tables and fields.
from django.db import models

# This is a default Django comment. It is just a placeholder telling you this is where models are defined.
# Create your models here.

# This imports Django's built-in user model so each profile is connected to a user account.
from django.contrib.auth.models import User


# This creates a new model called Profile that stores extra information about a user.
class Profile(models.Model): 

    # These are the allowed roles for a user profile and the labels shown in the admin page.
    ROLE_CHOICES = [
        # A normal employee user.
        ('employee', 'Employee'),
        # A user who works in IT support.
        ('support', 'IT Support'),
        # A user with admin permissions.
        ('admin', 'Administrator'),
    ]

    # This links each profile to exactly one user account.
    # If the user is deleted, this profile will also be deleted automatically.
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    # This stores the user's role, and it must be one of the values in ROLE_CHOICES.
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='employee'
    )

    # This stores the user's department name. It is allowed to be blank.
    department = models.CharField(
        max_length=100,
        blank=True
    )

    # This stores the user's phone number. It is allowed to be blank.
    phone_number = models.CharField(
        max_length=20,
        blank=True
    )

    # This automatically records the date and time when the profile was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # This tells Django how to display a Profile object when it is shown in the terminal or admin area.
    def __str__(self):
        # This shows the username and the readable name of the role, such as "Employee".
        return f"{self.user.username} - {self.get_role_display()}"
