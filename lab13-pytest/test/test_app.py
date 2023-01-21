from app import hello
from app import extract_sentiment
from app import text_contain_word
from app import bubble_sort
import pytest
import numpy as np


def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want


testdata = ["I think today will be a great day","I think this will turn out very well"]

@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):

    sentiment = extract_sentiment(sample)

    assert sentiment > 0



testdata = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
    ]

@pytest.mark.parametrize('sample, word, expected_output', testdata)
def test_text_contain_word(sample, word, expected_output):

    assert text_contain_word(word, sample) == expected_output




examples =(([39, 12, 18, 85, 72, 10, 2, 18],[2, 10, 12, 18, 18, 39, 72, 85]),
([1,2,3],[1,3,2]),
([-3,-6,-2,-7,-2,-4,-3],[-7, -6, -4, -3, -3, -2, -2]),
([38, 12, 18, 85, 72, 10, 2, 18],[2, 10, 12, 18, 18, 38, 72, 85]),
("string","string"),
([1],[1]),
(np.NaN,4),
(([1,2,3]),([1,2,3])),
({1,4,2},{1,2,4}),
(np.array([5,4,3]),np.array([3,4,5]))
)


@pytest.mark.parametrize("data, expected",examples)
def test_if_sorting_works(data,expected):

    assert bubble_sort(data) == expected




