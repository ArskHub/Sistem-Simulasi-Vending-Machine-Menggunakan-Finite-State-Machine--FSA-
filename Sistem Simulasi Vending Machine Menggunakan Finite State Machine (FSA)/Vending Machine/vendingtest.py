import tkinter as tk
from PIL import Image, ImageTk

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vending Machine Baju Adat Otomatis")
        self.geometry('500x350')
        self.configure(bg="white")
        self.resizable(False, False)

        self.show_welcome_screen()
        
        self.harga_barang = {
            'Pria': {
                'Baju Adat': {'Safari': 100000, 'Kemeja': 90000},
                'Kamen': {'Lembaran': 80000, 'Setengah Jadi': 85000},
                'Udeng': {'Lembaran': 40000, 'Jadi': 55000},
                'Selendang': {'Motif': 25000, 'Polos': 15000}
            },
            'Wanita': {
                'Kebaya': {'Brokat': 100000, 'Sari': 90000},
                'Kamen': {'Lembaran': 110000, 'Jadi': 150000},
                'Selendang': {'Motif': 25000, 'Polos': 15000}
            }
        }
        
        self.state = 'q0'
        self.gender = 'M'
        self.sizes = ['M', 'L', 'XL']
        self.total_harga = 0
        
    def hide_content(self):
        for widget in self.winfo_children():
            widget.place_forget()

    def show_welcome_screen(self):
        self.pilihan_barang = []
        
        image = Image.open("image\cover.png")
        resized_image = image.resize((500, 350), Image.Resampling.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(resized_image)
        
        image = tk.Label(self, image=self.bg_image, bg="white")
        image.place(x=0, y=0)
        
        # Tampilkan layar selamat datang
        welcome_label = tk.Label(self, text="Selamat datang di Vending Machine \nBaju Adat Otomatis", font=("Montserrat", 16), bg="#f5f5f5")
        welcome_label.place(x=80, y=30)

        start_button = tk.Button(self, text="Mulai", width=12, command=self.size_selection)
        start_button.place(x=200, y=300)

    def size_selection(self):
        self.state = 'q1'
        # Sembunyikan elemen dari layar selamat datang
        self.hide_content()

        # Tampilkan elemen untuk memilih ukuran baju
        size_label = tk.Label(self, text="Silahkan pilih ukuran baju anda", font=("Montserrat", 16), bg="white")
        size_label.place(x=110, y=130)
        # Buat button
        for i, size in enumerate(self.sizes):
            button = tk.Button(
                self,
                text=size,
                width=12,
                command=lambda s=size: self.gender_selection(s),
            )
            button.place(x=105 + i * 100, y=180)
    
    def gender_selection(self, s):
        self.ukuran = s
        if self.ukuran == 'M':
            self.state = 'q2'
        elif self.ukuran == 'L':
            self.state = 'q3'
        elif self.ukuran == 'XL':
            self.state = 'q4'
        # Sembunyikan elemen dari layar size selection
        self.hide_content()
        
        # Tampilkan elemen untuk memilih gender
        gender_label = tk.Label(self, text="Untuk siapa baju ini?", font=("Montserrat", 16), bg="white")
        gender_label.place(x=150, y=80)
        # Input gambar
        image_f = Image.open("image\wanita.png")
        image_m = Image.open("image\pria.png")
        # Resize gambar
        resized_image_f = image_f.resize((90, 90), Image.Resampling.LANCZOS)
        self.tk_image_f = ImageTk.PhotoImage(resized_image_f)
        resized_image_m = image_m.resize((90, 90), Image.Resampling.LANCZOS)
        self.tk_image_m = ImageTk.PhotoImage(resized_image_m)
        # Tampilkan gambar
        image_f_label = tk.Label(self, image=self.tk_image_f, bg="white")
        image_f_label.place(x=145, y=120)
        image_m_label = tk.Label(self, image=self.tk_image_m, bg="white")
        image_m_label.place(x=265, y=120)
        # Buat button
        gender_F_button = tk.Button(self, text="Wanita", width=12, command=self.female_select)
        gender_F_button.place(x=145, y=225)
        gender_M_button = tk.Button(self, text="Pria", width=12, command=self.male_select)
        gender_M_button.place(x=265, y=225)

    def female_select(self):
        self.state = 'q6'
        # Sembunyikan elemen dari layar gender selection
        self.hide_content()
        
        self.gender = 'F'
        #Tampilkan pilihan barang yang ingin dibeli
        female_label = tk.Label(self, text="Pakaian apa yang ingin anda beli?", font=("Montserrat", 16), bg="white")
        female_label.place(x=90, y=80)
        
        # Akses gambar
        kebaya_img = Image.open("image\kebaya.png")
        kamen_img = Image.open("image\kamen_f.png")
        selendang_img = Image.open("image\selendang_f.png")
        # Atur ukuran gambar
        resized_kebaya = kebaya_img.resize((90, 90), Image.Resampling.LANCZOS)
        self.kebaya_image = ImageTk.PhotoImage(resized_kebaya)
        resized_kamen = kamen_img.resize((90, 90), Image.Resampling.LANCZOS)
        self.kamen_image = ImageTk.PhotoImage(resized_kamen)
        resized_selendang = selendang_img.resize((90, 90), Image.Resampling.LANCZOS)
        self.selendang_image = ImageTk.PhotoImage(resized_selendang)
        # Tempatkan gambar pada GUI
        kebaya_img = tk.Label(self, image=self.kebaya_image, bg="white")
        kebaya_img.place(x=90, y=120)
        kamen_img = tk.Label(self, image=self.kamen_image, bg="white")
        kamen_img.place(x=205, y=120)
        selendang_img = tk.Label(self, image=self.selendang_image, bg="white")
        selendang_img.place(x=320, y=120)
        # Buat button
        kebaya_button = tk.Button(self, text="Kebaya", width=12, command=self.kebaya_select)
        kebaya_button.place(x=90, y=235)
        kamen_button = tk.Button(self, text="Kamen", width=12, command=self.kamen_select)
        kamen_button.place(x=205, y=235)
        selendang_button = tk.Button(self, text="Selendang", width=12, command=self.selendang_f_select)
        selendang_button.place(x=320, y=235)
            
    def male_select(self):
        self.state = 'q5'
        # Sembunyikan elemen dari layar gender selection
        self.hide_content()
        
        self.gender = 'M'
        # Tampilkan pilihan barang yang ingin dibeli
        male_label = tk.Label(self, text="Pakaian apa yang ingin anda beli?", font=("Montserrat", 16), bg="white")
        male_label.place(x=90, y=80)
        # Akses gambar
        baju_img = Image.open("image\safari.png")
        udeng_img = Image.open("image\m_udeng.png")
        kamen_img = Image.open("image\kamen_m.png")
        selendang_img = Image.open("image\selendang_m_polos.png")
        # Atur ukuran gambar
        resized_baju = baju_img.resize((90, 90), Image.Resampling.LANCZOS)
        self.baju_image = ImageTk.PhotoImage(resized_baju)
        resized_udeng = udeng_img.resize((90, 90), Image.Resampling.LANCZOS)
        self.udeng_image = ImageTk.PhotoImage(resized_udeng)
        resized_kamen = kamen_img.resize((90, 90), Image.Resampling.LANCZOS)
        self.kamen_image = ImageTk.PhotoImage(resized_kamen)
        resized_selendang = selendang_img.resize((90, 90), Image.Resampling.LANCZOS)
        self.selendang_image = ImageTk.PhotoImage(resized_selendang)
        # Tempatkan gambar pada GUI
        baju_img = tk.Label(self, image=self.baju_image, bg="white")
        baju_img.place(x=50, y=120)
        udeng_img = tk.Label(self, image=self.udeng_image, bg="white")
        udeng_img.place(x=150, y=120)
        kamen_img = tk.Label(self, image=self.kamen_image, bg="white")
        kamen_img.place(x=250, y=120)
        selendang_img = tk.Label(self, image=self.selendang_image, bg="white")
        selendang_img.place(x=350, y=120)
        # Buat button
        baju_button = tk.Button(self, text="Baju Adat", width=12, command=self.baju_adat_select)
        baju_button.place(x=50, y=235)
        udeng_button = tk.Button(self, text="Udeng", width=12, command=self.udeng_select)
        udeng_button.place(x=150, y=235)
        kamen_button = tk.Button(self, text="Kamen & Saput", width=12, command=self.kamen_saput_select)
        kamen_button.place(x=250, y=235)
        selendang_button = tk.Button(self, text="Selendang", width=12, command=self.selendang_m_select)
        selendang_button.place(x=350, y=235)
        
    def kebaya_select(self):
        self.state = 'q11'
        # Sembunyikan elemen dari layar female select
        self.hide_content()
        
        # Tampilkan pilihan kebaya
        kebaya_label = tk.Label(self, text="Kebaya jenis apa yang ingin anda beli?", font=("Montserrat", 14), bg="white")
        kebaya_label.place(x=90, y=75)
        
        # Input gambar
        brokat_img = Image.open("image\kebaya.png")
        sari_img = Image.open("image\sari.png")
        # Resize gambar
        resized_brokat = brokat_img.resize((90, 90), Image.Resampling.LANCZOS)
        self.image_brokat = ImageTk.PhotoImage(resized_brokat)
        resized_sari = sari_img.resize((90, 90), Image.Resampling.LANCZOS)
        self.image_sari = ImageTk.PhotoImage(resized_sari)
        # Tampilkan gambar
        brokat_label = tk.Label(self, image=self.image_brokat, bg="white")
        brokat_label.place(x=140, y=120)
        sari_label = tk.Label(self, image=self.image_sari, bg="white")
        sari_label.place(x=260, y=120)
        # Buat button
        brokat_button = tk.Button(self, text="Kebaya Brokat", width=12, command=lambda: self.item_select('Wanita', 'Kebaya', 'Brokat', self.harga_barang['Wanita']['Kebaya']['Brokat']))
        brokat_button.place(x=140, y=230)
        sari_button = tk.Button(self, text="Kebaya Sari", width=12, command=lambda: self.item_select('Wanita', 'Kebaya', 'Sari', self.harga_barang['Wanita']['Kebaya']['Sari']))
        sari_button.place(x=260, y=230)
        # Isi harga
        brokat_price_label = tk.Label(self, text="Rp100.000,00", font=("Montserrat", 8), bg="white")
        brokat_price_label.place(x=150, y=260)
        sari_price_label = tk.Label(self, text="Rp90.000,00", font=("Montserrat", 8), bg="white")
        sari_price_label.place(x=270, y=260)
        
    def kamen_select(self):
        self.state = 'q12'
        # Sembunyikan elemen dari layar female select
        self.hide_content()
        
        # Tampilkan pilihan kamen
        kamen_label = tk.Label(self, text="Kamen jenis apa yang ingin anda beli?", font=("Montserrat", 14), bg="white")
        kamen_label.place(x=90, y=75)
        # Input gambar
        kamen_img = Image.open("image\kamen_f.png")
        lembar_img = Image.open("image\kamen_lembar.png")
        # Resize gambar
        resized_kamen = kamen_img.resize((90, 90), Image.Resampling.LANCZOS)
        self.image_kamen = ImageTk.PhotoImage(resized_kamen)
        resized_lembar = lembar_img.resize((90, 90), Image.Resampling.LANCZOS)
        self.image_lembar = ImageTk.PhotoImage(resized_lembar)
        # Tampilkan gambar
        kamen_label = tk.Label(self, image=self.image_kamen, bg="white")
        kamen_label.place(x=140, y=120)
        lembar_label = tk.Label(self, image=self.image_lembar, bg="white")
        lembar_label.place(x=260, y=120)
        # Buat button
        kamen_jadi_button = tk.Button(self, text="Kamen Jadi", width=12, command=lambda: self.item_select('Wanita', 'Kamen', 'Jadi', self.harga_barang['Wanita']['Kamen']['Jadi']))
        kamen_jadi_button.place(x=140, y=230)
        kamen_lembar_button = tk.Button(self, text="Kamen Lembar", width=12, command=lambda: self.item_select('Wanita', 'Kamen', 'Lembaran', self.harga_barang['Wanita']['Kamen']['Lembaran']))
        kamen_lembar_button.place(x=260, y=230)
        # Isi harga
        kamen_price_label = tk.Label(self, text="Rp150.000,00", font=("Montserrat", 8), bg="white")
        kamen_price_label.place(x=150, y=260)
        lembar_price_label = tk.Label(self, text="Rp110.000,00", font=("Montserrat", 8), bg="white")
        lembar_price_label.place(x=270, y=260)
        
    def selendang_f_select(self):
        self.state = 'q13'
        # Sembunyikan elemen dari layar female select
        self.hide_content()
        
        # Tampilkan pilihan selendang
        selendang_label = tk.Label(self, text="Selendang jenis apa yang ingin anda beli?", font=("Montserrat", 14), bg="white")
        selendang_label.place(x=80, y=75)
        # Input gambar
        motif_img = Image.open("image\selendang_f.png")
        polos_img = Image.open("image\selendang_polos.png")
        # Resize gambar
        resized_motif = motif_img.resize((90, 90), Image.Resampling.LANCZOS)
        self.image_motif = ImageTk.PhotoImage(resized_motif)
        resized_polos = polos_img.resize((90, 90), Image.Resampling.LANCZOS)
        self.image_polos = ImageTk.PhotoImage(resized_polos)
        # Tampilkan gambar
        motif_label = tk.Label(self, image=self.image_motif, bg="white")
        motif_label.place(x=140, y=120)
        polos_label = tk.Label(self, image=self.image_polos, bg="white")
        polos_label.place(x=260, y=120)
        # Buat button
        selendang_motif_button = tk.Button(self, text="Motif", width=12, command=lambda: self.item_select('Wanita', 'Selendang', 'Motif', self.harga_barang['Wanita']['Selendang']['Motif']))
        selendang_motif_button.place(x=140, y=230)
        selendang_polos_button = tk.Button(self, text="Polos", width=12, command=lambda: self.item_select('Wanita', 'Selendang', 'Polos', self.harga_barang['Wanita']['Selendang']['Polos']))
        selendang_polos_button.place(x=260, y=230)
        # Input harga
        motif_price_label = tk.Label(self, text="Rp25.000,00", font=("Montserrat", 8), bg="white")
        motif_price_label.place(x=150, y=260)
        polos_price_label = tk.Label(self, text="Rp15.000,00", font=("Montserrat", 8), bg="white")
        polos_price_label.place(x=270, y=260)
    
    def baju_adat_select(self):
        self.state = 'q7'
        # Sembunyikan elemen dari layar male select
        self.hide_content()
        
        # Tampilkan pilihan selendang
        baju_adat_label = tk.Label(self, text="Baju adat jenis apa yang ingin anda beli?", font=("Montserrat", 14), bg="white")
        baju_adat_label.place(x=80, y=75)
        # Input gambar
        safari_img = Image.open("image\safari.png")
        kemeja_img = Image.open("image\kemeja.png")
        # Resize gambar
        resized_safari = safari_img.resize((90, 90), Image.Resampling.LANCZOS)
        self.image_safari = ImageTk.PhotoImage(resized_safari)
        resized_kemeja = kemeja_img.resize((90, 90), Image.Resampling.LANCZOS)
        self.image_kemeja = ImageTk.PhotoImage(resized_kemeja)
        # Tampilkan gambar
        safari_label = tk.Label(self, image=self.image_safari, bg="white")
        safari_label.place(x=140, y=120)
        kemeja_label = tk.Label(self, image=self.image_kemeja, bg="white")
        kemeja_label.place(x=260, y=120)
        # Buat button
        safari_button = tk.Button(self, text="Safari", width=12, command=lambda: self.item_select('Pria', 'Baju Adat', 'Safari', self.harga_barang['Pria']['Baju Adat']['Safari']))
        safari_button.place(x=140, y=230)
        kemeja_button = tk.Button(self, text="Kemeja", width=12, command=lambda: self.item_select('Pria', 'Baju Adat', 'Kemeja', self.harga_barang['Pria']['Baju Adat']['Kemeja']))
        kemeja_button.place(x=260, y=230)
        # Input harga
        safari_price_label = tk.Label(self, text="Rp100.000,00", font=("Montserrat", 8), bg="white")
        safari_price_label.place(x=150, y=260)
        kemeja_price_label = tk.Label(self, text="Rp90.000,00", font=("Montserrat", 8), bg="white")
        kemeja_price_label.place(x=270, y=260)
        
    def udeng_select(self):
        self.state = 'q8'
        # Sembunyikan elemen dari layar male select
        self.hide_content()
        
        # Tampilkan pilihan udeng
        udeng_label = tk.Label(self, text="Udeng jenis apa yang ingin anda beli?", font=("Montserrat", 14), bg="white")
        udeng_label.place(x=80, y=75)
        # Input gambar
        udeng_jadi_img = Image.open("image\m_udeng_jadi.png")
        udeng_lembar_img = Image.open("image\m_udeng_lembar.png")
        # Resize gambar
        resized_udeng_jadi = udeng_jadi_img.resize((90, 90), Image.Resampling.LANCZOS)
        self.image_udeng_jadi = ImageTk.PhotoImage(resized_udeng_jadi)
        resized_udeng_lembar = udeng_lembar_img.resize((90, 90), Image.Resampling.LANCZOS)
        self.image_udeng_lembar = ImageTk.PhotoImage(resized_udeng_lembar)
        # Tampilkan gambar
        udeng_jadi_label = tk.Label(self, image=self.image_udeng_jadi, bg="white")
        udeng_jadi_label.place(x=140, y=120)
        udeng_lembar_label = tk.Label(self, image=self.image_udeng_lembar, bg="white")
        udeng_lembar_label.place(x=260, y=120)
        # Buat button
        udeng_jadi_button = tk.Button(self, text="Udeng Jadi", width=12, command=lambda: self.item_select('Pria', 'Udeng', 'Jadi', self.harga_barang['Pria']['Udeng']['Jadi']))
        udeng_jadi_button.place(x=140, y=230)
        udeng_lembar_button = tk.Button(self, text="Udeng Lembaran", width=12, command=lambda: self.item_select('Pria', 'Udeng', 'Lembaran', self.harga_barang['Pria']['Udeng']['Lembaran']))
        udeng_lembar_button.place(x=260, y=230)
        # Input harga
        jadi_price_label = tk.Label(self, text="Rp55.000,00", font=("Montserrat", 8), bg="white")
        jadi_price_label.place(x=150, y=260)
        lembar_price_label = tk.Label(self, text="Rp40.000,00", font=("Montserrat", 8), bg="white")
        lembar_price_label.place(x=270, y=260)
    
    def kamen_saput_select(self):
        self.state = 'q9'
        # Sembunyikan elemen dari layar male select
        self.hide_content()
        
        # Tampilkan pilihan selendang
        kamen_label = tk.Label(self, text="Kamen & saput jenis apa yang ingin anda beli?", font=("Montserrat", 14), bg="white")
        kamen_label.place(x=60, y=75)
        # Input gambar
        kamen_jadi_img = Image.open("image\kamen_m.png")
        kamen_lembar_img = Image.open("image\kamen_lembar_m.png")
        # Resize gambar
        resized_kamen_jadi = kamen_jadi_img.resize((90, 90), Image.Resampling.LANCZOS)
        self.image_kamen_jadi = ImageTk.PhotoImage(resized_kamen_jadi)
        resized_kamen_lembar = kamen_lembar_img.resize((90, 90), Image.Resampling.LANCZOS)
        self.image_kamen_lembar = ImageTk.PhotoImage(resized_kamen_lembar)
        # Tampilkan gambar
        kamen_jadi_label = tk.Label(self, image=self.image_kamen_jadi, bg="white")
        kamen_jadi_label.place(x=140, y=120)
        kamen_lembar_label = tk.Label(self, image=self.image_kamen_lembar, bg="white")
        kamen_lembar_label.place(x=260, y=120)
        # Buat button
        kamen_jadi_button = tk.Button(self, text="Setengah Jadi", width=12, command=lambda: self.item_select('Pria', 'Kamen', 'Setengah Jadi', self.harga_barang['Pria']['Kamen']['Setengah Jadi']))
        kamen_jadi_button.place(x=140, y=230)
        kamen_setjadi_button = tk.Button(self, text="Lembaran", width=12, command=lambda: self.item_select('Pria', 'Kamen', 'Lembaran', self.harga_barang['Pria']['Kamen']['Lembaran']))
        kamen_setjadi_button.place(x=260, y=230)
        # Input harga
        jadi_price_label = tk.Label(self, text="Rp85.000,00", font=("Montserrat", 8), bg="white")
        jadi_price_label.place(x=150, y=260)
        lembar_price_label = tk.Label(self, text="Rp80.000,00", font=("Montserrat", 8), bg="white")
        lembar_price_label.place(x=270, y=260)
    
    def selendang_m_select(self):
        self.state = 'q10'
        # Sembunyikan elemen dari layar male select
        self.hide_content()
        
        # Tampilkan pilihan selendang
        selendang_label = tk.Label(self, text="Selendang jenis apa yang ingin anda beli?", font=("Montserrat", 14), bg="white")
        selendang_label.place(x=70, y=75)
        # Input gambar
        motif_img = Image.open("image\selendang_m_motif.png")
        polos_img = Image.open("image\selendang_m_polos.png")
        # Resize gambar
        resized_motif = motif_img.resize((90, 90), Image.Resampling.LANCZOS)
        self.image_motif = ImageTk.PhotoImage(resized_motif)
        resized_polos = polos_img.resize((90, 90), Image.Resampling.LANCZOS)
        self.image_polos = ImageTk.PhotoImage(resized_polos)
        # Tampilkan gambar
        motif_label = tk.Label(self, image=self.image_motif, bg="white")
        motif_label.place(x=140, y=120)
        polos_label = tk.Label(self, image=self.image_polos, bg="white")
        polos_label.place(x=260, y=120)
        # Buat button
        selendang_motif_button = tk.Button(self, text="Motif", width=12, command=lambda: self.item_select('Pria', 'Selendang', 'Motif', self.harga_barang['Pria']['Selendang']['Motif']))
        selendang_motif_button.place(x=140, y=230)
        selendang_polos_button = tk.Button(self, text="Polos", width=12, command=lambda: self.item_select('Pria', 'Selendang', 'Polos', self.harga_barang['Pria']['Selendang']['Polos']))
        selendang_polos_button.place(x=260, y=230)
        # Input harga
        motif_price_label = tk.Label(self, text="Rp25.000,00", font=("Montserrat", 8), bg="white")
        motif_price_label.place(x=150, y=260)
        polos_price_label = tk.Label(self, text="Rp15.000,00", font=("Montserrat", 8), bg="white")
        polos_price_label.place(x=270, y=260)
    
    def item_select(self, jenis_kelamin, kategori, variasi, harga):
        self.pilihan_barang.append({'jenis_kelamin': jenis_kelamin, 'kategori': kategori, 'variasi': variasi, 'ukuran': self.ukuran, 'harga': harga})
        self.confirmation()
    
    def confirmation(self):
        self.state = 'q14, q15'
        # Sembunyikan elemen dari layar male select
        self.hide_content()
        
        # Tampilkan pilihan konfirmasi
        konfirmasi_label = tk.Label(self, text="Apakah anda sudah selesai belanja?", font=("Montserrat", 14), bg="white")
        konfirmasi_label.place(x=90, y=140)
        
        ya_button = tk.Button(self, text="Ya", width=12, command=self.nota)
        ya_button.place(x=140, y=180)

        tidak_button = tk.Button(self, text="Tidak", width=12, command=self.choice)
        tidak_button.place(x=260, y=180)
    
    def choice(self):
        if self.gender == "M":
            self.male_select()
        else:
            self.female_select()
            
    def nota(self):
        self.state = 'q16'
        # Sembunyikan elemen dari layarsebelumnya
        self.hide_content()
        
        # Buat frame
        self.nota_frame = tk.Frame(self, bg="white")
        self.nota_frame.pack(side='left', padx=30, pady=20)
        self.qr_frame = tk.Frame(self, bg="white")
        self.qr_frame.pack(side='right', padx=30, pady=20)

        # Menampilkan barang-barang yang dibeli
        nota_label = tk.Label(self.nota_frame, text="Nota Pembelian", font=("Montserrat", 14), bg="white")
        nota_label.pack(pady=7)

        for pembelian in self.pilihan_barang:
            detail_barang = f"{pembelian['jenis_kelamin']} - {pembelian['kategori']} ({pembelian['variasi']}, Ukuran: {pembelian['ukuran']}): Rp{pembelian['harga']}"
            detail_barang_label = tk.Label(self.nota_frame, text=detail_barang, font=("Montserrat", 8), bg="white")
            detail_barang_label.pack(anchor='w', pady=4)

        # Menampilkan total harga
        self.total_harga = sum(pembelian['harga'] for pembelian in self.pilihan_barang)
        total_harga_label = tk.Label(self.nota_frame, text=f"Total Harga: Rp{self.total_harga}", font=("Montserrat", 10), bg="white")
        total_harga_label.pack(anchor='w', pady=7)
        
        qr_img = Image.open("image\qr.png")
        # Resize gambar
        resized_qr = qr_img.resize((140, 140), Image.Resampling.LANCZOS)
        self.qr_image = ImageTk.PhotoImage(resized_qr)
        qr_label = tk.Label(self.qr_frame, image=self.qr_image)
        qr_label.pack(pady=10)

        # Tombol pembayaran
        bayar_button = tk.Button(self.qr_frame, text="Bayar", width=12, command=self.finish)
        bayar_button.pack(pady=10)
        
    def finish(self):
        self.state = 'q17'
        # Sembunyikan elemen dari layarsebelumnya
        for widget in self.winfo_children():
            widget.pack_forget()
        
        image = Image.open("image\cover.png")
        resized_image = image.resize((500, 350), Image.Resampling.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(resized_image)
        
        image = tk.Label(self, image=self.bg_image, bg="white")
        image.place(x=0, y=0)
        
        goodbye_label = tk.Label(self, text="Terima kasih telah berbelanja di\nVending Machine Baju Adat Otomatis", font=("Montserrat", 14), bg="#f5f5f5")
        goodbye_label.place(x=80, y=30)
        
        ambil_button = tk.Button(self, text="Ambil Barang", width=12, command=self.show_welcome_screen)
        ambil_button.place(x=200, y=300)
        
    def run(self):
        self.mainloop()
        
        
if __name__ == "__main__":
    vending_machine_gui = GUI()
    vending_machine_gui.run()