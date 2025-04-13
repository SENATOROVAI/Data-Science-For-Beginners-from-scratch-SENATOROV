import time
    
start_time = time.time()
total = 0
for i in range(1, 10000000):
    total += i
end_time = time.time()

print("Result:", total)
print("Execution time:", end_time - start_time, "seconds")