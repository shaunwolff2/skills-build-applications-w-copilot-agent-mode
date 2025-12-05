from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient(host='localhost', port=27017)
        db = client['octofit_db']

        # Drop collections if they exist
        for col in ['users', 'teams', 'activities', 'leaderboard', 'workouts']:
            db[col].drop()

        # Create unique index on email for users
        db['users'].create_index('email', unique=True)

        # Insert test data
        marvel_team = {'name': 'Marvel', 'members': ['Iron Man', 'Captain America', 'Thor', 'Hulk']}
        dc_team = {'name': 'DC', 'members': ['Superman', 'Batman', 'Wonder Woman', 'Flash']}
        db['teams'].insert_many([marvel_team, dc_team])

        users = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team': 'Marvel'},
            {'name': 'Thor', 'email': 'thor@marvel.com', 'team': 'Marvel'},
            {'name': 'Hulk', 'email': 'hulk@marvel.com', 'team': 'Marvel'},
            {'name': 'Superman', 'email': 'superman@dc.com', 'team': 'DC'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'DC'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'DC'},
            {'name': 'Flash', 'email': 'flash@dc.com', 'team': 'DC'},
        ]
        db['users'].insert_many(users)

        activities = [
            {'user': 'Iron Man', 'activity': 'Running', 'duration': 30},
            {'user': 'Superman', 'activity': 'Flying', 'duration': 60},
        ]
        db['activities'].insert_many(activities)

        leaderboard = [
            {'team': 'Marvel', 'points': 100},
            {'team': 'DC', 'points': 90},
        ]
        db['leaderboard'].insert_many(leaderboard)

        workouts = [
            {'name': 'Push Ups', 'difficulty': 'Medium'},
            {'name': 'Squats', 'difficulty': 'Easy'},
        ]
        db['workouts'].insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
