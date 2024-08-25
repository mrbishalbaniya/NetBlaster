# NetBlaster

NetBlaster is a Python script designed to send multiple HTTP requests concurrently using multithreading. It supports both GET and POST requests, allowing users to specify the target URL, request method, payload data, and the number of parallel requests to send.

## Features

- Sends concurrent HTTP GET and POST requests.
- Handles HTTP response codes such as 429 (throttling) and 500 (server errors).
- Configurable number of parallel requests.
- Option to specify payload data for POST requests.

## Installation

Ensure you have Python and the `requests` library installed:

```bash
pip install requests


Usage
Run the script from the command line with the following options:

bash
Copy code
python NetBlaster.py -u <URL> [-p] [-d <DATA>] [-c <COUNT>]
Command-Line Arguments
-u, --url (required): The target URL for the requests.
-p, --post (optional): Indicates that the request should be a POST request.
-d, --data (optional): The payload data for POST requests.
-c, --count (optional): Number of parallel requests (default is 100).
Examples
Sending 100 GET Requests:

bash
Copy code
python NetBlaster.py -u "https://example.com" -c 100
Sending 50 POST Requests with Data:

bash
Copy code
python NetBlaster.py -u "https://example.com" -p -d "key1=value1&key2=value2" -c 50