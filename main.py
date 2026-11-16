# here is where the app is ran
import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from app import ExpenseApp
from database import init_db

def main():
    app = QApplication(sys.argv)

    if not init_db("myExpenses.db"):
        QMessageBox.critical(None, "Error","Could not load database.")
        sys.exit(2)

    window = ExpenseApp()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()