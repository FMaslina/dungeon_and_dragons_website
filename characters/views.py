from rest_framework import generics

from dungeon_and_dragons.characters.models import Skill, Race, Character
from dungeon_and_dragons.characters.serializers import SkillSerializer, RaceSerializer, CharacterSerializer


class SkillCreate(generics.CreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillGet(generics.RetrieveAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillDelete(generics.DestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillList(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillUpdate(generics.UpdateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class RaceCreate(generics.CreateAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer


class RaceGet(generics.RetrieveAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer


class RaceDelete(generics.DestroyAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer


class RaceList(generics.ListAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer


class RaceUpdate(generics.UpdateAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer


class CharacterCreate(generics.CreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class CharacterGet(generics.RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class CharacterDelete(generics.DestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class CharacterList(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class CharacterUpdate(generics.UpdateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
