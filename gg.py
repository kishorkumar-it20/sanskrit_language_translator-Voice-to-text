prons = {'क': 'ka', 'ख': "kha", 'ग': "ga", 'घ': 'gha', 'ङ': "nga", 'च': "ca", 'छ': "cha", 'ज': "ja", 'झ': "jha",
         'ञ': "ña", 'ट': "Ṭa", 'ठ': "Ṭha", 'ड': "Ḍa", 'ढ': "Ḍha", 'ण': "Ṇa",
         'त': "ta", 'थ': "tha", 'द': "da", 'ध': "dha", 'न': "na", 'प': "pa", 'फ': "pha", 'ब': "ba", 'भ': "bha",
         'म': "ma", 'य': "ya", 'र': "ra", 'ल': "la", 'व': "va", 'श': "śa", 'ष': "Ṣa", 'स': "sa", 'ह': "ha"}
kk=0
for i in prons:
    kk += 1
    print("'{}' : '{}',".format(prons[i],i),end= ' ')
    if kk == 33:
        kk = 0
        print("\n")