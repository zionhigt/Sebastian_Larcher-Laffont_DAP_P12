from rest_framework.exceptions import PermissionDenied
from .serializers import RegisterSerializer

from rest_framework.viewsets import ModelViewSet


def is_manager(user):
    return user.__str__() != "AnonymousUser" and user.role.name == "MANAGER"


class RegisterViewSet(ModelViewSet):

    @classmethod
    def as_view(self, *args, **kwargs):
        return super().as_view({'post': "create"})

    serializer_class = RegisterSerializer

    def create(self, request):
        if is_manager(request.user):
            return super().create(request)
        else:
            raise PermissionDenied()
