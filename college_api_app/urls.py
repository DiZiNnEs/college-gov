from django.urls import include, path

from college_api_app.routes import router

app_name = 'api'

urlpatterns = [
    path('', include(router.urls))
]

