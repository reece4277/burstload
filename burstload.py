import threading
import requests
import random
import time
import argparse
from datetime import datetime

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X)"
]

def send_request(url, timeout, log):
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "*/*",
        "Connection": "keep-alive"
    }
    try:
        start = time.time()
        response = requests.get(url, headers=headers, timeout=timeout)
        latency = round(time.time() - start, 3)
        log_entry = f"[{datetime.now()}] {response.status_code} - {latency}s"
        print(log_entry)
        if log:
            with open(log, "a") as f:
                f.write(log_entry + "\n")
    except requests.RequestException as e:
        error_entry = f"[{datetime.now()}] ERROR - {str(e)}"
        print(error_entry)
        if log:
            with open(log, "a") as f:
                f.write(error_entry + "\n")

def worker(url, delay, timeout, log):
    while True:
        send_request(url, timeout, log)
        if delay > 0:
            time.sleep(delay)

def main():
    parser = argparse.ArgumentParser(description="BurstLoad v4.1 – High-Concurrency Web Stress Simulator")
    parser.add_argument("url", help="Target URL")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Number of concurrent threads")
    parser.add_argument("-d", "--delay", type=float, default=0, help="Delay between requests (per thread)")
    parser.add_argument("--timeout", type=int, default=5, help="Request timeout in seconds")
    parser.add_argument("--log", type=str, help="Optional log file")
    args = parser.parse_args()

    print(f"Starting BurstLoad on {args.url} with {args.threads} threads...")
    for _ in range(args.threads):
        thread = threading.Thread(target=worker, args=(args.url, args.delay, args.timeout, args.log))
        thread.daemon = True
        thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Interrupted by user. Exiting...")

if __name__ == "__main__":
    main()
# TODO: Add CLI support
# Added User-Agent randomisation
