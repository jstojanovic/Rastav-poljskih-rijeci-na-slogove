from poljske_metode import rastav_naSlova

with open('tekst.txt', 'r') as file:
    for redak in file:
        for rijec in redak.strip().split(' '):
            if redak != '\n':
                print(rastav_naSlova(rijec.lower()))

