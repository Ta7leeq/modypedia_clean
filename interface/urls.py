from django.urls import path
from .views import item_list,memory,details,new,task,reset,test,upload_exercise

urlpatterns = [
    path('', item_list, name='item_list'),
    path('memory/', memory, name='memory'),
    path('new/', new, name='new'),
    path('reset/', reset, name='reset'),
    path('task/', task, name='task'),
    path('details/<int:item_id>/', details, name='details'),
    
    path('test/', test, name='test'),

    path('upload_exercise/', upload_exercise, name='upload_exercise'),

    # Add other paths as needed
]
