import speedtest

st = speedtest.Speedtest()
descarga = st.download() / 1_000_000
subida = st.upload() / 1_000_000
ping = st.results.p
