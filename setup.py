from setuptools import setup, find_packages

setup(
    name="web-scraper",
    version="0.1.0",
    description="A simple Python web scraper",
    author="hopelee8964",
    packages=find_packages(),
    py_modules=["scraper"],
    install_requires=[
        "requests",
        "beautifulsoup4"
    ],
    entry_points={
        'console_scripts': [
            'web-scraper=scraper:fetch_title',
        ],
    },
)
