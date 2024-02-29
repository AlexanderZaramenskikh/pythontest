from django.db import models
from datetime import datetime
import sqlite3

connect = sqlite3.connect("db.sqlite3")
cursor = connect.cursor()



class Product(models.Model):
    product_name = models.CharField(max_length=200)
    start_date = models.CharField(max_length=50) # т.к дата фиксированная не используем DateTimeField
    price = models.IntegerField(default=0)
    creator = models.ForeignKey(to='Teacher',on_delete=models.CASCADE)
    #Запрос -----------------------------------------------
    cursor.execute("SELECT COUNT(*) FROM business_lesson WHERE product_id = 1")
    count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM business_lesson WHERE product_id = 2")
    count1 = cursor.fetchone()[0]



class Lesson(models.Model):
    product_name = models.CharField(max_length=200)
    url = models.URLField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)


class Group(models.Model):
    students = models.ForeignKey(to='Student',on_delete=models.CASCADE)
    group_name = models.CharField(max_length=50)
    product_name = models.ForeignKey(Product,on_delete=models.CASCADE)


class Teacher(models.Model):
    name = models.CharField(max_length=200)


class Student(models.Model):
    name = models.CharField(max_length=200)
    balance = models.IntegerField(default=0)
    access = models.BooleanField(default=False)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)