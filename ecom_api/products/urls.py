from django.urls import path
from .views import (
    ProductList,
    ProductDetail,
    ProductDelete,
    UserCreate,
    TokenPairObtainView,
)


# urls for api access for all the operations.
urlpatterns = [
    path("products/", ProductList.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetail.as_view(), name="product-detail"),
    path("products/<int:pk>/delete/", ProductDelete.as_view(), name="product-delete"),
    path("users/create/", UserCreate.as_view(), name="user-create"),
    path("users/token/", TokenPairObtainView.as_view(), name="token_obtain_pair"),
]
