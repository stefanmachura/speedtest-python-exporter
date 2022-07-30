import datetime
from dataclasses import dataclass

from schemas import ResultSchema


@dataclass
class Result:
    download: float
    upload: float
    ping: float
    timestamp: datetime.datetime
