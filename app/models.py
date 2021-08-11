from django.db import models

# DB Structure to store the input and calculated closest pair to database
class Points(models.Model):
    user_points = models.CharField(max_length=255)
    closest_pair = models.CharField(max_length=255)

    def __str__(self):
        return self.user_points + ' ' + self.closest_pair