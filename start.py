from poljske_metode import *

with open('tekst.txt', 'r') as file:
    for redak in file:
        for rijec in redak.strip().split(' '):
            if redak != '\n':
                print(foo(rastav_naSlova(rijec.lower())) )

