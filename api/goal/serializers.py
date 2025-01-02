from api.goal.models import Goal, Milestone, CheckIn
from rest_framework.serializers import ModelSerializer

class GoalSerializer(ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']

class MilestoneSerializer(ModelSerializer):
    class Meta:
        model = Milestone
        fields = ['id', 'goal', 'title', 'description', 'due_date', 'completed', 'created_at', 'updated_at']

class CheckInSerializer(ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ['id', 'milestone', 'date', 'progress_notes', 'created_at']
