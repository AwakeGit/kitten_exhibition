from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from exhibition.models import Breed, Kitten


class Command(BaseCommand):
    help = 'Генерация реалистичных данных о котятах и породах'

    def handle(self, *args, **kwargs):
        user1, created = User.objects.get_or_create(
            username="owner1",
            defaults={
                "email": "owner1@example.com",
                "password": "password123"}
        )
        user2, created = User.objects.get_or_create(
            username="owner2",
            defaults={
                "email": "owner2@example.com",
                "password": "password123"}
        )

        breed1, created = Breed.objects.get_or_create(name="Сиамская")
        breed2, created = Breed.objects.get_or_create(name="Персидская")
        breed3, created = Breed.objects.get_or_create(name="Мейн-кун")

        kittens_data = [
            {
                "name": "Луна",
                "color": "Белый",
                "age": 6,
                "description": "Луна – игривая сиамская кошка с голубыми "
                               "глазами. Она очень любопытна и любит играть с"
                               " игрушками.",
                "breed": breed1,
                "user": user1,
            },
            {
                "name": "Майло",
                "color": "Серый",
                "age": 8,
                "description": "Майло – спокойный персидский кот, который "
                               "любит отдыхать на солнце. Он обожает внимание "
                               "и спокойные игры.",
                "breed": breed2,
                "user": user1,
            },
            {
                "name": "Симба",
                "color": "Золотистый",
                "age": 5,
                "description": "Симба – это мейн-кун с роскошной гривой. Он "
                               "уверен в себе, любит исследовать мир и очень "
                               "дружелюбен.",
                "breed": breed3,
                "user": user2,
            },
            {
                "name": "Белла",
                "color": "Чёрный",
                "age": 4,
                "description": "Белла – маленькая и энергичная кошка. Она "
                               "обожает лазить и играть с другими питомцами.",
                "breed": breed1,
                "user": user2,
            },
            {
                "name": "Оливер",
                "color": "Оранжевый",
                "age": 7,
                "description": "Оливер – дружелюбный котенок, который любит "
                               "следовать за хозяином по дому. Очень ласковый "
                               "и привязчивый.",
                "breed": breed3,
                "user": user1,
            },
        ]

        # Добавляем котят в базу данных
        for kitten_data in kittens_data:
            Kitten.objects.create(
                name=kitten_data['name'],
                color=kitten_data['color'],
                age=kitten_data['age'],
                description=kitten_data['description'],
                breed=kitten_data['breed'],
                user=kitten_data['user']
            )

        self.stdout.write(
            self.style.SUCCESS('Данные о котятах успешно добавлены!'))
