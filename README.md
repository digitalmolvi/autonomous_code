Welcome to theautonomous_code! This README file provides step-by-step instructions on how to set up and use the project.

## Prerequisites

Before you get started, make sure you have the following prerequisites installed on your system:

- Python 3.x: [Download Python](https://www.python.org/downloads/)
- pip: Included with Python 3.x
- [Virtualenv](https://pypi.org/project/virtualenv/): A tool to create isolated Python environments.

## Setup

1. Clone the project repository to your local machine:

   ```bash
   git clone https://github.com/digitalmolvi/autonomous_code.git
Navigate to the project directory:

bash

cd autonomous_code
Create a virtual environment:

bash

python -m venv venv
Activate the virtual environment:

On Windows:

bash

venv\Scripts\activate
On macOS and Linux:

bash

source venv/bin/activate
Install project requirements:

bash

pip install -r requirements.txt
Database Setup
Run database migrations:

bash

python manage.py makemigrations
python manage.py migrate
Create a superuser for accessing the admin panel:

bash

python manage.py createsuperuser
Follow the prompts to set up the superuser account.

Running the Development Server
Start the development server by running the following command:

bash

python manage.py runserver
The project should now be running at http://127.0.0.1:8000/. You can access the admin panel at http://127.0.0.1:8000/admin/ using the superuser credentials you created earlier.

Creating User Accounts and Plans
Log in to the admin panel.

Navigate to the "Users" section and click "Add" to create user accounts.

Navigate to the "Subscription" section and click "Add" to create subscription plans. You can create plans like "Free," "Standard," and "Pro" with the desired features and pricing.

Assign the created plans to user accounts to activate their subscriptions.