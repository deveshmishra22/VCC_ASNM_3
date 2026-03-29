import psutil
import requests
import time

# CONFIGURATION
CLOUD_URL = "http://34.131.188.242/process"
THRESHOLD = 75  # CPU threshold %

# Local task
def heavy_task(x):
    return x * x

print(" Starting CPU Monitor...")

while True:
    cpu = psutil.cpu_percent(interval=2)
    print(f"\nCPU Usage: {cpu}%")

    if cpu < THRESHOLD:
        print(" Running locally")
        result = heavy_task(10)
        print("Result:", result)
    else:
        print(" Offloading to cloud")
        try:
            response = requests.post(
                CLOUD_URL,
                json={"data": 10},
                timeout=5
            )
            print("Cloud Result:", response.json())
        except Exception as e:
            print(" Cloud not reachable:", e)

    time.sleep(3)