from typing import List

from home.QuoteEngine import CSVIngestor, DocxIngestor, PDFIngestor
from home.QuoteEngine.IngestorInterface import IngestorInterface
from home.QuoteEngine.QuoteModel import QuoteModel
from home.QuoteEngine.TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """Encapsulates helper classes to ingest multiple file types."""

    ingestors = [TextIngestor, CSVIngestor, DocxIngestor, PDFIngestor]

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the file can be ingested."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return True
        return False

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file and return a list of quotes."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise ValueError(f"Cannot ingest file: {path}")