import sys
import os

print("--- DIAGNOSTIC INFO ---")
print(f"Current Python Executable: {sys.executable}")
print(f"Virtual Env Path (from env): {os.environ.get('VIRTUAL_ENV', 'None')}")
print(f"Python Path (sys.path):")
for path in sys.path:
    print(f"  - {path}")
print("-----------------------")

try:
    import IPython
    print("✅ Success! IPython imported perfectly.")
except ImportError:
    print("❌ Fail! IPython could not be found by this Python instance.")