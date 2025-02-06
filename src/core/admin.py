from django.contrib import admin

import src.core.models as models


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "role")


@admin.register(models.FileManager)
class FileManagerADMIN(admin.ModelAdmin):
    list_display = ("id",)


@admin.register(models.Region)
class FileManagerADMIN(admin.ModelAdmin):
    list_display = ("id",)


@admin.register(models.District)
class FileManagerADMIN(admin.ModelAdmin):
    list_display = ("id",)


@admin.register(models.Stadion)
class FileManagerADMIN(admin.ModelAdmin):
    list_display = ("id",)


@admin.register(models.StadionContact)
class FileManagerADMIN(admin.ModelAdmin):
    list_display = ("id",)


@admin.register(models.StadionImages)
class FileManagerADMIN(admin.ModelAdmin):
    list_display = ("id",)
