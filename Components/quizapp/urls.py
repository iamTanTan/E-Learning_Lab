
from django.urls import path
from Components.quizapp import views

urlpatterns = [
   # path('admin/', admin.site.urls),
   path('<id_field>/',views.examonline, name='examonline')
]
