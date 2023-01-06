from poljske_metode import  rastav_naSlova
fonemi = {
'V' : ('a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y'),
'C' : { 'G' : ('j', 'ł'),
        'L' : ('l', 'r'),
        'O' : ('p', 't', 'k', 'b', 'd', 'g', 'q', 'x'),
        'F' : ('dz', 'dż', 'f', 'cz', 'c', 'ć', 'dź', 'z', 'ź', 'ż', 'w', 'h', 'v'),
        'S' : ('ś', 's', 'sz'),
        'N' :  ('n', 'ń', 'm'),
      },
}
iznimke = {'VCCV' : {'VOCV' : 'V-OCV',
                     'VFCV' : 'V-FCV',
                     'VSCV' : 'V-SCV', #osim ako je C=S
                     'VCGV' : 'V-CGV'},
           'VCCCV' : {'VOOCV' : 'V-OOCV',
                      'VFFGV' : 'V-FFGV'}}
pravila = {'VV' : 'V-V',
           'VCV' : 'V-CV',
           'VCCV' : 'VC-CV',
           'VCCCV' : 'VC-CCV',
           'VCCCCV' : 'VC-CCCV',
           'VCCCCCV' : 'VCC-CCCV',
           'VCCCCCCV' : 'VCC-CCCCV'}

def main():
    word = input().lower()
    slova = rastav_naSlova(word)
    slog = []
    kandidati = []
    v_count = 0
    for i, sl in enumerate(slova):
        slog += sl
        if sl in fonemi['V']:
            v_count += 1
        if v_count == 2 or i == len(slova)-1:
            v_count = 0
            kandidati.append(slog)
            slog = []
            v_count = 0
        
    print(kandidati)
    #for x in CV:print(x,end="")
    

main()

