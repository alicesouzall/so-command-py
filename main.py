import win32net

users = win32net.NetUserEnum(None, 0)

for user in users[0]:
    print(user['name'])

print("Aluna: Alice Souza Lima")
print("RA: 324136989")
