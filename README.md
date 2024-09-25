# API Test Framework for Wishlist APIs

This framework is designed to test the Wishlist API endpoints.

## Prerequisites

- Python 3.10+
- pip

## Setup

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run all tests:

    ```bash
    pytest tests --html=report.html --self-contained-html
    ```

3. Generate Allure reports:

    ```bash
    pytest tests --alluredir=allure-results
    allure serve allure-results
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
