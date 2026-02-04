def get_student_courses(enrollments, student_id):
    """Return set of courses this student has completed."""
    course = set()
    for element in enrollments:
        if student_id in element:
            course.add(element[1])
    
    return course

def find_missing_courses(completed_courses, required_courses):
    """Return set of required courses not yet completed."""
    return required_courses - completed_courses
    

def build_student_report(students, enrollments, required_courses):
    """Return sorted list of tuples (student_id, missing_count) for students with missing courses."""
    report_list = []
    for student in students:
        student_courses = get_student_courses(enrollments, student)
        missing = find_missing_courses(student_courses, required_courses)
        report_list.append((student, len(missing)))
    
    return report_list

def find_incomplete_students(enrollments, required_courses):
    """Find students who haven't completed all required courses."""
    
    
