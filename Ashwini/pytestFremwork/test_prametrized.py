import pytest

list_db_craditionl =[('user1','password1'),('user2','password2'),('user6','password6'),('user5','password5')]
@pytest.mark.parametrize("user,password",[('user1','password1'),('user2','password2'),
                         ('user3','password3'),('user4','password4')])


def test_login(user,password):
    assert (user,password)in list_db_craditionl