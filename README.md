# My Expenses

A lightweight desktop expense-tracking application built with **Python**, **PyQt6**, and **SQLite**. It allows users to log daily expenses by date, category, amount, and description, view them in a sortable table, and delete entries with confirmation prompts.

## Features

- **Add Expenses:** Record expenses with a date picker, predefined categories (`Food`, `Rent`, `Entertainment`, `Transportation`, `Utilities`, `Other`), dollar amount, and description.
- **Persistent Storage:** Automatically creates and manages a local SQLite database (`myExpenses.db`) using `PyQt6.QtSql`.
- **Formatted Expense Table:** Displays all logged expenses ordered by most recent date, with currency formatting (`$0.00`) and automatic column stretching.
- **Safe Deletion:** Select any row to remove an expense from both the interface and the database after a confirmation dialog.

## Project Structure

```text
├── main.py          # Application entry point and database initialization
├── app.py           # PyQt6 GUI layout, table rendering, and user event handlers
├── database.py      # SQLite connection setup and CRUD query functions
└── myExpenses.db    # Auto-generated SQLite database file (created on first run)
```

## Prerequisites

- **Python 3.8+**
- **PyQt6**

## Installation & Setup

1. **Clone or download** this repository to your local machine.
2. **Install PyQt6** using `pip`:
   ```bash
   pip install PyQt6
   ```
3. **Run the application:**
   ```bash
   python main.py
   ```

## Usage

1. **Enter Expense Details:**
   - Choose a **Date** (defaults to the current date).
   - Select a **Category** from the dropdown menu.
   - Enter an **Amount** and a brief **Description** (both fields are required).
2. **Save:** Click **Add Expense** to insert the entry into the database and refresh the table.
3. **Delete:** Click on any row in the table to highlight it, then click **Delete Expense** and confirm **Yes** to remove it.

## Database Schema

The application stores records in a single SQLite table named `expenses`:

| Column | Type | Description |
| :--- | :--- | :--- |
| `id` | `INTEGER` | Auto-incrementing primary key |
| `date` | `TEXT` | Expense date formatted as `YYYY-MM-DD` |
| `category` | `TEXT` | Expense category |
| `amount` | `REAL` | Numeric cost of the expense |
| `description` | `TEXT` | Notes or details about the expense |