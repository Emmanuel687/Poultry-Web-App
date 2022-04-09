from django.test import TestCase
from .models import Profile,Project,Rating

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(user='manu', bio='your king is good', profile_photo='cloudlink.cloud')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))