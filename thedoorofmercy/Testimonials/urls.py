from django.urls import path

from . import views

urlpatterns = [
	path('/testimonials/',views.testimonials, name='testimonials'),
	path('/testimonials/enter/',views.entertestimonial, name='input_testimonial'),
	path('/testimonials/view/<int:testimonial_id>', views.viewtestimonial, name='view_testimonial'),
	path('/testimonials/thank/<int:testimonial_id>', views.thank, name='thank'),
	path('/testimonials/thanks/<int:testimonial_id>/<int:thanks_count>', views.givethanks, name='give_thanks'),
]
