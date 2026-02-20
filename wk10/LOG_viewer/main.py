from PySide6.QtWidgets import QApplication
from challenge.log_source_factory import LogSourceFactory
from ui.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    # log = LogSourceFactory.create_log_source("mock")
    log = LogSourceFactory.create_log_source("csv", file_path="logs/sample_logs.csv")
    viewer = MainWindow(log)
    viewer.show()
    app.exec()