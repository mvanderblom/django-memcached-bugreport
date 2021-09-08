import os
from concurrent import futures

import requests


server_host = os.getenv('SERVER_HOST', 'localhost')
server_port = os.getenv('SERVER_PORT', '8000')


def do_request(num):
    print(f'request {num}')
    response = requests.get(f'http://{server_host}:{server_port}/polls/')
    print(f'response {num}: {response}')


if __name__ == '__main__':
    with futures.ThreadPoolExecutor(max_workers=100) as executor:
        for i in range(0, 1000):
            executor.submit(do_request, i)
