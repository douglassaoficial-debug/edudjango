
- **manage.py**: Command-line utility for administrative tasks.
- **edudjango/**: Contains project settings and configurations.
- **apps/**: Contains individual Django applications/modules.
  - **core/**: Contains core functionality models and views.
  - **users/**: Handles user authentication and profiles.
- **templates/**: HTML templates for rendering views.
- **static/**: Static files such as CSS and JS.

## Features

- User authentication (registration, login, logout)
- Profile management for students and teachers
- Course creation and management
- Enrollment functionality for students
- Assignment submission and grading

## Models

### User
- `username`: char field, unique
- `email`: char field, unique
- `password`: hashed password
- `profile_pic`: URL for user profile picture

### Course
- `title`: char field
- `description`: text field
- `created_by`: foreign key to User

### Enrollment
- `user`: foreign key to User
- `course`: foreign key to Course
- `date_enrolled`: date field

## Views

- **Core Views**: Responsible for displaying courses and user profiles.
- **User Views**: Handle registration, login, and logout actions using class-based views.

## Authentication System

Utilizes Django's built-in authentication system with a custom user model. Users can register via the registration form and log in through the login view. Passwords are securely hashed using Django's hashing system.

## Forms

- **RegistrationForm**: For new user registrations.
- **LoginForm**: For user authentication.
- **CourseForm**: For creating and updating courses.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/edudjango.git
   cd edudjango
