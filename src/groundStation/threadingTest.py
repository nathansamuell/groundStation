#imports
import concurrent.futures
import threading

previous = 0
lock = threading.Lock()
results = []

def sumPrevious() -> int:
    global previous
    with lock:
        previous += 1
        return(previous)

threads = []

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(sumPrevious) for _ in range (10)]
    
    for f in concurrent.futures.as_completed(results):
        print(f.result())


# for _ in range(10):
#     t = threading.Thread(target=sumPrevious)
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()

print(threads)
print(results)