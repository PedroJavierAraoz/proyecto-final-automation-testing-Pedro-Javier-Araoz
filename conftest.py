import pytest



@pytest.fixture
def post_data():
    return {
        "title":"",
        "body":"",
        "userId":""
    }

@pytest.fixture
def user_data():
    return {
        "name":"",
        "username":"",
        "userId": ""    
    }
