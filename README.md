# Car Sales Platform

A Django-based web application for buying and selling cars, with support for both individual customers and corporate sellers.

## Features

- User registration (Customer and Corporate)
- Car advertisement creation and management
- Image upload support
- Detailed car information display
- Responsive design using Bootstrap 5

## Prerequisites

- Python 3.8 or higher
- MySQL Server
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd car-sales-platform
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create a MySQL database:
```sql
CREATE DATABASE car_sales_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

5. Update the database settings in `qrotom/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'car_sales_db',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

6. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

7. Create a superuser:
```bash
python manage.py createsuperuser
```

8. Run the development server:
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage

1. Register as either a Customer or Corporate user
2. Log in to your account
3. Create car advertisements with images
4. Browse and search for cars
5. View detailed information about each car
6. Manage your advertisements

## Project Structure

- `qrotom/models.py`: Database models
- `qrotom/views.py`: View functions
- `qrotom/forms.py`: Form definitions
- `qrotom/urls.py`: URL routing
- `qrotom/templates/`: HTML templates
- `media/`: Uploaded images
- `static/`: Static files (CSS, JS, images)

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 