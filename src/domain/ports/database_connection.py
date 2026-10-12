from abc import ABC, abstractmethod
from contextlib import AbstractContextManager
from typing import Any


class IDatabaseConnection(ABC):
    """Define the interface for managing database connections.

    This interface provides an abstraction for establishing database
    connections through a context manager, allowing resources to be managed
    throughout database operations.
    """
    @abstractmethod
    def connect(self) -> AbstractContextManager[Any]:
        """Establish a database connection managed by a context manager.

        Returns:
            AbstractContextManager[Any]: A context manager that provides
                access to the database connection and manages its lifecycle.
        """
        pass
