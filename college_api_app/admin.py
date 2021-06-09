from django.contrib import admin

from college_api_app.models import College, Category, City, Country


@admin.register(College)
class AdminCollege(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryCollege(admin.ModelAdmin):
    pass


@admin.register(City)
class CityCollege(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryCollege(admin.ModelAdmin):
    pass
