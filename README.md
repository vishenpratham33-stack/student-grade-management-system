# Student Grade Management System

A Python-based console application for managing student records, grades, searching, sorting, and analyzing academic performance.

## Features

- Add new student records
- Search students by roll number or name
- Sort students based on marks
- Display and analyze student grades
- Calculate academic performance statistics
- Persistent data storage using JSON
- Simple command-line interface for managing records

## Data Structures & Algorithms

This project demonstrates practical implementation of:

- **List of Dictionaries** — stores student records such as roll number, name, and marks
- **Merge Sort** — implemented from scratch to sort students by marks
- **Binary Search** — implemented from scratch to efficiently find students by roll number
- **Linear Search** — used as a fallback for name-based searches
- **File Handling** — used for persistent storage of student data

## Technologies Used

- Python
- JSON
- Data Structures & Algorithms
- File Handling
- Command-Line Interface

## Data Persistence

Student records are stored in a JSON file so that data remains available between different program executions.

Example student record:

```json
{
    "roll_no": 101,
    "name": "Rahul",
    "marks": 85.5
}
