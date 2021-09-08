from concurrent import futures

import requests


def do_request(num):
    print(f'request {num}')
    response = requests.get('http://localhost:8000/polls/')
    print(f'response {num}: {response}')


with futures.ThreadPoolExecutor(max_workers=100) as executor:
    for i in range(0,1000):
        executor.submit(do_request, i)



