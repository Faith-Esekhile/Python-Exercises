def kinetic_energy(mass,vel):
    ke=0.5*mass*(vel**2)
    return ke
v=int(input("enter velocity"))
m=int(input("enter mass"))
print(kinetic_energy(m,v))