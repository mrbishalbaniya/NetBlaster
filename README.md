## NetBlaster
NetBlaster is a powerful Python script designed to send multiple HTTP requests concurrently using multithreading. It supports both GET and POST methods, enabling you to specify the target URL, request method, payload data, and the number of parallel requests.

## 🚀 Features
Concurrent Requests: Efficiently sends multiple HTTP GET and POST requests simultaneously.
Response Handling: Manages HTTP response codes like 429 (throttling) and 500 (server errors).
Customizable Parallelism: Configure the number of parallel requests.
Payload Support: Easily include data payloads for POST requests.

## 💻 Installation
To get started, you need Python 3 and the requests library. Install the required dependency using pip:

```bash
pip install requests
```

## 📜 Usage
Run the script from the command line with the following options:

```python
python NetBlaster.py -u <URL> [-p] [-d <DATA>] [-c <COUNT>]
```

## Command-Line Arguments ```
-u, --url (required): The target URL for the requests.
-p, --post (optional): Use this flag to make POST requests instead of GET.
-d, --data (optional): Specify the payload data for POST requests.
-c, --count (optional): Define the number of parallel requests (default is 100)
```

## Examples
Sending 100 GET Requests:

```python
python NetBlaster.py -u "https://example.com" -c 100
```

Sending 50 POST Requests with Data:

```python
python NetBlaster.py -u "https://example.com" -p -d "key1=value1&key2=value2" -c 50
```
