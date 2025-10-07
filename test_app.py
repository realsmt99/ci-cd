import unittest
from unittest.mock import Mock
from app import calculate_distance
from app import testifnewuser
import datetime
from app import todays_expiration

class TestApp(unittest.TestCase):
    def test_calculate_distance(self):
        point1 = Mock()
        point1.distance = 0
        self.assertEqual(calculate_distance(point1), 1)
    

    def test_user_is_new(self):
        user = Mock()
        user.is_new = True
        assert testifnewuser(user) == True

    def test_user_todays_exp(self):
        user = Mock()
        fixed_time = datetime.datetime(2024, 1, 15, 12, 0, 0)
        user.iseq =    fixed_time 
        assert todays_expiration(user) == False