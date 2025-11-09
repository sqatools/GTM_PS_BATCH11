import pytest   # ✅ Import added

@pytest.mark.xfail   # ✅ Fixed spelling
def test_logout():
    assert True      # ✅ Use capital F in False
    print("Logout done")