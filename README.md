
# CSV Data Cleaner & Analyzer 🧹📊

A beginner-friendly Python project that cleans CSV files, removes duplicate records, validates data, and generates a simple marks analysis report.

## 📌 Project Overview

CSV files often contain missing values, invalid marks, or duplicate records. This project helps clean student data automatically and produces a new CSV file containing only valid, unique records.

## ✨ Features

- Read student records from a CSV file
- Detect missing student names and subjects
- Validate marks and reject non-numeric values
- Ensure marks are between 0 and 100
- Detect and remove duplicate records
- Export cleaned data to a new CSV file
- Calculate average, highest, and lowest marks
- Display a cleaning summary and analysis report

## 🛠️ Technologies Used

- Python
- CSV module
- File handling
- Exception handling
- Lists, dictionaries, and sets
- Functions such as `sum()`, `max()`, and `min()`

##  Project Structure

```text
csv-data-cleaner/
├── data_cleaner.py
├── students.csv
├── cleaned_students.csv
└── README.md
```

## 🚀 How to Run

### 1. Install Python

Install Python if it is not already available on your computer.

### 2. Prepare the input file

Keep `students.csv` in the same folder as `data_cleaner.py`.

The CSV file should contain these column names:

```csv
Name,Subject,Marks
Aarav,Python,85
Priya,Python,92
Rahul,DSA,78
```

### 3. Run the program

Open the terminal in the project folder and execute:

```bash
python data_cleaner.py
```

### 4. Check the output

The program generates `cleaned_students.csv` and displays a summary of invalid records, duplicates, and marks statistics.

## 📊 Sample Results

Using the included test data:

- Total records processed: 9
- Invalid records: 4
- Duplicate records removed: 1
- Final valid unique records: 4
- Average marks: 81.25
- Highest marks: 92
- Lowest marks: 70

## 🎯 Learning Outcomes

Through this project, I practiced:

- Reading and writing CSV files
- Validating user and file data
- Handling exceptions
- Removing duplicate records with sets
- Processing data with lists and dictionaries
- Generating summary statistics
- Organizing a Python project

## 🔮 Future Improvements

- Support Excel files using pandas or openpyxl
- Add more detailed data quality reports
- Allow users to choose input and output filenames
- Add automated unit tests

## 👩‍💻 Author

**Anveshka Kushwah**

GitHub: [anveshkakushwah](https://github.com/anveshkakushwah)

LinkedIn: [Connect with me](https://www.linkedin.com/in/anveshkakushwah-0b54443b1/)

---

If you find this project useful, feel free to explore the code and suggest improvements!
