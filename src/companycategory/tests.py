from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category, Company  # モデルのインポート
from django.test import tag


class CategoryAPITest(APITestCase):
    def setUp(self):
        self.company = Company.objects.create(name="Test Company")
        self.category = Category.objects.create(
            company=self.company,
            name="Test Category",
            parent_category=None,
        )

    @tag("create")
    def test_create_category(self):
        url = reverse("category-list")
        data = {
            "company": str(self.company.id),
            "name": "New Category",
            "parent_category": None,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)

    @tag("create")
    def test_create_category_invalid_name(self):
        url = reverse("category-list")
        data = {
            "company": str(self.company.id),
            "name": "",
            "parent_category": None,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Category.objects.count(), 1)

    @tag("create")
    def test_create_category_invalid_company(self):
        url = reverse("category-list")
        data = {
            "company": "",
            "name": "New Category",
            "parent_category": None,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Category.objects.count(), 1)

    @tag("read")
    def test_read_category(self):
        url = reverse("category-detail", args=[str(self.category.id)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @tag("read")
    def test_read_category_not_found(self):
        url = reverse("category-detail", args=[str("00000000000")])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @tag("update")
    def test_update_category(self):
        url = reverse("category-detail", args=[str(self.category.id)])
        data = {"name": "Updated Category"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, "Updated Category")

    @tag("delete")
    def test_delete_category(self):
        url = reverse("category-detail", args=[str(self.category.id)])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.count(), 0)

    @tag("delete")
    def test_delete_category_not_found(self):
        url = reverse("category-detail", args=[str("000000000")])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Category.objects.count(), 1)
