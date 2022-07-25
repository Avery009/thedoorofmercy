from django.urls import path

from . import views

urlpatterns = [
	path('/alms/',views.alms, name='alms'),
	path('/alms/enter/',views.enteralms, name='enter_alms'),
	path('/alms/view/<int:alms_id>', views.viewalms, name='view_alms'),
	path('/alms/edit/<int:alms_id>', views.editalms, name='edit_alms'),
	path('/alms/remove/<int:alms_id>', views.removealms, name='remove_alms'),
]
