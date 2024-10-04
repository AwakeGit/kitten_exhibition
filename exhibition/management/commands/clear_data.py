from django.core.management.base import BaseCommand

from exhibition.models import Breed, Kitten


class Command(BaseCommand):
    help = 'Удаление всех данных о котятах и породах'

    def handle(self, *args, **kwargs):
        # Удаляем всех котят
        Kitten.objects.all().delete()
        # Удаляем все породы
        Breed.objects.all().delete()

        self.stdout.write(self.style.SUCCESS(
            'Все данные о котятах и породах успешно удалены!'))
