# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import datetime
from django.db import models


ROOM_LEN = 5


class Status(models.Model):
    timestamp = models.DateTimeField(default=datetime.now)
    room = models.CharField(max_length=ROOM_LEN, primary_key=True)
    text = models.TextField()

    def __str__(self):
        return 'Status: ' + self.room


class Complaint(models.Model):
    chat = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return 'Complaint: ' + self.chat.room


class User(models.Model):
    chat_id = models.IntegerField(primary_key=True)
    telephone_number = models.CharField(max_length=12)
    room = models.CharField(max_length=ROOM_LEN, blank=True, null=True)

    def __str__(self):
        return 'User [' + self.telephone_number + '] from ' + self.room
