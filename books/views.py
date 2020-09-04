from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,)
                        

from .forms import *
from .models import *

class BookCreateView(CreateView):
    model = UserBook
    fields =['isbn']
    
    def form_valid(self,form):
        form.instance.user = self.request.user.profile
        return super().form_valid(form)
        