from random import randrange

print("Please answer the following questions without any Space! ")
firstname = input("Firstname: ")
lastname = input("Lastname: ")
favDate = input("favourite Date DD.MM.YYYY")
country = input("Country: ")
city = input("City: ")
zipCode = input("Zip-Code:")
favSport = input("Favourite Sport: ")
pet = input("favPet")
specChars = "?!#"
#format Data correctly
favDate = favDate[0] + favDate[1] + favDate[3] + favDate[4] + favDate[6]+ favDate[7] + favDate[8]+favDate[9]
# password generieren
szFN = len(firstname)
szLN = len(lastname)
szCounty = len(country)
szCity = len(city)
szZipCode = len(zipCode)
szFavSport = len(favSport)
szPet = len(pet)
secretNames = firstname[randrange(szFN)] + firstname[randrange(szFN)] + \
              lastname[randrange(szLN)] + lastname[randrange(szLN)] + \
              favDate[randrange(7)] + favDate[randrange(7)] + \
              country[randrange(szCounty)] + country[randrange(szCounty)] + \
              city[randrange(szCity)] + city[randrange(szCity)] + \
              specChars[randrange(2)] + \
              zipCode[randrange(szZipCode)] + zipCode[randrange(szZipCode)] + \
              favSport[randrange(szFavSport)] + favSport[randrange(szFavSport)] + \
              pet[randrange(szPet)] + pet[randrange(szPet)] + \
              specChars[randrange(2)]

print("  ")
print(secretNames)