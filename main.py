import streamlit as st
from numerize import numerize
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

st.set_page_config(layout="wide")

df1 = pd.read_csv("dki1.csv")
df2 = pd.read_csv("dki2.csv")
df3 = pd.read_csv("dki3.csv")
df4 = pd.read_csv("dki4.csv")
df5 = pd.read_csv("dki5.csv")
gabungan = pd.read_csv("gabungan.csv")
dfcat1 = pd.read_csv("categ1.csv")
dfcat2 = pd.read_csv("categ2.csv")
dfcat3 = pd.read_csv("categ3.csv")
dfcat4 = pd.read_csv("categ4.csv")
dfcat5 = pd.read_csv("categ5.csv")
gabunganchat = pd.read_csv("categg.csv")
kendaraan = pd.read_csv("jumlah_kendaraan.csv")
df11 = pd.read_csv("jakpus.csv")
df22 = pd.read_csv("jakbar.csv")
df33 = pd.read_csv("jaktim.csv")
df44 = pd.read_csv("jaksel.csv")
df55 = pd.read_csv("jakut.csv")
df66 = pd.read_csv("seribu.csv")
penduduk = pd.read_csv("penduduk.csv")

df1['tanggal'] = pd.to_datetime(df1['tanggal'])
df2['tanggal'] = pd.to_datetime(df2['tanggal'])
df3['tanggal'] = pd.to_datetime(df3['tanggal'])
df4['tanggal'] = pd.to_datetime(df4['tanggal'])
df5['tanggal'] = pd.to_datetime(df5['tanggal'])
gabungan['tanggal'] = pd.to_datetime(gabungan['tanggal'])
kendaraan['tahun'] = pd.to_datetime(kendaraan['tahun'])
df11['tahun'] = pd.to_datetime(df11['tahun'])
df22['tahun'] = pd.to_datetime(df22['tahun'])
df33['tahun'] = pd.to_datetime(df33['tahun'])
df44['tahun'] = pd.to_datetime(df44['tahun'])
df55['tahun'] = pd.to_datetime(df55['tahun'])
df66['tahun'] = pd.to_datetime(df66['tahun'])
penduduk['tahun'] = pd.to_datetime(penduduk['tahun'])

st.title("COVID MEREDA, TETAP WAJIB PAKAI MASKER???")
st.markdown("Analisis Polusi Udara di DKI Jakarta.")
st.markdown("Author : Christophe Samuel Diaz Harnanto Putra")

# Input Gambar Headline Berita
berita = Image.open('berita.jpeg')
berita1 = Image.open('berita1.JPG')
berita2 = Image.open('berita2.JPG')
berita3 = Image.open('berita3.png')

img1, img2,img3 = st.columns([1.2,1.5,1.4])
with img1:
    st.image(berita, width = 310, caption='Indeks AQI DKI Jakrta tanggal 3 Agustus 2022')
with img2:
    st.image(berita1, width =450, caption='Cuplikan berita CNBC Indonesia 22 Juni 2022')
    st.image(berita2, width = 400, caption='Cuplikan berita BBC Indonesia 24 Juni 2022')
with img3:
    st.image(berita3, width = 450, caption='Cuplikan berita BBC Indonesia 24 Juni 2022')

st.markdown('Perlahan-lahan, bencana virus Covid telah mereda di Indonesia. Hal ini diperkuat oleh pernyataan Presiden Jokowi (18 Mei 2022) yang memperbolehkan untuk melepas masker ketika di luar ruangan. Namun, pemerintah seakan lupa dengan kondisi udara di DKI Jakarta. Tercatat hari ini, indeks AQI DKI Jakarta berada pada kategori "tidak sehat". Apa sajakah yang menjadi faktor penyebab tingginya tingkat pencemaran udara di DKI? Dengan bertambahnya penduduk, tingkat konsumsi terhadap suatu kebutuhan meningkat. Sebut saja, kebutuhan akan transportasi, listrik, dan lain-lain. Selain kebutuhan-kebutuhan tersebut, perilaku manusia seperti membakar sampah atau pembuangan limbah industri mengakibatkan pencemaran udara. Oleh karena itu, kita akan melihat korelasi-korelasi antara tingkat pencemaran udara dengan berbagai macam faktor.')

