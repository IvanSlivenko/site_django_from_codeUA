from django.db import models

from django.contrib.auth.models import User

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    website = models.URLField(blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    rental_fee = models.DecimalField(max_digits=6, decimal_places=2)
    late_fee_multiplier = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='books', null=True, blank=True)
    pages = models.PositiveIntegerField()
    language = models.CharField(max_length=100)


    def __str__(self):
        return self.title

class Rentall(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rented_on = models.DateField(null=True, blank=True)
    returned_on = models.DateField(null=True, blank=True)
    lare_fee_paid = models.BooleanField(default=False)
    
    def is_late(self):
        return self.returned_on is None and self.due_on < date.today() 

    def  calculate_rental_fee(self):
        if self.is_late():
            return self.book.rental_fee * self.book.late_fee_multiplier * (date.today() - self.due_on).days
        else:
            return self.book.rental_fee * (self.returned_on - self.rented_on).days   

class Payment(models.Model):
    rental = models.ForeignKey(Rentall, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_date = models.DateField(auto_now=True)

class UserProfile(models.Model):
    uaer = models.OneToOneField(User, on_delete=models.CASCADE)
    credit_cart_number = models.CharField(max_length=16)