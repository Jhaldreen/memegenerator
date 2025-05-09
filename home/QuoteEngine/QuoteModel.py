class QuoteModel:
    """Encapsulates body and author of a quote."""

    def __init__(self, body: str, author: str):
        """Create a new quote.

        :param body: the text of the quote
        :param author: the author of the quote
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Return string representation of the quote."""
        return f'"{self.body}" - {self.author}'