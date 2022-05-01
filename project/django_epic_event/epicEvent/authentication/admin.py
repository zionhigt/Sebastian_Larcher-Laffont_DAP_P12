from django.contrib import admin
from authentication.models import User
from guardian.admin import GuardedModelAdmin

# Old way:
#class AuthorAdmin(admin.ModelAdmin):
#    pass

# With object permissions support
class UserAdmin(GuardedModelAdmin):
    list_display = ["first_name", "last_name", "email"]

admin.site.register(User, UserAdmin)