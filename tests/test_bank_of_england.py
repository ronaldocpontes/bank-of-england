"""Test."""
from dateutil.relativedelta import relativedelta
from bank_of_england import getSeries, mortage_instruments, test
from datetime import datetime


def test_mortgage_instruments():
    """Test."""
    instruments = mortage_instruments().SERIES
    # instruments.apply(lambda x: print(x))
    # df = getSeries(
    #     "IUMBV34,IUMBV37,IUMBV42,IUMBV45", datetime.now() - relativedelta(months=3)
    # )
    df = test()
    # df.head()
    # df.info()
    # df.plot()
    # assert say_hello() == "Hello"
