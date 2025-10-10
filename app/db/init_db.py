"""Database initialization helpers."""

from sqlalchemy.orm import Session

from app import models


def init_db(db: Session) -> None:
    """Placeholder for database initialization logic."""

    _ = models  # noqa: F841  # Import models for side effects
    # Add initialization logic here (e.g., create default users)
