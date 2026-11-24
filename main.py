"""How Many Tabs Do You Have Open? — entry for make.fun.

Writes one number to /output/entry.txt.
The entry is one number in digits and nothing else: an honest count of open browser tabs.
"""
import os

LINE = "47"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
