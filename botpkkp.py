import telebot,pymysql,datetime,random
token = "YourOwnAPI"
bot = telebot.TeleBot(token=token,threaded=False)

def connect(sql):
	con=pymysql.connect(host='localhost',user='root',password='',db='pkkp')
	a=con.cursor()
	a.execute(sql)
	return con,a

def select(tabel,column,ids):
	con,a=connect(f"Select * from {tabel} where {column}={ids}")
	con=a.fetchall()
	return con

def select_berita():
	con,a=connect(f"Select berita_judul,berita_text from pkkp_berita")
	con=a.fetchall()
	return con

def insert_daftar(ids):
	con,_=connect(f"Insert into pkkp_daftar(daftar_idtele,daftar_status) values({ids},'tidak')")
	con.commit()
	con.close()

def insert_history(ids,tipe,chat):
	con,_=connect(f"Insert into pkkp_history(history_chat,daftar_idtele,key_id) values('{chat}',{ids},{tipe})")
	con.commit()
	con.close()

def update_key(ids):
	con,_=connect(f"Update pkkp_key set key_count=key_count + 1 where key_id={ids}")
	con.commit()
	con.close()

def update_daftar(ids,nama,email,jk):
	con,_=connect(f"Update pkkp_daftar set daftar_nama='{nama}', daftar_email='{email}', daftar_jk='{jk}' where daftar_idtele={ids}")
	con.commit()
	con.close()

def update_foto(ids,foto,fotoid):
	con,_=connect(f"Update pkkp_daftar set daftar_foto='{foto}', daftar_fotoid='{fotoid}' where daftar_idtele={ids}")
	con.commit()
	con.close()

def checkdaftar(ids,tipe,chat):
	try:
		insert_daftar(ids)
	except:
		pass
	insert_history(ids,tipe,chat)
	update_key(tipe)

@bot.message_handler(commands=["start"])
def welcome(message):
	checkdaftar(message.chat.id,1,message.text)
	teks = f"""
Selamat datang {message.from_user.first_name} 😃

Ini adalah bot PKKP 2021 yang dibuat oleh Aldhiya Rozak guna untuk menyelesaikan tugas kuliah.

Terimakasih kepada bapak Ajib Susanto M.Kom yang telah memberi tugas ini, karena dengan begitu saya belajar banyak tentang topik yang diberikan.

Informasi bot ini dapat diliat di menu /bantuan.

Untuk informasi bot lainnya bisa kunjungi bot yang telah dibuat oleh Aldhiya Rozak, @Bejjox_bot.
"""
	bot.send_message(message.chat.id,teks)

@bot.message_handler(commands=["hey"])
def hey(message):
	checkdaftar(message.chat.id,2,message.text)
	teks = f"""
Hello {message.from_user.first_name},

untuk saat ini bot hanya bisa merespon percakapan sederhana saja.
Bot bisa saja menjawab pertanyaan dengan bantuan google, jika ingin bantuan google sertakan kata "google" diawal pesan.
Untuk membantu bot lebih banyak lagi silahkan berikan /saran.
"""
	bot.send_message(message.chat.id,teks)

@bot.message_handler(commands=["tolong"])
def tolong(message):
	checkdaftar(message.chat.id,3,message.text)
	teks = f"""
Hello {message.from_user.first_name},

kamu dapat menemukan semua menu bot ini pada menu /bantuan, namun jika perlu bantuan lebih lanjut lagi silahkan kontak @Bejjoeqq.
"""
	bot.send_message(message.chat.id,teks)

@bot.message_handler(commands=["bantuan"])
def bantuan(message):
	checkdaftar(message.chat.id,4,message.text)
	teks = f"""
Hello {message.from_user.first_name},

<b>Beberapa menu yang tersedia di bot ini :</b>
/start : untuk memulai chat
/hey : untuk menyapa
/tolong : untuk kontak owner
/bantuan : untuk informasi seputar menu bot
/saran : untuk memberikan saran kepada owner
/info : untuk informasi seputar PKKP 2021
/daftar : untuk mendaftar dan mengedit PKKP 2021
/foto : untuk mengupload foto PKKP 2021
/status : untuk melihat status data
/hasil : untuk informasi hasil PKKP 2021
/materi : untuk informasi materi ujian
/pembekalan : untuk informasi pembekalan
/syarat : untuk informasi syarat pendaftaran
"""
	bot.send_message(message.chat.id,teks,parse_mode="html")

