from sport_activities_features_gui import __version__
from unittest import TestCase

class TestSportActivitiesFeaturesGui(TestCase):
    def test_version(self):
        assert __version__ == '0.4.0'
