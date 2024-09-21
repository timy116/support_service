from enum import Enum
from typing import Literal


class BaseEnum(str, Enum):
    def __str__(self) -> str:
        return str(self.value)


class SupplyType(BaseEnum):
    ORIGIN = "產地"
    WHOLESALE = "批發"
    RETAIL = "零售"


class Category(BaseEnum):
    AGRICULTURE = "農產品"
    LIVESTOCK = "畜禽產品"
    FISHERY = "漁產品"


class ProductType(BaseEnum):
    # Agriculture
    RICE = "糧"
    VEGETABLE = "蔬菜"
    FRUIT = "水果"
    FLOWER = "花卉"

    # Livestock
    HOG = "豬"
    RAM = "羊"
    CHICKEN = "雞"
    DUCK = "鴨"
    GOOSE = "鵝"

    # Fishery
    FISH = "魚類"
    SHRIMP = "蝦類"
    SHELLFISH = "貝類"

    # Others
    OTHERS = "其他"


class LogLevel(BaseEnum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class FileTypes(BaseEnum):
    CSV = "csv"
    JSON = "json"
    EXCEL = "excel"
    PDF = "pdf"
    TXT = "txt"


class GmailScopes(BaseEnum):
    READ_ONLY= "https://www.googleapis.com/auth/gmail.readonly"
    SEND = "https://www.googleapis.com/auth/gmail.send"
    MODIFY = "https://www.googleapis.com/auth/gmail.modify"
    FULL = "https://mail.google.com/"


class IsNotHolidays(BaseEnum):
    LABOR_DAY = "勞動節"
    ARMED_FORCES_DAY = "軍人節"


class OpenApis(BaseEnum):
    TAIWAN_CALENDAR_API = "https://data.ntpc.gov.tw/api/datasets/308DCD75-6434-45BC-A95F-584DA4FED251"


class RedisCacheKey(BaseEnum):
    TAIWAN_CALENDAR = "taiwan_calendar_{year}"
