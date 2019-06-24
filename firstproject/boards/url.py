from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('board/<int:id>/',views.boards_topic, name='boards_topic'),
    path('board/<int:id>/new/',views.new_topic, name='new_topic'),
    path('board/<int:id>/topic/<int:topic_id>/',views.topic_posts, name='topic_posts'),
    path('board/<int:id>/topic/<int:topic_id>/reply',views.reply_topic, name='reply_topic')

]