@bot.message_handler(commands=["saran"])
def sarannn(message):
	checkdaftar(message.chat.id,5,message.text)
	if message.text.lower() != "/saran":
		last = message.from_user.last_name
		usrn = message.from_user.username
		if message.from_user.last_name is None:
			last = ""
		if message.from_user.username is None:
			usrn = ""
			
		if len(message.text)<4095:
			bot.send_message("1309620134","Nama: "+message.from_user.first_name+" "+last+"\nUsername: "+usrn+"\nPesan: "+message.text+"\n\n"+str(datetime.datetime.now()))
			bot.reply_to(message,"Terima kasih, itu pasti sangat membantuku ❤️")
		else:
			bot.send_message("1309620134","Nama: "+message.from_user.first_name+" "+last+"\nUsername: "+usrn+"\nPesan: "+message.text[:4000]+"\n\n"+str(datetime.datetime.now()))
			bot.reply_to(message,"Terima kasih, itu pasti sangat membantuku ❤️")
	else:
		bot.reply_to(message,f"Hello {message.from_user.first_name},\n\n<b>Cara penggunaan</b>\n/saran isi pesan",parse_mode="html")

@bot.message_handler(commands=["info"])
def infoo(message):
	checkdaftar(message.chat.id,6,message.text)
	teks = f"""
Hello {message.from_user.first_name},

Program Pengembangan Kepedulian dan Kepeloporan Pemuda (PKKP) merupakan program unggulan Dinas Kepemudaan, evadengan tujuan untuk mengakselerasikan pembangunan khususnya dipedesaan yang masuk zona merah di 15 Kabupaten melalui peran kepeloporan pemuda dalam berbagai aktivitas kepemudaan. Aktivitas tersebut secara langsung harus berpengaruh terhadap dinamisasi kehidupan pemuda desa, pengembangan potensi sumber daya kepemudaan, dan sekaligus meningkatkan kesejahteraan pemuda dan masyarakat desa. Melalui program PKKP ini, diharapkan dapat meningkatkan peran dan kemampuan pemuda dalam bidang kepemimpinan, kemandirian dan kepeloporan serta kewirausahaan pemuda khususnya pemuda sarjana sebagai implementasi dari Undang-Undang Nomor 40 Tahun 2009 tentang Kepemudaan.
"""
	bot.send_message(message.chat.id,teks)

@bot.message_handler(commands=["daftar"])
def daftarr(message):
	checkdaftar(message.chat.id,7,message.text)
	ids = message.chat.id
	data = select("pkkp_daftar","daftar_idtele",ids)[0]
	if message.text.lower() != "/daftar":
		teks = message.text.lower().split("\n")
		nama = teks[1].title()
		email = teks[2]
		jk = teks[3]
		if jk == "mr":
			jk = "Laki-Laki"
		elif jk == "mrs":
			jk = "Perempuan"
		else:
			jk = "-"

		update_daftar(ids,nama,email,jk)
		bot.send_message(message.chat.id,"Data berhasil diperbaharui")
	else:
		nama=""
		email=""
		jk=""
		foto=""
		if data[1]:
			nama = data[1]
		if data[2]:
			email = data[2]
		if data[3]:
			jk = data[3]
		if data[4]:
			foto = "Uploaded"
		teks = f"<b>Data Anda</b>\nNama : {nama}\nEmail : {email}\nJenis Kelamin : {jk}\nFoto : {foto}"
		bot.reply_to(message,f"{teks}\n\n<b>Cara Penggunaan</b>\n/daftar\nNama Lengkap\nEmail\nJenis Kelamin(mr/mrs)",parse_mode="html")

@bot.message_handler(commands=["foto"])
def fotoo(message):
	checkdaftar(message.chat.id,8,message.text)
	teks = ""
	data = select("pkkp_daftar","daftar_idtele",message.chat.id)[0]
	try:
		teks = "Foto sudah diupload.\n\n"
		bot.send_photo(message.chat.id, data[5])
	except Exception as e:
		print(e)
		teks = "Foto belum diupload.\n\n"
	ms = bot.send_message(message.chat.id, f"{teks}Silahkan upload foto anda (maks : 100kb)(pastikan berbentuk foto, tidak document) : ")
	bot.register_next_step_handler(ms,uploaded)
