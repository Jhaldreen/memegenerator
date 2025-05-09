import pandas as pd
from typing import List

from home.QuoteEngine.IngestorInterface import IngestorInterface
from home.QuoteEngine.QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Ingestor for csv files."""

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the file can be ingested."""
        return path.endswith('.csv')

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the csv file and return a list of quotes."""
        quotes = []
        try:
            df = pd.read_csv(path)
            for _, row in df.iterrows():
                quotes.append(QuoteModel(row['body'], row['author']))
        except Exception as e:
            print(f"Error parsing CSV file {path}: {e}")
        return quotes