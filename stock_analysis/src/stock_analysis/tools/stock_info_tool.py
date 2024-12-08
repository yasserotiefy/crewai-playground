from typing import Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field

import yfinance as yf

from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter


class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
   pass

session = CachedLimiterSession(
   limiter=Limiter(RequestRate(2, Duration.SECOND*5)),  # max 2 requests per 5 seconds
   bucket_class=MemoryQueueBucket,
   backend=SQLiteCache("yfinance.cache"),
)


class StockInfoInput(BaseModel):
    """Input schema for StockInfoTool."""

    company_ticker: str = Field(..., description="The stock ticker to get information for.")


class StockInfoTool(BaseTool):
    name: str = "StockInfoTool"
    description: str = (
        "Get information about a stock."
    )
    args_schema: Type[BaseModel] = StockInfoInput

    def _run(self, company_ticker: str):
        # Create a session with rate limiting and caching
        session = CachedLimiterSession(
            limiter=Limiter(RequestRate(2, Duration.SECOND*5)),  # max 2 requests per 5 seconds
            bucket_class=MemoryQueueBucket,
            backend=SQLiteCache("yfinance.cache"),
        )
        stock = yf.Ticker(company_ticker, session=session)
        return [stock.info, stock.analyst_price_targets, stock.funds_data]
