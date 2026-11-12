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
    args = parser.parse_args()
    return None if not args else args


args = registerArgs()

path = Path(".") if args == None else Path(args.input)




