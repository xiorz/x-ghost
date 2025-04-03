import requests
import datetime
from rich import print
from rich.table import Table
from rich.console import Console

console = Console()

# API Data Wilayah
API_PROVINSI = "https://emsifa.github.io/api-wilayah-indonesia/api/provinces.json"
API_KABKOT = "https://emsifa.github.io/api-wilayah-indonesia/api/regencies/{}.json"
API_KECAMATAN = "https://emsifa.github.io/api-wilayah-indonesia/api/districts/{}.json"

def ambil_data(api_url):
    """ Mengambil data wilayah dari API """
    try:
        response = requests.get(api_url)
        return response.json() if response.status_code == 200 else None
    except requests.exceptions.RequestException:
        return None

def cari_nama(id_wilayah, data):
    """ Mencari nama wilayah berdasarkan ID """
    if not data:
        return "[red]❌ Data tidak ditemukan[/red]"
    
    for item in data:
        if str(item["id"]) == str(id_wilayah):
            return item["name"]
    
    return "[red]❌ Tidak ditemukan[/red]"

def cek_nik(nik):
    """ Memeriksa dan mengurai NIK """
    if not nik.isdigit() or len(nik) != 16:
        return "[bold red]❌ NIK tidak valid! Harus 16 digit angka.[/bold red]"

    # Ekstrak data dari NIK
    kode_provinsi = nik[:2]
    kode_kabkot = nik[:4]
    kode_kecamatan = nik[:6]
    tanggal = int(nik[6:8])
    bulan = int(nik[8:10])
    tahun = int(nik[10:12]) + 1900  # Asumsi lahir sebelum 2000
    uniqcode = nik[12:]

    # Koreksi tahun jika lebih masuk akal lahir setelah 2000
    if tahun < 1950:
        tahun += 100

    # Tentukan jenis kelamin
    if tanggal > 40:
        tanggal -= 40
        jenis_kelamin = "[bold magenta]👩 Perempuan[/bold magenta]"
    else:
        jenis_kelamin = "[bold blue]👨 Laki-laki[/bold blue]"

    # Validasi tanggal lahir
    try:
        datetime.date(tahun, bulan, tanggal)
    except ValueError:
        return "[bold red]❌ Tanggal lahir tidak valid![/bold red]"

    # Ambil data provinsi
    data_provinsi = ambil_data(API_PROVINSI)
    nama_provinsi = cari_nama(kode_provinsi, data_provinsi) if data_provinsi else "[red]⚠ Gagal mengambil data[/red]"

    # Ambil data kabupaten/kota
    data_kabkot = ambil_data(API_KABKOT.format(kode_provinsi))
    nama_kabkot = cari_nama(kode_kabkot, data_kabkot) if data_kabkot else "[red]⚠ Gagal mengambil data[/red]"

    # Ambil data kecamatan
    data_kecamatan = ambil_data(API_KECAMATAN.format(kode_kabkot))
    nama_kecamatan = cari_nama(kode_kecamatan, data_kecamatan) if data_kecamatan else "[red]⚠ Gagal mengambil data[/red]"

    # Menampilkan hasil dalam tabel
    table = Table(title="[cyan]📌 Hasil Cek NIK[/cyan]", style="bold magenta")
    table.add_column("Keterangan", style="yellow", justify="left", no_wrap=True)
    table.add_column("Data", style="green", justify="center")

    table.add_row("📆 Tanggal Lahir", f"{tanggal}/{bulan}/{tahun}")
    table.add_row("🚻 Jenis Kelamin", jenis_kelamin)
    table.add_row("🌍 Provinsi", nama_provinsi)
    table.add_row("🏙️ Kab/Kota", nama_kabkot)
    table.add_row("🏠 Kecamatan", nama_kecamatan)
    table.add_row("🔢 Kode Unik", uniqcode)

    return table  # Kembalikan tabel, bukan print langsung!

# Program utama
console.print("[bold cyan]🔍 Masukkan NIK: [/bold cyan]", end="")
nik = input()
hasil = cek_nik(nik)  # Ambil hasilnya
console.print(hasil)  # Cetak tabel hasilnya