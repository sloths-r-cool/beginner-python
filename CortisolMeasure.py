import time
import random

print("Measuring cortisol...")

# wait 10 seconds
time.sleep(10)

# generate random cortisol level
cortisol_level = random.randint(-10, 100)

print("Cortisol level:", cortisol_level, "%.")