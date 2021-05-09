from django.urls import path
from . import views as v
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('<int:id>/', csrf_exempt(v.TasksView.as_view()), name='Todos'),
    path('', v.index, name='Todo'),
]
