from InventoryClass import Inventory, connection, cursor
from UserClass import User
from CartClass import Cart

#create database tables if they don't exist here
connection.execute('''
    CREATE TABLE IF NOT EXISTS inventory(
        ISBN integer PRIMARY KEY,
        Title text NOT NULL, 
        Author text NOT NULL,
        Genre text NOT NULL,
        Pages integer NOT NULL,
        ReleaseDate date NOT NULL
        Stock integer NOT NULL)
        ''')
connection.execute('''
    CREATE TABLE IF NOT EXISTS user(
        UserID integer PRIMARY KEY,
        Email text NOT NULL,
        Password text NOT NULL,
        FirstName text NOT NULL,
        LastName text NOT NULL,
        Address text NOT NULL,
        City text NOT NULL,
        State text NOT NULL,
        Zip integer NOT NULL,
        Payment text NOT NULL)
        ''')
connection.execute('''
    CREATE TABLE IF NOT EXITS cart(
        UserID integer,
        ISBN integer,
        Quantity integer NOT NULL,
        FOREIGN KEY(userID) REFERENCES user(userID)
        FOREIGN KEY(isbn) REFERENCES inventory(isbn))
        ''')
#create sample datasets here if they do not exist
