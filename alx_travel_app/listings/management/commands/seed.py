from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = "Seed the database with initial Listing data"

    def handle(self, *args, **options):
        data = [
            {"title": "Beach House", "description": "A beautiful beach house.", "price_per_night": 120.00, "location": "Miami"},
            {"title": "Mountain Cabin", "description": "Cozy cabin in the mountains.", "price_per_night": 95.50, "location": "Colorado"},
            {"title": "City Apartment", "description": "Modern apartment downtown.", "price_per_night": 150.00, "location": "New York"},
        ]

        for item in data:
            Listing.objects.create(**item)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
