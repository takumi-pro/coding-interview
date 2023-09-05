import uuid

from django.db import models


class Company(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, db_comment="企業ID"
    )
    name = models.CharField(max_length=255, db_comment="企業名")
    created_at = models.DateTimeField(auto_now_add=True, db_comment="作成日時")
    updated_at = models.DateTimeField(auto_now=True, db_comment="更新日時")

    class Meta:
        db_table = "companies"
        db_table_comment = "企業テーブル"
        verbose_name = "company"
        verbose_name_plural = "companies"


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, help_text="カテゴリID（UUID）")
    company = models.ForeignKey(
        Company, related_name="+", on_delete=models.CASCADE, db_comment="企業ID", help_text="企業ID"
    )
    name = models.CharField(max_length=255, db_comment="カテゴリ名", help_text="カテゴリ名")
    parent_category = models.ForeignKey(
        "self",
        null=True,
        related_name="subcategories",
        on_delete=models.SET_NULL,
        db_comment="親カテゴリID",
        help_text="親カテゴリID"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, db_comment="作成日時", help_text="作成日時"
    )
    updated_at = models.DateTimeField(auto_now=True, editable=False, db_comment="更新日時", help_text="更新日時")

    class Meta:
        db_table = "categories"
        db_table_comment = "カテゴリテーブル"
        verbose_name = "category"
        verbose_name_plural = "categories"
        constraints = [
            models.UniqueConstraint(
                fields=["company", "name"], name="unique_company_category_combination"
            )
        ]
        indexes = [models.Index(fields=["company", "name"])]
