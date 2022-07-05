# ----------------------------------------------------------------
# Author: Anya Ugolik, Damian Wilder
# Date: 29 November 2021
#
# This module supports changes in the registered courses
# for students in the class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------


def list_courses(id, c_roster):
    # ------------------------------------------------------------
    # This function displays and counts courses a student has
    # registered for.  It has two parameters: id is the ID of the
    # student; c_roster is the list of class rosters. This function
    # has no return value.
    # Author: Damian Wilder
    # -------------------------------------------------------------
    course_list = []
    for course in c_roster:
        for student in c_roster[course]:
            if student == id:
                course_list.append(course)
    if not course_list:
        print('No courses registered')
    else:
        print('Currently registered for the following courses:')
        for course in course_list:
            print(course)


def add_course(id, c_roster, c_max_size):
    # ------------------------------------------------------------
    # This function adds a student to a course.  It has three
    # parameters: id is the ID of the student to be added; c_roster is the
    # list of class rosters; c_max_size is the list of maximum class sizes.
    # This function asks user to enter the course he/she wants to add.
    # If the course is not offered, display error message and stop.
    # If student has already registered for this course, display
    # error message and stop.
    # If the course is full, display error message and stop.
    # If everything is okay, add student ID to the course’s
    # roster and display a message if there is no problem.  This
    # function has no return value.
    # Author: Anya Ugolik
    # -------------------------------------------------------------
    add = input('Enter course you want to add: ')
    for course in c_roster.keys():
        if add not in c_roster.keys():
            print('Course not found')
            break
        elif str(id) in c_roster[add]:
            print('You are already enrolled in that course.')
            break
        elif c_max_size[add] <= len(c_roster[add]):
            print('Course already full.')
            break
        else:
            c_roster[add].append(str(id))
            print('Course added')
            break


def drop_course(id, c_roster):
    # ------------------------------------------------------------
    # This function drops a student from a course.  It has two
    # parameters: id is the ID of the student to be dropped;
    # c_roster is the list of class rosters. This function asks
    # the user to enter the course he/she wants to drop.  If the course
    # is not offered, display error message and stop.  If the student
    # is not enrolled in that course, display error message and stop.
    # Remove student ID from the course’s roster and display a message
    # if there is no problem.
    # Author: Anya Ugolik
    # -------------------------------------------------------------
    drop = input('Enter course you want to drop: ')
    for course in c_roster.keys():
        if drop not in c_roster.keys():
            print('Course not found.')
            break
        elif str(id) not in c_roster[drop]:
            print('You are not enrolled in that course: ')
            break
        else:
            c_roster[drop].remove(str(id))
            print('Course dropped')
            break
