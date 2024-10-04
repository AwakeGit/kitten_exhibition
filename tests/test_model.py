import pytest
from django.contrib.auth.models import User

from exhibition.models import Breed, Kitten, Rating


@pytest.mark.django_db
def test_create_breed():
    breed = Breed.objects.create(name="Сиамская")
    assert breed.name == "Сиамская"


@pytest.mark.django_db
def test_create_kitten():
    user = User.objects.create(username="testuser")
    breed = Breed.objects.create(name="Персидская")
    kitten = Kitten.objects.create(
        name="Луна",
        color="Белый",
        age=6,
        description="Игривая кошка",
        breed=breed,
        user=user
    )
    assert kitten.name == "Луна"
    assert kitten.breed.name == "Персидская"


@pytest.mark.django_db
def test_create_rating():
    user = User.objects.create(username="testuser")
    breed = Breed.objects.create(name="Сиамская")
    kitten = Kitten.objects.create(
        name="Снежок",
        color="Белый",
        age=3,
        description="Милый котенок",
        breed=breed,
        user=user
    )
    rating = Rating.objects.create(user=user, kitten=kitten, rating=5)
    assert rating.rating == 5
    assert rating.kitten.name == "Снежок"
