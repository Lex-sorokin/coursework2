from unittest.mock import patch

import pytest
import requests

from src.hh import ConnectHHError


def test_load_vacancies(object_hh, crude_data) -> None:
    with patch("requests.get") as mock_requests:
        mock_requests.return_value.json.return_value = crude_data
        object_hh.load_vacancies("python")
        assert object_hh.get_vacancies == crude_data.get("items")


@patch("requests.get")
def test_connect(mock_requests, object_hh) -> None:
    mock_requests.return_value.status_code = 200
    assert object_hh.connect()


@patch("requests.get")
def test_disconnect(mock_requests, object_hh) -> None:
    with pytest.raises(ConnectHHError):
        mock_requests.return_value.status_code = 404
        object_hh.connect()


@patch("requests.get", side_effect=requests.RequestException)
def test_side_effect_connect(mock_requests, object_hh) -> None:
    with pytest.raises(ConnectHHError):
        object_hh.connect()
