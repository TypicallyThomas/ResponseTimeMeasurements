import requests
import time

TIMEOUT = 10
TOTAL_ATTEMPTS = 20

total_time = 0

for i in range(TOTAL_ATTEMPTS):
  response = requests.get("https://primevideo.com/")
  total_time += response.elapsed.total_seconds()
  output = f"Request {i + 1}, {response.elapsed.total_seconds()}"
  average = f"{i + 1} Average seconds response time: {total_time / (i + 1):.4f}"
  print(average, end="\r")
  with open("output.txt", "a") as file:
    file.write(output + "\n")
  time.sleep(TIMEOUT)
