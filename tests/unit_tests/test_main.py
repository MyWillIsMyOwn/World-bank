from unittest import mock

import pytest

from task.main import get_list_of_countries, count_projects_per_country_amount, get_money, money_invested_per_country


input_data = [
    {"some_key": "some_value", "countryname": "Polska", "totalamt": 100},
    {"some_key": "some_value", "countryname": "Polska", "totalamt": 200},
    {"some_key": "some_value", "countryname": "Czechy", "totalamt": 50}
]
list_of_countries = [
    "Polska",
    "Polska",
    "Czechy"
]


@mock.patch("task.main.open_json")
def test_get_countries(open_json):
    open_json.return_value = input_data
    assert get_list_of_countries() == list_of_countries


def test_amount_of_projects():
    assert count_projects_per_country_amount(list_of_countries) == {'Polska': 2, 'Czechy': 1}


@pytest.mark.parametrize('in_data, out_data', [
    ("Polska", 300),
    ("Czechy", 50)
])
@mock.patch("task.main.open_json")
def test_money_invested(open_json, in_data, out_data):
    open_json.return_value = input_data
    assert get_money(in_data) == out_data


@mock.patch("task.main.open_json")
def test_rere(open_json):
    open_json.return_value = input_data
    assert money_invested_per_country(list_of_countries) == {'Czechy': 50, 'Polska': 300}
