from abc import ABC, abstractmethod


class IConfigRepository(ABC):
    """Define the interface for managing application configuration settings.

    This repository provides operations to set, retrieve, and persist
    configuration values.
    """
    @abstractmethod
    def get_section(self, section: str) -> dict:
        """Retrieve all configuration options within a section.

        Args:
            section (str): Name of the configuration section to retrieve.

        Returns:
            dict: Dictionary containing the options and their values for
                the specified section.
        """
        raise NotImplementedError

    @abstractmethod
    def get_value(self, section: str, option: str) -> str:
        """Retrieve the value of an specific option.

        Args:
            section (str): Name of the section.
            option (str): Name of the option to retrieve.

        Returns:
            str: Value associated with the specified option.
        """
        raise NotImplementedError

    @abstractmethod
    def set_item(self, section: str, option: str, value: str) -> None:
        """Set a configuration value for a specific option.

        Args:
            section (str): Name of the section.
            option (str): Name of the option to set.
            value (str): Value to assign to theoption.

        Returns:
            None: This method does not return a value.
        """
        raise NotImplementedError

    @abstractmethod
    def _save(self) -> None:
        """Persist the current configuration settings.

        Returns:
            None: This method does not return a value.
        """
        raise NotImplementedError
