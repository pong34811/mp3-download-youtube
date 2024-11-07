import tkinter as tk
from tkinter import messagebox
import yt_dlp
import threading
import pyperclip

def download_mp3():
    youtube_url = url_entry.get()
    if not youtube_url:
        messagebox.showwarning("Warning", "กรุณากรอก URL ของ YouTube")
        return

    # แสดงข้อความ Loading ใน Log
    log_text.insert(tk.END, "กำลังดาวน์โหลด...\n")
    log_text.see(tk.END)  # เลื่อนลงไปที่ข้อความล่าสุด
    download_button.config(state=tk.DISABLED)  # ปิดปุ่มดาวน์โหลด

    # การตั้งค่าต่างๆ สำหรับการดาวน์โหลดไฟล์ MP3
    ydl_opts = {
        'format': 'bestaudio/best',  # เลือกคุณภาพเสียงดีที่สุด
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # ใช้ ffmpeg เพื่อแปลง
            'preferredcodec': 'mp3',  # กำหนด codec เป็น mp3
            'preferredquality': '192',  # กำหนดคุณภาพที่ 192kbps
        }],
        'ffmpeg_location': r'C:\ffmpeg\bin\ffmpeg.exe',  # ระบุพาธของ ffmpeg (ใช้ raw string)
        'outtmpl': '%(title)s.%(ext)s',  # ตั้งชื่อไฟล์ให้เป็นชื่อของเพลง
        'noplaylist': True,  # ปิดการดาวน์โหลด Playlist (ถ้ามี)
        'quiet': False,  # กำหนดให้มีการแสดงข้อความในระหว่างดาวน์โหลด
        'extractaudio': True,  # ทำการแยกเสียงจากวิดีโอ
    }

    def run_download():
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([youtube_url])
            log_text.insert(tk.END, f"ดาวน์โหลดเพลงจาก {youtube_url} สำเร็จ\n")
        except Exception as e:
            log_text.insert(tk.END, f"เกิดข้อผิดพลาด: {e}\n")
        finally:
            download_button.config(state=tk.NORMAL)  # เปิดปุ่มดาวน์โหลดอีกครั้ง

    # เริ่มการดาวน์โหลดใน thread ใหม่
    threading.Thread(target=run_download).start()

def paste_url():
    # นำ URL จากคลิปบอร์ดมาวางใน Entry
    url_entry.delete(0, tk.END)  # ลบข้อความเดิมใน Entry
    url_entry.insert(0, pyperclip.paste())  # วางข้อความจากคลิปบอร์ด

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("YouTube MP3 Downloader")
root.configure(bg="#2C3E50")  # เปลี่ยนสีพื้นหลัง
root.resizable(False, False)  # ทำให้ไม่สามารถขยายหน้าต่างได้

# คำนวณตำแหน่งเพื่อให้หน้าต่างอยู่ตรงกลาง
window_width = 400
window_height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# ตั้งค่า geometry ของหน้าต่าง
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# สร้าง Label ```python
label = tk.Label(root, text="กรุณากรอก URL ของ YouTube:", bg="#2C3E50", fg="white", font=("Helvetica", 12))
label.pack(pady=10)

# สร้าง Entry สำหรับกรอก URL
url_entry = tk.Entry(root, width=50, font=("Helvetica", 12))
url_entry.pack(pady=5)

# สร้างปุ่ม "วาง URL"
paste_button = tk.Button(root, text="วาง URL จากคลิปบอร์ด", command=paste_url, bg="#3498DB", fg="white", font=("Helvetica", 12))
paste_button.pack(pady=5)

# สร้างปุ่มดาวน์โหลด
download_button = tk.Button(root, text="ดาวน์โหลด MP3", command=download_mp3, bg="#3498DB", fg="white", font=("Helvetica", 12))
download_button.pack(pady=20)

# สร้าง Text widget สำหรับแสดง Log
log_text = tk.Text(root, height=8, width=50, bg="#34495E", fg="white", font=("Helvetica", 12))
log_text.pack(pady=10)
log_text.config(state=tk.NORMAL)  # ทำให้ Text widget สามารถแก้ไขได้

# เริ่มต้น GUI
root.mainloop()