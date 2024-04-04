# Car Predictor Pro+

## Overview
Car Predictor Pro+ is an advanced machine learning application designed to predict the price of cars based on various features. It leverages a full-stack development approach, incorporating machine learning algorithms, web development technologies, and database management tools.

## Technologies Used
| Category              | Tools                       |
|-----------------------|-----------------------------|
| Machine Learning      | Python, Scikit-learn       |
| Web Development       | Django, HTML, CSS, JavaScript |
| Database Management   | MySQL, XAMPP                |
|  Data Visualization   | MAtplotlib,Seaborn,Pandas    |
| Version Control       | Git, GitHub                 |

## Features
- Predicts the price of cars using machine learning algorithms.
- Provides a web interface for users to input car features and receive price predictions.
- Stores data in a MySQL database for efficient retrieval and management.
- Utilizes XAMPP for local server setup and hosting.

## Project Structure
- `models/`: Contains machine learning models for price prediction.
- `views/`: Includes Django views for rendering web pages and handling user input.
- `templates/`: Stores HTML templates for the web interface.
- `static/`: Contains static files such as CSS and JavaScript.
- `database/`: Contains SQL scripts and database configurations.
- `requirements.txt`: Lists all Python dependencies for easy installation.

## Usage
1. Clone the repository: `git clone https://github.com/radhirsh/Car_Predictor_Pro+.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Setup XAMPP and MySQL database.
4. Run migrations: `python manage.py migrate`
5. Start the Django server: `python manage.py runserver`
6. Access the web interface in your browser: `http://localhost:8000`

## Contributors
- [Sridhar S](https://github.com/radhirsh): Project Lead & Developer

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
