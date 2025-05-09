from abc import ABC, abstractmethod
from typing import List

from home.QuoteEngine import QuoteModel


class IngestorInterface(ABC):
    """Abstract base class for file ingestors."""

    @classmethod
    @abstractmethod
    def can_ingest(cls, path: str) -> bool:
        """Determine if the file can be ingested.

        :param path: path to the file
        :return: True if the file can be ingested, False otherwise
        """
        pass

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file and return a list of quotes.

        :param path: path to the file
        :return: list of QuoteModel objects
        """
        pass