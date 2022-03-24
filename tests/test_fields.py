import pytest
from src.fields.field import Field

class TestField:

    def test_init(cls):
        f = Field(order=3)