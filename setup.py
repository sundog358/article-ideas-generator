from setuptools import setup

setup(
    name="article-ideas-generator",
    version="0.1.0",
    description="A Flask-based app for generating Wikipedia article ideas",
    py_modules=["articles"],  # Specify the Python file without the `.py` extension
    install_requires=["flask", "requests"],  # Add your dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
