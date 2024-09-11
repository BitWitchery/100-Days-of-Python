student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

# sum() function
students_scores = [180, 124, 165, 173, 189, 169, 146]
total_score = sum(students_scores)

sum = 0
for score in students_scores:
    sum += score

print(sum)

# max() function
students_scores = [180, 124, 165, 173, 189, 169, 146]


max_score = 0
for score in students_scores:
    if score < max_score:
        max_score = score

print(max_score)


# min() function
students_scores = [180, 124, 165, 173, 189, 169, 146]

min_score = students_scores[0]  # Start by assuming the first score is the smallest
for score in students_scores:
    if score < min_score:  # If a smaller score is found
        min_score = score  # Update min_score with the smaller value

print(min_score)