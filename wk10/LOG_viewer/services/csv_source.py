import csv
from interface.data_source import ILogSource


class CsvLogSource(ILogSource):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_logs(self) -> list[str]:
        logs = []
        with open(self.file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # Skip header
            for row in reader:
                if row:  # Skip empty rows
                    # Join all columns with space to form log string
                    log_entry = ' '.join(row)
                    logs.append(log_entry)
        return logs