from django.urls import path
from .views import item_list,memory,details,new,task,reset,test,upload_exercise,update_item_author,translate_to_arabic

urlpatterns = [
    path('', item_list, name='item_list'),
    path('memory/', memory, name='memory'),
    path('new/', new, name='new'),
    path('reset/', reset, name='reset'),
    path('task/', task, name='task'),
    path('details/<int:item_id>/', details, name='details'),
    
    path('test/', test, name='test'),

    path('upload_exercise/', upload_exercise, name='upload_exercise'),
    path("update-item-author/<int:item_id>/", update_item_author, name="update_item_author"),
    path("arabic/<int:item_id>/", translate_to_arabic, name="translate_to_arabic"),
    # Add other paths as needed
]


