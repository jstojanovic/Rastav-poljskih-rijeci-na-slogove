from re import search

fonemi = {
'V' : ('a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y'),
'C' : ('G','L','O','F','S','N'),

'G' : ('j', 'ł'),
'L' : ('l', 'r'),
'O' : ('p', 't', 'k', 'b', 'd', 'g', 'q', 'x'),
'F' : ('dz', 'dż', 'f', 'cz', 'c', 'ć', 'dź', 'z', 'ź', 'ż', 'w', 'h', 'v'),
'S' : ('ś', 's', 'sz'),
'N' :  ('n', 'ń', 'm'),
}

iznimke = {
'VCCV' : {'VOCV' : 'V-OCV',
        'VFCV' : 'V-FCV',
        'VSCV' : 'V-SCV', #osim ako je C=S
        'VCGV' : 'V-CGV'},
'VCCCV' : {'VOOCV' : 'V-OOCV',
        'VFFGV' : 'V-FFGV'}}
pravila = {
'VV' : 'V-V',
'VCV' : 'V-CV',
'VCCV' : 'VC-CV',
'VCCCV' : 'VC-CCV',
'VCCCCV' : 'VC-CCCV',
'VCCCCCV' : 'VCC-CCCV',
'VCCCCCCV' : 'VCC-CCCCV'}

def VGLOFSN(slovo):
    if slovo in fonemi['V']:
        return 'V'
    elif slovo in fonemi['G']:
        return 'G'
    elif slovo in fonemi['L']:
        return 'L'
    elif slovo in fonemi['O']:
        return 'O'
    elif slovo in fonemi['F']:
        return 'F'
    elif slovo in fonemi['S']:
        return 'S'
    elif slovo in fonemi['N']:
        return 'N'
    else:
        return ''

def osnovni_oblik(slova):
    return map(VGLOFSN, slova)
   
def rastav_naSlova(rijec):
    """rastavlja rijec na slova ukljucujuci sz, cz, dz ..."""
    slova = [x for x in list(rijec) if x not in [',','.','!','?','-',':']]
    
    for i in range(len(rijec)):
        if i+1 < len(slova) and slova[i]+slova[i+1] == 'dz':
            slova[i : i+2] = [''.join(slova[i : i+2])]
        elif i+1 < len(slova) and slova[i]+slova[i+1] == 'dż':
            slova[i : i+2] = [''.join(slova[i : i+2])]
        elif i+1 < len(slova) and slova[i]+slova[i+1] == 'dź':
            slova[i : i+2] = [''.join(slova[i : i+2])]
        elif i+1 < len(slova) and slova[i]+slova[i+1] == 'sz':
            slova[i : i+2] = [''.join(slova[i : i+2])]
        elif i+1 < len(slova) and slova[i]+slova[i+1] == 'cz':
            slova[i : i+2] = [''.join(slova[i : i+2])]
    return slova


def rastav(rijec):
    pass
