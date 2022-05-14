from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from django.contrib.auth.models import Group
from django.forms import ValidationError


class Role(models.Model):
    name = models.CharField(max_length=25)
    use_in_migrations = True

    def __str__(self):
        return self.name

    @classmethod
    def get_manager_role_id(self):
        return Role.objects.get_or_create(name="MANAGER")[0].id

def manager_validator(manager_id):
    try:
        manager = User.objects.get(pk=manager_id)
    except User.DoesNotExist:
        raise ValidationError("User not found for relation manager_id")
    if manager.role.id != Role.get_manager_role_id():
        raise ValidationError("This user cannot be assigned as a manager")

def get_manager_role_id():
    return Role.get_manager_role_id()

class User(AbstractUser):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    manager_id = models.ForeignKey(
        "authentication.User",
        verbose_name="manager",
        on_delete=models.SET_NULL,
        related_name="manager",
        blank=True, null=True,
        validators=[manager_validator],
        limit_choices_to={"role_id": get_manager_role_id()}
        )
    role = models.ForeignKey("authentication.Role", on_delete=models.SET_NULL, blank=True, null=True)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["email"], name="unique_user"),
        ]


    def set_role(self, role_id):
        """Ensure that role corespond whith permission groups

        Args:
            role_id (int): private key of a role record
        """
        try:
            role = Role.objects.get(pk=int(role_id))
        except Role.DoesNotExist:
            raise ValidationError("Entity not found", code="invalide")
        try:
            group = Group.objects.get(name=role.name.lower() + 's')
        except Group.DoesNotExist:
            raise ValidationError("This Role has bad settings, no group can be found", code="invalide")
        # Remove all groups for user, ensure one role = one group
        [self.groups.remove(grp) for grp in list(self.groups.all())]
        self.groups.add(group)

