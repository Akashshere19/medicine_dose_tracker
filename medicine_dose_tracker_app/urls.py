from django.urls import path
from .import views
from .views import MedicineView,MedicineCreate,MedicineEditView,MedicineUpdate,MedicineDelete


urlpatterns =[
    path('home',MedicineView.as_view(), name='home'),
    path('add_dosage', MedicineCreate.as_view(), name="add_dose"),
    path('edit_dose/<int:pk>/', MedicineEditView.as_view(), name="edit"),
    path('update_dose/<int:pk>/',MedicineUpdate.as_view(), name="update_dose"),
    path('delete_delete/<int:pk>/', MedicineDelete.as_view(), name='delete_dose')
]
