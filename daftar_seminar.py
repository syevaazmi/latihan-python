database_peserta = {}

print("\nDaftar Seminar")
print("1. Seminar Pengantar Pemrograman Python")
print("2. Seminar Pengantar UI/UX Design")

pilihan = input("Pilih jenis seminar yang ingin diikuti (1/2): ")
def daftar_peserta(nama, nim, telepon, email, pilihan_seminar):
    if (pilihan_seminar not in ['1', '2'] or 
        "@" not in email or 
        "." not in email or 
        not telepon.isdigit() or 
        len(telepon) < 10):
    
        print("Pendaftaran gagal! Mohon periksa kembali data yang Anda masukkan.")
        return
    
    database_peserta[email] = {
        'nama': nama,
        'nim': nim,
        'telepon': telepon,
        'seminar': pilihan_seminar,
        'status': 'sudah verifikasi'
    }
    
    print(f"Pendaftaran seminar {nama} berhasil!")

def cek_status(email):
    if email in database_peserta:
        print(f"Status Pendaftaran untuk {database_peserta[email]['nama']}: {database_peserta[email]['status']}")
    else:
        print("Email tidak terdaftar!")

nama = input('Nama Lengkap: ')
nim = input("NIM: ")
telepon = input("No HP: ")
email = input("Email: ")

daftar_peserta(nama, nim, telepon, email, pilihan)
email_cek = input("Masukkan Email untuk cek status pendaftaran: ")
cek_status(email_cek)


