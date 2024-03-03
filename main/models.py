from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    task = models.TextField()

    def __str__(self):
        return self.title


class Note(models.Model):
    title = models.CharField(max_length=50)
    task = models.TextField()

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=50)
    task = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email
