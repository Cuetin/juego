from gameobjects import actions

#for mier in GameObject.objects:
#    print(mier, ":", GameObject.objects[mier])

print(actions.ayuda("general"))

print(actions.register.__doc__)

while True:
    actions.get_input()
