def words_change(a):
    b = []
    for i in range(0,len(a)):
        b.append(str(a[i]))
    #print(b)


    sanlish = {'क':'ka','ख':"kha" , 'ग':"ga" ,'घ':'gha' ,'ङ':"nga" ,'च':"ca" ,'छ':"cha" ,'ज':"ja" ,'झ':"jha" ,'ञ':"ña" ,'ट': "Ṭa",'ठ':"Ṭha" ,'ड':"Ḍa" ,'ढ': "Ḍha",'ण':"Ṇa",
    'त':"ta" ,'थ':"t    ha" ,'द':"da" ,'ध':"dha", 'न':"na" ,'प':"pa" ,'फ':"pha" ,'ब':"ba" ,'भ':"bha" ,'म':"ma" ,'य':"ya" ,'र':"ra" ,'ल':"la" ,'व':"va" ,'श':"śa" ,'ष':"Ṣa" ,'स':"sa" ,'ह':"ha" ,'अ':"a" ,
    'आ':"ā" ,'इ':"i" ,'ई':"ī" ,'उ':"u" ,'ऊ':"ū" , 'ऋ':"ri" ,'ॠ':"rī" ,'ऌ':"li" ,"ॡ":"lī" ,'ए':"e" ,'ऐ':"ai" ,'ओ':"o" ,'औ':"au",'ा':"ā" ,'ि':"i" ,'ी':"ī" ,'ु':"u" ,'ू':'ū' ,
    'ृ':"ri"  ,'ॄ':"rī"  ,'ॢ':"li" ,'ॣ':"lī" ,'े':"e" ,'ै':"ai" ,
        'ो':"o" ,'ौ':"au" ,'०':"0" ,'१':"1" ,'२':"2" ,'३':"3" ,'४':"4" ,'५':"5" ,'६':"6" ,'७':"7" ,'८':"8",'९':"9"," ":" " }
    c = ""
    print('क'+'अ')
    for i in b:
        for j in sanlish:
            if i == j:
                c+=sanlish[j]


    return c

words_change('भवान्‌ कथमसि')