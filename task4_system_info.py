import platform
import os

print("===== System Information =====")

print("\nOperating System:")
print(platform.system(), platform.release())

print("\nCurrent User:")
print(os.getlogin())

print("\nProcessor Info:")
print(platform.processor())
