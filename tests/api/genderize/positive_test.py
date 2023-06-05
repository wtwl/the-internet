import pytest
from pytest_schema import exact_schema, Or
import allure
import requests
from data.constants import ENDPOINTS, STATUSCODES
from assertpy import assert_that

response_schema = {
    "count": int,
    "gender": Or(str, None),
    "name": str,
    "probability": float
}

response_multiple_names_schema = [{"count": int,
                                   "gender": str,
                                   "name": str,
                                   "probability": float}]


@pytest.mark.parametrize("test_input", ["Андрей", "Максим", "Ирина"])
def test_get_ok_gender(test_input):
    response = requests.get(ENDPOINTS.genderize, {"name": test_input})
    assert_that(response.status_code).is_in(*STATUSCODES.OK)
    assert_that(exact_schema(response_schema)).is_equal_to(response.json())

@pytest.mark.parametrize("test_input", ["Дима", "Катя", "Настя"])
def test_not_existing_name(test_input):
    response = requests.get(ENDPOINTS.genderize, {"name": test_input})
    assert_that(response.status_code).is_in(*STATUSCODES.OK)
    assert_that(exact_schema(response_schema)).is_equal_to(response.json())

def test_multiple_names():
    response = requests.get(ENDPOINTS.genderize, [('name[]', 'Андрей'), ('name[]', 'Максим'), ('name[]', 'Ирина')])
    assert_that(response.status_code).is_in(*STATUSCODES.OK)
    assert_that(exact_schema(response_multiple_names_schema)).is_equal_to(response.json())
