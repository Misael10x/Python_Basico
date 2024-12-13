clima = {'New York': 'Nieve', 'Boston': 'Soleado', 'Los Angeles': 'Soleado',  'Chicago': 'Nublado'}
clima_soleado = {key: value for (key, value) in clima.items() if value == 'Soleado' }
print(clima_soleado)
