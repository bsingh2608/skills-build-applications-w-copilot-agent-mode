from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker import models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear existing data
        User.objects.all().delete()
        models.Team.objects.all().delete()
        models.Activity.objects.all().delete()
        models.Leaderboard.objects.all().delete()
        models.Workout.objects.all().delete()

        # Create Teams
        marvel = models.Team.objects.create(name='Marvel')
        dc = models.Team.objects.create(name='DC')

        # Create Users
        tony = User.objects.create_user(username='tony', email='tony@stark.com', password='ironman', team=marvel)
        steve = User.objects.create_user(username='steve', email='steve@rogers.com', password='captain', team=marvel)
        bruce = User.objects.create_user(username='bruce', email='bruce@wayne.com', password='batman', team=dc)
        clark = User.objects.create_user(username='clark', email='clark@kent.com', password='superman', team=dc)

        # Create Activities
        models.Activity.objects.create(user=tony, type='run', duration=30, distance=5)
        models.Activity.objects.create(user=steve, type='cycle', duration=60, distance=20)
        models.Activity.objects.create(user=bruce, type='swim', duration=45, distance=2)
        models.Activity.objects.create(user=clark, type='run', duration=50, distance=10)

        # Create Workouts
        models.Workout.objects.create(name='Morning Cardio', description='A quick morning run', suggested_for=marvel)
        models.Workout.objects.create(name='Strength Training', description='Heavy lifting', suggested_for=dc)

        # Create Leaderboard
        models.Leaderboard.objects.create(team=marvel, points=100)
        models.Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
