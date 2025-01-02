from django.shortcuts import render
from rest_framework import authentication, response, views, status
from rest_framework.permissions import IsAuthenticated
from api.authentication.serializers import SignUpSerializer, LoginSerializer
from api.authentication.models import User
from api.goal.models import Goal, CheckIn, Milestone
from api.goal.serializers import GoalSerializer, CheckInSerializer, MilestoneSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from core.constants.request import Request


class GoalView(views.APIView):
    permission_classes = [
        IsAuthenticated
    ]  # Ensures all endpoints are protected by auth

    """Get all current user current goals"""

    def get(self, request: Request) -> response.Response:
        goals = Goal.objects.filter(user=request.user)
        if len(goals) == 0:
            return response.Response(
                {
                    "message": "No goals found.",
                    "username": request.user.username,
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = GoalSerializer(goals, many=True)
        return response.Response(
            {
                "message": "Goals fetched successfully.",
                "username": request.user.username,
                "goals": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )

    """Create goal for user"""

    def post(self, request: Request) -> response.Response:
        serializer = GoalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(
                {
                    "message": "Goal created successfully.",
                    "username": request.user.username,
                    "goal": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return response.Response(
            {"message": "Bad request.", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

class MilestoneView(views.APIView):
    permission_classes = [
        IsAuthenticated
    ]  # Ensures all endpoints are protected by auth

    """Get all current user current milestones"""

    def get(self, request: Request) -> response.Response:
        milestones = Milestone.objects.filter(user=request.user)
        if len(milestones) == 0:
            return response.Response(
                {
                    "message": "No milestones found.",
                    "username": request.user.username,
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = MilestoneSerializer(milestones, many=True)
        return response.Response(
            {
                "message": "Milestones fetched successfully.",
                "username": request.user.username,
                "milestones": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )

    """Create milestone for user"""

    def post(self, request: Request, goal_id) -> response.Response:
        request.data['goal'] = goal_id
        serializer = MilestoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(
                {
                    "message": "Milestones created successfully.",
                    "username": request.user.username,
                    "milestone": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return response.Response(
            {"message": "Bad request.", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
