import argparse
import requests
import threading
import time

# Global state
request_count = 0
handled_messages = set()
request_lock = threading.Lock()

def log_message(message):
    """Log unique messages."""
    with request_lock:
        if message not in handled_messages:
            print(f"\n{message} after {request_count} requests")
            handled_messages.add(message)

def manage_response(status):
    """Handle various HTTP response codes."""
    global request_count
    with request_lock:
        request_count += 1
        print(f"\rTotal Requests Sent: {request_count}", end="")

    if status == 429:
        log_message("Throttling detected (429)")
    elif status == 500:
        log_message("Server error encountered (500)")

def perform_get(target_url):
    """Executes a GET request."""
    try:
        response = requests.get(target_url)
        manage_response(response.status_code)
    except requests.RequestException:
        pass

def perform_post(target_url, data_payload):
    """Executes a POST request."""
    try:
        response = requests.post(target_url, data=data_payload)
        manage_response(response.status_code)
    except requests.RequestException:
        pass

def main():
    parser = argparse.ArgumentParser(description="Multi-threaded HTTP request sender")
    parser.add_argument("-u", "--url", required=True, help="Target URL for requests")
    parser.add_argument("-p", "--post", action="store_true", help="Use POST instead of GET")
    parser.add_argument("-d", "--data", help="Payload for POST requests")
    parser.add_argument("-c", "--count", type=int, default=100, help="Number of parallel requests")
    args = parser.parse_args()

    threads = []
    for _ in range(args.count):
        if args.post:
            thread = threading.Thread(target=perform_post, args=(args.url, args.data))
        else:
            thread = threading.Thread(target=perform_get, args=(args.url,)
            )
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
