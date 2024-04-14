from rest_framework import serializers
from dungeon_and_dragons.characters.models import Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
