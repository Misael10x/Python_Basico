def check_temp(value):
    if value >=70:
        return "CALOR"
    elif 60 >= value >=40:
        return "Normal"
    else:
     return "FRIO"
     

ciudades = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
clima = {key: check_temp(value) for (key, value) in ciudades.items()}
print(clima)
