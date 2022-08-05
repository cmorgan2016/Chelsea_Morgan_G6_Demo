from sqlite3 import connect
from django.db import models
import webbrowser
#import mysql.connector
# class Home(models.Model):
#     conn = connect('Approved.db')

#     if conn:
#         print ("Connected Successfully")
#     else:
#         print ("Connection Not Established")

#     select_genre = """SELECT * FROM genre"""
#     cursor = conn.cursor()
#     cursor.execute(select_genre)
#     result = cursor.fetchall()

#     p = []

#     tbl = "<tr><td>Genres</td></tr>"
#     p.append(tbl)

#     for row in result:
#         a = "<tr><td>%s</td>"%row[0]
#         p.append(a)


#Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre')

    def __str__(self):
        return self.name


class To_Approve(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre')

    def __str__(self):
        return self.name