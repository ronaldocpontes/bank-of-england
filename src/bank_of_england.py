"""Downloads data from Bank of England Statistical Interactive Database - IADB."""
import pandas as pd
import requests
import io
from datetime import datetime

from importlib.resources import open_text

_URL_ENDPOINT = (
    "http://www.bankofengland.co.uk/boeapps/iadb/fromshowcolumns.asp?csv.x=yes"
)

_TEMPLATE = {"CSVF": "TN", "UsingCodes": "Y", "VPD": "Y", "VFD": "N"}


def mortage_instruments():
    """Pandas dataframe with the mortgage instruments configured in data/mortgage-instruments.csv."""
    return pd.read_csv(open_text("data", "mortgage-instruments.csv"))


def getSeries(series_codes, date_from, date_to=datetime.now(), replace_zeros=True):
    """Get Series data.

    Arguments:
        series_codes {[type]} -- [description]
        date_from {[type]} -- [description]

    Keyword Arguments:
        date_to {[type]} -- [description] (default: {datetime.now()})
        replace_zeros {bool} -- [description] (default: {True})

    Returns:
        [type] -- [description]

    """
    if not isinstance(series_codes, str):
        series_codes = ",".join(series_codes)

    date_from = date_from.strftime("%d/%b/%Y")
    date_to = date_to.strftime("%d/%b/%Y")
    p2 = {"SeriesCodes": series_codes, "Datefrom": date_from, "Dateto": date_to}
    payload = {**_TEMPLATE, **p2}
    response = requests.get(_URL_ENDPOINT, params=payload)
    try:
        df = pd.read_csv(io.BytesIO(response.content))
    except:
        raise Exception(
            f"Error making CSV request to BOE at {response.url}\nPayload:\n{payload}"
        )

    df["DATE"] = pd.to_datetime(df["DATE"])
    df = df.set_index("DATE")
    # convert object collums to numeric
    df = df.apply(lambda x: pd.to_numeric(x, errors="coerce"))
    if replace_zeros:
        df = df.replace(0, None)
    return df


def test():
    url_endpoint = (
        "http://www.bankofengland.co.uk/boeapps/iadb/fromshowcolumns.asp?csv.x=yes"
    )
    payload = {
        "Datefrom": "01/Jan/2000",
        "Dateto": "01/Oct/2018",
        "SeriesCodes": "IUMBV34,IUMBV37,IUMBV42,IUMBV45",
        "CSVF": "TN",
        "UsingCodes": "Y",
        "VPD": "Y",
        "VFD": "N",
    }

    full_url = "http://www.bankofengland.co.uk/boeapps/iadb/fromshowcolumns.asp?csv.x=yes&Datefrom=01%2FJan%2F2000&Dateto=01%2FOct%2F2018&SeriesCodes=IUMBV34%2CIUMBV37%2CIUMBV42%2CIUMBV45&CSVF=TN&UsingCodes=Y&VPD=Y&VFD=N"

    req = requests.Request("GET", url_endpoint, params=payload).prepare()
    print("\nreq1", req.url)
    print("\nreq2", full_url)
    print(req.headers)

    headers = {
        "User-Agent": "python-requests/2.22.0",
    }

    session = requests.Session()
    print(session.headers)
    session.headers.update(headers)
    print(session.headers)

    response = session.send(req)
    print(response.url)

    if True:
        return

    response = requests.get(url_endpoint, params=payload)
    try:
        df = pd.read_csv(io.BytesIO(response.content))
    except:
        raise Exception(
            f"Error making CSV request to BOE at {response.url}\nPayload:\n{payload}"
        )

    return df
