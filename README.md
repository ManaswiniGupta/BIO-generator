# DinnerTonight Bio Generator

DinnerTonight Bio Generator is a web application that creates unique, personalized bios based on user inputs, such as career, personality, interests, and relationship goals. This app is designed to provide engaging and descriptive bios for social platforms or personal use. The application uses natural language processing (NLP) through an AI model to generate bios that match the user's attributes.

## Features
- Generates a catchy title along with a personalized bio
- Interactive user form for easy input
- Hosted on Render for easy access


## Getting Started

### Prerequisites
- Python 3.12
- `pip` (Python package manager)
- A `.env` file containing necessary environment variables

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/dinnertonight-bio-generator.git
   cd dinnertonight-bio-generator
2. **Install dependencies:** Use `pip` to install the required dependencies
    ```bash
    pip install -r requirements.txt
3. **Set up environment variables:**
  - Create a `.env` file in the root directory and add your environment variables, such as the API key.
    ```bash
    GROQ_API_KEY=your-api-key-here
    ```
  - Ensure `.env` is listed in .gitignore to keep it private.

### Running the Application
To start the Flask server, run the following command:
```bash
    flask run
```
    


The application will be available at `http://127.0.0.1:5000`.

## Running in Production
This application is configured to use Gunicorn for production environments. To run with Gunicorn:
```bash
  gunicorn app:app
```
## Deployment
This application can be deployed on Render. Be sure to include gunicorn in requirements.txt to ensure compatibility.

## Project Structure
- `app.py`: Main application file for Flask server setup and endpoints
- `templates/`: HTML templates for the web interface
- `static/`: Static files such as CSS for styling
- `requirements.txt`: Python dependencies
- `.env`: Contains environment variables (should be added to .gitignore)




