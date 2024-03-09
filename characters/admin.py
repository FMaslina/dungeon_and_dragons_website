from django.contrib import admin
from .models import Skill, Race, Character


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'effect',)
    search_fields = ('name', 'effect',)
    list_filter = ('name',)


admin.site.register(Skill, SkillAdmin)


class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_character_stat_points',)
    search_fields = ('name',)
    list_filter = ('start_character_stat_points',)


admin.site.register(Race, RaceAdmin)


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'race', 'avaliable_stat_points', 'health', 'mana', 'armor_class',)
    search_fields = ('owner', 'name', 'race',)
    list_filter = ('owner', 'race',)


admin.site.register(Character, CharacterAdmin)
