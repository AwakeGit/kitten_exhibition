import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from exhibition.models import Breed, Kitten, Rating


@pytest.mark.django_db
def test_jwt_authentication():
    """Проверка аутентификации с помощью JWT."""
    client = APIClient()

    user = User.objects.create_user(username="testuser", password="password")

    response = client.post(
        '/api/token/',
        {'username': 'testuser', 'password': 'password'}
    )
    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data

    access_token = response.data['access']

    client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)

    response = client.get('/api/breeds/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_breeds():
    """Проверка получения списка пород котов."""
    client = APIClient()

    Breed.objects.create(name="Мейн-кун")
    Breed.objects.create(name="Сиамская")

    response = client.get('/api/breeds/')
    assert response.status_code == 200
    assert len(response.data) == 2
    assert response.data[0]['name'] == "Мейн-кун"


@pytest.mark.django_db
def test_create_kitten():
    """Проверка создания котов."""
    client = APIClient()

    user = User.objects.create_user(username="testuser", password="password")
    breed = Breed.objects.create(name="Персидская")

    client.force_authenticate(user=user)

    data = {
        "name": "Барсик",
        "color": "Черный",
        "age": 2,
        "description": "Очень игривый",
        "breed_id": breed.id
    }

    response = client.post('/api/kittens/', data)
    assert response.status_code == 201
    assert response.data['name'] == "Барсик"


@pytest.mark.django_db
def test_get_kittens():
    """Проверка получения списка котов."""
    client = APIClient()

    user = User.objects.create_user(username="testuser", password="password")
    breed = Breed.objects.create(name="Сиамская")
    Kitten.objects.create(
        name="Луна",
        color="Белый",
        age=3,
        description="Милая кошечка",
        breed=breed,
        user=user
    )

    client.force_authenticate(user=user)

    response = client.get('/api/kittens/')
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == "Луна"


@pytest.mark.django_db
def test_filter_kittens_by_breed():
    """Проверка фильтрации котов по породе. """
    client = APIClient()

    user = User.objects.create_user(username="testuser", password="password")
    breed1 = Breed.objects.create(name="Сиамская")
    breed2 = Breed.objects.create(name="Мейн-кун")

    Kitten.objects.create(
        name="Луна",
        color="Белый",
        age=3,
        description="Милая кошечка",
        breed=breed1,
        user=user
    )

    Kitten.objects.create(
        name="Снежок",
        color="Серый",
        age=4,
        description="Большой кот",
        breed=breed2,
        user=user
    )

    response = client.get('/api/kittens/?breed={}'.format(breed1.id))
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == "Луна"


@pytest.mark.django_db
def test_rate_kitten():
    """Проверка добавления оценки коту. """
    client = APIClient()

    user = User.objects.create_user(username="testuser", password="password")
    breed = Breed.objects.create(name="Персидская")
    kitten = Kitten.objects.create(
        name="Барсик",
        color="Черный",
        age=2,
        description="Очень игривый",
        breed=breed,
        user=user
    )

    client.force_authenticate(user=user)

    data = {
        "rating": 5
    }

    response = client.post(f'/api/kittens/{kitten.id}/rate/', data)
    assert response.status_code == 201
    assert response.data['status'] == "Оценка успешно добавлена!"

    assert Rating.objects.filter(user=user, kitten=kitten).exists()


@pytest.mark.django_db
def test_update_kitten():
    """Проверка обновления кота."""
    client = APIClient()

    user = User.objects.create_user(username="testuser", password="password")
    breed = Breed.objects.create(name="Сиамская")
    kitten = Kitten.objects.create(
        name="Мурзик",
        color="Черный",
        age=3,
        description="Очень дружелюбный кот",
        breed=breed,
        user=user
    )

    client.force_authenticate(user=user)

    data = {
        "name": "Мурзик",
        "color": "Белый",
        "age": 4,
        "description": "Измененное описание",
        "breed_id": breed.id
    }

    response = client.put(f'/api/kittens/{kitten.id}/', data)
    assert response.status_code == 200
    assert response.data['color'] == "Белый"
    assert response.data['age'] == 4
    assert response.data['description'] == "Измененное описание"


@pytest.mark.django_db
def test_delete_kitten():
    """Проверка удаления кота."""
    client = APIClient()

    user = User.objects.create_user(username="testuser", password="password")
    breed = Breed.objects.create(name="Сиамская")
    kitten = Kitten.objects.create(
        name="Барсик",
        color="Черный",
        age=2,
        description="Очень игривый",
        breed=breed,
        user=user
    )

    client.force_authenticate(user=user)

    response = client.delete(f'/api/kittens/{kitten.id}/')
    assert response.status_code == 204

    assert not Kitten.objects.filter(id=kitten.id).exists()
