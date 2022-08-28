from pydantic import BaseModel


class CurrencyPrice(BaseModel):
    base: str
    currency: str
    amount: float
