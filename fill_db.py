import os

from django.contrib.auth import get_user_model
from django.db import IntegrityError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin_panel.settings")

import django
django.setup()


from datetime import datetime, timedelta
import random
from decimal import Decimal
from faker import Faker

from apps.products.models import Product, ProductCategory
from apps.clients.models import Client, CartProducts
from apps.orders.models import Order, OrderProducts
from apps.faq.models import FAQ
from apps.mailing.models import Mailing
from PIL import Image
import random

# Initialize Faker for generating random data
faker = Faker()

# Configuration Variables
num_categories = 5
num_subcategories = 10
num_items_in_cart = 4
num_orders = 2
num_items_in_paid_order = 3
num_items_in_registered_order = 2
num_faq = 8
num_messagings = 5

User = get_user_model()


def create_superuser():
    username = 'admin'
    email = 'admin@example.com'
    password = 'admin'

    # Check if the superuser already exists
    if not User.objects.filter(username=username).exists():
        try:
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f"Superuser '{username}' created successfully.")
        except IntegrityError as e:
            print(f"Error creating superuser: {e}")
    else:
        print(f"Superuser '{username}' already exists.")


create_superuser()


def create_products_and_client_cart_orders():
    # Create Categories and Subcategories
    categories = []
    for i in range(num_categories):
        category = ProductCategory.objects.create(
            name=faker.word()
        )
        categories.append(category)

    subcategories = []
    for i, category in enumerate(categories):
        subcount = num_subcategories if i == 0 else num_subcategories - 3
        for j in range(subcount):
            subcategory = ProductCategory.objects.create(
                name=faker.word(),
                parent_category=category
            )
            subcategories.append(subcategory)

    # Create Products for Subcategories
    products = []
    for subcategory in subcategories:
        num_products = random.randint(1, 5)
        for i in range(num_products):
            product = Product.objects.create(
                name=faker.word(),
                description=faker.text(),
                price=Decimal(random.uniform(10.0, 100.0)).quantize(Decimal("0.01")),
                category=subcategory,
                image="product_images/default.jpg"  # Replace with a valid default image path
            )
            products.append(product)

    # Create a User
    client = Client.objects.create(is_active=True)

    # Add Items to the Cart
    cart_products = random.sample(products, min(num_items_in_cart, len(products)))
    for product in cart_products:
        CartProducts.objects.create(amount=random.randint(1, 5), client=client, product=product)

    # Create Orders
    for i in range(num_orders):
        order_status = "paid" if i == 0 else "registered"
        order = Order.objects.create(
            delivery_address=faker.address(),
            status=order_status,
            client=client,
        )

        num_items = num_items_in_paid_order if i == 0 else num_items_in_registered_order
        order_products = random.sample(products, min(num_items, len(products)))
        for product in order_products:
            OrderProducts.objects.create(
                amount=random.randint(1, 5),
                price=product.price,
                product=product,
                order=order,
            )


create_products_and_client_cart_orders()

img_prefix = 'random_color_image_'
def create_other():
    # Create FAQs
    for i in range(num_faq):
        FAQ.objects.create(
            question=faker.sentence(),
            answer=faker.text()
        )

    # Create Mailings
    for i in range(num_messagings):
        Mailing.objects.create(
            message_text=faker.text(),
            sending_date=datetime.now() + timedelta(days=i),
            is_sent=random.choice([True, False]),
            message_image=f"static_content/mailing_images/{img_prefix}{random.randint(0, 10)}.png"
        )

    print("Data generation with all required fields populated is complete!")


create_other()


def create_random_color_image(width=128, height=256, output_path="random_color_image.png"):
    # Generate a random color (R, G, B)
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Create an image with the given dimensions and fill it with the random color
    img = Image.new("RGB", (width, height), random_color)

    # Save the image to the specified output path
    img.save(f'static_content/mailing_images/{output_path}')
    print(f"Image created and saved as '{output_path}' with color {random_color}")


def create_random_color_images():
    for i in range(10):
        # Create and save the image
        create_random_color_image(width=180, height=320, output_path=f"{img_prefix}{i}.png")


create_random_color_images()
