#Command-line arguments in Python
import sys
print("Command-line arguments:")
for arg in sys.argv:
    print(arg)
print(f"Number of arguments: {len(sys.argv) - 1}")