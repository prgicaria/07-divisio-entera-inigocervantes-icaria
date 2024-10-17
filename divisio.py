dividend = int(input("Diguem el dividend de la divisió: "))
divisor = int(input("Diguem el divisor de la divisió: "))
quocient = dividend // divisor  # Divisió entera per obtenir el quocient sencer
residu = dividend % divisor

print(f"Divisió: {dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")