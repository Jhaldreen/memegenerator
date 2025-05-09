from typing import List
import docx

from home.QuoteEngine.IngestorInterface import IngestorInterface
from home.QuoteEngine.QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Ingestor for docx files."""

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the file can be ingested."""
        return path.endswith('.docx')

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the docx file and return a list of quotes."""
        quotes = []
        try:
            doc = docx.Document(path)
            for para in doc.paragraphs:
                if para.text:
                    parts = para.text.split(' - ')
                    if len(parts) == 2:
                        body, author = parts
                        quotes.append(QuoteModel(body.strip(), author.strip()))
        except Exception as e:
            print(f"Error parsing DOCX file {path}: {e}")
        return quotes