import pytest
from datetime import datetime   


@pytest.fixture
def post_data():
    return {
        "title":"pepe",
        "body":"mensaje 1",
        "userId": 25
    }

@pytest.fixture
def user_data():
    return {
        "name":"",
        "username":"",
        "userId": ""    
    }

def pytest_html_report_title(report):
  
    report.title= "Api-test-report JsonPlaceholder - posts"