<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <style>
        .bg-navy {
          background-color: #0e0950;
        }
      </style>
    <title>Home Page</title>
  </head>
  <body>
    
    <nav class="navbar-expand-md navbar-dark bg-navy">
        <a class="navbar-brand" href="#">Ajoke Alasooke Store</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Market store</a>
                </li>
            </ul>
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="#">Login</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Register</a>
                </li>
            </ul>
        </div>
    </nav>
    <h1>Home page</h1>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>

    <!-- Option 2: jQuery, Popper.js, and Bootstrap JS
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" integrity="sha384-w1Q4orYjBQndcko6MimVbzY0tgp4pWB4lZ7lr30WKz0vr/aWKhXdBNmNb5D92v7s" crossorigin="anonymous"></script>
    -->
  </body>
  <style>
    body {
        background-color: #060630;
        color: whitesmoke;
    }
  </style>
</html>

market html

{% extends 'base.html' %}
{% block title %}
    Market Page
{% endblock %}

{% block content %}
<table class="table table-hover table-gold">
    <thead>
        <tr>
            <th scope="col">ID</th>
            <th scope="col">NAME</th>
            <th scope="col">COLOR</th>
            <th scope="col">LENGHT</th>
            <th scope="col">PRICE</th>
            <th scope="col">OPTIONS</th>
        </tr>
    </thead>
    <tbody>
        <!--your rows inside the table here-->
        {% for item in aitems %}
        <tr>
            <td>{{ aitems.id }}</td>
            <td>{{ aitems.name }}</td>
            <td>{{ aitems.color }}</td>
            <td>{{ aitems.lenght }}</td>
            <td>#{{ aitems.price }}</td>
            <td>
                <button class="btn btn-outline btn-info">More info</button>
                <button class="btn btn-outline btn-success">Purchase this item</button>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>

{% endblock %}

adbms 
import pyodbc

class DatabaseManager:
    def __init__(self, server, database):
        self.server = server
        self.database = database

    def connect(self):
        self.conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';Trusted_Connection=yes;'
        )
        self.cursor = self.conn.cursor()
        print(f"Connected to {self.database} at {self.server}")

    def create_table(self):
        try:
            print("Creating table 'aitems' if not exists...")
            self.cursor.execute('''
            IF OBJECT_ID('aitems', 'U') IS NULL
            BEGIN
                CREATE TABLE aitems (
                    id int PRIMARY KEY,
                    Name nvarchar(50),
                    color nvarchar(50),
                    length int,
                    price int
                );
            END
            ''')
            self.conn.commit()
            print("Table 'aitems' checked/created.")
        except pyodbc.Error as err:
            print(f"Error creating table: {err}")

    def insert_item(self, item_id, name, color, length, price):
        try:
            print(f"Inserting item: {item_id}, {name}, {color}, {length}, {price}")
            self.cursor.execute('''
            INSERT INTO aitems (id, Name, color, length, price)
            VALUES (?, ?, ?, ?, ?)
            ''', (item_id, name, color, length, price))
            self.conn.commit()
            print("Item inserted.")
        except pyodbc.Error as err:
            print(f"Error inserting item: {err}")

    def get_items(self):
        try:
            print("Fetching all items from 'aitems' table...")
            self.cursor.execute('SELECT * FROM aitems')
            items = self.cursor.fetchall()
            return items
        except pyodbc.Error as err:
            print(f"Error fetching items: {err}")
            return []

    def close_connection(self):
        self.conn.close()
        print("Connection closed.")

# Usage example
if __name__ == '__main__':
    server = 'DANDY\\SQLEXPRESS'
    database = 'mstore'
    db_manager = DatabaseManager(server, database)
    db_manager.connect()
    db_manager.create_table()
    
    # Insert some items
    db_manager.insert_item(1, 'Loom-Asooke', 'Gold', 90, 30000)
    db_manager.insert_item(2, 'Plain Cotton Asooke', 'blue', 70, 22000)
    db_manager.insert_item(3, 'Mettalic Asooke', 'pink', 90, 19000)
    db_manager.insert_item(4, 'Ojutonsoro', 'yellow', 80, 19000)

    # Fetch and print all items
    aitems = db_manager.get_items()
    for item in aitems:
        print(item)

    db_manager.close_connection()
