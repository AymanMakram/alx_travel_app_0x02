# ALX Travel App 0x01

This project provides CRUD API endpoints for managing travel listings and bookings.

## API Endpoints

- `/api/listings/` - CRUD operations for listings
- `/api/bookings/` - CRUD operations for bookings
- `/swagger/` - Interactive API documentation

## Tools Used

- Django
- Django REST Framework
- drf-yasg (Swagger documentation)
- Postman for API testing

## How to Run

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
