prons = {'క': 'क', 'ఖ': 'ख', 'సి': 'ग', 'ఘ': 'घ', 'ఇ': 'इ', 'చ': 'छ', 'జ': 'ज', 'ఝ': 'झ', 'ఞ': 'ञ', 'ట': 'ट', 'వ': 'व', 'డ': 'ड', 'ఢ': 'ढ', 'ణ': 'ण', 'టా': 'त', 'థ': 'थ', 'ద': 'द', 'ధ': 'ध', 'ప': 'प', 'ఫ': 'फ', 'బ': 'ब', 'భ': 'भ', 'మ': 'म', 'య': 'य', 'ర': 'र', 'ఎల్': 'ल', 'శ': 'श', 'ష': 'ष', 'లు': 'स', 'హా': 'ह', 'అ ': 'अ', 'ఆ': 'आ', 'ఈ': 'ई', 'ఉ': 'उ', 'ఊ': 'ऊ', 'ఋ': 'ऋ',
    'ౠ': 'ॠ', 'ఌ': 'ऌ', 'ౡ': 'ॡ', 'ఎ': 'ए', 'ఐ': 'ऐ', 'ఒ': 'ओ', 'ఔ': 'औ', 'ా': 'ा', 'ి': 'ि', 'ీ': 'ी', 'ు': 'ु', 'ూ': 'ू', 'ృ': 'ृ', 'ౄ': 'ॄ', 'ౢ': 'ॢ', 'ౣ': 'ॣ', 'ె': 'े', 'ై': 'ै', ' ం': 'ो', ' ః ': 'ौ', '0': '०', '1': '१', '2': '२', '3': '३', '4': '४', '5': '५', '6': '६', '7': '७', '8': '८', '9': '९', ' ': ' ',
    'క' : 'क', 'ఖ' : 'ख', 'సి' : 'ग', 'ఘ' : 'घ', 'ఇ' : 'ङ', 'చ' : 'च', 'చ' : 'छ', 'జ' : 'ज', 'ఝ' : 'झ', 'ఞ' : 'ञ', 'ట' : 'ट', 'వ' : 'ठ', 'డ' : 'ड', 'ఢ' : 'ढ', 'ణ' : 'ण', 'టా' : 'त', 'థ' : 'थ', 'ద' : 'द', 'ధ' : 'ध', 'ప' : 'न', 'ప' : 'प', 'ఫ' : 'फ', 'బ' : 'ब', 'భ' : 'भ', 'మ' : 'म', 'య' : 'य', 'ర' : 'र', 'ఎల్' : 'ल', 'వ' : 'व', 'శ' : 'श', 'ష' : 'ष', 'లు' : 'स', 'హా' : 'ह',

    'అ ' : 'अ', 'ఆ' : 'आ', 'ఇ' : 'इ', 'ఈ' : 'ई', 'ఉ' : 'उ', 'ఊ' : 'ऊ', 'ఋ' : 'ऋ', 'ౠ' : 'ॠ', 'ఌ' : 'ऌ', 'ౡ' : 'ॡ', 'ఎ' : 'ए', 'ఐ' : 'ऐ', 'ఒ' : 'ओ', 'ఔ' : 'औ', 'ా' : 'ा', 'ి' : 'ि', 'ీ' : 'ी', 'ు' : 'ु', 'ూ' : 'ू', 'ృ' : 'ृ', 'ౄ' : 'ॄ', 'ౢ' : 'ॢ', 'ౣ' : 'ॣ', 'ె' : 'े', 'ై' : 'ै', ' ం' : 'ो', ' ః ' : 'ौ', '0' : '०', '1' : '१', '2' : '२', '3' : '३', '4' : '४', '5' : '५',

    '6' : '६', '7' : '७', '8' : '८', '9' : '९', ' ' : ' '}



cc = " "
def lib(a):
    ss = a
    ll = ss.split()
    print(ll)
    for i in ll:
        s = i
        cc = ""
        c = len(s)
        for j in i:
            cc += prons[j]
        c+= " "
    return cc
