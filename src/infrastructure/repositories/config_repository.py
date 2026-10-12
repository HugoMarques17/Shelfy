from ...domain.repositories import IConfigRepository
from configparser import RawConfigParser
from threading import Lock


class ConfigRepository(IConfigRepository):
    """Implement the config repository using an INI file.

    This repository provides operations to read, update, and persist
    configuration settings stored in an INI file. It uses a thread lock
    to synchronize access to the configuration parser and preserves the
    case of option names.
    """
    def __init__(self, path: str = 'config.ini'):
        """Initialize the config repository.

        Args:
            path (str): Path to the INI configuration file. Defaults to
                'config.ini'.
        """
        self.path = path
        self.config = RawConfigParser()
        self._lock = Lock()

    def get_section(self, section: str) -> dict:
        """Retrieve all options in a section.

        Reads the config file and returns the options and their
        corresponding values as a dictionary.

        Args:
            section (str): Name of the section to retrieve.

        Returns:
            dict: Dictionary containing the options and their values.

        Raises:
            RuntimeError: If the config file cannot be read or the
                requested section cannot be retrieved.
        """
        with self._lock:
            try:
                self.config.read(self.path, encoding='utf-8-sig')
                return dict(self.config.items(section))
            
            except Exception as e:
                raise RuntimeError(f"Erro ao ler seção {section}: {str(e)}")

    def get_value(self, section: str, option: str) -> str:
        """Retrieve the value of an option.

        Reads the config file and retrieves the value associated
        with the specified section and option.

        Args:
            section (str): Name of the section.
            option (str): Name of the option to retrieve.

        Returns:
            str: Value associated with the specified option.

        Raises:
            RuntimeError: If the configfile cannot be read or the
                requested section or option cannot be retrieved.
        """
        with self._lock:
            try:
                self.config.read(self.path, encoding='utf-8-sig')
                value = self.config.get(section, option)
                if value is None:
                    raise ValueError(f"Valor vazio para {section}.{option}")
                
                return value
            
            except Exception as e:
                raise RuntimeError(f"Erro ao ler {section}.{option}: {str(e)}")

    def set_item(self, section: str, option: str, value: str) -> None:
        """Set a value and persist the changes.

        Reads the existing config file, updates the specified option,
        and saves the changes to disk while holding the thread lock.

        Args:
            section (str): Name of the section.
            option (str): Name of the option to update.
            value (str): Value to assign to the option.
        """
        with self._lock:
            self.config.read(self.path, encoding='utf-8-sig')
            self.config.set(section, option, value)
            self._save()

    def _save(self) -> None:
        """Persist the current config to the INI file.

        Opens the config file in write mode and serializes the
        current config using UTF-8 with a byte order mark.
        """
        with open(self.path, 'w', encoding='utf-8-sig') as file:
            self.config.write(file)