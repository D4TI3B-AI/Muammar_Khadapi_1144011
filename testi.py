graph = {'Bohorok': ['Kualanamu', 'Medan','sarijadi'],
             'Kualanamu': ['Medan',' Bohorok'],
             'Husaein': ['Bandung','Medan','Bohorok'],
             'pasteur': ['sarijadi','bohorok'],
             'sarijadi': ['Pasteur','bohorok'],
           
         }
def jalur_terpendek(graph, awal, tujuan, jalur=[]):
        jalur = jalur + [awal]
        if awal == tujuan:
            return jalur
        if not graph.has_key(awal):
            return None
        jalurpendek = None
        for node in graph[awal]:
            if node not in jalur:
                newjalur = jalur_terpendek(graph, node, tujuan, jalur)
                if newjalur:
                    if not jalurpendek or len(newjalur) < len(jalurpendek):
                        jalurpendek = newjalur
        return jalurpendek
print("Jalur Alternatif Ciwaruga Kabupaten Bandung")
print ("ciwaruga,sersan bajuri ,pinus raya,gegerkalong,cigugur")
print ("\n")
awal = raw_input("Masukan Awal : ")
tujuan = raw_input("Masukan Tujuan : ")
hasil = jalur_terpendek(graph, awal, tujuan, jalur=[])
print "Jalur Terpendek", hasil
