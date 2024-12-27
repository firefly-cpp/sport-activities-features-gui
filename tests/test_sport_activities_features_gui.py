from sport_activities_features_gui import __version__
from unittest import TestCase

class TestSportActivitiesFeaturesGui(TestCase):
    def test_version():
        assert __version__ == '0.3.2'
