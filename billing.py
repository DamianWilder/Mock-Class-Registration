# ----------------------------------------------------------------
# Author: Rick Symonds
# Date: 29 November 2021
#
# This module calculates and displays billing information
# for students in the class registration system.  Student and
# class records are reviewed and tuition fees are calculated.
# -----------------------------------------------------------------


def calculate_hours_and_bill(id, s_in_state, c_rosters, c_hours):
    # ------------------------------------------------------------
    # This function calculate billing information. It takes four
    # parameters: id, the student id; s_in_state, the list of
    # in-state students; c_rosters, the rosters of students in
    # each course; c_hours, the number of hours in each course.
    # This function returns the number of course hours and tuition
    # cost.
    # ------------------------------------------------------------
    hours_tot = 0

    # Create and populate list of courses assigned to student
    course_list = []
    for key, value in c_rosters.items():
        if id in c_rosters[key]:
            for v in value:
                if key not in course_list:
                    course_list.append(key)
    for element in course_list:
        hours_tot += int(c_hours[element])

    # Calculate total tuition based on in-state status
    if s_in_state[id]:
        tot_cost = hours_tot * 225
    else:
        tot_cost = hours_tot * 850

    return hours_tot, tot_cost


def display_hours_and_bill(hours, cost):
    # ------------------------------------------------------------
    # This function prints the number of course hours the student
    # is taking and the total tuition cost. It takes two parameters:
    # hours and cost. This function has no return value.
    # ------------------------------------------------------------
    print(f'Course load: {hours} credit hours')
    print(f'Enrollment cost: ${format(cost, ",.2f")}')
