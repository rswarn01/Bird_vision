from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product
from .serializers import ProductSerializer


class ProductTests(APITestCase):
    def setUp(self):
        self.product1 = Product.objects.create(
            title="Product 1", description="Description 1", price=10.99
        )
        self.product2 = Product.objects.create(
            title="Product 2", description="Description 2", price=20.99
        )

    def test_get_all_products(self):
        url = reverse("product-list")
        response = self.client.get(url)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_product_detail(self):
        url = reverse("product-detail", args=[self.product1.pk])
        response = self.client.get(url)
        product = Product.objects.get(pk=self.product1.pk)
        serializer = ProductSerializer(product)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_product(self):
        data = {
            "title": "New Product",
            "description": "New Description",
            "price": 30.99,
        }
        url = reverse("product-list")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 3)

    def test_update_product(self):
        data = {
            "title": "Updated Product",
            "description": "Updated Description",
            "price": 40.99,
        }
        url = reverse("product-detail", args=[self.product1.pk])
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Product.objects.get(pk=self.product1.pk).title, "Updated Product"
        )

    def test_delete_product(self):
        url = reverse("product-detail", args=[self.product1.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 1)
