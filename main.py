def calculate_class_averages(classrooms):
    class_averages = {}

    for classroom, students in classrooms.items():

        if not students:
            class_averages[classroom] = 0
            continue
        
        scores = 0
        num_grades = 0
        
        for grades in students.values():
            for grade in grades:
                scores += grade
                num_grades += 1
                
        avg = scores / num_grades
        class_averages[classroom] = avg

    return class_averages

# {
#     "Math": {
#         "Alice": [85, 90, 78],
#         "Bob": [72, 88, 91],
#         "Charlie": [95, 100, 92]
#     },
#     "Science": {
#         "Alice": [80, 85, 88],
#         "Bob": [78, 82, 85],
#         "Diana": [90, 91, 89]
#     },
#     "History": {
#         "Charlie": [70, 75, 80],
#         "Diana": [88, 92, 84]
#     }
# }