import pytest

list_db_cred=[('user1','password1'),('user2','password2'),('user5','password5'),('user6','password6')]

@pytest.mark.parametrize("user,password",[('user1','password1'),('user2','password2'),('user3','password3'),('user4','password4')])

def test_login(user,password):
    assert(user,password) in list_db_cred


# python -m pytest -v .\test_parameterize.py
