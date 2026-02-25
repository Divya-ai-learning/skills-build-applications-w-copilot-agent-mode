from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name="Test Hero", email="hero@test.com", team="marvel")
        self.assertEqual(user.name, "Test Hero")
        self.assertEqual(user.email, "hero@test.com")
        self.assertEqual(user.team, "marvel")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="marvel", members=["Test Hero"])
        self.assertEqual(team.name, "marvel")
        self.assertIn("Test Hero", team.members)

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user="Test Hero", activity="Running", duration=30)
        self.assertEqual(activity.activity, "Running")
        self.assertEqual(activity.duration, 30)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team="marvel", points=100)
        self.assertEqual(leaderboard.team, "marvel")
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(user="Test Hero", workout="Pushups", reps=50)
        self.assertEqual(workout.workout, "Pushups")
        self.assertEqual(workout.reps, 50)
