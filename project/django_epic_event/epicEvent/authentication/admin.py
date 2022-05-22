from django.contrib import admin
from django.forms import ValidationError
from authentication.models import User



# Old way:
#class AuthorAdmin(admin.ModelAdmin):
#    pass

# With object permissions support
class UserAdmin(admin.ModelAdmin):
    exclude = (
        "groups",
        "last_login",
        "date_joined",
        "is_staff"
    )
    list_display = [
        "first_name",
        "last_name",
        "email",
    ]
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.base_fields.get("manager_id").queryset = User.objects.filter(role__name="MANAGER")
        return form

    def append_to_exclude(self, *args):
        exclude = list(self.exclude)
        for arg in args:
            if arg not in exclude:
                exclude.append(arg)
        self.exclude = tuple(exclude)

    def save_model(self, request, obj, form, change):
        password = request.POST.get("password", None)
        if password is None:
            return ValidationError("Password is required", code="invalid")

        if change:
            user = User.objects.get(pk=obj.id)
            if user.password != obj.password:
                obj.set_password(password)
        else:
            obj.set_password(password)
        
        obj.as_staff()

        super().save_model(request, obj, form, change)
        role_id = request.POST.get("role", [False])
        if role_id:
            obj.set_role(role_id)


admin.site.register(User, UserAdmin)