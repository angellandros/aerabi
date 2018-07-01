from django.db import models


class BlogPost(models.Model):
    text = models.TextField()
    truncated = models.TextField()
    pub_date = models.DateTimeField('date published')
    location = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100, db_index=True, unique=True)

    def __str__(self):
        return self.title


class Page(models.Model):
    url = models.CharField(max_length=100, db_index=True, unique=True)
    text = models.TextField()

    def __str__(self):
        return self.url
