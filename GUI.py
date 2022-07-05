import tkinter as tk


class GUI:
    def __init__(self):
        self.student_list = [
            ("1001", "111"),
            ("1002", "222"),
            ("1003", "333"),
            ("1004", "444"),
        ]
        self.student_in_state = {
            "1001": True,
            "1002": False,
            "1003": True,
            "1004": False,
        }

        self.course_hours = {"CSC101": 3, "CSC102": 4, "CSC103": 5, "CSC104": 3}
        self.course_roster = {
            "CSC101": ["1004", "1003"],
            "CSC102": ["1001"],
            "CSC103": ["1002"],
            "CSC104": [],
        }
        self.course_max_size = {"CSC101": 3, "CSC102": 2, "CSC103": 1, "CSC104": 3}
        self.main_window = tk.Tk()
        self.main_window.title("Class Registration App")
        self.main_window.geometry("500x500")
        self.main_window.iconbitmap(
            "E:\Wake Tech\CSC-121 Python Programming\CSC121 Group Project\student_registration_base\student_registration_base\GUI exe\waketech.ico"
        )

        self.student_id = tk.StringVar()
        self.student_id.set("")
        self.total_hours = tk.IntVar()

        self.build_login_menu()

        self.main_window.mainloop()

    # build main menu after logged in
    def build_main_menu(self):

        # frames for main window
        self.frame_main_page = tk.Frame(self.main_window, padx=10, pady=10)

        # frames packed into main window
        self.frame_student_information = tk.Frame(
            self.frame_main_page, padx=10, pady=10
        )
        self.frame_billing_information = tk.Frame(
            self.frame_main_page, padx=10, pady=10
        )
        self.frame_menues = tk.Frame(self.frame_main_page, padx=10, pady=10)
        self.frame_classes = tk.LabelFrame(
            self.frame_main_page, text="", borderwidth=5, padx=10, pady=10
        )

        # build the clickable course buttons
        self.course_button_signal = {}
        self.course_selection = []
        for course in self.course_roster:
            self.course_button_signal[course] = tk.IntVar()
            self.course = tk.Checkbutton(
                self.frame_classes,
                text=course,
                padx=10,
                pady=10,
                variable=self.course_button_signal[course],
            )
            self.course.deselect()
            self.course.pack(side=tk.LEFT)

        # build registered classes list and create label for it
        self.registered_classes = []
        self.main_page_courses = tk.Label(
            self.frame_student_information,
            text=f"Registered Courses: {self.registered_classes}",
        )
        self.get_registered_courses()

        # build main headers for main page
        self.main_page_header = tk.Label(
            self.frame_student_information, text=self.login_message.get()
        )
        self.main_page_student = tk.Label(
            self.frame_student_information, text=f"Student ID: {self.student_id.get()}"
        )

        # get total registered hours
        self.total_hours_label = tk.Label(
            self.frame_billing_information,
            text=f"Total Registered Hours: {self.total_hours.get()}",
        )
        self.get_total_hours()

        # build stringvar messages for error and success, and labels for them
        self.reg_success_message = tk.StringVar()
        self.reg_success_message.set("")
        self.reg_success = tk.Label(
            self.frame_student_information, text=self.reg_success_message.get()
        )
        self.reg_error_message = tk.StringVar()
        self.reg_error_message.set("")
        self.reg_error = tk.Label(
            self.frame_student_information, text=self.reg_error_message.get()
        )

        # pack student information into student information frame
        self.main_page_header.grid(row=0, column=0, pady=2)
        self.main_page_student.grid(row=1, column=0, pady=2)
        self.main_page_courses.grid(row=2, column=0, pady=2)
        self.reg_success.grid(row=3, column=0, pady=2)
        self.reg_error.grid(row=4, column=0, pady=2)

        # get cost and pack cost and hours into billing frame
        self.cost = tk.IntVar()
        self.billing_label = tk.Label(
            self.frame_billing_information, text=f"Total Cost: ${self.cost.get()}"
        )
        self.get_cost()
        self.total_hours_label.grid(row=0, column=0, pady=2)
        self.billing_label.grid()

        # build buttons for adding, dropping, and logging out
        self.logout = tk.Button(
            self.frame_menues,
            text="logout",
            command=lambda: [self.frame_main_page.forget(), self.build_login_menu()],
            padx=10,
            pady=10,
            width=25,
        )
        self.add_button = tk.Button(
            self.frame_menues,
            text="Add Course",
            padx=10,
            pady=10,
            command=self.add_course,
        )
        self.drop_button = tk.Button(
            self.frame_menues,
            text="Drop Course",
            padx=10,
            pady=10,
            command=self.drop_course,
        )

        # pack buttons for adding, dropping, and logging out
        self.add_button.grid(row=0, column=0, padx=10, pady=10)
        self.drop_button.grid(row=0, column=1, padx=10, pady=10)
        self.logout.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

        # pack main frame, and frames into main frame
        self.frame_main_page.pack()
        self.frame_student_information.pack()
        self.frame_billing_information.pack()
        self.frame_classes.pack()
        self.frame_menues.pack()

    def get_cost(self):
        if self.student_in_state[self.student_id.get()] == True:
            self.cost.set(self.total_hours.get() * 225)
        else:
            self.cost.set(self.total_hours.get() * 850)
        self.billing_label.config(text=f"Total Cost: ${self.cost.get()}")

    # find out registered courses from the course roster
    def get_registered_courses(self):
        for course in self.course_roster:
            if self.student_id.get() in self.course_roster[course]:
                self.registered_classes.append(course)
        if self.registered_classes:
            self.main_page_courses.config(
                text=f"Registered Courses: {self.registered_classes}"
            )
        else:
            self.main_page_courses.config(text="No Classes Registered")

    # get total hours based on registered courses
    def get_total_hours(self):
        self.course_hours_total = 0
        for course in self.course_roster:
            if self.student_id.get() in self.course_roster[course]:
                self.course_hours_total += self.course_hours[course]
        self.total_hours.set(self.course_hours_total)
        self.total_hours_label.config(
            text=f"Total Registered Hours: {self.total_hours.get()}"
        )

    # build login menu
    def build_login_menu(self):
        self.frame_login_entry = tk.LabelFrame(
            self.main_window,
            text="Please enter your login credentials",
            padx=10,
            pady=10,
            borderwidth=5,
        )

        self.frame_login_submit = tk.Frame(self.main_window, padx=5, pady=5)

        self.login_label = tk.Label(self.frame_login_entry, text="User ID")
        self.key_label = tk.Label(self.frame_login_entry, text="Key")

        self.id_window = tk.Entry(self.frame_login_entry, width=15, borderwidth=5)
        self.key_window = tk.Entry(self.frame_login_entry, width=15, borderwidth=5)

        self.login_message = tk.StringVar()
        self.login_message.set("")

        self.login_button = tk.Button(
            self.frame_login_submit, text="Submit", padx=10, pady=5, command=self.login
        )
        self.quit_button = tk.Button(
            self.frame_login_submit,
            text="Quit",
            padx=18,
            pady=5,
            command=self.main_window.destroy,
        )

        self.key_label = tk.Label(
            self.frame_login_submit, text=self.login_message.get()
        )

        self.login_label.grid(row=0, column=0)
        self.key_label.grid(row=0, column=1)
        self.id_window.grid(row=1, column=0, padx=10, pady=10)
        self.key_window.grid(row=1, column=1, padx=10, pady=10)
        self.frame_login_entry.pack(padx=10, pady=10)
        self.frame_login_submit.pack(padx=10, pady=10)
        self.login_button.grid(row=0, column=0, padx=5, pady=5)
        self.quit_button.grid(row=0, column=1, padx=5, pady=5)
        self.key_label.grid(row=1, column=0, columnspan=2)

    def login(self):
        # ------------------------------------------------------------
        # This function allows a student to log in.
        # It has two parameters: id and s_list, which is the student
        # list. This function asks user to enter PIN. If the ID and PIN
        # combination is in s_list, display message of verification and
        # return True. Otherwise, display error message and return False.
        # Author: Damian Wilder
        # -------------------------------------------------------------
        for student in self.student_list:
            if (
                self.id_window.get() == student[0]
                and self.key_window.get() == student[1]
            ):
                self.login_message.set("Login Successful!")
                self.student_id.set(self.id_window.get())
                self.frame_login_entry.forget()
                self.frame_login_submit.forget()
                self.build_main_menu()
                # self.login_label.grid_forget()
                break
            else:
                self.login_message.set("Invalid ID or Key")
            # self.login_message
        self.id_window.delete(0, tk.END)
        self.key_window.delete(0, tk.END)
        self.key_label.config(text=self.login_message.get())

    def check_course_selection(self):
        self.course_selection = []
        for key, value in self.course_button_signal.items():
            if value.get() != 0:
                self.course_selection.append(key)
                self.course_button_signal[key].set(0)
        # self.main_page_selected_courses.config(text=self.course_selection)

    def add_course(self):
        error_list = []
        class_full = []
        self.check_course_selection()
        reg_copy = self.registered_classes[:]
        for course in self.course_selection:
            if course in self.registered_classes:
                error_list.append(course)
            else:
                if len(self.course_roster[course]) < self.course_max_size[course]:
                    self.registered_classes.append(course)
                    self.course_roster[course].append(self.student_id.get())
                else:
                    class_full.append(course)

        if error_list:
            if class_full:
                self.reg_error_message.set(
                    f"You've already registered for: {error_list} These classes full: {class_full}"
                )
            else:
                self.reg_error_message.set(
                    f"You've already registered for: {error_list}"
                )
        else:
            if class_full:
                self.reg_error_message.set(f"These classes are full: {class_full}")
            else:
                self.reg_error_message.set("")

        if reg_copy != self.registered_classes:
            self.reg_success_message.set(
                f"Successfully Registered: {[x for x in self.registered_classes if x not in reg_copy]}"
            )
        else:
            self.reg_success_message.set("")

        self.reg_success.config(text=self.reg_success_message.get())
        self.reg_error.config(text=self.reg_error_message.get())
        self.get_total_hours()
        self.get_cost()
        self.main_page_courses.config(
            text=f"Registered Courses: {self.registered_classes}"
        )

    def drop_course(self):
        error_list = []
        self.check_course_selection()
        reg_copy = self.registered_classes[:]
        for course in self.course_selection:
            if course not in self.registered_classes:
                error_list.append(course)
            else:
                self.registered_classes.remove(course)
                self.course_roster[course].remove(self.student_id.get())

        if error_list:
            self.reg_error_message.set(f"You weren't registered for: {error_list}")
        else:
            self.reg_error_message.set("")

        if reg_copy != self.registered_classes:
            self.reg_success_message.set(
                f"Successfully dropped: {[x for x in reg_copy if x not in self.registered_classes]}"
            )
        else:
            self.reg_success_message.set("")

        self.reg_success.config(text=self.reg_success_message.get())
        self.reg_error.config(text=self.reg_error_message.get())
        if self.registered_classes:
            self.main_page_courses.config(
                text=f"Registered Courses: {self.registered_classes}"
            )
        else:
            self.main_page_courses.config(text="No Classes Registered")
        self.get_total_hours()
        self.get_cost()


GUI()
