from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.todolist_home, name='todolist_home'),
    path('list', views.list_todolist, name='list_todolist'),
    path('topic_edit/<int:pk>', views.newtodolist_edit, name='edit_todolist'),
    path('topic_delete/<int:pk>', views.newtodolist_delete, name='delete_todolist'),
    path('sorted_todolist', views.newtodolist_sorted, name='sorted_todolist'),

    path('newtodolistitems/<int:pk>', views.list_newtodolistitems, name='list_newtodolistitems'),
    path('display_newtodolistitems/', views.display_tree, name='display_newtodolistitems'),
    path('display_todolist_as_table/', views.display_todolist_as_table, name='display_todolist_as_table'),
    path('display_todolist_as_table_id/<int:pk>', views.display_todolist_as_table_id, name='display_todolist_as_table_id'),
    path('newtodolist_update/', views.newtodolist_update, name='newtodolist_update'),

    path('clone_newtodolistitems/<int:pk>', views.clone_newtodolistitems, name='clone_newtodolistitems'),
    path('deepclone_newtodolistitems/<int:pk>', views.deepclone_newtodolistitems, name='deepclone_newtodolistitems'),
]