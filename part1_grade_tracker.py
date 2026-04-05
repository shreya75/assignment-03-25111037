### Task 1 — Data Parsing & Profile Cleaning
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]
processed_students = []
#Requirement1: 
for student in raw_students:    
    name = student["name"].strip().title() # to clean name and roll
    roll = int(student["roll"])    
    marks = []
    for mark in student["marks_str"].split(","): # to convert marks string into list of integers
        marks.append(int(mark.strip()))    
    is_valid = all(word.isalpha() for word in name.split()) # To Check each word contains only alphabets
#Requirement2:
    if not is_valid:
        print("✗ Invalid name")
    else:
        print("✓ Valid name")

    # Requirement3:
    print("=" * 32)
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("=" * 32)

    # Requirement4:
    if roll == 103:
        print(name.upper())
        print(name.lower())

    # Store processed data
    processed_students.append({
        "name": name,
        "roll": roll,
        "marks": marks
    })

### Task 2 - Marks Analysis Using Loops & Conditionals — Data Parsing & Profile Cleaning    
student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]
# Requirement1:
for i in range(len(subjects)):
    mark = marks[i]

    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"

    print(subjects[i], mark, grade)##Prints requirement 1 output
# Requirement2:
total = sum(marks)
average = round(total / len(marks), 2) ## rounded to 2 decimals

highest = max(marks)
lowest = min(marks)

high_sub = subjects[marks.index(highest)]
low_sub = subjects[marks.index(lowest)]
# Requirement3:
new_count = 0

while True:
    subject = input("Enter subject (or 'done'): ")
    
    if subject.lower() == "done":
        break
    
    marks_input = input("Enter marks: ")
    
    if not marks_input.isdigit():
        print("Invalid input")
        continue
    
    marks_val = int(marks_input)
    
    if marks_val < 0 or marks_val > 100:
        print("Marks must be between 0 and 100")
        continue
    
    subjects.append(subject)
    marks.append(marks_val)
    new_count += 1        

    new_avg = round(sum(marks) / len(marks), 2)
### Task 3 - Class Performance Summary
### Task 4 - String Manipulation Utility