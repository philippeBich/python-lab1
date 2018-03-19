print("Insert a string: ")
string=input()

if len(string) < 2:
    print("")
    exit(0)
if len(string) < 4:
    print("That's a too short string")
    exit(0)

finale = string[0]+string[1]+string[len(string)-1]+string[len(string)-2]
print("The final string is "+finale+".")

