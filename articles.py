#!/usr/bin/python3

"""
===================================================================================
File Name: articles.py

===================================================================================
Description:
This script powers the Article Ideas Generator web app. It uses the Flask framework 
to serve a dynamic web application that interacts with the MediaWiki Action API. The 
app allows users to explore categories, subcategories, and missing articles (red links) 
on English Wikipedia.

===================================================================================
Purpose:
- Provides a Flask-based web interface for generating Wikipedia article ideas.
- Fetches and displays missing articles (red links) using the MediaWiki Action API.
- Dynamically navigates through categories and subcategories to explore topics.

===================================================================================
Usage:
1. Run the script using Python:
   `python articles.py`

2. Access the web app in a browser at:
   `http://127.0.0.1:5000/`

3. Explore top-level categories, subcategories, and red links dynamically.

Dependencies:
- Flask: For building the web app.
- Requests: For making HTTP requests to the MediaWiki Action API.

===================================================================================
Key Components:
1. **Global Variables**:
   - `SESSION`: A persistent session object for making HTTP requests.
   - `API_ENDPOINT`: The base URL for the MediaWiki Action API.
   - `PAGE`: A global dictionary that stores the current state of the app (e.g., current page name and type).

2. **Flask Routes**:
   - `/`: Handles both GET and POST requests for navigating categories and subcategories.

3. **Functions**:
   - `index()`: Main route handler that manages user interactions and renders the web app.
   - `get_page_sections(page)`: Fetches the top-level sections of a specified Wikipedia page.
   - `get_red_links(title)`: Retrieves the titles of missing articles (red links) from a specified Wikipedia page.

4. **Jinja2 Templates**:
   - `articles.html`: The dynamic HTML template used to render the app’s UI.

===================================================================================
Implementation Details:
1. **Initialization**:
   - The Flask app (`APP`) is initialized with default configurations.
   - A persistent `SESSION` object is created to minimize overhead during repeated API calls.

2. **API Interaction**:
   - `get_page_sections(page)`: Uses the "parse" API module to retrieve and parse top-level sections.
   - `get_red_links(title)`: Uses the "query" API module with the "links" generator to fetch red links.

3. **Dynamic Navigation**:
   - User interactions via POST requests update the `PAGE` dictionary, which drives navigation between categories and subcategories.

4. **Error Handling**:
   - Functions handle API errors gracefully by returning empty results if necessary.

5. **Development Server**:
   - Runs on `http://127.0.0.1:5000` using Flask's built-in development server.

===================================================================================
Key Points, Ideas, and Concepts:
1. **Dynamic Web App**:
   - The app dynamically renders content based on user input and API responses.

2. **API-Driven Navigation**:
   - Leverages the MediaWiki Action API to fetch structured data from Wikipedia.

3. **Scalability**:
   - Modular design separates API interaction, business logic, and front-end rendering, making the app easy to extend.

4. **Error Resilience**:
   - Handles API errors and empty responses to ensure a smooth user experience.

5. **User-Centric Design**:
   - Simplifies navigation and exploration of missing articles on Wikipedia.

===================================================================================
Notes:
1. Ensure that Flask and Requests libraries are installed:
   - `pip install flask requests`

2. For production deployment:
   - Use a WSGI server like Gunicorn or Waitress instead of Flask's development server.

3. The API requests are limited to 20 links per query. This can be adjusted based on app requirements.

4. The app assumes the availability of a "Wikipedia:Requested_articles" page for top-level navigation.

5. Customize the `articles.html` template for better UI/UX or additional functionality.

===================================================================================
"""

from flask import Flask, request, render_template  # Flask for web app and templates
import requests  # For making HTTP requests to MediaWiki API

# Initialize the Flask app
APP = Flask(__name__)

# Create a session for HTTP requests to Wikipedia API
SESSION = requests.Session()

# Base API endpoint for MediaWiki API
API_ENDPOINT = 'https://en.wikipedia.org/w/api.php'

# Global dictionary to store the current page's state
PAGE = {}


@APP.route('/', methods=['GET', 'POST'])
def index():
    """
    Displays the index page at '/'.
    Handles GET and POST requests for category and subcategory selections.
    """
    global PAGE  # Access the global PAGE variable to manage state
    results = []  # Initialize an empty list for results

    if request.method == 'POST':  # Handle POST requests
        if 'category' in request.form:  # If a category is selected
            # Update the PAGE name and type for the selected category
            PAGE['name'] += '/' + request.form.to_dict()['category']
            PAGE['type'] = 'subcategory'
            # Fetch subsections for the selected category
            results = get_page_sections(PAGE['name'])
        elif 'subcategory' in request.form:  # If a subcategory is selected
            # Update the PAGE name and type for the selected subcategory
            PAGE['name'] += '#' + request.form.to_dict()['subcategory']
            PAGE['type'] = 'links'
            # Fetch red links (missing articles) for the subcategory
            results = get_red_links(PAGE['name'])
    else:  # Handle GET requests
        # Set the initial PAGE state to Wikipedia's requested articles page
        PAGE = {'name': 'Wikipedia:Requested_articles', 'type': 'category'}
        # Fetch top-level sections from the initial page
        results = get_page_sections(PAGE['name'])

    # Render the HTML template with results and page type
    return render_template(
        "articles.html",
        results=results,
        pagetype=PAGE['type']
    )


def get_page_sections(page):
    """
    Fetches the top-level sections of a Wikipedia page using MediaWiki API.

    :param page: The name of the Wikipedia page to query.
    :return: List of top-level section titles.
    """
    params = {
        "action": "parse",  # Use the "parse" API module
        "page": page,       # The name of the page to parse
        "prop": "sections", # Retrieve section data
        "format": "json"    # Request data in JSON format
    }

    # Make a GET request to the API endpoint with the specified parameters
    res = SESSION.get(url=API_ENDPOINT, params=params)
    data = res.json()  # Parse the JSON response

    # If there's an error in the response, return an empty list
    if 'error' in data:
        return []

    # Extract sections from the response if available
    parsed_sections = data.get('parse', {}).get('sections', [])
    # Return only the top-level sections (toclevel 1)
    return [section['line'] for section in parsed_sections if section['toclevel'] == 1]


def get_red_links(title):
    """
    Fetches the missing links (red links) from a Wikipedia page using MediaWiki API.

    :param title: The title of the Wikipedia page to query.
    :return: List of missing article titles (red links).
    """
    params = {
        "action": "query",    # Use the "query" API module
        "titles": title,      # The title of the page to query
        "generator": "links", # Retrieve links from the page
        "gpllimit": 20,       # Limit the number of links to 20
        "format": "json"      # Request data in JSON format
    }

    # Make a GET request to the API endpoint with the specified parameters
    res = SESSION.get(url=API_ENDPOINT, params=params)
    data = res.json()  # Parse the JSON response

    # Extract pages from the response if available
    pages = data.get('query', {}).get('pages', {})
    # Return titles of missing pages (red links)
    return [page['title'] for page in pages.values() if 'missing' in page]


if __name__ == '__main__':
    """
    Main entry point of the script. Starts the Flask web server.
    """
    # Run the Flask development server
    APP.run(host='127.0.0.1', port=5000, debug=True)
