from .serializers import MembersSerializer, EcasRoleSerializer
from .models import Members, EcasRole
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .paginators import CustomPagination

class MembersView(ListAPIView):
    serializer_class = MembersSerializer
    queryset = Members.objects.all()
    pagination_class = CustomPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # prefetch related EcasRole objects for each member
        queryset = self.serializer_class.setup_eager_loading(queryset)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
