import json as js

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

file = open("sample.json", 'r').read()
d = js.loads(file)

for i in d["imdata"]:
    print(i["l1PhysIf"]["attributes"]["dn"], "                              ", i["l1PhysIf"]["attributes"]["fecMode"], "   ", i["l1PhysIf"]["attributes"]["mtu"])