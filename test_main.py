"""
Test goes here

"""

from mylib.query import query


def test_query():
    assert query("SELECT Pregnancies FROM diabetesDB WHERE Glucose = '85'") == [
        ("1",),
        ("2",),
        ("6",),
        ("8",),
        ("5",),
        ("4",),
        ("11",),
    ]

    pass


def test_extract():
    pass


def test_transform_load():
    pass
