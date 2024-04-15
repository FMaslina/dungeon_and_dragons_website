from rest_framework import generics

from dungeon_and_dragons.characters.models import Skill
from dungeon_and_dragons.characters.serializers import SkillSerializer


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
    