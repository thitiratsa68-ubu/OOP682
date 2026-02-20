from services.file_source import FileLogSource
from services.mock_source import MockLogSource
from services.csv_source import CsvLogSource


class LogSourceFactory:
    @staticmethod
    def create_log_source(source_type: str, **kwargs):
        if source_type == "file":
            return FileLogSource(kwargs.get("file_path"))
        elif source_type == "mock":
            return MockLogSource()
        elif source_type == "csv":
            return CsvLogSource(kwargs.get("file_path"))
        else:
            raise ValueError(f"Unknown source type: {source_type}")