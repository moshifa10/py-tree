from pathlib import Path
import argparse



'''
    Idea 

    python tree.py --input <Path> 


    python tree.py --input .

    py-tree
        documents
            reports.pdf
            invoice/
                invoices.pdf

    
                
    



'''


def registerArgs():
    parser = argparse.ArgumentParser(description="Welcome to Njabs File tree Managements")
    parser.add_argument("-i", "--input", help="The file you want to see the tree")
    parser.add_argument("-o", "--output", help="Output file ")
    parser.add_argument("-n", "--name", help="Name of the project")
    args = parser.parse_args()
    return None if not args else args

def main(args : argparse.Namespace):
    tree = {}
    path = Path(args.input) if args.input  else Path.cwd()


    if not path.exists():
        print(f"{args.input} <- this path is not existing Please type existing path")
        return

    if args:
        if args.name:
            tree['name'] = args.name

    


    




    # folder =
    print(path)

def getFiles(path: Path) -> list[Path]:
    return [i for i in path.iterdir() if i.is_dir() and i.name != ".git"]

def getFolder(path: Path) -> list[Path]:
    return [i for i in path.iterdir() if i.is_dir() and i.name != ".git"]

    



if __name__ == "__main__":
    main(registerArgs())

