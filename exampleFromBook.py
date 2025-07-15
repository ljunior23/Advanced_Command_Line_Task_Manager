from pathlib import Path

path = Path("data.txt")
content= path.read_text()
print(content)