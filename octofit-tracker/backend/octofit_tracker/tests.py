from django.test import TestCase
from .models.user import User
from .models.team import Team
from .models.activity import Activity
from .models.leaderboard import Leaderboard
from .models.workout import Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username='testuser')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(name='Running')
        self.assertEqual(activity.name, 'Running')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(name='Main Leaderboard')
        self.assertEqual(leaderboard.name, 'Main Leaderboard')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Push Ups')
        self.assertEqual(workout.name, 'Push Ups')
