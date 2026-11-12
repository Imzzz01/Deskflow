# This imports Django's admin tools, which let us control how models appear in the admin page.
from django.contrib import admin

# This is a default Django comment. It is just a reminder that this file is where models are registered.
# Register your models here.

# This imports the Profile model from this app so we can show it in the admin panel.
from .models import Profile


# This tells Django to register the Profile model in the admin area.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # This decides which fields show up in the list of profiles in the admin page.
    list_display = ('user', 'role', 'department', 'created_at')
    # This adds filter options on the admin page so you can sort by role or department.
    list_filter = ('role', 'department')
    # This allows searching for profiles by the linked user's username or email.
    search_fields = ('user__username', 'user__email')

