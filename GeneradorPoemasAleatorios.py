sustantivos = ["alma", "luz", "sombra", "tierra", "viento", "mar", "noche"]

verbos = ["llora", "brilla", "cae", "grita", "suspira", "calla", "canta"]

adjetivos = ["oscura", "silente", "eterna", "fugaz", "triste", "brillante", "vacía"]

for _ in range(4):

      linea = f"La {random.choice(sustantivos)} {random.choice(verbos)} en la {random.choice(adjetivos)} noche."

