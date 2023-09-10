from django.urls import path
from minecraft.views import(

    create_minecraft_view,
)

app_name = 'minecraft'

urlpatterns = [
    path('create/', create_minecraft_view, name='create')
]
