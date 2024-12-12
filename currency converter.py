#Dollar -> 84.88 Indian Rupee
#Euro   -> 89.16 Indian Rupee
#Pound  -> 108.34 Indian Rupee
#Kuwaiti Dinar -> 275.93 Indian Rupee 
print('""""""""""""""""""""""""""""""""""')
print("WELLCOME TO THE CURRENCY CONVERTER")
print('""""""""""""""""""""""""""""""""""')
print("Select : 1  for Dollar to Rupee\n")

print("Select : 2  for Euro to Rupee\n")
print("Select : 3  for Pound\n")
print("Select : 4  for Kuwaiti Dinar\n")
print("Select : 5  for Exist ")
#dollar
def dollar():
    dol=int(input("Enter the value :"))
    Dollar=84.88
    print(Dollar*dol)
#Euro
def euro():
    eur=int(input("Enter the value :"))
    Euro=89.16
    print(Euro*eur)
#pound
def pound():
    pou=int(input("Enter the value :"))
    Pound=108.34
    print(Pound*pou)
#Kuwaiti Dinar
def Kuwaiti_Dinar():
    kud=int(input("Enter the value :"))
    Kuwaiti_Dinar=275.93
    print(Kuwaiti_Dinar*kud)

