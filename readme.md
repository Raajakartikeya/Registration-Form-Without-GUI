Registration Form System Documentation

Introduction:

The Registration Form System is a simple Python-based application that allows students to register their details, and an admin can manage and view the registered student records. The application interacts with a MySQL database to store and retrieve student information.

Project Structure:

The project consists of a single Python script containing multiple functions and an interactive command-line interface for user interaction. It uses the MySQL Connector library to connect to the MySQL database.

Files

•   main.py: The main Python script containing all the functions and the user interface.

Requirements

•   Python 3.x

•   MySQL Server

•   MySQL Connector for Python (install using pip install mysql-connector-python)

Functionality

The Registration Form System has the following main functionalities:

1.Student Registration (student_reg() function)

•   The user can register their details, including name, mobile number, email, department, college name, and age.

•   The provided information is validated, and if valid, the details are stored in the MySQL database.

•   Each student is assigned a unique ID that is automatically generated by the database.

•   Upon successful registration, the system displays the newly registered student's unique ID.

2. Admin Login and Management (admin_data() function)

•   The admin can log in using the username "admin" and password "admin".

•   After successful login, the admin can perform the following actions:

•   View all student details (ID, name, mobile number, email, department, college name, and age) stored in the database.

•   Add a new student record by invoking the student_reg() function.

•   Delete a student record by providing the student's ID.


3.Home Screen (home_screen() function)

•   The initial screen of the application that offers three options: Admin Login, Student Registration, and Exit.

•   Based on the user's choice, the respective functions are invoked.

How to Run

1.  Install the required Python packages (mysql-connector-python) using pip install mysql-connector-python.

2.  Set up the MySQL server and create a database named "RAAJA".

3.  Run the registration_form.py script using python registration_form.py.

4.  Follow the on-screen instructions to navigate through the application's functionalities.

Conclusion

The Registration Form System is a user-friendly application that allows students to register their details and an admin to manage and view the registered student records. It demonstrates basic database interaction using MySQL Connector in Python and offers a simple, command-line-based user interface for ease of use. The system can be extended and customized further to meet specific requirements of a larger registration management system.
