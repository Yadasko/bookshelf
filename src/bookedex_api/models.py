from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return "%s" % (self.name)


class Book(models.Model):
    id = models.CharField(max_length=45, primary_key=True)
    title = models.CharField(max_length=45)
    subtitle = models.CharField(max_length=45, null=True)
    ISBN_13 = models.CharField(max_length=13, null=True)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return f"@{self.id}: {self.title} - {self.subtitle} (ISBN_13: {self.ISBN_13}"


class BookHunter(models.Model):
    username = models.CharField(max_length=45)

    def __str__(self):
        return "%s" % (self.username)


class CollectedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    hunter = models.ForeignKey(BookHunter, on_delete=models.CASCADE)

    def __str__(self):
        return "%s: %s" % (self.hunter.username, self.book.title)


class WantedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    hunter = models.ForeignKey(BookHunter, on_delete=models.CASCADE)

    def __str__(self):
        return "%s: %s" % (self.hunter.username, self.book.title)
