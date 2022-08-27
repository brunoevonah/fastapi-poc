import requests
from fastapi import APIRouter

from app.models.config import Health

# from app.models.domain import CurrencyPrice

router = APIRouter(tags=["API"])

spot_prices_callback_router = APIRouter()


@router.get("/health", response_model=Health)
async def get_health():
    """
    Get API's health status
    """
    return Health()


# @spot_prices_callback_router.get(
#     "https://api.coinbase.com/v2/prices/spot?currency=USD", response_model=CurrencyPrice
# )
# def spot_prices():
#     response = requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD")
#     return response.json()


@router.get("/{currency}")
def get_spot_price_by_currency(currency: str):
    """
    Returns Currency spot price
    Currently using only coinbase validation for the currency passed on.
    """
    response = requests.get(
        f"https://api.coinbase.com/v2/prices/spot?currency={currency}"
    )
    return response.json()