# DATA ISPU DKI JAKARTA
st.subheader('Data Indeks Standar Pencemaran Udara (ISPU) DKI Jakarta')
st.markdown('Data Indeks Standar Pencemaran Udara (ISPU) DKI Jakarta tahun 2010-2021. Data berupa :\n- Tabel yang berisi jumlah hari berdasarkan kategori Indeks Standar Pencemaran Udara (ISPU)\n- Grafik yang menunjukkan rata-rata Indeks Standar Pencemaran Udara (ISPU) di stasiun DKI Jakarta')

sb1, sb2 = st.columns(2)
with sb1:
    pilih_chart = st.selectbox('Masukkan daerah stasiun yang dipilih', ('DKI 1 (Bunderan HI)', 'DKI 2 (Kelapa Gading)','DKI 3 (Jagakarsa)','DKI 4 (Lubang Buaya)','DKI 5 (Kebon Jeruk)','DKI Jakarta'))
with sb2:
    freq = st.selectbox("Masukkan frekuensi", ('D', 'W', 'M', 'Q', 'Y'))

if pilih_chart == 'DKI 1 (Bunderan HI)':
    max_df1= df1[['tanggal', 'max']].set_index('tanggal').resample(freq).mean()
    chat1, cht1_max = st.columns([1.25, 4])
    with chat1:
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(dfcat1)
    with cht1_max:
        st.line_chart(max_df1)
    st.caption('Keterangan : 0-49 = BAIK; 50-99 = SEDANG; 100-199 = TIDAK SEHAT; 200-299 = SANGAT TIDAK SEHAT; 300-dst = BERBAHAYA')
elif pilih_chart=='DKI 2 (Kelapa Gading)':
    max_df2= df2[['tanggal', 'max']].set_index('tanggal').resample(freq).mean()
    chat2, cht2_max = st.columns([1.25, 4])
    with chat2:
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(dfcat2)
    with cht2_max:
        st.line_chart(max_df2)
    st.caption('Keterangan : 0-49 = BAIK; 50-99 = SEDANG; 100-199 = TIDAK SEHAT; 200-299 = SANGAT TIDAK SEHAT; 300-dst = BERBAHAYA')
elif pilih_chart=='DKI 3 (Jagakarsa)':
    max_df3= df3[['tanggal', 'max']].set_index('tanggal').resample(freq).mean()
    chat3, cht3_max = st.columns([1.25, 4])
    with chat3:
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(dfcat3)
    with cht3_max:
        st.line_chart(max_df3)
    st.caption('Keterangan : 0-49 = BAIK; 50-99 = SEDANG; 100-199 = TIDAK SEHAT; 200-299 = SANGAT TIDAK SEHAT; 300-dst = BERBAHAYA')
elif pilih_chart=='DKI 4 (Lubang Buaya)':
    max_df4= df4[['tanggal', 'max']].set_index('tanggal').resample(freq).mean()
    chat4, cht4_max = st.columns([1.25, 4])
    with chat4:
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(dfcat4)
    with cht4_max:
        st.line_chart(max_df4)
    st.caption('Keterangan : 0-49 = BAIK; 50-99 = SEDANG; 100-199 = TIDAK SEHAT; 200-299 = SANGAT TIDAK SEHAT; 300-dst = BERBAHAYA')
elif pilih_chart=='DKI 5 (Kebon Jeruk)':
    max_df5= df5[['tanggal', 'max']].set_index('tanggal').resample(freq).mean()
    chat5, cht5_max = st.columns([1.25, 4])
    with chat5:
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(dfcat5)
    with cht5_max:
        st.line_chart(max_df5)
    st.caption('Keterangan : 0-49 = BAIK; 50-99 = SEDANG; 100-199 = TIDAK SEHAT; 200-299 = SANGAT TIDAK SEHAT; 300-dst = BERBAHAYA')
else :
    max_gabungan= gabungan[['tanggal', 'max']].set_index('tanggal').resample(freq).mean()
    gabungan_chat, chatg_max = st.columns([1.25, 4])
    with gabungan_chat:
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(gabunganchat)
    with chatg_max:
        st.line_chart(max_gabungan)
    st.caption('Keterangan : 0-49 = BAIK; 50-99 = SEDANG; 100-199 = TIDAK SEHAT; 200-299 = SANGAT TIDAK SEHAT; 300-dst = BERBAHAYA')

