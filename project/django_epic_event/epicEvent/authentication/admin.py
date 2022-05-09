from django.contrib import admin
from authentication.models import User
from django.contrib.auth.models import Group
from authentication.models import Role

# Old way:
#class AuthorAdmin(admin.ModelAdmin):
#    pass

# With object permissions support
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
         "last_name",
          "email"
    ]

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ("groups", )
        form = super().get_form(request, obj, **kwargs)
        return form

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        role_id = request.POST.get("role", [False])[0]
        role = Role.objects.get(pk=int(role_id))
        group = Group.objects.get(name=role.name.lower() + 's')
        user = User.objects.get(email=obj.email)
        print(len(user.groups.all()))
        for old_group in obj.groups.all():
            user.groups.remove(old_group)
        user.groups.add(group)
        print(user.groups.all())


admin.site.register(User, UserAdmin)