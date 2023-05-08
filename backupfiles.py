import requests
import re
import sys
import argparse
import concurrent.futures
from urllib.parse import urljoin
import random

# Create the argument parser
parser = argparse.ArgumentParser()

# Add an argument for the number of threads
parser.add_argument("-t","--threads", type=int, default=8, help="number of threads to use")

# Parse the command-line arguments
args = parser.parse_args()

# Set the list of extensions
extensions = [".gz",".tgz",".zip",".tar",".tar.gz",".csv",".doc",".docx",".xls",".xlsx",".sql",".7z",".rar",".dump.sql",".sql.tar.gz",".sql.zip",".bak",".bk",".backup",".bakup",".old",".tmp",".log",".db",".sql.bak",".zip.bak",".zip.old",".jar",".bz2",".war",".dll"]

# Set the User-Agent string
user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 Edge/16.16299",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
    ]

# Read the list of URLs from sys.stdin
urls = sys.stdin.readlines()

# Create a ThreadPoolExecutor with the specified number of threads
with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
    # Iterate over the URLs
    for url in urls:
        url = url.strip()  # remove leading and trailing whitespace

        # Use a regular expression to search for the domain name
        domain_name = re.search(r'(?:https?:\/\/)?(?:www\.)?([^\/]+)', url).group(1)

        # Iterate over the extensions
        for extension in extensions:
            # Construct the URL using the domain name and the extension
            domain = urljoin(url, domain_name + extension)

            # Set the headers with the User-Agent string
            headers = {"User-Agent": random.choice(user_agents)}

            try:
                # Submit the request to the ThreadPoolExecutor with the headers
                future = executor.submit(requests.get, domain, headers=headers)
                # Get the result of the request and print it
                result = future.result()
                print(domain, [result.status_code])
            except requests.exceptions.SSLError as e:
                pass
            except KeyboardInterrupt:
                exit(0)