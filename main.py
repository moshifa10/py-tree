from pathlib import Path


def createFilesFolder(*args):

    for pth in args:
        p = Path(pth)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.touch(exist_ok=True)
    print("Successfully created")


file =  Path("documents/report.pdf")

# print(file.name)
# print(file.suffix)
# print(file.stem)
# print(file.parent)
# print(file.absolute())

'''

Activity 2: Check filesystem existence
Difficulty: Easy


Write a program that checks whether the following paths exist:
- documents/
- documents/report.pdf
- documents/missing.pdf
For each path, print whether it exists and whether it is a file or directory.

'''


file2 = Path("documents/")

file3 = Path("documents/missing.pdf")
file4 = Path("documents/report.pdf")

# print(file2.exists())
# print(file3.exists())
# print(file4.exists())
# print(file2.is_file(), file2.is_dir())
# print(file3.is_file(), file3.is_dir())
# print(file4.is_file(), file4.is_dir())



'''

Activity 3: List directory contents
Difficulty: Easy


Write a program that lists everything inside pathlib-practice/.
'''


curr = Path.cwd()
save = [j for i in curr.iterdir() if i.name == "documents" for j in i.iterdir()]

print(save)
'''Activity 4: Find files by extension
Difficulty: Intermediate


Find all PDF files inside the documents/ directory.

Then:
1. Find all .py files inside projects/.
2. Find all .jpg files inside images/.
3. Count how many PDF files exist.'''

globsPDF = [i.glob("*.pdf", case_sensitive=False) for i in curr.iterdir() if i.name == "documents" ]
print("\n\n\nPDF")
for idx, i in enumerate(globsPDF, start=1):
    print(f"{idx}. {list(i)[0].name}")
print(f"Length of the pdf files in documents folder: {len(globsPDF)}" )


globsJPG = [i.glob("*.jpg", case_sensitive=False) for i in curr.iterdir() if i.name == "images" ]

print("\n\n\nJPG")
for idx, i in enumerate(globsJPG, start=1):
    print(f"{idx}. {list(i)[0].name}")

print(f"Length of jpg: {len(globsJPG)}")


globsPY = [j.glob("*.py", case_sensitive=False) for i in curr.iterdir() if i.name == "projects" for j in i.iterdir() ]

print("\n\n\nPYTHON")
print()
for idx, i in enumerate(globsPY, start=1):
    print(f"{idx}. {list(i)[0].name}")

print(f"Length of py files: {len(globsPY)}")


# if __name__ == '__main__':
#     createFilesFolder("documents/report.pdf", "documents/notes.txt", "documents/notes.txt", "images/profile.png", "images/logo.jpg", "projects/project1/main.py", "projects/project2/app.py")