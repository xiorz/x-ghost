import os,time
from rich.console import Console
from rich.table import Table

console = Console()

# Membuat tabel Rich
table = Table(title="\nMeng-install Paket Yang Dibutuhkan")
table.add_column("Paket", style="cyan")
table.add_row("yt-dlp")

time.sleep(2)

console.print(table)


# Input URL dari user
os.system("clear")
URL = console.input("[bold cyan]Masukkan URL: [/bold cyan]")

# Buat folder jika belum ada
os.system("mkdir -p /sdcard/YTMp3/download/")

# Unduh audio dari YouTube
os.system(f'yt-dlp -f bestaudio --extract-audio --audio-format mp3 -o "/sdcard/YTMp3/download/%(title)s.%(ext)s" "{URL}"')
console.print("[bold green]\nDownload selesai! Cek di folder: [/bold green]/sdcard/YTMp3/download/")