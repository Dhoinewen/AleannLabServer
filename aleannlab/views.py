from rest_framework import generics
from .models import User, Rank
from .serializers import UserSerializer, RankSerializer


class UsersAPIView(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):

        queryset = User.objects.all()
        sort_type = self.request.query_params.get('sort')
        if sort_type is not None:
            if sort_type == 'asc':
                queryset = queryset.order_by('id')
            if sort_type == 'desc':
                queryset = queryset.order_by('-id')
        sort_rank_type = self.request.query_params.get('sort_rank')
        if sort_rank_type is not None:
            if sort_rank_type == 'asc':
                queryset = queryset.order_by('rank__queue')
            if sort_rank_type == 'desc':
                queryset = queryset.order_by('-rank__queue')
        return queryset


class UserAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RankAPIView(generics.ListCreateAPIView):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer


class RankAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer
