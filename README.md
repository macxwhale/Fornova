﻿```markdown
# Fornova Web Scraping

## Instructions

To get started with Fornova's web scraping scripts, follow the steps below:

1. Navigate to the root directory of the project.

2. Run the following command to install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   This will install the necessary Python packages for the project.

## Web Scraping Scripts

### 1. `webscrapping_using_selenium.py`

This script utilizes Selenium for interacting with dynamic web pages. Selenium is a powerful tool for automating browser actions, making it suitable for scenarios where web pages rely on JavaScript or other dynamic elements.

#### Usage:

```bash
python webscrapping_using_selenium.py
```

### 2. `webscrapping_using_requests.py`

This script employs the `requests` library for interacting with web pages that return JSON. It ensures that the data is formatted according to GitHub guidelines.

#### Usage:

```bash
python webscrapping_using_requests.py
```

Feel free to explore and modify these scripts based on your specific requirements. If you encounter any issues or have questions, please refer to the documentation or reach out to the project maintainers.

## Important Note

Make sure to review the documentation for each script to understand the specific functionality and any additional configurations that may be required for your use case.

```

## Challenges
Getting data in collapsible HTML using selenium