from django.urls import path
from userbase.views import UserBaseSerializerView

app_name = 'userbase'

urlpatterns = [
    path('', UserBaseSerializerView.as_view(), name='userbase_serializer_url'),

]