def uploaded(message):
	try:
		file = message.photo[-1]
		file_info = bot.get_file(file.file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		if int(file.file_size)<=100000:
			with open(f'foto/{message.chat.id}.png', 'wb') as new_file:
				new_file.write(downloaded_file)
				update_foto(message.chat.id,f"{message.chat.id}.png",file.file_id)
				bot.send_message(message.chat.id,"Berhasil upload foto")
		else:
			bot.send_message(message.chat.id,"Ukuran file lebih dari 100kb")
	except:
		bot.send_message(message.chat.id,"Gagal mengupload foto")


@bot.message_handler(commands=["hasil"])
def hasill(message):
	checkdaftar(message.chat.id,9,message.text)
	doc = open('file/Hasil 2020.pdf', 'rb')
	teks = f"""
Hello {message.from_user.first_name},

Hasil seleksi PKKP 2021 akan diumumkan segera, berikut lampiran hasil PKKP 2020.
"""
	bot.send_message(message.chat.id,teks)
	bot.send_chat_action(message.chat.id, 'upload_document')
	bot.send_document(message.chat.id, doc)


@bot.message_handler(commands=["materi"])
def materii(message):
	checkdaftar(message.chat.id,10,message.text)
	doc1 = open('file/Materi Kepeloporan Pemuda dalam Masyarakat.pdf', 'rb')
	doc2 = open('file/Materi Pemberdayaan Masyarakat Pedesaan.pdf', 'rb')
	teks = f"""
Hello {message.from_user.first_name},

Berikut adalah lampiran materi PKKP 2021, silahkan mendownload file tersebut.
"""
	bot.send_message(message.chat.id,teks)
	bot.send_chat_action(message.chat.id, 'upload_document')
	bot.send_document(message.chat.id, doc1)
	bot.send_chat_action(message.chat.id, 'upload_document')
	bot.send_document(message.chat.id, doc2)

@bot.message_handler(commands=["pembekalan"])
def pembekalann(message):
	checkdaftar(message.chat.id,11,message.text)
	doc = open('file/Pembekalan 2021.pdf', 'rb')
	teks=f"""
Hello {message.from_user.first_name},

Dinas Pemuda dan Olahraga Provinsi Jawa Tengah memberikan pembekalan dalam Kegiatan Pengembangan Kepedulian dan Kepeloporan Pemuda (PKKP) Provinsi Jawa Tengah Tahun 2021 dengan maksud dan tujuan Memberikan informasi kepada peserta mengenai kegiatan Pengembangan Kepedulian dan Kepeloporan Pemuda (PKKP) Provinsi Jawa Tengah Tahun 2021, kegiatan ini memberikan informasi tentang Peran, Fungsi dan Tugas PKKP di desa penempatan, Menumbuhkan semangat nasionalisme dan pengabdian kepada masyarakat, Menumbuhkan mental disiplin, berbudi pekerti dan wawasan kebangsaaan. 

Acara dilaksanakan pada hari senin s.d. rabu tanggal 23 s.d. 25 pebruari 2021 bertempat di Wisma PKBI Jawa Tengah Jl. Jembawan Raya No. 8-12 Semarang dengan jumlah Peserta 50 (lima puluh) orang yang merupakan Peserta PKKP Provinsi Jawa Tengah Tahun 2021 yang akan ditugaskan di 25 desa di 15 kabupaten di Jawa Tengah.Hadir sebagai narasumber dalam kegiatan ini Tim Teknis PKKP Provinsi Jawa Tengah, Universitas Dian Nuswantoro Semarang, Universitas Diponegoro Semarang, SMK Negeri 6 Semarang, Forum Purna PSP-3 Jawa Tengah' Forum Purna SP-3 Jawa Tengah' Motivator Tim Outbond KWARDA Pramuka Jateng. 

Kegiatan ini dibuka secara langsung oleh ibu rihayati kabid pemuda dinpora prov.jateng, beberapa hal disampaikan dalam sambutan bahwa Bentuk penugasan PKKP bersifat perorangan, namun bekerja secara tim atau kelompok dalam lingkup desa, kecamatan dan kabupaten/Kota. Dalam Penugasan PKKP akan melakukan 3 (tiga) tugas utama yaitu menggerakkan, mendampingi serta mengembangkan kemandirian Oleh karena begitu beratnya tugas PKKP ini maka diperlukan dukungan dari berbagai pihak agar dapat berjalan baik, lancar dan mendapat hasil yang kita harapkan. 
"""
	bot.send_message(message.chat.id,teks,parse_mode="html")
	bot.send_chat_action(message.chat.id, 'upload_document')
	bot.send_document(message.chat.id,doc)


@bot.message_handler(commands=["syarat"])
def syaratt(message):
	checkdaftar(message.chat.id,12,message.text)
	doc = open('file/Pedoman Umum.pdf', 'rb')
	teks=f"""
Hello {message.from_user.first_name},

<b>Syarat Peserta</b>
Peserta Program PKKP Tahun 2021 adalah pemuda sarjana yang memiliki persyaratan sebagai berikut : 
a. Penduduk Provinsi Jawa Tengah, dibuktikan dengan memiliki KTP Provinsi Jawa Tengah. 
b. Usia maksimal 28 tahun pada tanggal 1 Maret 2021. 
c. Pendidikan S-1 semua jurusan dengan IPK > 2,75.
d. Sehat Jasmani dan Rohani yang dibuktikan dengan Surat Keterangan Sehat dari Dokter Pemerintah setempat.
e. Berkelakuan baik yang dibuktikan dengan Surat Keterangan Catatan Kepolisian (SKCK) dari kepolisian setempat.
f. Belum menikah dan bersedia tidak menikah selama menjalani masa kontrak dengan dibuktikan dengan Surat Pernyataan dan diketahui Kepala Desa calon peserta.
g. Tidak terikat kontrak kerja pada lembaga/instansi manapun selama menjadi peserta PKKP, dibuktikan dengan surat pernyataan.
h. Tidak menuntut diangkat menjadi CPNS.
i. Bersedia menandatangani kontrak kerja dan bersedia ditempatkan di desa lokasi penugasan/penempatan dan tidak meninggalkan desa lokasi penugasan selama masa kontrak.
j. Lulus seleksi penerimaan PKKP.
k. Mempunyai kemampuan menulis dan mendokumentasikan laporan melalui teknologi informatika (internet).
l. Tidak sedang menjalani pendidikan S2 atau telah terdaftar sebagai mahasiswa S2 di Universitas Negeri atau Swasta manapun.
m. Bersedia mengikuti pembekalan sebelum ditempatkan di desa penempatan.
n. Penyandang disabilitas dapat mengikuti apabila tidak mengganggu aktifitas sehari-hari dan atau dapat bekerja.

Selengkapnya bisa mendownload file Pedoman Umum berikut.
"""
	bot.send_message(message.chat.id,teks,parse_mode="html")
	bot.send_chat_action(message.chat.id, 'upload_document')
	bot.send_document(message.chat.id, doc)

@bot.message_handler(commands=["berita"])
def beritaa(message):
	checkdaftar(message.chat.id,14,message.text)
	data = select_berita()
	print(data)
	for y,x in enumerate(data):
		teks = f"<b>{y+1}. {x[0]}</b>\n\n{x[1]}"
		bot.send_message(message.chat.id,teks,parse_mode="html",disable_web_page_preview=True)

@bot.message_handler(commands=["status"])
def statuss(message):
	checkdaftar(message.chat.id,15,message.text)
	data = select("pkkp_daftar","daftar_idtele",message.chat.id)[0]
	status = "<b>Tidak Valid</b>"
	tidak = "Pastikan mengisi seluruh data pada menu /daftar dan /foto agar dapat di validasi oleh Admin"
	if data[6]=="ya":
		status = "<b>Valid</b>"
		tidak = "Data kamu sudah valid, silahkan melihat informasi terupdate pada menu /berita"
	teks = f"""
Hello {message.from_user.first_name},

Status : {status}

{tidak}
"""
	bot.send_message(message.chat.id,teks,parse_mode="html")



@bot.message_handler(func=lambda msg: msg.text is not None and ("makasih" in msg.text.lower() or "terima kasih" in msg.text.lower() or "thank" in msg.text.lower() or "thx" in msg.text.lower().split(' ')))
def thx(message):
	checkdaftar(message.chat.id,13,message.text)
	bot.reply_to(message,random.choice(["Saya senang dapat membantumu 👌","Terima kasih kembali.","Ok 👍","Dengan senang hati 😊","Tidak masalah."]))
		
@bot.message_handler(func=lambda msg: msg.text is not None and ("hi" in msg.text.lower().split(' ') or "hai" in msg.text.lower().split(' ') or "halo" in msg.text.lower().split(' ') or "hello" in msg.text.lower().split(' ') or "hey" in msg.text.lower().split(' ')))
def hih(message):
	checkdaftar(message.chat.id,13,message.text)
	bot.reply_to(message,random.choice(["Hai juga 😄","Halo ada apa ?","Ya, ada yang bisa saya bantu ?","Halo !, hari yang indah ya.","Hey !, bagaimana kabarmu ?"]))
		
@bot.message_handler(func=lambda msg: msg.text is not None and ("ok" in msg.text.lower().split(' ') or "oke" in msg.text.lower().split(' ') or "okeh" in msg.text.lower().split(' ') or "sip" in msg.text.lower().split(' ') or "ya" in msg.text.lower().split(' ')))
def okeeh(message):
	checkdaftar(message.chat.id,13,message.text)
	bot.reply_to(message,random.choice(["Ok.","Ya.","👍","Sip."]))

@bot.message_handler(func=lambda msg: msg.text is not None)
def other(message):
	checkdaftar(message.chat.id,13,message.text)
	bot.reply_to(message,random.choice(["Saya belum bisa chit chat denganmu 🤓","Saya sedang tahap pengembangan 🤩","Hm... 🧐","Apa ?","Tidak mengerti."]))

while True:
	try:
		bot.polling()
	except Exception as e:
		print(e)
		file1 = open("logs.txt","a")
		file1.write(str(e)+"\n\n")
		file1.close()
		bot.stop_polling()