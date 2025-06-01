import speedtest

st = speedtest.Speedtest()
descarga = st.download() / 1_000_000
