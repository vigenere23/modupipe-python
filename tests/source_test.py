import unittest
from typing import Iterator

from modupipe.exceptions import MaxIterationsReached
from modupipe.mapper import Mapper
from modupipe.source import MaxIterations, Source

VALUE = 3.546
MAPPED_VALUE = 6.394


class FakeSource(Source[float]):
    def fetch(self) -> Iterator[float]:
        yield VALUE
        yield VALUE


class FakeMapper(Mapper[float, float]):
    def map(self, _: Iterator[float]) -> Iterator[float]:
        yield MAPPED_VALUE
        yield MAPPED_VALUE


class MaxIterationsTest(unittest.TestCase):
    def test_itStopsAfterMaxIterations(self):
        source = MaxIterations(FakeSource(), nb_iterations=1)
        items = source.fetch()

        next(items)

        with self.assertRaises(MaxIterationsReached):
            next(items)

    def test_givenMaxIterationsSameAsNumberOfSourceItems_itDoesNotStop(self):
        source = MaxIterations(FakeSource(), nb_iterations=2)
        items = source.fetch()

        next(items)
        next(items)


class MappedSourceTest(unittest.TestCase):
    def setUp(self) -> None:
        pass
