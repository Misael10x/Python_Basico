import speedtest

st = speedtest.Speedtest()
descarga = st.download() / 1_000_000
subida = st.upload() / 1_000_000
ping = st.results.ping

print(f"Velocidad de descarga: {descarga:.2f} Mbps")
print(f"Velocidad de subida: {subida:.2f} Mbps")
print(f"Ping: {ping:.2f} ms")
