import urllib.request
import threading

def testing():
    url = "YOUR_INTENDED_WEB_URL"
    
    try:
        with urllib.request.urlopen(url) as response:
            print(f'Response status code: {response.getcode()}')
    except Exception as e:
        print(f'Error: {e}')

def main():
    num_threads = 100000
    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=testing)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
