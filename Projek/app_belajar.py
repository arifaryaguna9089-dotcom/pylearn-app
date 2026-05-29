import streamlit as st
import pandas as pd
import time

# ==========================================
# SETUP HALAMAN & TEMA MODERN WITH BLUE BORDERS
# ==========================================
st.set_page_config(
    page_title="PyLearn.zip - Platform Belajar Web Dev Modern",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom gaya Gen Z + Kustomisasi Garis Tepi Biru via CSS
st.markdown("""
    <style>
    .main { background-color: #0f172a; }
    h1, h2 { color: #22d3ee !important; font-weight: 800 !important; }
    h3, h4 { color: #f43f5e !important; font-weight: 700 !important; }
    .stSelectbox label { color: #cbd5e1 !important; font-weight: 600; }
    
    /* MENGUBAH SEMUA GARIS TEPI CONTAINER MENJADI BIRU */
    div[data-testid="stContainerBorder"] {
        border: 1px solid #3b82f6 !important;
        box-shadow: 0px 0px 10px rgba(59, 130, 246, 0.25);
    }
    
    /* MENGUBAH GARIS PEMBATAS HORIZONTAL (hr / ---) MENJADI BIRU GELAP */
    hr {
        border-color: #1e3a8a !important;
    }
    
    /* Style untuk Tombol Utama */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #f43f5e 0%, #3b82f6 100%);
        color: #ffffff;
        font-weight: bold;
        border: none;
        border-radius: 12px;
        padding: 0.5rem 2rem;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        transform: scale(1.03);
        box-shadow: 0px 0px 15px rgba(244, 63, 94, 0.4);
    }
    
    /* Style Kotak Output Konsol */
    .console-box {
        background-color: #011627;
        color: #ecc48d;
        font-family: 'Courier New', Courier, monospace;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #00e676;
        margin-top: 10px;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# INITIALIZE POMODORO STATE (Agar State Awet)
# ==========================================
if "pomodoro_running" not in st.session_state:
    st.session_state.pomodoro_running = False

# ==========================================
# 1. RUNNING TEXT (TEKS BERJALAN) DI ATAS WEB
# ==========================================
st.markdown("""
    <marquee behavior="scroll" direction="left" style="color: #22d3ee; font-weight: bold; background: #1e293b; padding: 8px; border-radius: 8px; border: 1px solid #3b82f6;">
        🔥 INFO KELAS: Modul Struktur Data "Binary Tree" telah diperbarui sesuai modul kuliah terbaru! • ⚡ Developer Tips: Gunakan shortcut Ctrl+S di VS Code untuk auto-refresh tampilan web ini! • 🎓 Tetap produktif dan semangat ngoding, No Cap No Gatekeeping!
    </marquee>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# SIDEBAR: ENTITAS, NAVIGASI, POMODORO & IKLAN
# ==========================================
with st.sidebar:
    # 🌟 KOLOM ENTITAS DEVELOPER (PROFIL KAMU)
    st.markdown("### 🛠️ Developer Profile")
    with st.container(border=True):
        st.markdown("""
            <div style="text-align: center; margin-bottom: 10px;">
                <span style="font-size: 3rem;">👨‍💻</span>
                <h4 style="color: #22d3ee; margin: 5px 0 0 0;">Arif Aryaguna</h4>
                <p style="color: #f43f5e; font-size: 0.85rem; font-weight: bold; margin: 0;">Status: Mahasiswa</p>
                <p style="color: #94a3b8; font-size: 0.75rem; margin-top: 5px;">Sistem Informasi • Universitas Islam Negeri Imam Bonjol Padang</p>
            </div>
            <hr style="border-color: #3b82f6; margin: 10px 0;">
            <div style="font-size: 0.8rem; color: #cbd5e1; line-height: 1.4;">
                ⚡ <b>Focus:</b> Python Web Dev & Data Structures<br>
                🚀 <i>"Building the future, one line of code at a time."</i>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")

    # 🍅 INOVASI BARU: POMODORO TIMER WORKSPACE
    st.markdown("### ⏱️ Pomodoro Space")
    with st.container(border=True):
        st.markdown("<p style='font-size: 0.85rem; color: #cbd5e1; margin-bottom: 5px;'>Pilih Mode Pomodoro:</p>", unsafe_allow_html=True)
        pomo_mode = st.selectbox(
            "Mode",
            ["Fokus Ngoding (25 Menit)", "Rest Sementara (5 Menit)", "Mode Test Cepat (10 Detik)"],
            label_visibility="collapsed"
        )
        
        # Penentuan durasi (dalam detik) berdasarkan pilihan user
        if pomo_mode == "Fokus Ngoding (25 Menit)":
            duration = 25 * 60
            msg_success = "Waktu fokus habis! Rileks dulu gils, rehat riil no fek! 🧠"
        elif pomo_mode == "Rest Sementara (5 Menit)":
            duration = 5 * 60
            msg_success = "Waktu istirahat habis! Gas ngoding lagi, let's gooo! 🔥"
        else:
            duration = 10 # Mode cepat buat testing program
            msg_success = "Test berhasil! Fitur Pomodoro kamu berjalan mulus! 🚀"

        # Tombol Kendali Pomodoro
        pomo_button = st.button("Mulai Timer ⏳")

        if pomo_button:
            st.session_state.pomodoro_running = True
            countdown_place = st.empty()
            progress_place = st.empty()
            
            # Loop hitung mundur
            for t in range(duration, -1, -1):
                mins, secs = divmod(t, 60)
                time_format = f"{mins:02d}:{secs:02d}"
                
                # Tampilkan teks waktu berjalan mundur
                countdown_place.markdown(f"<h2 style='text-align: center; color: #f43f5e;'>{time_format}</h2>", unsafe_allow_html=True)
                
                # Update progress bar
                pct_complete = (duration - t) / duration
                progress_place.progress(pct_complete)
                
                time.sleep(1)
            
            st.session_state.pomodoro_running = False
            countdown_place.empty()
            progress_place.empty()
            st.balloons()
            st.success(msg_success)
        else:
            if not st.session_state.pomodoro_running:
                st.markdown("<h3 style='text-align: center; color: #94a3b8;'>00:00</h3>", unsafe_allow_html=True)

    st.markdown("---")

    # 👤 USER SESSION
    st.markdown("### 👤 User Session")
    username_input = st.text_input("Username", placeholder="Username andalanmu...", label_visibility="collapsed")
    tombol_login = st.button("Gas Masuk ✨")
    if tombol_login:
        if username_input:
            st.success(f"Gas! Selamat datang, **{username_input}**! ⚡")
        else:
            st.warning("Isi dulu bos username-nya 🫣")
            
    st.markdown("---")
    
    # 🌐 BOX MERUBAH BAHASA
    bahasa = st.selectbox("🌐 Pilih Bahasa / Language", ("Bahasa Indonesia", "English"))
    st.markdown("---")
    
    # 🛠️ NAVIGATION MENU UTAMA
    st.markdown("### 🧭 Main Menu")
    menu_pilihan = st.radio(
        "Pilih Halaman:",
        ["📚 Kelas Web Dev (Utama)", "💡 Inovasi IoT & Kerja", "🎓 Modul Tree (Struktur Data)"]
    )
    
    st.markdown("---")
    
    # 📢 WIDGET IKLAN / PROMOSI KREATIF INTERNAL
    st.markdown("### 📢 Sponsored Info")
    with st.container(border=True):
        st.markdown("""
            <div style="background: linear-gradient(135deg, #1e1b4b 0%, #31102f 100%); padding: 12px; border-radius: 8px; text-align: center;">
                <span style="font-size: 1.5rem;">🎒</span>
                <h5 style="color: #ff007f; margin: 5px 0;">HIMASI Merch Pre-Order!</h5>
                <p style="color: #cbd5e1; font-size: 0.75rem; margin-bottom: 10px;">Dapatkan PDH dan Jaket Hoodie eksklusif angkatan terbaru dengan harga khusus mahasiswa.</p>
                <a href="#" style="background: #22d3ee; color: #0f172a; padding: 4px 10px; border-radius: 5px; font-size: 0.75rem; font-weight: bold; text-decoration: none;">Hubungi Kominfo</a>
            </div>
        """, unsafe_allow_html=True)


# ==========================================
# HALAMAN 1: KELAS WEB DEV (UTAMA)
# ==========================================
if menu_pilihan == "📚 Kelas Web Dev (Utama)":
    st.title("Bikin Web Sendiri? Gampang Parah! 🚀")
    st.markdown("<p style='font-size:1.2rem; color:#94a3b8;'>Gak usah ribet, kita kuliti cara bikin website pakai Python dari nol sampai siap pamer. No cap, ini seru abis!</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    kolom_kiri, kolom_kanan = st.columns([2.2, 1], gap="large")
    
    with kolom_kiri:
        with st.container(border=True):
            st.markdown("### 📌 Spill Core Materi (Latar Belakang)")
            st.markdown("""
            Website adalah ruang digital untuk berbagi informasi serta memperkenalkan diri, bisnis, proyek, maupun tujuan Anda di internet. Saat ini, website menjadi tool penting bagi siapa pun yang ingin membangun reputasi di dunia online.
            
            Baik Anda menjalankan usaha kecil, perusahaan besar, maupun bekerja sebagai freelancer, website merupakan salah satu cara paling efektif untuk membuat bisnis atau personal brand Anda lebih mudah dikenal oleh audiens yang lebih luas.
            """)
            st.info("💡 **Core Insight:** Di platform ini, kita dirancang khusus buat kamu yang mau akselerasi masuk ke dunia web dev tanpa pusing. Kita bakal bahas fundamental penting, setup tools kekinian di VS Code, sampai website kamu beneran live!")
            
        st.markdown(" ")
        
        st.markdown("## 📖 Materi Pembelajaran")
        tab1, tab2, tab3 = st.tabs([
            "1. Alat-Alat (Tools)", 
            "2. Langkah-Langkah Pembuatan", 
            "3. Manfaat Bikin Web"
        ])
        
        with tab1:
            st.markdown("<h3 style='text-align: center; margin-bottom: 20px;'>🛠️ Senjata Utama Developer Web Python</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 1rem;'>Untuk membangun website modern, ini 3 tools esensial yang wajib bertengger di laptopmu:</p>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            
            t_col1, t_col2, t_col3 = st.columns(3, gap="large")
            with t_col1:
                with st.container(border=True):
                    st.markdown("""
                        <div style="text-align: center; min-height: 280px;">
                            <img src="https://www.python.org/static/community_logos/python-logo-generic.svg" width="110" style="margin-bottom: 20px;">
                            <h4 style="color: #22d3ee; margin-bottom: 10px;">Python 3</h4>
                            <p style="color: #cbd5e1; font-size: 0.85rem; line-height: 1.5;">
                                Bahasa pemrograman utama kita yang super bersih, efisien, dan ramah pemula. Semua logika web diatur di sini.
                            </p>
                        </div>
                    """, unsafe_allow_html=True)
            with t_col2:
                with st.container(border=True):
                    st.markdown("""
                        <div style="text-align: center; min-height: 280px;">
                            <img src="https://upload.wikimedia.org/wikipedia/commons/9/9a/Visual_Studio_Code_1.35_icon.svg" width="90" style="margin-bottom: 20px; padding-top: 10px;">
                            <h4 style="color: #22d3ee; margin-bottom: 10px;">VS Code</h4>
                            <p style="color: #cbd5e1; font-size: 0.85rem; line-height: 1.5;">
                                Code editor sejuta umat tempat kita mengetik kode. Ringan, sat set, dan punya banyak extension pendukung otomatis.
                            </p>
                        </div>
                    """, unsafe_allow_html=True)
            with t_col3:
                with st.container(border=True):
                    st.markdown("""
                        <div style="text-align: center; min-height: 280px;">
                            <img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.svg" width="120" style="margin-bottom: 35px; padding-top: 15px;">
                            <h4 style="color: #22d3ee; margin-bottom: 10px;">Streamlit UI</h4>
                            <p style="color: #cbd5e1; font-size: 0.85rem; line-height: 1.5;">
                                Framework Python ajaib yang menyulap script kode Python biasamu menjadi tampilan web interaktif secara instan.
                            </p>
                        </div>
                    """, unsafe_allow_html=True)

        with tab2:
            st.markdown("### 🏁 5 Langkah Instan Bikin Web Sampai Live")
            roadmap_data = [
                {"step": "Step 1: Environment Setup", "desc": "Install Python di PC-mu dan pasang Visual Studio Code sebagai arena tempur utama."},
                {"step": "Step 2: Coding Fondasi Backend", "desc": "Tulis script logika bisnis websitemu pakai Python. Definisikan rute halaman dan variabel data."},
                {"step": "Step 3: Merancang Tampilan (UI)", "desc": "Gunakan komponen visual atau framework CSS (seperti Tailwind/Streamlit UI) agar layout-mu estetik dan responsif di HP/Laptop."},
                {"step": "Step 4: Integrasi Data & Event", "desc": "Hubungkan tombol masukkan data (seperti box login atau input text) dengan fungsi logika backend Python-mu."},
                {"step": "Step 5: Deployment", "desc": "Unggah kodemu ke cloud platform (GitHub, Streamlit Community Cloud, atau Heroku) biar dapet link live yang bisa di-share ke siapa saja!"}
            ]
            for item in roadmap_data:
                with st.chat_message("user", avatar="💻"):
                    st.markdown(f"**{item['step']}** — {item['desc']}")

        with tab3:
            st.markdown("### 🌟 Kenapa Kamu Harus Bisa Bikin Website?")
            st.markdown("""
            * **Personal Branding Naik Level 🚀**: Punya website portofolio sendiri bikin kamu kelihatan mencolok di mata rekruter.
            * **Otomatisasi Ide 🧠**: Kamu bisa bikin solusi digital buat masalah apa aja di sekitarmu secara mandiri.
            * **Peluang Karir Fleksibel 💼**: Skill web development adalah salah satu skill dengan bayaran paling stabil di industri tech.
            * **Fondasi Menuju Industri Tech 📈**: Memahami alur kerja web membuatmu lebih gampang saat belajar Data Science, IoT, atau AI integration.
            """)

    with kolom_kanan:
        st.markdown(f"### 📊 Silabus Ringkas")
        with st.container(border=True):
            st.markdown("#### 🐍 Python Basics")
            st.caption("LEVEL: BASIC")
            st.write("Sintaksis seru dan ringkas yang ramah banget buat pemula.")
        st.markdown(" ")
        with st.container(border=True):
            st.markdown("#### 🌐 Routing System")
            st.caption("LEVEL: INTERMEDIATE")
            st.write("Cara nge-link halaman web biar user-mu gak kesasar.")
        st.markdown(" ")
        with st.container(border=True):
            st.markdown("#### 💾 Data Handling")
            st.caption("LEVEL: ADVANCED")
            st.write("Ngasih otak ke aplikasi web biar bisa menyimpan data.")

# ==========================================
# HALAMAN 2: INOVASI LAINNYA (IoT & KESELAMATAN KERJA)
# ==========================================
elif menu_pilihan == "💡 Inovasi IoT & Kerja":
    st.title("💡 Hub Inovasi Mahasiswa")
    st.markdown("Eksplorasi ide solutif masa kini yang menggabungkan pemrograman Python dengan teknologi mutakhir.")
    st.markdown("---")
    
    i_col1, i_col2 = st.columns(2, gap="medium")
    with i_col1:
        with st.container(border=True):
            st.markdown("### 🦾 Inovasi IoT Keselamatan Kerja (K3)")
            st.write("Bagaimana mahasiswa memanfaatkan Python untuk melindungi pekerja di lapangan?")
            st.markdown("""
            1.  **Smart Helmet Detection 🪖**: Menggunakan kamera berbasis AI (OpenCV + Python) yang otomatis mendeteksi apakah pekerja konstruksi memakai helm proyek secara benar atau tidak.
            2.  **Gas Leak & Fire Tracker 🚨**: Sensor IoT yang mendeteksi kebocoran gas berbahaya di pabrik, mengolah datanya via script Python, lalu mengirimkan alarm darurat instan ke HP supervisor.
            3.  **Fatigue Tracker 🥱**: Sensor kamera AI mini di dashboard truk tambang untuk mendeteksi pola mata mengantuk pada pengemudi guna mencegah kecelakaan fatal akibat kelelahan.
            """)
            st.button("Pelajari IoT Lebih Dalam ⚡", key="btn_iot")

    with i_col2:
        with st.container(border=True):
            st.markdown("### 📊 Statistik Kasus Kecelakaan Kerja")
            st.write("Kenapa inovasi keselamatan berbasis teknologi di atas itu krusial banget?")
            
            data_stat = pd.DataFrame({
                'Tahun': ['2023', '2024', '2025', '2026 (Prediksi)'],
                'Kasus Tanpa IoT (Ribuan)': [150, 142, 135, 130],
                'Kasus Dengan Implementasi IoT (Ribuan)': [110, 85, 50, 22]
            })
            data_stat = data_stat.set_index('Tahun')
            st.line_chart(data_stat)
            st.caption("Grafik perbandingan kasus kecelakaan kerja sebelum vs sesudah optimalisasi sistem IoT cerdas.")

# ==========================================
# HALAMAN 3: MODUL TREE (LIVE TRAVERSAL SIMULATOR)
# ==========================================
elif menu_pilihan == "🎓 Modul Tree (Struktur Data)":
    st.title("🎓 Modul Struktur Data: Tree & Traversal")
    st.markdown("Struktur data non-linier untuk merepresentasikan hubungan hierarki antar data.")
    st.markdown("---")
    
    data_mahasiswa = [
        {"nobp": 221003, "nama": "Citra", "alamat": "Padang", "nohp": "0811111111"},
        {"nobp": 221001, "nama": "Andi", "alamat": "Bukittinggi", "nohp": "0822222222"},
        {"nobp": 221002, "nama": "Budi", "alamat": "Payakumbuh", "nohp": "0844444444"},
        {"nobp": 221004, "nama": "Dina", "alamat": "Solok", "nohp": "0833333333"},
        {"nobp": 221005, "nama": "Evi", "alamat": "Pariaman", "nohp": "0855555555"}
    ]

    t_left, t_right = st.columns([1.3, 1], gap="large")
    
    with t_left:
        with st.container(border=True):
            st.markdown("### 🌲 Apa itu Binary Tree?")
            st.write("Tree merupakan struktur data non-linier berbentuk seperti pohon dengan satu akar (root) dan cabang (node). Di dalam **Binary Tree**, setiap node maksimal memiliki 2 anak (Left child & Right child).")
            
            st.markdown("""
            **Aturan Pembacaan (Traversal Tree):**
            * **Preorder**: Urutan baca dimulai dari **Root** &rarr; Left &rarr; Right.
            * **Inorder**: Urutan baca dari Left &rarr; **Root** (di tengah) &rarr; Right.
            * **Postorder**: Urutan baca dari Left &rarr; Right &rarr; **Root** (di akhir).
            """)
            
        st.markdown(" ")
        
        st.markdown("### ⚡ Live Console Traversal Simulator")
        st.write("Klik tombol di bawah ini untuk melihat bagaimana script Python memproses dan membaca urutan data mahasiswa:")
        
        c1, c2, c3 = st.columns(3)
        with c1: btn_pre = st.button("▶️ Run Preorder")
        with c2: btn_in = st.button("▶️ Run Inorder")
        with c3: btn_post = st.button("▶️ Run Postorder")
            
        if btn_pre:
            urutan = [0, 1, 2, 3, 4]
            st.markdown("**Output Console (=== Preorder ===):**")
            output_lines = []
            for idx in urutan:
                m = data_mahasiswa[idx]
                output_lines.append(f"NOBP: {m['nobp']} | Nama: {m['nama']} | Alamat: {m['alamat']} | HP: {m['nohp']}")
            st.markdown(f"<div class='console-box'>{'<br>'.join(output_lines)}</div>", unsafe_allow_html=True)
            
        elif btn_in:
            urutan = [1, 2, 0, 3, 4]
            st.markdown("**Output Console (=== Inorder ===):**")
            output_lines = []
            for idx in urutan:
                m = data_mahasiswa[idx]
                output_lines.append(f"NOBP: {m['nobp']} | Nama: {m['nama']} | Alamat: {m['alamat']} | HP: {m['nohp']}")
            st.markdown(f"<div class='console-box'>{'<br>'.join(output_lines)}</div>", unsafe_allow_html=True)
            
        elif btn_post:
            urutan = [2, 1, 4, 3, 0]
            st.markdown("**Output Console (=== Postorder ===):**")
            output_lines = []
            for idx in urutan:
                m = data_mahasiswa[idx]
                output_lines.append(f"NOBP: {m['nobp']} | Nama: {m['nama']} | Alamat: {m['alamat']} | HP: {m['nohp']}")
            st.markdown(f"<div class='console-box'>{'<br>'.join(output_lines)}</div>", unsafe_allow_html=True)
        else:
            st.info("Silakan klik salah satu tombol di atas untuk melihat output log datanya!")

    with t_right:
        with st.container(border=True):
            st.markdown("### 🗂️ Representasi Hierarki Data")
            st.write("Visualisasi pohon data mahasiswa berdasarkan variabel inisialisasi script:")
            st.markdown("""
```text
                     [Citra - 221003 (Root)]
                         /          \\
            [Andi - 221001]      [Dina - 221004]
                  \\                    \\
            [Budi - 221002]      [Evi - 221005]
            ```
            """)
            st.caption("Struktur folder sistem operasi, database indexing, hingga AI memanfaatkan konsep hierarki ini.")
            
        st.markdown(" ")
        with st.container(border=True):
            st.markdown("#### 💻 Kode Program (Class Node & Inisialisasi)")
            st.code("""
class Node:
    def __init__(self, nobp, nama, alamat, nohp):
        self.nobp = nobp
        self.nama = nama
        self.alamat = alamat
        self.nohp = nohp
        self.left = None
        self.right = None

# Membuat hierarki pohon mahasiswa
root = Node(221003, "Citra", "Padang", "0811111111")
root.left = Node(221001, "Andi", "Bukittinggi", "0822222222")
root.right = Node(221004, "Dina", "Solok", "0833333333")
root.left.right = Node(221002, "Budi", "Payakumbuh", "0844444444")
root.right.right = Node(221005, "Evi", "Pariaman", "0855555555")
            """, language="python")

# ==========================================
# FOOTER UTAMA
# ==========================================
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #475569; font-size: 0.8rem; font-weight: bold;'>"
    "© 2026 PyLearn.zip • Created 100% with Python by Arif Aryaguna.</p>", 
    unsafe_allow_html=True
)