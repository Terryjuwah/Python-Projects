# student_gradebook.py
# ZenfuraVision Student Grade Book
# Stores courses and scores in lists, calculates average,
# finds best and worst subject, prints formatted report.
# Concepts: lists, append, indexing, for loops, functions,
# return values, try/except, f-strings, global scope
# Author: Terry Juwah


courses = [ ]
scores = [ ]

def get_courses():
    global courses, scores
    
    while True:
        course_name = input("Enter a course name (or 'done' to finish): ")
        
        if course_name.lower() == 'done':
            break
        try:
            score_value = int(input(f'Score for {course_name} over 100%: ')) 
            
            courses.append(course_name)
            scores.append(score_value)
            
            print(f"✓ Added: {course_name} - {score_value}%\n")
            
        except ValueError:
            print('Only numbers can be entered for score. Try again.\n')

def calculate_average(scores):
    
    running_total = 0
    for i in range(len(scores)):
        running_total = running_total + scores[i]
    average = running_total/len(scores)
    if average >= 70:
    	grade = 'A'
    elif average >= 60:
    	grade = 'B'
    elif average >= 50:
    	grade = 'C'
    elif average >= 40:
    	grade = 'D'
    elif average >= 30:
    	grade = 'E'
    else: 
    	grade = 'F'
    
    return average, grade 

def get_best_worst(courses, scores):
    
    best_course = courses[0]
    best_score = scores[0]
    worst_course = courses[0]
    worst_score = scores[0]
    
    for i in range(1, len(scores)):
        if scores[i] > best_score:
            best_score = scores[i]
            best_course = courses[i]
        
        if scores[i] < worst_score:
            worst_score = scores[i]
            worst_course = courses[i]
            
    return best_course, best_score, worst_course, worst_score
        
    
def print_report(courses, scores, average, best_course, best_score, worst_course, worst_score,grade):
    
    print("\n" + "="*40)
    print("ZENFURAVISON GRADEBOOK".center(40))
    print("="*40)
    
    print("\n\n" + f"{'#':<4} {'COURSE':<20} {'SCORE':>8}")
    print("-" * 40)

    for i in range(len(courses)):
        print(f"{i+1:<4} {courses[i]:<20} {scores[i]:>7}%")
    
    print("-" * 40)
    
    print(f"\nAverage: {average:.1f}%")
    print(f"\nBest Course: {best_course}")
    print(f"Best Score: {best_score}%")
    print(f"Worst Course: {worst_course}")
    print(f"Worst Score: {worst_score}%")
    print(f"Grade: {grade}")
    print("\n" + "=" *40)	
    
                
# Call the functions
get_courses()
average, grade = calculate_average(scores)
best_course, best_score, worst_course, worst_score = get_best_worst(courses, scores)
print_report(courses, scores, average, best_course, best_score, worst_course, worst_score,grade)
