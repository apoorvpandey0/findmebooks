# #This is the signal that will be sent
# from django.db.models.signals import post_save

# #This is the object which will send the signal
# from django.contrib.auth.models import User

# #This will receive the signal
# from django.dispatch import receiver

# #We need this to perform operations on UserBooks table
# from .models import Book,UserBook

# #This function creates new UserBook for each user created
# @receiver(post_save, sender=Book)
# def create_UserBook(sender, instance, created, **kwargs):
#     if created:
#         UserBook.objects.create(book=instance)
#         print("Create_UserBook function executed!")

# #This function saves those newly created UserBooks
# @receiver(post_save, sender=Book)
# def save_UserBook(sender, instance, **kwargs):
#     instance.UserBook.save()
#     print("Save_UserBook function executed!")
