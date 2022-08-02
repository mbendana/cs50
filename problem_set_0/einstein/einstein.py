mass = input("Enter a 'mass' amount in kilograms\nm: ")

joules = 300_000_000
energy = int(mass) * pow(joules, 2)

print(f"E: {energy:,}")
