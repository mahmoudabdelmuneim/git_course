"""Logging setup."""

import logging


def configure_logging(level: str) -> None:
    """Configure a concise consistent log format."""
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
