from django.contrib import admin

from .models import Breed, Kitten, Rating


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Kitten)
class KittenAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'age', 'breed', 'user')
    list_filter = ('breed', 'color')
    search_fields = ('name', 'breed__name', 'color')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('get_kitten_name', 'rating', 'user')
    search_fields = ('kitten__name', 'user__username')
    list_filter = ('rating', 'kitten__breed')

    def get_kitten_name(self, obj):
        return f"{obj.kitten.name} ({obj.kitten.breed.name})"

    get_kitten_name.short_description = 'Имя котенка'