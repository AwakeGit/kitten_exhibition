from rest_framework import serializers

from exhibition.models import Breed, Kitten


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name']


class KittenSerializer(serializers.ModelSerializer):
    breed = BreedSerializer(read_only=True)
    breed_id = serializers.PrimaryKeyRelatedField(
        queryset=Breed.objects.all(),
        source='breed',
        write_only=True
    )
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Kitten
        fields = ['name', 'id', 'color', 'age', 'description', 'breed', 'breed_id',
                  'user']


from exhibition.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Rating
        fields = ['id', 'user', 'kitten', 'rating']
