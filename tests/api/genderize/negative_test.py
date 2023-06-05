import pytest
from pytest_schema import exact_schema, Or
import allure
import requests
from data.constants import ENDPOINTS, STATUSCODES
from assertpy import assert_that


def test_without_name_param():
    response = requests.get(ENDPOINTS.genderize)
    assert_that(response.status_code).is_in(*STATUSCODES.BAD_REQUEST)

def test_without_name_value():
    response = requests.get(ENDPOINTS.genderize, {'name': ''})
    response_json = response.json()
    assert_that(response.status_code).is_in(*STATUSCODES.OK)
    assert_that(response_json.get('count')).is_equal_to(0)
    assert_that(response_json.get('gender')).is_equal_to(None)
    assert_that(response_json.get('name')).is_equal_to('')
    assert_that(response_json.get('probability')).is_equal_to(0.0)

def test_with_numerical_name_value():
    response = requests.get(ENDPOINTS.genderize, {'name': 123})
    response_json = response.json()
    assert_that(response.status_code).is_in(*STATUSCODES.OK)
    assert_that(response_json.get('count')).is_equal_to(0)
    assert_that(response_json.get('gender')).is_equal_to(None)
    assert_that(response_json.get('name')).is_equal_to('123')
    assert_that(response_json.get('probability')).is_equal_to(0.0)

