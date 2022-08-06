import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="WebApp Cyber", page_icon=":alien:", layout="wide")

st.title("Main Page")
st.sidebar.success("Select a page above.")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_zdtukd5q.json")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("BELAJAR CYBERSECURITY YUK :wave:")
    st.title("Apa itu 'Cybersecurity?'")
    st.write(
        "Kejahatan dunia maya atau dikenal Cyber crime adalah kejahatan yang ditimbulkan karena pemanfaatan teknologi internet. Di antaranya yaitu ancaman keamanan cyber seperti rekayasa sosial, eksploitasi kerentanan perangkat lunak, dan serangan jaringan. Tetapi itu juga termasuk tindakan kriminal seperti pelecehan dan pemerasan, pencucian uang, dan banyak lagi."
    )
    st.write("[Learn More >](https://www.djkn.kemenkeu.go.id/kanwil-sulseltrabar/baca-artikel/14190/Tantangan-Cyber-Security-di-Era-Revolusi-Industri-40.html)")

# ---- JENIS DAN CONTOH ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Jenis dan Contoh")
        st.write("##")
        st.write(
            """
            - Unauthorized access Adalah kejahatan siber yang terjadi saat seseorang masuk atau menyusup ke sistem jaringan komputer tanpa izin dan tidak sah. Contohnya tindakan probing dan port.
            - Illegal contents  dilakukan dengan memasukkan sejumlah data atau informasi ke dalam internet yang sifatnya tidak betul, tidak etis, dan dapat dianggap melanggar hukum.
            - Penyebaran virus dengan sengaja Sering kali dilakukan melalui e-mail. Orang yang menerima e-mail tersebut tidak menyadari bahwa dalam pesan yang diterimanya itu memuat virus.
            - Data forgery Merupakan kejahatan siber yang dilakukan dengan memalsukan data pada dokumen penting di internet. Contohnya memalsukan alamat situs bank atau lembaga resmi.
            - Cyber espionage, sabotage, and extortion  Dalam kejahatan siber, cyber espionage merupakan kejahatan dengan memanfaatkan internet untuk memata-matai pihak lain.
            - Sabotage and extortion adalah kejahatan yang dilakukan dengan mengganggu, merusak, atau menghancurkan suatu data, program, dan atau sistem jaringan komputer. Misalnya kegiatan memata-matai rahasia dagang, dan merusak sistem jaringan yang digunakan untuk menyimpan rahasia tersebut.
            - Cyberstalking  Dilakukan dengan mengganggu atau melecehkan seseorang melalui perangkat komputer dan internet
            - Carding merupakan kejahatan yang dilakukan untuk mencuri nomor kartu kredit orang lain, dan menggunakannya untuk bertransaksi di internet. Sebagai contoh, pelaku kejahatan mengirim situs yang ketika nanti dibuka akan menyebarkan virus ke perangkat milik korban. Kemudian pelaku tersebut akan mulai melakukan carding.
            - Hacking dan cracker Istilah hacker mengacu pada seseorang yang memiliki minat besar untuk mempelajari komputer secara detail. Namun, ada pula yang melakukan aksi perusakan internet, ini disebut cracker. Misalnya melakukan pembajakan akun, menyebarkan virus, melakukan probing, dan sebagainya.
            - Cybersquatting and typosquatting Cybersquatting adalah kejahatan siber dengan mendaftarkan alamat domain nama perusahaan orang lain, kemudian berusaha menjualnya kepada perusahaan tersebut dengan harga lebih mahal. Sementara typosquatting dilakukan dengan membuat domain yang mirip dengan milik orang lain. Nama domain tersebut merupakan saingan suatu perusahaa
           """
        )
with right_column:
        st_lottie(lottie_coding, height=1000, key="coding")

# ---- CARA MENGAMANKAN WEBSITE ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Cara Mengamankan Website")
        st.write("##")
        st.write(
            """
- Pastikan Hosting Aman
- Install Plugin Keamanan
- Pasang SSL
- Update Website
- Gunakan Username dan Password yang Kuat
- Install Plugin Backup
- Amankan File Website dengan Antivirus Terbaik
- Ganti URL Login
- Terapkan 2-Factor Authentication
- Batasi Percobaan Login
- Logout Otomatis
- Perlindungan DDos
- Atur Google Analytics dan Search Console
           
           """
        )
st.write("[Learn More >](https://www.youtube.com/watch?v=FKxgZWmXkIE)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Report Cyber Crime?")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/larasgilangrahmany@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()