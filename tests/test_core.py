import pytest

from toycalc import split_once


def test_split_once_basic():
    assert split_once("a,b,c", ",") == ["a", "b", "c"]


def test_split_once_type_error():
    with pytest.raises(TypeError):
        split_once(["a,b,c"], ",")
