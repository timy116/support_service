from datetime import datetime, date
from typing import Optional

from beanie import Document, Indexed, WriteRules
from beanie.odm.documents import DocType
from pydantic import BaseModel, ConfigDict
from pymongo.client_session import ClientSession

from app.models.utils import get_datetime_utc_8


class Product(BaseModel):
    product_name: str
    average_price: float


class DailyReport(Document):
    date: Indexed(date)
    category: Indexed(str)
    source: Indexed(str)
    products: list[Product]
    created_at: datetime = get_datetime_utc_8()
    updated_at: Optional[datetime] = None
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "date": "2024-09-11",
                "category": "水果",
                "source": "產地",
                "products": [
                    {
                        "product_name": "香蕉",
                        "average_price": 10.0
                    },
                    {
                        "product_name": "芒果",
                        "average_price": 15.3
                    }
                ]
            }
        }
    )

    class Settings:
        name = "daily_reports"
        indexes = ["date", "category", "source"]

    async def save(self: DocType, session: Optional[ClientSession] = None,
                   link_rule: WriteRules = WriteRules.DO_NOTHING, ignore_revision: bool = False, **kwargs) -> DocType:
        self.updated_at = get_datetime_utc_8()
        return await super().save(session, link_rule, ignore_revision, **kwargs)
