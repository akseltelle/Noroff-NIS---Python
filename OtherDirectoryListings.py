import os
from pathlib import Path

entries = os.listdir("C:\\Users\\Python\\Desktop\\Noroff-NIS---Python")
for entry in entries:
    print(entry)
print()

entries = os.scandir("C:\\Users\\Python\\Desktop\\Noroff-NIS---Python")
for entry in entries:
    print(entry)
print()

entries = Path("C:\\Users\\Python\\Desktop\\Noroff-NIS---Python")
for entry in entries.iterdir():
    print(entry)
print()
