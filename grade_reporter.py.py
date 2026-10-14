# Start with the given scores list
scores = [72, 45, 90, 61, 38]

passed_count = 0
failed_count = 0
total_score = 0

# Loop through every score in the list
for score in scores:
    total_score += score
    
    # Determine the grade using if / elif / else
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
        
    # Print each score with its grade on its own line
    print(f"Score: {score} - Grade: {grade}")
    
    # Count passes and fails (pass is 50 or more)
    if score >= 50:
        passed_count += 1
    else:
        failed_count += 1

# Calculate the average score rounded to one decimal place
average = total_score / len(scores)

print("\n--- Summary ---")
print(f"Passed learners: {passed_count}")
print(f"Failed learners: {failed_count}")
print(f"Average score: {round(average, 1)}")