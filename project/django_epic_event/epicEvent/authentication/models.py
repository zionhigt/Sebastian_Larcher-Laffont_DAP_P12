from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from django.contrib.auth.models import Group


class Role(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    @classmethod
    def get_manager_role_id(self):
        return self.objects.get_or_create(name="MANAGER")[0].id

        
class User(AbstractUser):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    manager_id = models.ForeignKey("authentication.User", verbose_name="manager", on_delete=models.SET_NULL, related_name="manager", blank=True, null=True)
    role = models.ForeignKey("authentication.Role", on_delete=models.SET_NULL, blank=True, null=True)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["email"], name="unique_user"),
            models.CheckConstraint(
                name="is_able_to_be_manager",
                check=models.Q(manager_id=Role.get_manager_role_id())
            ),
        ]

    
    def set_role(self, role_id):
        """Ensure that role corespond whith permission groups

        Args:
            role_id (int): private key of a role record
        """
        role = Role.objects.get(pk=int(role_id))
        group = Group.objects.get(name=role.name.lower() + 's')
        # Remove all groups for user, ensure one role = one group
        [self.groups.remove(grp) for grp in list(self.groups.all())]
        self.groups.add(group)

