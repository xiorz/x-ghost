import requests
import random
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
    """Mengambil data dari API"""
    try:
        response = requests.get(api_url)
        return response.json() if response.status_code == 200 else None
    except requests.exceptions.RequestException:
        return None

def pilih_wilayah(data, nama_wilayah):
    """Menampilkan daftar wilayah untuk dipilih pengguna"""
    if not data:
        console.print(f"[red]❌ Gagal mengambil data {nama_wilayah}![/red]")
        return None, None

    table = Table(title=f"📍 Pilih {nama_wilayah}", show_lines=True)
    table.add_column("No", justify="center", style="cyan")
    table.add_column("Nama", style="yellow")

    for i, item in enumerate(data, start=1):
        table.add_row(str(i), item["name"])

    console.print(table)

    while True:
        try:
            pilihan = int(input(f"Masukkan nomor {nama_wilayah}: ")) - 1
            if 0 <= pilihan < len(data):
                return data[pilihan]["id"], data[pilihan]["name"]
            else:
                console.print("[bold red]❌ Pilihan tidak valid![/bold red]")
        except ValueError:
            console.print("[bold red]⚠ Harap masukkan angka yang benar.[/bold red]")

def buat_nik():
    console.print("[bold cyan]🔍 Mengambil data wilayah...[/bold cyan]")

    # Pilih wilayah
    data_provinsi = ambil_data(API_PROVINSI)
    id_prov, nama_prov = pilih_wilayah(data_provinsi, "Provinsi")

    data_kabkot = ambil_data(API_KABKOT.format(id_prov))
    id_kabkot, nama_kabkot = pilih_wilayah(data_kabkot, "Kabupaten/Kota")

    data_kecamatan = ambil_data(API_KECAMATAN.format(id_kabkot))
    id_kecamatan, nama_kecamatan = pilih_wilayah(data_kecamatan, "Kecamatan")

    if not id_prov or not id_kabkot or not id_kecamatan:
        console.print("[red]⚠ Gagal mendapatkan wilayah yang dipilih![/red]")
        return

    # Pastikan kode kecamatan tepat 6 digit (dipotong jika lebih panjang)
    id_kecamatan = id_kecamatan[:6].ljust(6, "0")

    # Pilih jenis kelamin
    console.print("\n[bold cyan]Pilih Jenis Kelamin:[/bold cyan]")
    console.print("1️⃣ Laki-laki")
    console.print("2️⃣ Perempuan")
    console.print("3️⃣ Acak")

    while True:
        pilih_gender = input("Masukkan nomor pilihan: ")
        if pilih_gender == "1":
            jenis_kelamin = "[bold blue]👨 Laki-laki[/bold blue]"
            tambah_tgl = 0
            break
        elif pilih_gender == "2":
            jenis_kelamin = "[bold magenta]👩 Perempuan[/bold magenta]"
            tambah_tgl = 40
            break
        elif pilih_gender == "3":
            if random.choice([True, False]):
                jenis_kelamin = "[bold blue]👨 Laki-laki[/bold blue]"
                tambah_tgl = 0
            else:
                jenis_kelamin = "[bold magenta]👩 Perempuan[/bold magenta]"
                tambah_tgl = 40
            break
        else:
            console.print("[red]❌ Pilihan tidak valid! Pilih 1, 2, atau 3.[/red]")

    # Buat tanggal lahir acak
    tahun = random.randint(1970, 2020)
    bulan = random.randint(1, 12)
    hari = random.randint(1, 28)  # Aman untuk semua bulan
    hari_lahir = hari + tambah_tgl

    # Pastikan hari_lahir tetap 2 digit
    hari_lahir = f"{hari_lahir:02}"

    # Buat kode unik 4 digit
    kode_unik = str(random.randint(1000, 9999))

    # Format tahun (ambil 2 digit terakhir)
    tahun_str = str(tahun)[-2:]

    # Buat NIK (16 digit)
    nik = f"{id_kecamatan}{hari_lahir}{bulan:02}{tahun_str}{kode_unik}"

    # **PERBAIKAN PENTING**: Pastikan panjang NIK tetap 16 digit
    if len(nik) != 16:
        nik = nik[:16]  # Jika lebih panjang, potong hingga 16 digit
    elif len(nik) < 16:
        nik = nik.ljust(16, "0")  # Jika kurang, tambahkan nol di akhir

    # Tampilkan hasil dalam tabel
    table = Table(title="[green]✅ NIK Palsu Dibuat[/green]", style="bold magenta")
    table.add_column("Keterangan", style="yellow", justify="left", no_wrap=True)
    table.add_column("Data", style="green", justify="center")

    table.add_row("📆 Tanggal Lahir", f"{hari}/{bulan}/{tahun}")
    table.add_row("🚻 Jenis Kelamin", jenis_kelamin)
    table.add_row("🌍 Provinsi", nama_prov)
    table.add_row("🏙️ Kab/Kota", nama_kabkot)
    table.add_row("🏠 Kecamatan", nama_kecamatan)
    table.add_row("🔢 Kode Unik", kode_unik)
    table.add_row("🆔 NIK", f"[bold cyan]{nik}[/bold cyan]")

    console.print(table)

# Jalankan program
buat_nik()