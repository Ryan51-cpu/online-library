from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    title  = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    description = models.TextField()
    
    def __str__(self):
        return self.title

    def average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            return round(sum(r.rating for r in reviews) / len(reviews), 1)
        return 0

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.rating}/5)"
    
    