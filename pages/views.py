from django.shortcuts import render

from books.models import UserBook
# Create your views here.
def home_view(request):
    user = request.user.profile if request.user.is_authenticated else "No-one"
    # books = UserBook.objects.filter(user__pincode==123456)
    context = {'user':user}
    return render(request,"pages/home.html",context)
