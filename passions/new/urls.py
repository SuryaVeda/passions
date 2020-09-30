from django.urls import path
from . import views

app_name = "new"


urlpatterns = [
path('', views.library, name = 'lib'),
path('drafts', views.drafts, name = 'draf'),
path('draft/<int:pk>', views.save_draft, name = 'saveDraft'),
path('book/<int:pk>', views.save_book, name = 'saveBook'),
path('add', views.create_book, name = 'bookForm'),
path('details/<int:pk>', views.details, name = 'bookDetails'),
path('addPage/<int:pk>', views.create_page, name = 'pageForm'),
path('editPage/<int:pk>', views.edit_page, name = 'edit'),
path('save/<int:pk>', views.save_pdf, name = 'pdf'),
path('overview/<int:pk>', views.overview, name = 'bookOverview'),
path('comment/<int:pk>', views.add_comment, name="comment"), 
path('reply/<int:pk>/<int:post_pk>', views.add_reply, name="reply"), 
]