"""
Defines URL patterns for learning_logs
"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics!
    path('topics/', views.topics, name='topics'),
    # Page for Editing Topic
    path('edit_topic/<int:topic_id>/', views.edit_topic,name='edit_topic'),
    # Page that shows Entries of each topic!
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for Adding a New Topic!
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for Adding a New Entry!

    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Page for Editing Entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name = 'edit_entry'),
]