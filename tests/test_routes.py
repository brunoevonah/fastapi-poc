import json
from contextlib import contextmanager
from unittest.mock import MagicMock, patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.routes.api import router as api_router


@pytest.fixture
def client():
    """
    Creates app to use in the tests suite.
    """
    app = FastAPI()
    app.include_router(api_router)
    return TestClient(app)


@pytest.fixture
def coinbase_usd_spot_price():
    with open("tests/fixtures/usd_spot_price.json") as usd_json:
        return json.loads(usd_json.read())


@pytest.fixture
def coinbase_jpy_spot_price():
    with open("tests/fixtures/jpy_spot_price.json") as jpy_json:
        return json.loads(jpy_json.read())


@pytest.fixture
def coinbase_eur_spot_price():
    with open("tests/fixtures/eur_spot_price.json") as eur_json:
        return json.loads(eur_json.read())


@pytest.fixture
def coinbase_gbp_spot_price():
    with open("tests/fixtures/gbp_spot_price.json") as gbp_json:
        return json.loads(gbp_json.read())


@contextmanager
def mock_spot_price_requests(spot_price_request_value, status_code):
    """This context manager is used to reuse the patches of the spot price requests.

    The mocks will be yielded to the context as a dict.
    """
    with patch("app.routes.api.requests", autospec=True) as mocked_request:
        mock_response = MagicMock()
        mock_response.json.return_value = spot_price_request_value
        mock_response.status_code = status_code
        mocked_request.get.return_value = mock_response
        yield mocked_request


def test_get_spot_price_by_currency_usd(client, coinbase_usd_spot_price):
    """
    Test get spot price with USD
    """
    # Given
    currency = "usd"
    expected_response = {"base": "BTC", "currency": "USD", "amount": 21725.71}

    # When
    with mock_spot_price_requests(coinbase_usd_spot_price, 200) as mock:

        # Then
        response = client.get(f"/{currency}")

        mock.get.assert_called_with(
            f"https://api.coinbase.com/v2/prices/spot?currency={currency}"
        )
        assert response.status_code == 200
        assert response.json() == expected_response


def test_get_spot_price_by_currency_gbp(client, coinbase_gbp_spot_price):
    """
    Test get spot price with GBP
    """
    # Given
    currency = "gbp"
    expected_response = {"base": "BTC", "currency": "GBP", "amount": 18315.8}

    # When
    with mock_spot_price_requests(coinbase_gbp_spot_price, 200) as mock:

        # Then
        response = client.get(f"/{currency}")

        mock.get.assert_called_with(
            f"https://api.coinbase.com/v2/prices/spot?currency={currency}"
        )
        assert response.status_code == 200
        assert response.json() == expected_response


def test_get_spot_price_by_currency_eur(client, coinbase_eur_spot_price):
    """
    Test get spot price with EUR
    """
    # Given
    currency = "eur"
    expected_response = {"base": "BTC", "currency": "EUR", "amount": 21585.79}

    # When
    with mock_spot_price_requests(coinbase_eur_spot_price, 200) as mock:

        # Then
        response = client.get(f"/{currency}")

        mock.get.assert_called_with(
            f"https://api.coinbase.com/v2/prices/spot?currency={currency}"
        )
        assert response.status_code == 200
        assert response.json() == expected_response


def test_get_spot_price_by_currency_jpy(client, coinbase_jpy_spot_price):
    """
    Test get spot price with JPY
    """
    # Given
    currency = "jpy"
    expected_response = {
        "base": "BTC",
        "currency": "JPY",
        "amount": 2972700.3576599973908232,
    }

    # When
    with mock_spot_price_requests(coinbase_jpy_spot_price, 200) as mock:

        # Then
        response = client.get(f"/{currency}")

        mock.get.assert_called_with(
            f"https://api.coinbase.com/v2/prices/spot?currency={currency}"
        )
        assert response.status_code == 200
        assert response.json() == expected_response


def test_get_spot_price_by_currency_invalid(client):
    """
    Test get spot price with invalid currency
    """
    # Given
    currency = "gg"
    expected_response = {"message": "Currency is invalid"}

    # When
    with mock_spot_price_requests("Invalid Payload from Coinbase", 400) as mock:

        # Then
        response = client.get(f"/{currency}")

        mock.get.assert_called_with(
            f"https://api.coinbase.com/v2/prices/spot?currency={currency}"
        )
        assert response.status_code == 400
        assert response.json() == expected_response


def test_get_health(client):
    """
    Test get application health status
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "App running"}
