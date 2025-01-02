from django.urls import URLResolver, path, include
from api.goal.views import GoalView, MilestoneView
urlpatterns = [
    path('', GoalView.as_view()),
    path('milestone/<int:goal_id>', MilestoneView.as_view())
]
