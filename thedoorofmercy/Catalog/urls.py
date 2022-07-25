from django.urls import path

from . import views

urlpatterns = [
	path('sermons/',views.sermons, name='sermons'),
	path('sermons/enter/',views.entersermon, name='enter_sermon'),
	path('sermons/view/<int:sermon_id>', views.viewsermon, name='view_sermon'),
	path('sermons/edit/<int:sermon_id>', views.editsermon, name='edit_sermon'),
	path('sermons/remove/<int:sermon_id>', views.removesermon, name='remove_sermon'),
]
