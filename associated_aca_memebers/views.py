from .serializers import MembersSerializer, EcasRoleSerializer
from .models import Members, EcasRole
from rest_framework.generics import ListAPIView
from .paginators import CustomPagination

class MembersView(ListAPIView):
    serializer_class = MembersSerializer
    queryset = Members.objects.all()
    pagination_class = CustomPagination

class EcasRoleList(ListAPIView):
    serializer_class = EcasRoleSerializer

    def get_queryset(self):
        member = Members.objects.get(id=self.kwargs['id'])
        return EcasRole.objects.filter(member=member)
