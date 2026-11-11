from pathlib import Path


file =  Path("documents/report.pdf")

print(file.name)
print(file.suffix)
print(file.stem)
print(file.parent)
print(file.absolute())

