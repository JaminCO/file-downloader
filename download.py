from tkinter import *
from tkinter import messagebox, filedialog
import os
from urllib.request import urlopen, HTTPError, URLError 
import _thread


fln = ''
filesize = ''

def startDownload():
	global fln
	fln = filedialog.asksaveasfilename(initialdir=os.getcwd, title='Save File', filetypes=(('All Files', "*.*"), ("JPG Image File", "*.jpg"), ("PNG Image File", "*.png")))
	filename.set(os.path.basename(fln))
	_thread.start_new_thread(initDownload, ())

def initDownload():
	global filesize
	furl = url.get()
	target = urlopen(furl)
	meta = target.info()
	filesize = meta['Content-Length']
	if filesize == None:
		filesize = float(10)
	else:
		float(filesize)
	filesize_mb = round((filesize / 1024 / 1024), 2)
	downloaded = 0
	chunks = 1024 * 5
	with open(fln, 'wb') as f:
		while True:
			parts = target.read(chunks)
			if not parts:
				messagebox.showinfo("Download complete", "Your Download Has Been completed Succesfully.")
				break
			downloaded += chunks
			perc = round(((downloaded / filesize) * 100),2)
			download_progress.set(str(round((downloaded / 1024 / 1024), 2))+ "MB /"+str(filesize_mb)+" MB")
			download_percentage.set(str(perc)+"%")
			f.write(parts)
		f.close()




def exitprog():
	if messagebox.askyesno("Exit Program", "Are you sure you want to exit the program?") == False:
		return False
	exit()

root = Tk()

url = StringVar()
filename = StringVar()
download_progress = StringVar()
download_percentage = StringVar()

download_progress.set('N/A')
download_percentage.set('N/A')


wrapper = LabelFrame(root, text='File URL', bg='brown')
wrapper.pack(fill='both', expand='yes', padx=10, pady=10)

wrapper2 = LabelFrame(root, text='Download Information', bg='grey')
wrapper2.pack(fill='both', expand='yes', padx=10, pady=10)

lbl = Label(wrapper, text='Download URL: ')
lbl.grid(row=0, column=0, padx=10, pady=10)

ent = Entry(wrapper, textvariable=url, width=30, borderwidth=5)
ent.grid(row=0, column=1, padx=5, pady=10)

btn = Button(wrapper, text='Download', command=startDownload, bg='grey')
btn.grid(row=0, column=2, padx=5, pady=10)

lbl2 = Label(wrapper2, text='File: ')
lbl2.grid(row=0, column=0, padx=10, pady=10)
lbl3 = Label(wrapper2, textvariable=filename)
lbl3.grid(row=0, column=1, padx=10, pady=10)

lbl4 = Label(wrapper2, text="Download progress")
lbl4.grid(row=1, column=0, padx=10, pady=10)
lbl5  = Label(wrapper2, textvariable=download_progress)
lbl5.grid(row=1, column=1, padx=10, pady=10)

lbl6 = Label(wrapper2, text='Download Percentage')
lbl6.grid(row=2, column=0, padx=10, pady=10)
lbl7 = Label(wrapper2, textvariable=download_percentage)
lbl7.grid(row=2, column=1, padx=10, pady=10)

Button(wrapper2, text="Exit downloader", command=exitprog, bg='brown').grid(row=3, column=0, padx=10, pady=10)




root.geometry('450x400')
root.title('Downloader')
root.iconbitmap('Download.ico')
root.resizable(False, False)
root.mainloop()