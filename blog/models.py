from django.db import models

class Blog(models.Model):

    title = models.CharField(max_length=200)

    pub_date = models.DateTimeField()

    body = models.TextField(max_length=500)

    image = models.ImageField(upload_to='images/')

# t0 return summary instead 0f full bdy
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]


    def pub_date_short(self):
        return self.pub_date.strftime('%b %e %Y')