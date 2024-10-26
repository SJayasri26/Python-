import mysql.connector
from mysql.connector import Error


try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jayasri@26"
    )

    if connection.is_connected():
        print("Connected to MySQL server")


        cursor = connection.cursor()


        cursor.execute("SHOW DATABASES LIKE 'mydatabase'")
        database_exists = cursor.fetchone()

       if not database_exists:
            cursor.execute("CREATE DATABASE mydatabase")
            print("Database 'mydatabase' created.")
        else:
            print("Database 'mydatabase' already exists.")


        connection.database = 'mydatabase'

        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            age INT
        )
        """
        cursor.execute(create_table_query)
        print("Table 'users' created.")

        # Create 'orders' table if it doesn't exist
        create_orders_table = """
        CREATE TABLE IF NOT EXISTS orders (
            order_id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            product VARCHAR(255),
            amount DECIMAL(10,2),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """
        cursor.execute(create_orders_table)
        print("Table 'orders' created.")

        # Insert data into 'users' table, ignoring duplicate entries
        insert_users_query = """
        INSERT IGNORE INTO users (name, email, age)
        VALUES (%s, %s, %s)
        """
        user_values = [
            ("John Doe", "johndoe@example.com", 25),
            ("Jane Smith", "janesmith@example.com", 30),
            ("Jayasri", "sjayasri39@gmail.com", 20)
        ]

        cursor.executemany(insert_users_query, user_values)
        connection.commit()
        print(f"{cursor.rowcount} records inserted into 'users' table.")

        # Insert data into 'orders' table
        insert_orders_query = """
        INSERT INTO orders (user_id, product, amount)
        VALUES (%s, %s, %s)
        """
        order_values = [
            (1, "Laptop", 1200.50),
            (2, "Phone", 800.00),
            (1, "Tablet", 300.99)
        ]
        cursor.executemany(insert_orders_query, order_values)
        connection.commit()
        print(f"{cursor.rowcount} records inserted into 'orders' table.")

        # 1. WHERE clause: Select users where age > 25
        cursor.execute("SELECT * FROM users WHERE age > 25")
        print("\nUsers with age > 25:")
        for row in cursor.fetchall():
            print(row)

        # 2. ORDER BY clause: Select users ordered by age DESC
        cursor.execute("SELECT * FROM users ORDER BY age DESC")
        print("\nUsers ordered by age (DESC):")
        for row in cursor.fetchall():
            print(row)

        # 3. UPDATE: Update the age of a user
        update_query = "UPDATE users SET age = %s WHERE email = %s"
        cursor.execute(update_query, (26, "johndoe@example.com"))
        connection.commit()
        print(f"\nUpdated user age for 'johndoe@example.com'.")

        # 4. DELETE: Delete a user
        delete_query = "DELETE FROM users WHERE email = %s"
        cursor.execute(delete_query, ("janesmith@example.com",))
        connection.commit()
        print(f"\nDeleted user with email 'janesmith@example.com'.")

        # 5. JOIN: Select users and their orders using INNER JOIN
        join_query = """
        SELECT users.name, orders.product, orders.amount
        FROM users
        INNER JOIN orders ON users.id = orders.user_id
        """
        cursor.execute(join_query)
        print("\nUsers and their orders:")
        for row in cursor.fetchall():
            print(row)

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
import mysql.connector
from mysql.connector import Error

# Connect to MySQL
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="Jayasri@26"  # Replace with your MySQL password
    )

    if connection.is_connected():
        print("Connected to MySQL server")

        # Create a cursor object
        cursor = connection.cursor()

        # Check if the database already exists
        cursor.execute("SHOW DATABASES LIKE 'mydatabase'")
        database_exists = cursor.fetchone()

        # Create database if it doesn't exist
        if not database_exists:
            cursor.execute("CREATE DATABASE mydatabase")
            print("Database 'mydatabase' created.")
        else:
            print("Database 'mydatabase' already exists.")

        # Connect to the new database
        connection.database = 'mydatabase'

        # Create 'users' table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            age INT
        )
        """
        cursor.execute(create_table_query)
        print("Table 'users' created.")

        # Create 'orders' table if it doesn't exist
        create_orders_table = """
        CREATE TABLE IF NOT EXISTS orders (
            order_id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            product VARCHAR(255),
            amount DECIMAL(10,2),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """
        cursor.execute(create_orders_table)
        print("Table 'orders' created.")

        # Insert data into 'users' table, ignoring duplicate entries
        insert_users_query = """
        INSERT IGNORE INTO users (name, email, age)
        VALUES (%s, %s, %s)
        """
        user_values = [
            ("John Doe", "johndoe@example.com", 25),
            ("Jane Smith", "janesmith@example.com", 30),
            ("Jayasri", "sjayasri39@gmail.com", 20)
        ]

        cursor.executemany(insert_users_query, user_values)
        connection.commit()
        print(f"{cursor.rowcount} records inserted into 'users' table.")

        # Insert data into 'orders' table
        insert_orders_query = """
        INSERT INTO orders (user_id, product, amount)
        VALUES (%s, %s, %s)
        """
        order_values = [
            (1, "Laptop", 1200.50),
            (2, "Phone", 800.00),
            (1, "Tablet", 300.99)
        ]
        cursor.executemany(insert_orders_query, order_values)
        connection.commit()
        print(f"{cursor.rowcount} records inserted into 'orders' table.")

        # 1. WHERE clause: Select users where age > 25
        cursor.execute("SELECT * FROM users WHERE age > 25")
        print("\nUsers with age > 25:")
        for row in cursor.fetchall():
            print(row)

        # 2. ORDER BY clause: Select users ordered by age DESC
        cursor.execute("SELECT * FROM users ORDER BY age DESC")
        print("\nUsers ordered by age (DESC):")
        for row in cursor.fetchall():
            print(row)

        # 3. UPDATE: Update the age of a user
        update_query = "UPDATE users SET age = %s WHERE email = %s"
        cursor.execute(update_query, (26, "johndoe@example.com"))
        connection.commit()
        print(f"\nUpdated user age for 'johndoe@example.com'.")

        # 4. DELETE: Delete a user
        delete_query = "DELETE FROM users WHERE email = %s"
        cursor.execute(delete_query, ("janesmith@example.com",))
        connection.commit()
        print(f"\nDeleted user with email 'janesmith@example.com'.")

        # 5. JOIN: Select users and their orders using INNER JOIN
        join_query = """
        SELECT users.name, orders.product, orders.amount
        FROM users
        INNER JOIN orders ON users.id = orders.user_id
        """
        cursor.execute(join_query)
        print("\nUsers and their orders:")
        for row in cursor.fetchall():
            print(row)

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
import mysql.connector
from mysql.connector import Error

# Connect to MySQL
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="Jayasri@26"  # Replace with your MySQL password
    )

    if connection.is_connected():
        print("Connected to MySQL server")

        # Create a cursor object
        cursor = connection.cursor()

        # Check if the database already exists
        cursor.execute("SHOW DATABASES LIKE 'mydatabase'")
        database_exists = cursor.fetchone()

        # Create database if it doesn't exist
        if not database_exists:
            cursor.execute("CREATE DATABASE mydatabase")
            print("Database 'mydatabase' created.")
        else:
            print("Database 'mydatabase' already exists.")

        # Connect to the new database
        connection.database = 'mydatabase'

        # Create 'users' table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            age INT
        )
        """
        cursor.execute(create_table_query)
        print("Table 'users' created.")

        # Create 'orders' table if it doesn't exist
        create_orders_table = """
        CREATE TABLE IF NOT EXISTS orders (
            order_id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            product VARCHAR(255),
            amount DECIMAL(10,2),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """
        cursor.execute(create_orders_table)
        print("Table 'orders' created.")

        # Insert data into 'users' table, ignoring duplicate entries
        insert_users_query = """
        INSERT IGNORE INTO users (name, email, age)
        VALUES (%s, %s, %s)
        """
        user_values = [
            ("John Doe", "johndoe@example.com", 25),
            ("Jane Smith", "janesmith@example.com", 30),
            ("Jayasri", "sjayasri39@gmail.com", 20)
        ]

        cursor.executemany(insert_users_query, user_values)
        connection.commit()
        print(f"{cursor.rowcount} records inserted into 'users' table.")

        # Insert data into 'orders' table
        insert_orders_query = """
        INSERT INTO orders (user_id, product, amount)
        VALUES (%s, %s, %s)
        """
        order_values = [
            (1, "Laptop", 1200.50),
            (2, "Phone", 800.00),
            (1, "Tablet", 300.99)
        ]
        cursor.executemany(insert_orders_query, order_values)
        connection.commit()
        print(f"{cursor.rowcount} records inserted into 'orders' table.")

        # 1. WHERE clause: Select users where age > 25
        cursor.execute("SELECT * FROM users WHERE age > 25")
        print("\nUsers with age > 25:")
        for row in cursor.fetchall():
            print(row)

        # 2. ORDER BY clause: Select users ordered by age DESC
        cursor.execute("SELECT * FROM users ORDER BY age DESC")
        print("\nUsers ordered by age (DESC):")
        for row in cursor.fetchall():
            print(row)

        # 3. UPDATE: Update the age of a user
        update_query = "UPDATE users SET age = %s WHERE email = %s"
        cursor.execute(update_query, (26, "johndoe@example.com"))
        connection.commit()
        print(f"\nUpdated user age for 'johndoe@example.com'.")

        # 4. DELETE: Delete a user
        delete_query = "DELETE FROM users WHERE email = %s"
        cursor.execute(delete_query, ("janesmith@example.com",))
        connection.commit()
        print(f"\nDeleted user with email 'janesmith@example.com'.")

        # 5. JOIN: Select users and their orders using INNER JOIN
        join_query = """
        SELECT users.name, orders.product, orders.amount
        FROM users
        INNER JOIN orders ON users.id = orders.user_id
        """
        cursor.execute(join_query)
        print("\nUsers and their orders:")
        for row in cursor.fetchall():
            print(row)

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
        
cursor.execute("SELECT * FROM users WHERE age > 25")
