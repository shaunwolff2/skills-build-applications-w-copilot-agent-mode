
from rest_framework import viewsets, routers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models.user import User
from .models.team import Team
from .models.activity import Activity
from .models.leaderboard import Leaderboard
from .models.workout import Workout
from .serializers import (
    UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

@api_view(['GET'])
def api_root(request, format=None):
    import os
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev"
    else:
        base_url = request.build_absolute_uri('/')[:-1]  # fallback to current host
    return Response({
        'users': f"{base_url}{reverse('user-list', request=request, format=format)}",
        'teams': f"{base_url}{reverse('team-list', request=request, format=format)}",
        'activities': f"{base_url}{reverse('activity-list', request=request, format=format)}",
        'leaderboard': f"{base_url}{reverse('leaderboard-list', request=request, format=format)}",
        'workouts': f"{base_url}{reverse('workout-list', request=request, format=format)}",
    })
