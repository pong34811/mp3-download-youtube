import yt_dlp

def download_mp3(youtube_url):
    # การตั้งค่าต่างๆ สำหรับการดาวน์โหลดไฟล์ MP3
    ydl_opts = {
        'format': 'bestaudio/best',  # เลือกคุณภาพเสียงดีที่สุด
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # ใช้ ffmpeg เพื่อแปลง
            'preferredcodec': 'mp3',  # กำหนด codec เป็น mp3
            'preferredquality': '192',  # กำหนดคุณภาพที่ 192kbps
        }],

        'outtmpl': '%(title)s.%(ext)s',  # ตั้งชื่อไฟล์ให้เป็นชื่อของเพลง
        'noplaylist': True,  # ปิดการดาวน์โหลด Playlist (ถ้ามี)
        'quiet': False,  # กำหนดให้มีการแสดงข้อความในระหว่างดาวน์โหลด
        'extractaudio': True,  # ทำการแยกเสียงจากวิดีโอ
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
            print(f"ดาวน์โหลดเพลงจาก {youtube_url} สำเร็จ")
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

# ตัวอย่างการใช้งาน
youtube_url = input("กรุณากรอก URL ของ YouTube: ")
download_mp3(youtube_url)