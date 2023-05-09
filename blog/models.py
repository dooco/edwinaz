from django.db import models

from django.contrib.auth.models import User


class Post(models.Model):
    """ Article model """
    user = models.ForeignKey(
        User, related_name="article_user", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    excerpt = models.CharField(max_length=1000, null=False, blank=False)
    image = models.ImageField(upload_to="images/", null=False, blank=False)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["date_added"]

    def __str__(self):
        return str(self.title)
