from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from .models import *
from account.models import UserProfile
from .forms import MedicineForm
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

# Create your views here.

class  MedicineView(LoginRequiredMixin,ListView):
    model = Medicine
    template_name = 'medicine/medlist.html'
    paginate_by = 10           
    
    def get_context_data(self, **kwargs):
        context = super(MedicineView,self).get_context_data(**kwargs)       
        context['medicines'] = Medicine.objects.filter(user = self.request.user.userprofile).order_by('-tracked_medicine')        
       
        # search field section
        search_input = self.request.GET.get('search_input') or '' # the apostrophe is for an empty search
        if  search_input:
           context["medicines"] = context["medicines"].filter(tracked_medicine__startswith=search_input)        
        context['search_input'] = search_input
        return context   
        


class MedicineCreate(LoginRequiredMixin,CreateView):
    model = Medicine
    template_name = 'medicine/create.html'
    form_class = MedicineForm
    success_url = reverse_lazy('home')  
    
    def form_valid(self,form):
        my_form = UserProfile.objects.get(user=self.request.user.userprofile)
        form.instance.user= my_form.save()
        return super(MedicineCreate, self).form_valid(form)  
    
            
        
class MedicineUpdate(UpdateView):  # for edit
    model = Medicine
    template_name = 'medicine/update.html'
    form_class = MedicineForm
    success_url = reverse_lazy('home')
    
    
    
class MedicineEditView(DetailView):    # for  itemview
    model = Medicine
    template_name = 'medicine/edit.html'
      
    
class MedicineDelete(DeleteView):     # for delete
    model = Medicine
    template_name ='medicine/delete.html'
    success_url = reverse_lazy('home')