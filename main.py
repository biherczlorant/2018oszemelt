import string
data = []
sorcnt = -1
paros = 0
paratlan = -1
with open('kerites.txt', 'r') as f:
    for line in f:
        split = line.strip().split(' ')
        if int(split[0]) == 0:
            paros+=2
        else:
            paratlan+=2
        linedata = {
            'pp': 'páros' if int(split[0])==0 else 'páratlan',
            'tsz': int(split[1]),
            'szin': split[2],
            'hazszam': paros if int(split[0]) == 0 else paratlan
        }
        data.append(linedata)
# 2. feladat
print(f'2. feladat\nAz eladott telkek száma: {data.__len__()}')
# 3. feladat
paroscnt = 0
paratlancnt = -1
for i in data:
    if i['pp'] == 'páros':
        paroscnt += 2
    else:
        paratlancnt += 2
print(f'3. feladat\nA {data[data.__len__()-1]["pp"]} oldalon adték el az utolsó telket.\nAz utolsó telek házszáma: '
      f'{data[data.__len__()-1]["hazszam"]}')
# 4. feladat
paratlanszinekcnt = 1
szinekhaz = []
for i in data:
    if i['pp'] == 'páratlan':
        szinekhaz.append(i['szin'])
for hazszin in szinekhaz:
    paratlanszinekcnt+=1
    # print(f"{szinekhaz[paratlanszinekcnt]} {szinekhaz[paratlanszinekcnt-1]}")
    if hazszin == szinekhaz[paratlanszinekcnt-1] and hazszin != '#' and hazszin != ':':
            print(f"4. feladat\nA szomszédossal egyezik a kerítés színe: {paratlanszinekcnt*2-3}")
            break
# 5. feladat
szinekhaz = []
lehetsegeszsinek = string.ascii_uppercase
print("5. feladat")
hazszambeker = int(input("Adjon meg egy házszámot!"))
for i in data:
    if i["hazszam"] == hazszambeker-2 or i["hazszam"] == hazszambeker+2:
        szinekhaz.append(i["szin"])
        szinekhaz.append(data[data.index(i) - 2]["szin"])
    if hazszambeker == i["hazszam"]:
        szinekhaz.append(i["szin"])
        for j in lehetsegeszsinek:
            if j not in szinekhaz:
                print(f"A kerítés színe / állapota: {i['szin']}\nEgy lehetséges festési szín: {j}")
                break
