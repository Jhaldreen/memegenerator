from typing import List

from home.QuoteEngine.IngestorInterface import IngestorInterface
from home.QuoteEngine.QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Ingestor for txt files."""

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the file can be ingested."""
        return path.endswith('.txt')

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the txt file and return a list of quotes."""
        quotes = []
        try:
            with open(path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split(' - ')
                        if len(parts) == 2:
                            body, author = parts
                            quotes.append(QuoteModel(body.strip(), author.strip()))
        except Exception as e:
            print(f"Error parsing TXT file {path}: {e}")
        return quotes