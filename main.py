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

# if __name__ == '__main__':
#     createFilesFolder("documents/report.pdf", "documents/notes.txt", "documents/notes.txt", "images/profile.png", "images/logo.jpg", "projects/project1/main.py", "projects/project2/app.py")