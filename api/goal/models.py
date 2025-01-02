from django.db import models
from api.authentication.models import User

# Goal that the user inputted e.g "Learn boxing"
class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="goals")
    title = models.CharField(max_length=255)
    motivation = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # goal_type = models.TextChoices # Need to ensure how to integrate this.

# Automatically generated milestones required to reach main goal based on user profile
class Milestone(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name="milestones")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Progress checks based on type of goal
class CheckIn(models.Model):
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE, related_name="checkins")
    date = models.DateField(auto_now_add=True)
    progress_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)