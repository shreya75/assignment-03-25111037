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
class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

pass_count = 0
fail_count = 0
averages = []
topper_name = ""
topper_avg = 0
# Requirement1:
avg = round(sum(marks)/len(marks), 2)
averages.append(avg)
result_status = "Pass" if avg >= 60 else "Fail"
# Requirement2:
if result_status == "Pass":
    pass_count += 1
else:
    fail_count += 1

if avg > topper_avg:
    topper_avg = avg
    topper_name = name
print(f"{'Name':<18} | {'Average':<7} | Status")
print("-"*40)
print(f"{name:<18} | {avg:^7} | {result_status}")
# Requirement3:

class_avg = round(sum(averages)/len(averages), 2)

print("Passed:", pass_count)
print("Failed:", fail_count)
print("Topper:", topper_name, topper_avg)
print("Class Average:", class_avg)

### Task 4 - String Manipulation Utility
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

clean_essay = essay.strip() # to remove leading and trailing whitespace

print(clean_essay.title()) # to convert to title case

count = clean_essay.count("python") # to count occurrences of python word
print(count)

replaced = clean_essay.replace("python", "Python 🐍") # to replace python word
print(replaced)

sentences = clean_essay.split(". ") #  to split into sentences
print(sentences)

for i, s in enumerate(sentences, 1):
    if not s.endswith("."):
        s += "."
    print(f"{i}. {s}")