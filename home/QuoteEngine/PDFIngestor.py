from typing import List
import subprocess
import os
import tempfile
from home.QuoteEngine.IngestorInterface import IngestorInterface
from home.QuoteEngine.QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Ingestor for pdf files."""

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the file can be ingested."""
        return path.endswith('.pdf')

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the pdf file and return a list of quotes."""
        quotes = []
        try:
            with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as temp_file:
                temp_path = temp_file.name

            subprocess.run(['pdftotext', path, temp_path], check=True)

            with open(temp_path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split(' - ')
                        if len(parts) == 2:
                            body, author = parts
                            quotes.append(QuoteModel(body.strip(), author.strip()))

            os.remove(temp_path)
        except Exception as e:
            print(f"Error parsing PDF file {path}: {e}")
            if os.path.exists(temp_path):
                os.remove(temp_path)
        return quotes