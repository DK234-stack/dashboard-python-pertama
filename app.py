import streamlit as st
import pandas as pd
st.title(" Dashboard Penjualan Keren" )
st.title("Selamat Tinggal Excel yang gampang geser" )
Data = { 'Bulan' : ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni'], 'Keuntungan (Juta)' : [10, 15, 12, 22] }
df = pd.DataFrame(Data)
st.subheader("Tabel Data" )
st.dataframe(df)
st.subheader("Grafik Tren Keuntungan" )
st.line_chart(df.set_index('Bulan'))