import mysql.connector as mysql

mydb = mysql.connect(host="localhost", user="root", passwd="sql@1234", database="RAAJA")
mycursor = mydb.cursor()

sqlFormula = "INSERT INTO regform (name,mobileno,email,department,college,age)  VALUES (%s, %s, %s, %s, %s, %s)"


def student_reg():
    while True:
        data = []
        while True:
            print("\n1.New Student Registration")
            print("2.Back")
            print("Press 1 for New Registration and Press 2 for Back")
            a = int(input("Enter Your Input:"))
            if a == 1 or a == 2:
                break
            else:
                print("\nInvalid Input\n")
        if a == 2:
            break
        b = input("Enter Your Name:")
        data.append(b)
        b = int(input("Enter Your 10 Digit Mobile Number:"))
        data.append(b)
        b = input("Enter Your Email ID:")
        data.append(b)
        b = input("Enter Your Department:")
        data.append(b)
        b = input("Enter Your College Name:")
        data.append(b)
        b = int(input("Enter Your Age:"))
        data.append(b)

        data = tuple(data)

        mycursor.execute(sqlFormula, data)
        mydb.commit()
        mycursor.execute("select * from regform ORDER BY id DESC LIMIT 1;")
        for db in mycursor:
            uid = db[0]
        print("\nUser Registered Successfully with id number : ", uid, sep="")


def admin_data():
    print("1.View Student Details")
    print("2.Add a Student Record")
    print("3.Delete a Student Record")
    print("4.Logout")
    opt = input("Enter the Input:")
    if opt == "1":
        mycursor.execute("select * from regform;")
        for db in mycursor:
            print(db)
        admin_data()
    elif opt=="2":
        student_reg()
        admin_data()
    elif opt=="3":
        d = int(input("\nEnter the Student ID to be deleted:"))
        sqlDelete = "DELETE FROM regform WHERE id = '%d' " % (d)
        mycursor.execute(sqlDelete)
        mydb.commit()
        admin_data()
    elif opt=="4":
        home_screen()
    else:
        print("Invalid Input")
        admin_data()



def admin_login():
    username = input("Enter Username:")
    password = input("Enter Password:")
    if username=="admin":
        if password=="admin":
            print("\nLogin Successful\n")
            admin_data()
        else:
            print("\nIncorrect Password\n")
    else:
        print("\nIncorrect Username\n")


def home_screen():
    while 1:
        print("****** REGISTRATION FORM ******\n")
        print("1.Admin Login")
        print("2.Student Registration")
        print("3.Exit")
        option = input("Enter Option:")
        if option == "1":
            print("\nAdmin Login\n")
            admin_login()
        elif option == "2":
            print("\nStudent Registration\n")
            student_reg()
        elif option == "3":
            print("Exited")
            exit(1)
        else:
            print("Invalid Option\n")


home_screen()



