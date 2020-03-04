from .models import List
from .serializers import MySerializer, MyDetailSerializer, MyCreateSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from .pagination import ListPageNumberPagination

class Crud(ListAPIView):
    queryset = List.objects.all()
    serializer_class = MySerializer
    pagination_class = ListPageNumberPagination


class Crud_list(ListAPIView):
    queryset = List.objects.all()
    serializer_class = MySerializer
    pagination_class = ListPageNumberPagination





class Crud_detail(RetrieveAPIView):
    lookup_field = 'id'
    queryset = List.objects.all()
    serializer_class = MyDetailSerializer

class Crud_update(UpdateAPIView):
    lookup_field = 'id'
    queryset = List.objects.all()
    serializer_class = MySerializer

class Crud_delete(DestroyAPIView):
    lookup_field = 'id'
    queryset = List.objects.all()
    serializer_class = MySerializer

class Crud_create(CreateAPIView):
    queryset = List.objects.all()
    serializer_class = MyCreateSerializer