# DATA KEPADATAN PENDUDUK
st.subheader('Data Jumlah Penduduk Tiap Tahun DKI Jakarta')
st.markdown('Data jumlah penduduk tiap tahun DKI Jakarta tahun 2014-2020. Data berupa : grafik jumlah penduduk tiap tahun')

pilih1_chart= st.selectbox('Masukkan daerah yang dipilih',('Kepulauan Seribu','Jakarta Pusat','Jakarta Utara','Jakarta Selatan','Jakarta Timur','Jakarta Barat','DKI Jakarta'))
if pilih1_chart=='Kepulauan Seribu':
    pen_df66 = df66[['tahun', 'jumlah_penduduk']].set_index('tahun')
    st.line_chart(pen_df66)
elif pilih1_chart=='Jakarta Pusat':
    pen_df11 = df11[['tahun', 'jumlah_penduduk']].set_index('tahun')
    st.line_chart(pen_df11)
elif pilih1_chart=='Jakarta Utara':
    pen_df55 = df55[['tahun', 'jumlah_penduduk']].set_index('tahun')
    st.line_chart(pen_df55)
elif pilih1_chart=='Jakarta Selatan':
    pen_df44 = df44[['tahun', 'jumlah_penduduk']].set_index('tahun')
    st.line_chart(pen_df44)
elif pilih1_chart=='Jakarta Timur':
    pen_df33 = df33[['tahun', 'jumlah_penduduk']].set_index('tahun')
    st.line_chart(pen_df33)
elif pilih1_chart=='Jakarta Barat':
    pen_df22 = df22[['tahun', 'jumlah_penduduk']].set_index('tahun')
    st.line_chart(pen_df22)
else:
    pen_penduduk = penduduk[['tahun', 'jumlah_penduduk']].set_index('tahun')
    st.line_chart(pen_penduduk)

# DATA JUMLAH KENDARAAN DI JAKARTA 2008-2014
st.subheader('Data Jumlah Kendaraan Tiap Tahun DKI Jakarta')
pilih2_chart = st.selectbox('Masukkan kategori yang dipilih',('Kendaraan Pribadi','Angkutan Umum','Perbandingan Angkutan Umum : Kendaraan Pribadi'))
if pilih2_chart == 'Kendaraan Pribadi':
    kendaraan_pribadi = kendaraan[['tahun','jumlah_kendaraan_pribadi']].set_index('tahun')
    st.line_chart(kendaraan_pribadi)
elif pilih2_chart == 'Angkutan Umum':
    kendaraan_umum = kendaraan[['tahun','jumlah_angkutan_umum']].set_index('tahun')
    st.line_chart(kendaraan_umum)
else : 
    kendaraan_perbandingan = kendaraan[['tahun','perbandingan']].set_index('tahun')
    st.line_chart(kendaraan_perbandingan)

#KORELASI ANTARA KEPADATAN PENDUDUK DENGAN Indeks Standar Pencemaran Udara (ISPU) DI DKI JAKARTA
st.subheader('Hubungan antara Indeks Standar Pencemaran Udara (ISPU) dan Kepadatan Penduduk DKI JAKARTA TAHUN 2014-2020')

st.markdown('Berdasarkan Uji Korelasi Pearson, nilai yang didapat adalah 0.38782. Hal tersebut menunjukkan korelasi antara kepadatan penduduk dengan tingkat pencemaran udara di DKI Jakarta rendah')
st.markdown('Grafik di bawah adalah grafik kepadatan penduduk dan indeks standar pencemaran udara (ISPU) di DKI Jakarta yang sudah dinormalisasi.')
polusi_penduduk= pd.read_csv('polusi_penduduk.csv')
polusi_penduduk['tahun'] = pd.to_datetime(polusi_penduduk['tahun'])
polusi_penduduk["max"] = polusi_penduduk["max"] / polusi_penduduk["max"].max()
polusi_penduduk["jumlah_penduduk"] = polusi_penduduk["jumlah_penduduk"] / polusi_penduduk["jumlah_penduduk"].max()
pp = polusi_penduduk.set_index('tahun')
st.line_chart(pp)
st.caption('Keterangan: Grafik berwarna jingga adalah grafik  kepadatan penduduk dan grafik berwarna biru adalah indeks standar pencemaran udara (ISPU) di DKI Jakarta')

