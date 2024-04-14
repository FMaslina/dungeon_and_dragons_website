from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


# TODO: Додумать реализацию способностей
class Skill(models.Model):
    name = models.TextField(null=True, blank=True, verbose_name="Название способности")
    effect = models.TextField(null=True, blank=True, verbose_name="Эффект способности")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Способность'
        verbose_name_plural = 'Способности'


class Race(models.Model):
    name = models.TextField(null=True, blank=True, verbose_name="Название расы")
    start_character_stat_points = models.IntegerField(null=True, blank=True,
                                                      verbose_name="Количество очков характеристик")
    strength_bonus = models.IntegerField(null=True, blank=True, verbose_name="Бонус к силе")
    dexterity_bonus = models.IntegerField(null=True, blank=True, verbose_name="Бонус к ловкости")
    constitution_bonus = models.IntegerField(null=True, blank=True, verbose_name="Бонус к телосложению")
    intelligence_bonus = models.IntegerField(null=True, blank=True, verbose_name="Бонус к интеллекту")
    wisdom_bonus = models.IntegerField(null=True, blank=True, verbose_name="Бонус к мудрости")
    charisma_bonus = models.IntegerField(null=True, blank=True, verbose_name="Бонус к харизме")
    skills = models.ManyToManyField(Skill, blank=True, verbose_name="Способности")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Раса'
        verbose_name_plural = 'Расы'


class Character(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="Владелец")
    name = models.TextField(null=True, blank=True, verbose_name="Имя")
    race = models.ForeignKey(to=Race, on_delete=models.CASCADE, verbose_name="Раса")
    available_stat_points = models.IntegerField(null=True, blank=True, verbose_name="Доступные очки характеристик")
    strength = models.IntegerField(null=True, blank=True, verbose_name="Сила")
    dexterity = models.IntegerField(null=True, blank=True, verbose_name="Ловкость")
    constitution = models.IntegerField(null=True, blank=True, verbose_name="Телосложение")
    intelligence = models.IntegerField(null=True, blank=True, verbose_name="Интеллект")
    wisdom = models.IntegerField(null=True, blank=True, verbose_name="Мудрость")
    charisma = models.IntegerField(null=True, blank=True, verbose_name="Харизма")
    health = models.IntegerField(null=True, blank=True, verbose_name="Макс. здоровье")
    mana = models.IntegerField(null=True, blank=True, verbose_name="Макс. мана")
    current_health = models.IntegerField(null=True, blank=True, verbose_name="Текущее здоровье")
    current_mana = models.IntegerField(null=True, blank=True, verbose_name="Текущая мана")
    armor_class = models.IntegerField(null=True, blank=True, verbose_name="Класс доспеха")
    skills = models.ManyToManyField(Skill, blank=True, verbose_name="Способности")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'
