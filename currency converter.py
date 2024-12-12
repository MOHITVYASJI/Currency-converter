#Dollar -> 84.88 Indian Rupee
#Euro   -> 89.16 Indian Rupee
#Pound  -> 108.34 Indian Rupee
#Kuwaiti Dinar -> 275.93 Indian Rupee 
from unittest import case
def invalid():
    print("   ||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("   ||| Envalid Number!!","Please Select Correct     |||")
    print("   ||||||||||||||||||||||||||||||||||||||||||||||||||")

# print('||||||||||||||||||||||||||||||||||||||||||||||')
# print("||||   WELLCOME TO THE CURRENCY CONVERTER |||| ")
# print('||||||||||||||||||||||||||||||||||||||||||||||')

def welcome():
    print('||||||||||||||||||||||||||||||||||||||||||||||')
    print("||||   WELLCOME TO THE CURRENCY CONVERTER |||| ")
    print('||||||||||||||||||||||||||||||||||||||||||||||')

welcome()   
print("\n    Select : 1  for Dollar to Rupee\n")
print("    Select : 2  for Euro to Rupee\n")
print("    Select : 3  for Pound to Rupee\n")
print("    Select : 4  for Kuwaiti Dinar to Rupee\n")
print("    Select : 5  for Exist \n")
#dollar
def dollar():
    print(        "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print(        "||||                                                                ||||")
    dol=int(input("||||                    Enter How Many Dollar you have :            ||||"))
    Dollar=84.88
    print(        "||||                                                                ||||")
    print(        "||||                         ", Dollar*dol," Rupee" ,"                     ||||")
    print(        "||||                                                                ||||")
    print(        "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
#Euro
def euro():
    print(        "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print(        "||||                                                                ||||")
    eur=int(input("||||                Enter How Many Euro you have : "))
    Euro=89.16
    print(        "||||                                                                ||||")
    print("||||                ",Euro*eur," Rupee")
    print(        "||||                                                                ||||")
    print(        "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
#pound
def pound():
    print(        "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print(        "||||                                                                ||||")
    pou=int(input("||||                 Enter How Many Pound you have : "))
    Pound=108.34
    print(        "||||                                                                ||||")
    print("||||                     ",Pound*pou," Rupee")
    print(        "||||                                                                ||||")
    print(        "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
#Kuwaiti Dinar
def Kuwaiti_Dinar():
    print(        "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print(        "||||                                                                ||||")
    kud=int(input("||||          Enter How Many Kuwaiti Dinar you have : "))
    Kuwaiti_Dinar=275.93
    print(        "||||                                                                ||||")
    print("||||                  ",Kuwaiti_Dinar*kud," Rupee")
    print(        "||||                                                                ||||")
    print(        "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

print('"""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
x = int(input("  (((((((((((((((((*****SELECT*****))))))))))))))  => "))
print('"""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
# match = x:
# # if x is 0
#     case 1:
#         dollar()
#     case 2:
#         euro()
#     case 3:
#         pound()
#     case 4:
#         Kuwaiti_Dinar()
if x<5:
    if x==1:
       dollar()
    elif x==2:
        euro()
    elif x==3:
        pound()
    elif x==4:
        Kuwaiti_Dinar()
else:
    invalid()