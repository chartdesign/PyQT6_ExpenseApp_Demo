# application logic
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QDateEdit, QTableWidget, QVBoxLayout, QMessageBox, QTableWidgetItem, QHeaderView, QHBoxLayout
from PyQt6.QtCore import QDate, Qt
from database import fetch_expenses, add_expenses, delete_expense

class ExpenseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.settings()
        self.initUI()
        self.load_table_data()

    def settings(self):
        self.setGeometry(750, 300, 550, 500)
        self.setWindowTitle("My Expenses")

    # Design
    def initUI(self):
        # Create all objects that will be viewed on app
        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate()) 
        self.dropdown = QComboBox()
        self.amount = QLineEdit()
        self.description = QLineEdit()

        self.btn_add = QPushButton("Add Expense")
        self.btn_delete = QPushButton("Delete Expense")

        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(["ID", "Date", "Category", "Amount", "Description"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.populate_dropdown()

        self.btn_add.clicked.connect(self.addExpense)
        self.btn_delete.clicked.connect(self.deleteExpense)

        self.setup_layout()

    def setup_layout(self):

        master = QVBoxLayout()
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()

        # Row 1
        row1.addWidget(QLabel("Date"))
        row1.addWidget(self.date_box)
        row1.addWidget(QLabel("Category"))
        row1.addWidget(self.dropdown)

        # Row 2
        row2.addWidget(QLabel("Amount"))
        row2.addWidget(self.amount)
        row2.addWidget(QLabel("Description"))
        row2.addWidget(self.description)
        row3.addWidget(self.btn_add)
        row3.addWidget(self.btn_delete)

        master.addLayout(row1)
        master.addLayout(row2)
        master.addLayout(row3)
        master.addWidget(self.table)

        self.setLayout(master)

    def populate_dropdown(self):
        categories = ["Food", "Rent", "Entertainment", "Transportation", "Utilities", "Other"]
        self.dropdown.addItems(categories)

    # def load_table_data(self):
    #     expenses = fetch_expenses()
    #     self.table.setRowCount(0)
    #     for row_idx, expense in enumerate(expenses):
    #         self.table.insertRow(row_idx)
    #         for col_idx, data in enumerate(expense):
    #             self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))

    def load_table_data(self):
        expenses = fetch_expenses()
        self.table.setRowCount(0)
        for row_idx, expense in enumerate(expenses):
            self.table.insertRow(row_idx)
            for col_idx, data in enumerate(expense):
                if col_idx == 3:
                    display_text = f"${float(data):,.2f}"
                else:
                    display_text = str(data)
                
                item = QTableWidgetItem(display_text)
                
                # Optional: right-align currency values for cleaner reading
                # if col_idx == 3:
                #     item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
                    
                self.table.setItem(row_idx, col_idx, item)

    def clear_inputs(self):
        self.date_box.setDate(QDate.currentDate())
        self.dropdown.setCurrentIndex(0)
        self.amount.clear()
        self.description.clear()
    
    def addExpense(self):
        date = self.date_box.date().toString("yyyy-MM-dd")
        category = self.dropdown.currentText()
        amount = self.amount.text()
        description = self.description.text()

        if not amount or not description:
            QMessageBox.warning(self, "Input error.", "Amount and description can't be empty.")
            return

        if add_expenses(date, category, amount, description):
            self.load_table_data()
            self.clear_inputs()
        else:
            QMessageBox.critical(self, "Error", "Failed to add expense.")


    def deleteExpense(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "You must select a row to delete.")
            return

        expense_id = int(self.table.item(selected_row, 0).text())
        confirm = QMessageBox.question(self, "Confirm.", "Are you sure you want to delete this?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if confirm == QMessageBox.StandardButton.Yes and delete_expense(expense_id):
            self.load_table_data()
