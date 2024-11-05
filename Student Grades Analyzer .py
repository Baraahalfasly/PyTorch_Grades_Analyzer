import torch
import torch.nn as nn
import torch.nn.functional as F
from tabulate import tabulate

# List of student names
students = ['Ahmed', 'Sarah', 'Mohammed', 'Laila', 'Khalid']

# Grades for each subject for each student
grades = {
    'Math': [90, 85, 70, 60, 95],
    'Physics': [80, 75, 85, 70, 90],
    'Chemistry': [85, 80, 80, 65, 88],
    'Biology': [70, 90, 75, 80, 85],
    'English': [95, 85, 80, 75, 90]
}

# Convert grades to PyTorch tensors
math_grades = torch.tensor(grades['Math'], dtype=torch.float32)
physics_grades = torch.tensor(grades['Physics'], dtype=torch.float32)
chemistry_grades = torch.tensor(grades['Chemistry'], dtype=torch.float32)
biology_grades = torch.tensor(grades['Biology'], dtype=torch.float32)
english_grades = torch.tensor(grades['English'], dtype=torch.float32)

# Stack all grades into a single tensor
all_grades = torch.stack([math_grades, physics_grades, chemistry_grades, biology_grades, english_grades], dim=1)

# Calculate the average grade for each student
average_grades = all_grades.mean(dim=1)

# Define evaluation based on average grade
def get_evaluation(avg):
    if avg >= 90:
        return 'Excellent'
    elif avg >= 80:
        return 'Very Good'
    elif avg >= 70:
        return 'Good'
    elif avg >= 60:
        return 'Pass'
    else:
        return 'Fail'

# Get evaluations for each student
evaluations = [get_evaluation(avg.item()) for avg in average_grades]

# Prepare data for the table
headers = ['Student', 'Math', 'Physics', 'Chemistry', 'Biology', 'English', 'Average', 'Evaluation']
table = []
for i, student in enumerate(students):
    row = [
        student,
        grades['Math'][i],
        grades['Physics'][i],
        grades['Chemistry'][i],
        grades['Biology'][i],
        grades['English'][i],
        f"{average_grades[i].item():.2f}",
        evaluations[i]
    ]
    table.append(row)

# Display the table in the console
print(tabulate(table, headers=headers, tablefmt='fancy_grid', stralign='center', numalign='center'))

# Save the table to a text file
with open('student_grades.txt', 'w', encoding='utf-8') as f:
    f.write(tabulate(table, headers=headers, tablefmt='fancy_grid', stralign='center', numalign='center'))

# Save the data to a CSV file
import csv

with open('student_grades.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(headers)
    for row in table:
        csvwriter.writerow(row)
