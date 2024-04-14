from rest_framework import serializers
from dungeon_and_dragons.characters.models import Skill, Race


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = "__all__"
