from django.db import models

class PageVisit(models.Model):
    # id -> hidden -> primary key -> auto -> 1,2,3,4......
    path = models.TextField(blank=True, null = True)
    timestamp = models.DateTimeField(auto_now_add=True)
