import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easy_scrape",
    version="0.0.1",
    author="Sarthak Negi",
    author_email="sarthaknegi609@gmail.com",
    description="Helps in Scraping the Web",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/example-project",
    packages=setuptools.find_packages(),
    install_required=['requests','BeautifulSoup','selenium','pandas','webdriver'],
    classifiers=(
        "Development Status :: Alpha",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )
)