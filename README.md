# 📝 Article Ideas Generator Web App

Welcome to the **Article Ideas Generator** web application! This Flask-based app uses the MediaWiki Action API to help you explore and discover article topics that are missing or underdeveloped on Wikipedia. 🌐

---

### ⚙️ Technical Specifications

The **Article Ideas Generator Web App** is built using a lightweight yet powerful technology stack to ensure smooth operation and extensibility. 🌟

- **Programming Language**: Python 3.8+
- **Framework**: Flask - A minimal and flexible backend framework for building web applications. 🌐
- **Data Retrieval**: MediaWiki Action API - Used for querying and fetching structured data from Wikipedia. 📡
- **Frontend Rendering**: Jinja2 Templates - For dynamic UI generation and seamless integration with Flask. 🎨
- **HTTP Requests**: Python's `requests` library for efficient and reliable API communication. 📬
- **Styling**: Simple and clean CSS, with optional customization for enhanced user experience. 💅
- **Application Hosting**: Runs on a local development server, accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/). 🖥️

This architecture ensures the app is lightweight, responsive, and easy to deploy or extend for future use cases. 🚀

## 🚀 Features

### 📑 Dynamic Section Exploration

- Fetches **top-level sections** from a Wikipedia page.
- Dynamically displays subsections based on user selection.

### 🔗 Missing Links Detection

- Identifies **red links** (missing articles) from selected sections.
- Provides a curated list of potential articles to create.

### 🔄 Interactive Workflow

- Easy-to-use UI for exploring categories and subcategories.
- Offers seamless navigation through different sections of Wikipedia.

---

## 🛠️ Technologies Used

- **Backend**: Flask - A lightweight web framework for Python.
- **API**: MediaWiki Action API for querying Wikipedia data.
- **Frontend**: HTML + Jinja templates for dynamic rendering.
- **Styling**: Minimal CSS for a clean and user-friendly interface.

---

## 🔧 Installation

### Prerequisites

1. Python 3.8 or higher.
2. Flask installed in your Python environment:

`pip install flask`

3. Requests library

`pip install requests`

### Setup:

1. Clone the repository

git clone https://github.com/sundog358/article-ideas-generator.git

2. Navigate to the project directory:

`cd article-ideas-generator`

3. Run the app:

`python articles.py`

4. Open your browser and go to:

http://127.0.0.1:5000/

# 🛠️ Usage

## 🚀 Start the App

- Open the app in your browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

http://127.0.0.1:5000/

## 📑 Explore Categories

- Select a category from the displayed list of Wikipedia sections.

## 🔍 Dive Deeper

- Explore subsections or view missing links (red links) for potential article topics.

## ✍️ Discover Ideas

- Use the suggestions to write new articles or expand existing content on Wikipedia.

---

# 🎯 Key Functionalities

## 📂 Page Sections

- Fetches and displays **top-level sections** from `Wikipedia:Requested_articles`.

## 📑 Subcategories

- Allows users to explore subsections dynamically.

## 🔗 Red Links Detection

- Identifies **missing links** on Wikipedia pages, enabling users to discover new article ideas.

---

# 📂 File Structure

- **`articles.py`**:

  - The main Flask app logic.
  - Handles routing, API calls, and user interactions.

- **`templates/articles.html`**:

  - Jinja2 template for rendering the UI dynamically.

- **`static/style.css`**:
  - Optional custom CSS file for styling.

---

# 🚀 Future Enhancements

## 🔍 Enhanced Search

- Add **faceted search** and filtering for better article discovery.

## 🤝 Collaboration Features

- Enable users to **save and share article ideas**.

## 🌍 Multi-language Support

- Extend functionality for **non-English Wikipedia editions**.

---

# 💻 Contributing

We welcome contributions to improve this app! Feel free to fork the repository, make changes, and submit a pull request. 🙌

---

# 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

# 🌟 Acknowledgments

Special thanks to the \*\*Wikimedia Found
