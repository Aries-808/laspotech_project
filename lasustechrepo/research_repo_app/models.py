from django.db import models
from django.contrib.auth.models import User

class Thesis(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='theses/')

    def __str__(self):
        return self.title

class ResearchPaper(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='research_papers/')

    def __str__(self):
        return self.title

class ResearchData(models.Model):
    title = models.ForeignKey(ResearchPaper, on_delete=models.CASCADE)
    data_file = models.FileField(upload_to='research_data/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Data for {self.title}"
