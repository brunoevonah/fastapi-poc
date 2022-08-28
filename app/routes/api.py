import requests
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.models.config import Health
from app.models.domain import CurrencyPrice

router = APIRouter(tags=["API"])

spot_prices_callback_router = APIRouter()


@router.get("/health", response_model=Health)
async def get_health():
    """
    Get API's health status
    """
    return Health()


# TODO read more about the fastapi callback and check if this should be used here.
# @spot_prices_callback_router.get(
#     "https://api.coinbase.com/v2/prices/spot?currency=USD", response_model=CurrencyPrice
# )
# def spot_prices():
#     response = requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD")
#     return response.json()

# I would like to sugest here to have another URI,
# something like /price/{currency}  or price?currency={currency}
@router.get("/{currency}")
def get_spot_price_by_currency(currency: str):
    """
    Returns Currency spot price
    Currently using only coinbase validation for the currency passed on.
    """
    # TODO refactor this to use variable to set the URL.
    coinbase_response = requests.get(
        f"https://api.coinbase.com/v2/prices/spot?currency={currency}"
    )

    validate_response = validate_coinbase_response(coinbase_response)

    if not validate_response["valid"]:
        return validate_response["jsonResponse"]

    json_data = coinbase_response.json()["data"]

    response = CurrencyPrice(
        base=json_data["base"],
        currency=json_data["currency"],
        amount=json_data["amount"],
    )
    return response


def validate_coinbase_response(coinbase_response: requests.Response):

    validate_response = {"valid": True, "jsonResponse": JSONResponse}

    if coinbase_response.status_code in [
        status.HTTP_400_BAD_REQUEST,
        status.HTTP_500_INTERNAL_SERVER_ERROR,
    ]:
        error_response = {"message": "Currency is invalid"}
        validate_response["valid"] = False
        validate_response["jsonResponse"] = JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content=error_response
        )

    # TODO check how to mock this, and add json schema validation
    # try:
    #     json.loads(coinbase_response.text)
    # except ValueError as e:
    #     error_response = {
    #         "message": "Invalid json format"
    #     }
    #     validate_response["valid"] = False
    #     validate_response["jsonResponse"] =
    #       JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=error_response)

    return validate_response
