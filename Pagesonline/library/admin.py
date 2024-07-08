from django.contrib import admin
from library.models import Book, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'rental_fee', 'late_fee_multiplier')
    list_filter = ('author',)
    search_fields = ('title', 'author_first_name', 'author_last_name')



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('firsat_name', 'last_name', 'email')




