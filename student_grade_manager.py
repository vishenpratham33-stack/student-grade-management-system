"""
Student Grade Management System
--------------------------------
A small console app to manage student records: add, search, sort, and
analyze marks. Built to practice core data structures & algorithms
(sorting and searching) rather than relying on built-in shortcuts.

Data structure: list of dicts -> [{"roll_no": int, "name": str, "marks": float}, ...]
Persistence: simple JSON file so data survives between runs.

DSA concepts demonstrated:
  - Merge sort (implemented from scratch) to sort students by marks
  - Binary search (implemented from scratch) to find a student by roll number
  - Linear search as a fallback / for name lookups
"""

import json
import os

DATA_FILE = "students.json"


def load_students():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_students(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=2)


def add_student(students, roll_no, name, marks):
    students.append({"roll_no": roll_no, "name": name, "marks": marks})


# ---------- Sorting: merge sort implemented manually (descending by marks) ----------
def merge_sort_by_marks(students):
    if len(students) <= 1:
        return students

    mid = len(students) // 2
    left = merge_sort_by_marks(students[:mid])
    right = merge_sort_by_marks(students[mid:])

    return _merge(left, right)


def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        # descending order: higher marks first
        if left[i]["marks"] >= right[j]["marks"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ---------- Searching: binary search manually (requires sorting by roll_no first) ----------
def sort_by_roll_no(students):
    # simple insertion sort - fine for small class sizes, easy to explain in an interview
    arr = students[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j]["roll_no"] > key["roll_no"]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def binary_search_by_roll(sorted_students, roll_no):
    low, high = 0, len(sorted_students) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_students[mid]["roll_no"] == roll_no:
            return sorted_students[mid]
        elif sorted_students[mid]["roll_no"] < roll_no:
            low = mid + 1
        else:
            high = mid - 1
    return None


def linear_search_by_name(students, name):
    matches = [s for s in students if name.lower() in s["name"].lower()]
    return matches


def class_average(students):
    if not students:
        return 0
    return sum(s["marks"] for s in students) / len(students)


def topper(students):
    if not students:
        return None
    return max(students, key=lambda s: s["marks"])


# ---------------------------- CLI ----------------------------
def print_students(students):
    if not students:
        print("  (no records)")
        return
    for s in students:
        print(f"  Roll {s['roll_no']:<5} {s['name']:<20} Marks: {s['marks']}")


def menu():
    students = load_students()
    while True:
        print("\n--- Student Grade Management System ---")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student by roll number (binary search)")
        print("4. Search student by name (linear search)")
        print("5. Sort & view by marks (merge sort, descending)")
        print("6. Class average & topper")
        print("7. Save & exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            roll_no = int(input("Roll number: "))
            name = input("Name: ")
            marks = float(input("Marks: "))
            add_student(students, roll_no, name, marks)
            print("Added.")

        elif choice == "2":
            print_students(students)

        elif choice == "3":
            roll_no = int(input("Roll number to find: "))
            sorted_by_roll = sort_by_roll_no(students)
            result = binary_search_by_roll(sorted_by_roll, roll_no)
            print(f"Found: {result}" if result else "Not found.")

        elif choice == "4":
            name = input("Name (or part of it): ")
            results = linear_search_by_name(students, name)
            print_students(results)

        elif choice == "5":
            ranked = merge_sort_by_marks(students)
            print_students(ranked)

        elif choice == "6":
            print(f"  Class average: {class_average(students):.2f}")
            top = topper(students)
            print(f"  Topper: {top['name']} ({top['marks']} marks)" if top else "  No students yet.")

        elif choice == "7":
            save_students(students)
            print("Saved. Goodbye!")
            break

        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    menu()
