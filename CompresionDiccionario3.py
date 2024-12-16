
clima = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
clima2 = {key: ("CALOR" if value >=40 else "FRIO") for (key, value) in clima.items()}
print(clima2) 
