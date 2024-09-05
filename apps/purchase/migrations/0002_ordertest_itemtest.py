# Generated by Django 5.1 on 2024-08-29 11:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
        ("purchase", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderTest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("street", models.CharField(default="", max_length=500)),
                ("city", models.CharField(default="", max_length=100)),
                ("state", models.CharField(default="", max_length=100)),
                ("zip_code", models.CharField(default="", max_length=100)),
                ("phone_no", models.CharField(default="", max_length=100)),
                ("country", models.CharField(default="", max_length=100)),
                ("total_amount", models.IntegerField(default=0)),
                (
                    "payment_status",
                    models.CharField(
                        choices=[("PAID", "Paid"), ("UNPAID", "Unpaid")],
                        default="UNPAID",
                        max_length=20,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Processing", "Processing"),
                            ("Shipped", "Shipped"),
                            ("Delivered", "Delivered"),
                        ],
                        default="Processing",
                        max_length=50,
                    ),
                ),
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("COD", "Cod"),
                            ("CARD", "Card"),
                            ("PAYPAL", "Paypal"),
                        ],
                        default="CARD",
                        max_length=50,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ItemTest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="", max_length=200)),
                ("quantity", models.IntegerField(default=1)),
                ("price", models.DecimalField(decimal_places=2, max_digits=7)),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="product.product",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orderitems",
                        to="purchase.ordertest",
                    ),
                ),
            ],
        ),
    ]
