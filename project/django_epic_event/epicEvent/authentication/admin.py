from django.contrib import admin
from django.forms import ValidationError
from authentication.models import User

# Old way:
#class AuthorAdmin(admin.ModelAdmin):
#    pass

# With object permissions support
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "email",
    ]

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = (
            "groups",
            "last_login",
            "date_joined",
        )
        form = super().get_form(request, obj, **kwargs)
        return form 

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        password = request.POST.get("password", None)
        if password is not None:
            hashed_password = obj.set_password(password)
            request.POST.update({"password": hashed_password})
        else:
            return ValidationError("Password is required", code="invalid")
        role_id = request.POST.get("role", [False])[0]
        obj.set_role(role_id)


admin.site.register(User, UserAdmin)