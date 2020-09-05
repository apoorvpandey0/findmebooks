from rest_framework.generics import (ListAPIView,
                RetrieveAPIView,UpdateAPIView,
                DestroyAPIView,CreateAPIView,
                RetrieveUpdateAPIView)
from django.db.models import Q


from .serializers import *

class UserBookCreateAPIView(CreateAPIView):
    queryset = UserBook.objects.all()
    serializer_class = UserBookCreateSerializer

class UserBookDetailAPIView(RetrieveAPIView):
    queryset = UserBook.objects.all()
    serializer_class = UserBookDetailSerializer
    
class UserBookDeleteAPIView(DestroyAPIView):
    queryset = UserBook.objects.all()
    serializer_class = UserBookDetailSerializer

class UserBookUpdateAPIView(RetrieveUpdateAPIView):
    queryset = UserBook.objects.all()
    serializer_class = UserBookUpdateSerializer
    permission_classes = [IsAuthenticated]


class UserBookListAPIView(ListAPIView):
    queryset = UserBook.objects.all()
    serializer_class = UserBookListSerializer
    # pagination_class = UserBookPageNumberPagination   #UserBookLimitOffset  #LimitOffsetPagination #PageNumberPagination

    #Method 1 of search filtering
    # filter_backends =(filters.DjangoFilterBackend,SearchFilter,OrderingFilter)
    # filterset_fields = ('isbn')
    # search_fields = ['isbn']

    #Method 2 of Search Filtering
    def get_queryset(self,*args,**kwrgs):
        # quertyset_list = super(PostListAPIView,self).get_queryset(*args,**kwrgs)
        queryset_list = UserBook.objects.all()
        query = self.request.GET.get('q').lower()
        if query:
            queryset_list = UserBook.objects.filter(
              Q(user__pincode=query)).distinct()
        return queryset_list