# KORELASI ANTARA Jumlah Sampah DENGAN Indeks Standar Pencemaran Udara (ISPU) DI DKI JAKARTA 
st.subheader('Hubungan antara Indeks Standar Pencemaran Udara (ISPU) dan Jumlah Sampah di DKI JAKARTA Tahun 2011-2019')

st.markdown('Berdasarkan Uji Korelasi Pearson, nilai yang didapat adalah 0.038534. Hal tersebut menunjukkan korelasi antara jumlah sampah dengan tingkat pencemaran udara di DKI Jakarta sangat rendah.')
st.markdown('Grafik di bawah adalah grafik jumlah sampah dan indeks standar pencemaran udara (ISPU) di DKI Jakarta yang sudah dinormalisasi.')
sampah_polusi= pd.read_csv('polusi_sampah.csv')
sampah_polusi['bulan'] = pd.to_datetime(sampah_polusi['bulan'])
sampah_polusi["max"] = sampah_polusi["max"] / sampah_polusi["max"].max()
sampah_polusi["ritasi"] = sampah_polusi["ritasi"] / sampah_polusi["ritasi"].max()
sp = sampah_polusi.set_index('bulan')
st.line_chart(sp)
st.caption('Keterangan: Grafik berwarna jingga adalah grafik jumlah sampah dan grafik berwarna biru adalah indeks standar pencemaran udara (ISPU) di DKI Jakarta')

# KORELASI ANTARA Jumlah Kendaraan DENGAN Indeks Standar Pencemaran Udara (ISPU) DI DKI JAKARTA 
st.subheader('Hubungan antara Indeks Standar Pencemaran Udara (ISPU) dan Jumlah Kendaraan di DKI JAKARTA Tahun 2010-2014')

st.markdown('- Berdasarkan Uji Korelasi Pearson, nilai korelasi antara jumlah kendaraan pribadi dengan ISPU di DKI Jakarta adalah 0.185936. Hal tersebut menunjukkan korelasi antara jumlah kendaraan pribadi dengan tingkat pencemaran udara di DKI Jakarta sangat rendah.')
st.markdown('- Berdasarkan Uji Korelasi Pearson, nilai korelasi antara jumlah angkutan umum dengan ISPU di DKI Jakarta adalah 0.325856. Hal tersebut menunjukkan korelasi antara jumlah angkutan umum dengan tingkat pencemaran udara di DKI Jakarta rendah.')

st.markdown('Grafik di bawah adalah grafik jumlah kendaraan dan indeks standar pencemaran udara (ISPU) di DKI Jakarta yang sudah dinormalisasi.')
polusi_kendaraan=  pd.read_csv('polusi_kendaraan.csv')
polusi_kendaraan['tahun'] = pd.to_datetime(polusi_kendaraan['tahun'])
polusi_kendaraan["max"] = polusi_kendaraan["max"] / polusi_kendaraan["max"].max()
polusi_kendaraan["jumlah_kendaraan_pribadi"] = polusi_kendaraan["jumlah_kendaraan_pribadi"] / polusi_kendaraan["jumlah_kendaraan_pribadi"].max()
polusi_kendaraan["jumlah_angkutan_umum"] = polusi_kendaraan["jumlah_angkutan_umum"] / polusi_kendaraan["jumlah_angkutan_umum"].max()
pk = polusi_kendaraan[['tahun','max','jumlah_kendaraan_pribadi','jumlah_angkutan_umum']].set_index('tahun')
st.line_chart(pk)
st.caption('Keterangan: Grafik berwarna jingga adalah grafik jumlah kendaraan pribadi, grafik berwarna biru adalah jumlah angkutan umum, dan grafik berwarna merah adalah indeks standar pencemaran udara (ISPU) di DKI Jakarta')

st.subheader('Kesimpulan')
st.markdown('Ketiga hubungan di atas menunjukkan Indeks Standar Pencemaran Udara (ISPU) DKI Jakarta tidak berhubungan dengan kepadatan penduduk, jumlah sampah, dan jumlah kendaraan. Perlu dicari kembali faktor-faktor penyebab lainnya yang berkorelasi positif terhadap pencemaran udara di DKI Jakarta. Akan tetapi, terdapat kemungkinan hubungan tersebut berkorelasi positif. Hal tersebut dikarenakan jumlah data yang kurang lengkap dan tidak mewakili DKI Jakarta.')

st.subheader('Referensi Data')
st.markdown('https://data.jakarta.go.id/dataset')
