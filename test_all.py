import datetime

from services import ResultService

SAMPLE_RESULT = {
    "download": 50209317.274528176,
    "upload": 55289537.74748478,
    "ping": 12.031,
    "server": {
        "url": "http://ook-waw-x1.puregig.net:8080/speedtest/upload.php",
        "lat": "52.2323",
        "lon": "21.0084",
        "name": "Warsaw",
        "country": "Poland",
        "cc": "PL",
        "sponsor": "Netprotect",
        "id": "37600",
        "host": "ook-waw-x1.puregig.net:8080",
        "d": 274.0894577424545,
        "latency": 12.031,
    },
    "timestamp": "2022-07-30T07:55:08.214333Z",
    "bytes_sent": 69206016,
    "bytes_received": 62874376,
    "share": "http://www.speedtest.net/result/13473650590.png",
    "client": {
        "ip": "194.116.193.53",
        "lat": "52.5705",
        "lon": "17.006",
        "isp": "Komster Sp. z o.o.",
        "isprating": "3.7",
        "rating": "0",
        "ispdlavg": "0",
        "ispulavg": "0",
        "loggedin": "0",
        "country": "PL",
    },
}


def test_result_serialization():
    result = ResultService.create(SAMPLE_RESULT)
    assert result.download == 50209317.274528176
    assert result.upload == 55289537.74748478
    assert result.ping == 12.031
    assert result.timestamp == datetime.datetime(
        2022, 7, 30, 7, 55, 8, 214333, tzinfo=datetime.timezone.utc
    )


def test_result_as_dict():
    expected = {
        "download": 50209317.274528176,
        "upload": 55289537.74748478,
        "ping": 12.031,
        "timestamp": datetime.datetime(
            2022, 7, 30, 7, 55, 8, 214333, tzinfo=datetime.timezone.utc
        ),
    }
    result = ResultService.create(SAMPLE_RESULT)
    result_dict = ResultService.as_dict(result)
    assert result_dict == expected


def test_result_as_human_readable_dict():
    expected = {
        "download": 47.88333632901018,
        "upload": 52.728212115750104,
        "ping": 12.031,
        "timestamp": "07/30/2022, 07:55:08",
    }
    result = ResultService.create(SAMPLE_RESULT)
    result_dict = ResultService.as_dict(result, human=True)
    assert result_dict == expected
