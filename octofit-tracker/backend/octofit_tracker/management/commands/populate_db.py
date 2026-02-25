from django.core.management.base import BaseCommand
from django.db import connection
from djongo import models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Drop collections if they exist
        db = connection.cursor().db_conn
        db.drop_collection('users')
        db.drop_collection('teams')
        db.drop_collection('activities')
        db.drop_collection('leaderboard')
        db.drop_collection('workouts')

        # Create collections and insert test data
        users = [
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "marvel"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "dc"},
            {"name": "Superman", "email": "superman@dc.com", "team": "dc"},
        ]
        db.users.insert_many(users)
        db.users.create_index([("email", 1)], unique=True)

        teams = [
            {"name": "marvel", "members": ["Iron Man", "Captain America"]},
            {"name": "dc", "members": ["Wonder Woman", "Superman"]},
        ]
        db.teams.insert_many(teams)

        activities = [
            {"user": "Iron Man", "activity": "Running", "duration": 30},
            {"user": "Wonder Woman", "activity": "Cycling", "duration": 45},
        ]
        db.activities.insert_many(activities)

        leaderboard = [
            {"team": "marvel", "points": 100},
            {"team": "dc", "points": 90},
        ]
        db.leaderboard.insert_many(leaderboard)

        workouts = [
            {"user": "Iron Man", "workout": "Pushups", "reps": 50},
            {"user": "Superman", "workout": "Squats", "reps": 60},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
