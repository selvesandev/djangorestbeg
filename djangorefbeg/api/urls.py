from django.urls import path
from .views import ArticleApiView, ArticleApiSingleView, GenericApiView

urlpatterns = [
    # path('', article_list),
    path('', ArticleApiView.as_view()),
    path('generic/', GenericApiView.as_view()),
    path('generic/<int:id>/', GenericApiView.as_view()),
    path('<int:pk>/', ArticleApiSingleView.as_view())
    # path('<int:pk>/', ArticleApiView.as_view())
]
