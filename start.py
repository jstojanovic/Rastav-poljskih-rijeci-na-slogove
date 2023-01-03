from poljske_metode import uzorak

with open('tekst.txt', 'r') as file:
    for redak in file:
        for rijec in redak.strip().split(' '):
            if redak != '\n':
                print(uzorak(rijec.lower()))

