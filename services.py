import json
from dataclasses import asdict

from objects import Result
from schemas import ResultSchema


class ResultService:
    schema = ResultSchema()

    @classmethod
    def create(cls, result: dict) -> Result:
        return Result(**cls.schema.load(result))

    @classmethod
    def as_dict(cls, result: Result, human=False) -> dict:
        if human:
            # convert from bits/s to megabits/s
            result.upload = result.upload / 1024 / 1024
            result.download = result.download / 1024 / 1024
            result.timestamp = result.timestamp.strftime("%m/%d/%Y, %H:%M:%S")
        return asdict(result)

    @classmethod
    def to_file(cls, result: Result, fname="result.json"):
        with open(fname, "w") as result_file:
            json.dump(
                cls.as_dict(result, human=True),
                result_file,
                default=str,
                indent=4,
                sort_keys=True,
            )
