import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin@123"
    )
except Exception as e:
    print("Error connecting to the MySQL server:", e)
    exit()

cursor = mydb.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS contact_list")
cursor.execute("USE contact_list")

cursor.execute("CREATE TABLE IF NOT EXISTS CONTACTS (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), phone_number VARCHAR(10))")

def take_input():
    name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    cursor.execute("INSERT INTO CONTACTS (name, phone_number) VALUES (%s, %s)", (name, phone_number))
    mydb.commit()
    print("Contact saved successfully!")

choice = input("Do you want to add a contact? (y/n): ")
if choice.lower() == 'y':
    take_input()
else:
    print("Exiting the program.")

cursor.close()
mydb.close()