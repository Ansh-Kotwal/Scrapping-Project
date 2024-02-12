# Daily Data Scraper

This project is designed to automate the process of scraping daily data from a specific website using Python. The main components of the project include:

- **automation.py**: This module utilizes the Selenium library to interact with a website and retrieve the URL for the daily data. It is responsible for navigating the website, handling authentication if required, and extracting the relevant URL.

- **dailyDataScraper.py**: This module uses the URL obtained from `automation.py` to scrape daily data from the website. It leverages the BeautifulSoup library for parsing HTML and extracting the desired information from the web pages.

## Prerequisites

Before running the program, ensure that you have the following dependencies installed:

- Python 3.x
- Selenium
- BeautifulSoup

You can install the required Python packages using the following command:

```bash
pip install selenium beautifulsoup4
```

Additionally, make sure you have the appropriate web driver for Selenium (e.g., ChromeDriver) installed and accessible in your system's PATH.

## Usage

To run the daily data scraper, execute the following command:

```bash
python dailyDataScraper.py
```

This command will trigger the entire process, starting from navigating the website with `automation.py` to scraping data with `dailyDataScraper.py`.

## Configuration

You may need to configure the URLs and other settings within the `automation.py` and `dailyDataScraper.py` files to match the specifics of the website you are targeting. Ensure that the web driver path in `automation.py` points to the correct location on your machine.

## Issues and Contributions

If you encounter any issues or have suggestions for improvement, feel free to open an issue on the GitHub repository. Contributions are welcome through pull requests.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code as per your requirements.

Happy scraping!