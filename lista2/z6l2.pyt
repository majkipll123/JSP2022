
studenci=["Kasia", "Basia", "Marek", "Darek"]
studenci.append("Jozek")
print(studenci)
studenci.extend(["Anna", "Basia"])
print(studenci)
studenci.sort()
print(studenci)
print(studenci[3])
print(studenci[:2])
print(studenci[(len(studenci)-2):])
studenci.remove("Basia")
studenci.remove("Basia")
print(studenci)
print(len(studenci))
a=tuple(studenci)
print(a) 

