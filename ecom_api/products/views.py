from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import ProductSerializer, UserSerializer
from rest_framework.pagination import LimitOffsetPagination


class ProductPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


# class to create user, accepts username, password
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


# class to generate JWT token, accepts username, password
class TokenPairObtainView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        )


# class to get all product list, special product details and create new product.
class ProductList(generics.ListCreateAPIView):
    try:
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        permission_classes = [permissions.IsAuthenticated]
        pagination_class = ProductPagination
    except Exception as exc:
        print("Error in getting product", str(exc))

    # create new product, pass Name, Description, price
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as exc:
            print("Error in create product", str(exc))


# to update product details
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    try:
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        permission_classes = [permissions.IsAuthenticated]
    except Exception as exc:
        print("Error in update product", str(exc))

    def put(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Exception as exc:
            print("Error in updating product details", str(exc))


# to delete a product, accepts product id.
class ProductDelete(generics.DestroyAPIView):
    try:
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        permission_classes = [permissions.IsAuthenticated]
    except Exception as exc:
        print("Error in delete product", str(exc))

    def delete(self, request, *args, **kwargs):
        try:
            return self.destroy(request, *args, **kwargs)

        except Exception as exc:
            print("Error in delete product", str(exc))
