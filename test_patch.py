import datetime as dt
from mock import Mock, patch
from play_patch import find_expired_users

@patch("play_patch.get_all_users")
def test_find_expired_users(mocked_get_all_users):
    db = Mock()
    mocked_get_all_users.return_value = [
        Mock(id=1, expiration_date=dt.datetime.now() + dt.timedelta(days=1)),
        Mock(id=10, expiration_date=dt.datetime.now() + dt.timedelta(days=2)),
        Mock(id = 20 , expiration_date = dt.datetime.now() )
        Mock(id=3, expiration_date=dt.datetime.now() - dt.timedelta(days=1)),
        Mock(id=4, expiration_date=dt.datetime.now() - dt.timedelta(days=2)),
        Mock(id=5, expiration_date=dt.datetime.now()),
    ]
    res = find_expired_users(db)
    expected_res = [3, 4, 5,20]
    assert expected_res == rest





   

