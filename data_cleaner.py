


import csv

# Store valid records and track duplicates
valid_records = []
seen_records = set()

# Track cleaning statistics
total_records = 0
invalid_records = 0
duplicate_records = 0


# STEP 1: Read and validate the input CSV file
with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_records += 1

        name = (row.get("Name") or "").strip()
        subject = (row.get("Subject") or "").strip()
        raw_marks = (row.get("Marks") or "").strip()

        # Check for a missing student name
        if not name:
            invalid_records += 1
            print("Invalid record: Student name is missing")
            continue

        # Check for missing subject
        if not subject:
            invalid_records += 1
            print(f"Invalid record: Subject is missing for {name}")
            continue

        # Check whether marks are valid numbers
        try:
            marks = int(raw_marks)
        except (ValueError, TypeError):
            invalid_records += 1
            print(f"Invalid marks value for {name}: {raw_marks!r}")
            continue

        # Marks must be between 0 and 100
        if not 0 <= marks <= 100:
            invalid_records += 1
            print(f"Invalid marks for {name}: {marks}")
            continue

        # Check for duplicate records
        record_key = (name, subject, marks)

        if record_key in seen_records:
            duplicate_records += 1
            print(
                f"Duplicate record removed: "
                f"{name} | {subject} | {marks}"
            )
            continue

        # Save the valid, unique record
        seen_records.add(record_key)

        valid_records.append({
            "Name": name,
            "Subject": subject,
            "Marks": marks
        })

        print(f"Valid record: {name} | {subject} | {marks}")


# STEP 2: Export cleaned records to a new CSV file
with open(
    "cleaned_students.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:
    fieldnames = ["Name", "Subject", "Marks"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(valid_records)


# STEP 3: Display the cleaning summary
print("\n========== CLEANING SUMMARY ==========")
print(f"Total records processed: {total_records}")
print(f"Invalid records: {invalid_records}")
print(f"Duplicate records removed: {duplicate_records}")
print(f"Final valid unique records: {len(valid_records)}")
print("Output file: cleaned_students.csv")


# STEP 4: Analyze the cleaned data
if valid_records:
    marks_list = [record["Marks"] for record in valid_records]

    average_marks = sum(marks_list) / len(marks_list)
    highest_record = max(
        valid_records,
        key=lambda record: record["Marks"]
    )
    lowest_record = min(
        valid_records,
        key=lambda record: record["Marks"]
    )

    print("\n========== DATA ANALYSIS REPORT ==========")
    print(f"Total unique valid records: {len(valid_records)}")
    print(f"Average marks: {average_marks:.2f}")
    print(f"Highest marks: {highest_record['Marks']}")
    print(f"Lowest marks: {lowest_record['Marks']}")
    print(
        f"Top student: {highest_record['Name']} "
        f"({highest_record['Subject']})"
    )
    print(
        f"Lowest-scoring record: {lowest_record['Name']} "
        f"({lowest_record['Subject']})"
    )
else:
    print("\nNo valid records available for analysis.")
