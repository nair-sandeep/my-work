from tkinter import *
import tkinter.ttk as ttk
import pygame
import os
from PIL import ImageTk,Image
import random
from tkinter import filedialog
import time
from mutagen.mp3 import MP3

root = Tk()
c1=0
c2=0
class My_Music_Player():
	def __init__(self,root):
		#root of window
		self.root = root
		# Title of the window
		self.root.title("MusicPlayer")
		#Icon of the player
		self.root.iconbitmap(r"F:\shi\music\icon.ico")
		# Window Geometry
		self.root.geometry("1000x600+200+100")
		#configuring the root
		self.root.config(bg="#1d1c1d")
		# Initiating Pygame
		pygame.init()
		# Initiating Pygame Mixer
		pygame.mixer.init()
		# Declaring track Variable
		self.track = StringVar()
		# Declaring Status Variable
		self.status = StringVar()
		 # this is to prevent from resizing the window
		self.root.resizable(0, 0) 



		global pl,li,songslist,songname,trackstatus,stop,songtracks,time_rec,song_slider,slider_label,audio_len,start_time,stop_time,volume_slider
		global paused,stopped,volu,mute
		
		mute=False
		stopped=False
		paused=False
		stop =0		
		audio_len=0

		play = Frame(self.root, bd=0,bg="#333133",highlightbackground="black", highlightcolor="black") 
		play.place(x=0,y=500,width=1000, height=100)

		'''img1 = ImageTk.PhotoImage(Image.open(r'F:\shi\music\next.png').resize((50,50)))
								ub1=Button(play,image=img1)
								ub1.image=img1
								ub1.place(x=450,y=0)'''
		st=Button(play,text="",font=("Font Awesome 5 Free Solid",15),bg="#333133",bd=0,fg="#fff",activebackground="#333133",activeforeground="#fff",command=self.stopsong)
		st.place(x=143,y=30)
		pre=Button(play,text="",font=("Font Awesome 5 Free Solid",15),bg="#333133",bd=0,fg="#fff",activebackground="#333133",activeforeground="#fff",command=self.prev)
		pre.place(x=286,y=30)
		pl=Button(play,text="",font=("Font Awesome 5 Free Solid",25),bg="#333133",bd=0,fg="#fff",activebackground="#333133",activeforeground="#fff",command=self.pause)
		pl.place(x=429,y=20)
		# pa=Button(play,text="",font=("Font Awesome 5 Free Solid",25),bg="#333133",bd=0,fg="#fff",activebackground="#333133",activeforeground="#fff")
		#pa.place(x=285,y=20)
		ne=Button(play,text="",font=("Font Awesome 5 Free Solid",15),bg="#333133",bd=0,fg="#fff",activebackground="#333133",activeforeground="#fff",command=self.next)
		ne.place(x=572,y=30)
		sh=Button(play,text="",font=("Font Awesome 5 Free Solid",15),bg="#333133",bd=0,fg="#fff",activebackground="#333133",activeforeground="#fff",command=self.shuffle)
		sh.place(x=715,y=30)
		li=Button(play,text="",font=("Font Awesome 5 Free Solid",25),bg="#333133",bd=0,fg="#fff",activebackground="#333133",activeforeground="#fff",command=self.list)
		li.place(x=858,y=15)



		playerarea =Frame(self.root,bg="#000", highlightbackground="black", highlightcolor="black")
		playerarea.place(x=0,y=0,width=600,height=500)

		#menu
		Button(playerarea,text="Add Song",bg='#6600CC',fg='#FFCC00',font=('karam',15),activebackground="#FFCC00",activeforeground="#000",command=self.add_song).place(x=0,y=0,width=600)


		img2 = ImageTk.PhotoImage(Image.open(r'12.gif').resize((600,355)))
		ub2=Label(playerarea,image=img2,activebackground="#000",bg="#000",bd=0)
		ub2.image=img2
		ub2.place(x=0,y=35)


		songname=Label(playerarea,text="",bg='#000',fg="#FFCC00",anchor=W,font=('MV Boli',15),height=2,)
		# songname.place(x=0,y=415,width=575,)
		trackstatus = Label(playerarea,text="",textvariable=self.status,bg='#000',fg="#FFCC00",anchor=W,font=('MV Boli',12),height=1)
		# trackstatus.place(x=0,y=472,width=575)

		time_rec=Label(playerarea,text="",bd=1,relief='groove')
		#time_rec.place(x=100,y=100)
		
		song_slider=ttk.Scale(playerarea,from_=0,to=100,orient=HORIZONTAL,value=0,length=575,command=self.slide_song)
		#song_slider.place(x=0,y=390 )

		start_time=Label(playerarea,text="",bd=1,relief='flat',bg='#1d1c1d',fg='#FFCC00',font=('Staincool Base', 15))
		start_time.place(x=0,y=360)

		stop_time=Label(playerarea,text="",bd=1,relief='flat',bg='#1d1c1d',fg='#FFCC00',font=('Staincool Base', 15))
		stop_time.place(x=560,y=360)
		#song_slider.config(background='#000')

		# slider_label=Label(playerarea,text="")
		# slider_label.place(x=250,y=250)
		
		volume_slider=ttk.Scale(playerarea,from_=1,to=0,orient=VERTICAL,value=1,length=90,command=self.volume)
		volume_slider.place(x=575,y=415 )
		volu=Button(playerarea,text="",relief="flat",font=("Font Awesome 5 Free Solid",12),bg="#333133",fg="#fff",activebackground="#333133",activeforeground="#fff",command=lambda:self.mute(mute))
		volu.place(x=575,y=385)


		songslist = Frame(self.root,bg="#1d1c1d",highlightbackground="black", highlightcolor="black",highlightthickness=1)
		songslist.place(x=600,y=0,width=400,height=500)
		#songslist.pack(side=TOP,anchor=E)


		# songsframe = LabelFrame(self.root,text="Song Playlist",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
		# songsframe.place(x=600,y=0,width=400,height=200)
		# Inserting scrollbar
		scrol_y = Scrollbar(songslist,orient=VERTICAL)
		# Inserting Playlist listbox
		self.playlist = Listbox(songslist,height=500,yscrollcommand=scrol_y.set,selectbackground="#FF9900",selectforeground='#000',selectmode=SINGLE,font=("Bookman Old Style",12,),fg="#fff",bg="#333333",bd=5,relief='flat')
		# Applying Scrollbar to listbox #flat, groove, raised, ridge, solid, or sunken
		scrol_y.pack(side=RIGHT,fill=BOTH,)
		scrol_y.config(command=self.playlist.yview)
		#for Double Click
		self.playlist.bind('<Double-1>', self.go)
		self.playlist.pack(fill=BOTH)
		# Changing Directory for fetching Songs
		os.chdir(r"songs")
		# Fetching Songs
		songtracks = os.listdir()
		# print(songtracks)
		# print(random.sample(songtracks, k=len(songtracks)))
		# Inserting Songs into Playlist
		#songtracks=random.sample(songtracks, k=len(songtracks))
		# print(songtracks)
		for track in songtracks:
		  self.playlist.insert(END,track)
		
		

	#Song Adding
	def add_song(self):
		songs=filedialog.askopenfilenames(initialdir=r"songs/",title="Choose a Song",filetypes=(("mp3 Files","*.mp3"),))
		
		for song in songs:
			song=song.replace("F:/shi/songs/","")
			self.playlist.insert(END,song)
		#print(song)
	#double Click Function
	def go(self,event):
		global c1
		cs = self.playlist.curselection()   
		self.playsong()
		pl.config(text="")
		c1=1
	    # Updating label text to selected option
		#print(self.playlist.get(cs))

	def volume(self,X):
		pygame.mixer.music.set_volume(volume_slider.get())
		vol=pygame.mixer.music.get_volume()
		#slider_label.config(text=int(vol*100))

		if int(vol*100)==0:
			volu.config(text="")
		elif int(vol*100)>50:
			volu.config(text="")
		else:
			volu.config(text="")


	#play and pause button
	def pause(self):
			global c1,stop
			#global pl
			print("stop",stop)
			if stop==1:
				self.playsong()
				stop=0
				print("stop")
				c1=c1+1
			c1=c1+1
			if c1%2==0:
				pl.config(text="")
				#self.pausesong()
				self.pausesong(paused)
			else:
				#if
				#self.unpausesong()
				self.pausesong(paused)
				pl.config(text="")
			print(c1)
	
	#hiding play list
	def list(self):
			global c2,songslist
			#global pl

			c2=c2+1
			if c2%2==0:
				li.config(text="")
				songslist.place(x=600,y=0,width=400,height=500)
			else:
				li.config(text="")
				songslist.place_forget()

			#pa.place(x=285,y=20)
	def shuffle(self):
		time_rec.config(text='')
		start_time.config(text='')
		stop_time.config(text='')
		song_slider.config(value=0)

		global songtracks
		songtracks=random.sample(songtracks, k=len(songtracks))
		self.playlist.delete(0,END)
		pygame.mixer.music.stop()
		# print(songtracks)
		for track in songtracks:
		  self.playlist.insert(END,track)



	def playsong(self):
		# Displaying Selected Song title
		global stopped
		stopped=False
		self.status.set("-Playing")
		trackstatus.place(x=0,y=472,width=575)
	    # Displaying Status
		ss=self.playlist.get(ACTIVE)
		songname.config(text=ss)
		songname.place(x=0,y=415,width=575)
		song_slider.place(x=0,y=390 )
	    # Loading Selected Song
		pygame.mixer.music.load(self.playlist.get(ACTIVE))
		print(self.playlist.get(ACTIVE))
	    # Playing Selected Song
		pygame.mixer.music.play()
		self.song_time()

		# slider_position=int(audio_len)
		# song_slider.config(to=slider_position,value=0)

	def stopsong(self):
		global c1, stop
	    # Displaying Status
		time_rec.config(text='')
		song_slider.config(value=0)
		start_time.config(text='')
		stop_time.config(text='')

		self.status.set("-Stopped")
	    # Stopped Song
		c1=0
		stop=1
		pl.config(text="")
		pygame.mixer.music.stop()
		print("stopped",stop)
		time_rec.config(text="")

		global stopped
		stopped=True

	def mute(self,is_mute):
		global mute
		mute=is_mute

		if mute:
			volu.config(text="")
			pygame.mixer.music.set_volume(volume_slider.get())


			mute=False
		else:
			pygame.mixer.music.set_volume(0)
			volu.config(text="")
			#pygame.mixer.music.set_volume(volume_slider.get())
			mute=True

	def pausesong(self,is_paused):
		global paused
		paused=is_paused

		if paused:
			self.status.set("-Playing")
		# Playing back Song
			pygame.mixer.music.unpause()
			paused=False
		else:
			# Displaying Status
			self.status.set("-Paused")
		    # Paused Song
			pygame.mixer.music.pause()
			paused=True


	# def unpausesong(self):
	# 	# It will Display the  Status
	# 	self.status.set("-Playing")
	# 	# Playing back Song
	# 	pygame.mixer.music.unpause()
	

	def next(self):

		time_rec.config(text='')
		song_slider.config(value=0)
		start_time.config(text='')
		stop_time.config(text='')

		next_song=self.playlist.curselection()
		next_song=next_song[0]+1
		song=self.playlist.get(next_song)
		print(song)

		#for playing next song
		pygame.mixer.music.load(song)
		pygame.mixer.music.play()

		#for changing the selection
		self.playlist.selection_clear(0,END)
		self.playlist.activate(next_song)
		self.playlist.selection_set(next_song,last=None)
		#print(next_song)
	def prev(self):
		time_rec.config(text='')
		start_time.config(text='')
		stop_time.config(text='')

		song_slider.config(value=0)

		prev_song=self.playlist.curselection()
		prev_song=prev_song[0]-1
		song=self.playlist.get(prev_song)
		print(song)

		#for playing next song
		pygame.mixer.music.load(song)
		pygame.mixer.music.play()

		#for changing the selection
		self.playlist.selection_clear(0,END)
		self.playlist.activate(prev_song)
		self.playlist.selection_set(prev_song,last=None)
		print(prev_song)


	
	def song_time(self):

		if stopped:
			return
		global audio_len
		#current time
		current_time=pygame.mixer.music.get_pos()/1000

		#
		#slider_label.config(text=f'slider:{int(song_slider.get())} song Pos:{int(current_time)}')
		#time formating
		time_format=time.strftime('%M:%S',time.gmtime(current_time))

		

		#for song length
		#current_song=self.playlist.curselection()
		song1=self.playlist.get(ACTIVE) 
		audio=MP3(song1)
		audio_len=audio.info.length
		audio_len_format=time.strftime('%M:%S',time.gmtime(audio_len))

		current_time+=1

		if int(song_slider.get())==int(audio_len):
			time_rec.config(text=f'Time: {audio_len_format} by {audio_len_format} ')
			start_time.config(text=audio_len_format)
			stop_time.config(text=audio_len_format)
			self.next()

		elif paused:
			pass
		elif int(song_slider.get())==int(current_time):
			slider_position=int(audio_len)
			song_slider.config(to=slider_position,value=int(current_time))
		else:
			slider_position=int(audio_len)

			time_format=time.strftime('%M:%S',time.gmtime(song_slider.get()))
			song_slider.config(to=slider_position,value=int(song_slider.get()))
			time_rec.config(text=f'Time: {time_format} by {audio_len_format} ')
			start_time.config(text=time_format)
			stop_time.config(text=audio_len_format)
			next_time=int(song_slider.get())+1
			song_slider.config(value=next_time)


		#time_rec.config(text=f'Time: {time_format} by {audio_len_format} ')

		#slider pos value
		#song_slider.config(value=int(current_time))



		time_rec.after(1000,self.song_time)
	
	def slide_song(self,X):
		global audio_len
		#print("in slide")
		#print('audio',audio_len)
		if audio_len==0:
			pass
		else:
			#slider_label.config(text=f'{int(song_slider.get())} of {int(audio_len)}')
			pygame.mixer.music.load(self.playlist.get(ACTIVE))
			#print(self.playlist.get(ACTIVE))
	    # Playing Selected Song
			pygame.mixer.music.play(start=int(song_slider.get()))
		


My_Music_Player(root)
root.mainloop()