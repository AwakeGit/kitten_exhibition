from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from exhibition.models import Breed, Kitten, Rating
from .permissions import IsOwnerOrReadOnly
from .serializers import BreedSerializer, KittenSerializer, RatingSerializer


class BreedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class KittenViewSet(viewsets.ModelViewSet):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        breed_id = self.request.query_params.get('breed')
        if breed_id is not None:
            queryset = queryset.filter(breed_id=breed_id)
        return queryset

    @action(detail=True, methods=['post'])
    def rate(self, request, pk=None):
        kitten = self.get_object()
        user = request.user

        if Rating.objects.filter(kitten=kitten, user=user).exists():
            return Response({'status': 'Вы уже оценили этого котенка!'},
                            status=status.HTTP_400_BAD_REQUEST)

        data = request.data.copy()
        data['kitten'] = kitten.id
        serializer = RatingSerializer(data=data)

        if serializer.is_valid():
            serializer.save(user=request.user, kitten=kitten)
            return Response({'status': 'Оценка успешно добавлена!'},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
