from tkinter.ttk import Progressbar
from tkinter import *
import pygame
pygame.init()
from playsound import playsound
import os
import sounddevice as sd
from scipy.io.wavfile import write
from tkinter import simpledialog
from PIL import ImageTk,Image

w=Tk()
w.geometry(&quot;350x250+400+200&quot;)
w.overrideredirect(1)
progress=Progressbar(w,style=&quot;red.Horizontal.TProgressbar&quot;,orient=HORI
ZONTAL,length=500,mode=&#39;determinate&#39;,)
def virtual_piano():
root= Tk()
root.geometry(&#39;1300x700+0+0&#39;)
root.configure(background=&quot;black&quot;)
ABC=Frame(root, width=1300,height=400,bg=&quot;white&quot;)
ABC.place(x=20,y=100)
root.state(&quot;zoomed&quot;)

#defining the images

on= PhotoImage(file=r&quot;C:\Users\shrujanna\Downloads\switch images\on
(1)smol.png&quot;)
off= PhotoImage(file=r&quot;C:\Users\shrujanna\Downloads\switch images\off
(1)smol.png&quot;)

global is_on
is_on=False
def switch():
global is_on
if is_on:
label()
on_button.config(image=on)
is_on=False
else:
no_label()
on_button.config(image=off)
is_on=True
def no_label():
btnC1[&#39;text&#39;]=btnG1[&#39;text&#39;]=btnD1[&#39;text&#39;]=btnA1[&#39;text&#39;]=btnB1[&#39;text&#39;
]=btnF1[&#39;text&#39;]=btnE1[&#39;text&#39;]=&#39;&#39;
btnC2[&#39;text&#39;]=btnG2[&#39;text&#39;]=btnD2[&#39;text&#39;]=btnA2[&#39;text&#39;]=btnB2[&#39;text&#39;
]=btnF2[&#39;text&#39;]=btnE2[&#39;text&#39;]=&#39;&#39;
btnC3[&#39;text&#39;]=btnG3[&#39;text&#39;]=btnD3[&#39;text&#39;]=btnA3[&#39;text&#39;]=btnB3[&#39;text&#39;
]=btnF3[&#39;text&#39;]=btnE3[&#39;text&#39;]=&#39;&#39;
btnCs1[&#39;text&#39;]=btnGs1[&#39;text&#39;]=btnDs1[&#39;text&#39;]=btnFs1[&#39;text&#39;]=btnAs1
[&#39;text&#39;]=&#39;&#39;
btnCs2[&#39;text&#39;]=btnGs2[&#39;text&#39;]=btnDs2[&#39;text&#39;]=btnFs2[&#39;text&#39;]=btnAs2
[&#39;text&#39;]=&#39;&#39;
btnCs3[&#39;text&#39;]=btnGs3[&#39;text&#39;]=btnDs3[&#39;text&#39;]=btnFs3[&#39;text&#39;]=btnAs3
[&#39;text&#39;]=&#39;&#39;

def label():
btnC1[&#39;text&#39;]=&#39;C1&#39;
btnG1[&#39;text&#39;]=&#39;G1&#39;
btnD1[&#39;text&#39;]=&#39;D1&#39;
btnE1[&#39;text&#39;]=&#39;E1&#39;
btnF1[&#39;text&#39;]=&#39;F1&#39;
btnA1[&#39;text&#39;]=&#39;A1&#39;
btnB1[&#39;text&#39;]=&#39;B1&#39;
btnCs1[&#39;text&#39;]=&#39;C#\n1&#39;
btnGs1[&#39;text&#39;]=&#39;G#\n1&#39;
btnFs1[&#39;text&#39;]=&#39;F#\n1&#39;
btnDs1[&#39;text&#39;]=&#39;D#\n1&#39;
btnAs1[&#39;text&#39;]=&#39;A#\n1&#39;
btnC2[&#39;text&#39;]=&#39;C2&#39;
btnG2[&#39;text&#39;]=&#39;G2&#39;
btnD2[&#39;text&#39;]=&#39;D2&#39;
btnE2[&#39;text&#39;]=&#39;E2&#39;
btnF2[&#39;text&#39;]=&#39;F2&#39;
btnA2[&#39;text&#39;]=&#39;A2&#39;
btnB2[&#39;text&#39;]=&#39;B2&#39;
btnCs2[&#39;text&#39;]=&#39;C#\n2&#39;
btnGs2[&#39;text&#39;]=&#39;G#\n2&#39;
btnFs2[&#39;text&#39;]=&#39;F#\n2&#39;
btnDs2[&#39;text&#39;]=&#39;D#\n2&#39;
btnAs2[&#39;text&#39;]=&#39;A#\n2&#39;
btnC3[&#39;text&#39;]=&#39;C3&#39;
btnG3[&#39;text&#39;]=&#39;G3&#39;
btnD3[&#39;text&#39;]=&#39;D3&#39;
btnE3[&#39;text&#39;]=&#39;E3&#39;
btnF3[&#39;text&#39;]=&#39;F3&#39;
btnA3[&#39;text&#39;]=&#39;A3&#39;
btnB3[&#39;text&#39;]=&#39;B3&#39;
btnCs3[&#39;text&#39;]=&#39;C#\n3&#39;

btnGs3[&#39;text&#39;]=&#39;G#\n3&#39;
btnFs3[&#39;text&#39;]=&#39;F#\n3&#39;
btnDs3[&#39;text&#39;]=&#39;D#\n3&#39;
btnAs3[&#39;text&#39;]=&#39;A#\n3&#39;
def button_hover(e):
help_button[&quot;bg&quot;]=&quot;black&quot;
help_label.config(text=&quot;the toggle button displays notes on the
key&quot;,font=18)
def button_hover_leaver(e):
help_button[&quot;bg&quot;]=&quot;Black&quot;
help_label.config(text=&quot;&quot;)

help_image=PhotoImage(file=r&quot;C:\Users\shrujanna\Downloads\switch
images\helpsmol.png&quot;)
help_button=Button(root,image=help_image,bd=0,borderwidth=0,bg=&quot;black
&quot;,border=0)
help_button.place(x=110,y=50)
help_label=Label(root,text=&quot;&quot;,bd=0,bg=&#39;black&#39;,fg=&#39;white&#39;,border=0)
help_label.place(x=135,y=43)
help_button.bind(&quot;&lt;Enter&gt;&quot;,button_hover)
help_button.bind(&quot;&lt;Leave&gt;&quot;,button_hover_leaver)

on_button=Button(root,image=on,bg=&quot;black&quot;,borderwidth=0,bd=0,border=0
,command=switch)
on_button.place(x=10,y=30)

def value_CS1():
playsound(r&#39;C:\Users\shrujanna\Downloads\Z_Music_Notes\music
notes1\assets_notes_Db3.wav&#39;)
def value_DS1():
playsound(r&quot;C:\Users\shrujanna\Downloads\Z_Music_Notes\Music_Notes1
\D_s.wav&quot;)
def value_FS1():
playsound(r&#39;C:\Users\Shrujanna\Downloads\Z_Music_Notes\Music_Notes1
\F_s.wav&#39;)
def value_GS1():
playsound(r&#39;C:\Users\Shrujanna\Downloads\Z_Music_Notes\Music_Notes1
\G_s.wav&#39;)
def value_AS1():
playsound(r&quot;C:\Users\shrujanna\Downloads\Z_Music_Notes\Music_Notes1
\Bb.wav&quot;)

def value_C1():
playsound(r&#39;C:\Users\Shrujanna\Downloads\Z_Music_Notes\Music_Notes1
\C.wav&#39;)
def value_D1():
playsound(r&#39;C:\Users\Shrujanna\Downloads\Z_Music_Notes\Music_Notes1
\D.wav&#39;)
def value_E1():
playsound(r&#39;C:\Users\Shrujanna\Downloads\Z_Music_Notes\Music_Notes1
\E.wav&#39;)

def value_F1():

playsound(r&#39;C:\Users\Shrujanna\Downloads\Z_Music_Notes\Music_Notes1
\F.wav&#39;)
def value_G1():
playsound(r&#39;C:\Users\Shrujanna\Downloads\Z_Music_Notes\Music_Notes1
\G.wav&#39;)
def value_A1():
playsound(r&quot;C:\Users\shrujanna\Downloads\Z_Music_Notes\Music_Notes1
\A.wav&quot;)
def value_B1():
playsound(r&quot;C:\Users\shrujanna\Downloads\Z_Music_Notes\Music_Notes1
\B.wav&quot;)

btnC1 = Button(ABC, bd=4, width=3, height = 15, text = &#39;C1&#39;, bg = &#39;white&#39;,
fg = &#39;black&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;),command=value_C1)
btnC1.grid(row=0,column=0)
root.bind(&#39;&lt;Tab&gt;&#39;,lambda event:value_C1())
btnD1 = Button(ABC, bd=4, width=3, height = 15, text = &#39;D1&#39;, bg = &#39;white&#39;,
fg = &#39;black&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;),command=value_D1)
btnD1.grid(row = 0, column = 1)
root.bind(&#39;&lt;q&gt;&#39;,lambda event:value_D1())
btnCs1 = Button(ABC, height = 6, width = 2, bd = 4, text = &#39;C#\n1&#39;, bg =
&#39;black&#39;, fg = &#39;white&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;),command=value_CS1) #button
c#
btnCs1.place(x=35,y=0)
root.bind(1,lambda event:value_CS1())

btnE1= Button(ABC, bd=4, width=3, height = 15, text = &#39;E1&#39;, bg = &#39;white&#39;,
fg = &#39;black&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;),command=value_E1)
btnE1.grid(row = 0, column = 2)
root.bind(&#39;&lt;w&gt;&#39;,lambda event:value_E1())
btnDs1 = Button(ABC, height = 6, width = 2, bd = 4, text = &#39;D#\n1&#39;, bg =
&#39;black&#39;, fg = &#39;white&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;),command=value_DS1) #button
d#
btnDs1.place(x=95,y=0)
root.bind(2,lambda event:value_D1())
btnF1= Button(ABC, bd=4, width=3, height = 15, text = &#39;F1&#39;, bg = &#39;white&#39;,
fg = &#39;black&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;),command=value_F1)
btnF1.grid(row = 0, column = 3)
root.bind(&#39;&lt;e&gt;&#39;,lambda event:value_F1())
btnG1= Button(ABC, bd=4, width=3, height = 15, text = &#39;G1&#39;, bg = &#39;white&#39;,
fg = &#39;black&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;),command=value_G1)
btnG1.grid(row = 0, column = 4)
root.bind(&#39;&lt;r&gt;&#39;,lambda event:value_G1())
btnFs1 = Button(ABC, height = 6, width = 2, bd = 4, text = &#39;F#\n1&#39;, bg =
&#39;black&#39;, fg = &#39;white&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;),command=value_FS1) #button
c#
btnFs1.place(x=215,y=0)
root.bind(3,lambda event:value_D1())
btnA1= Button(ABC, bd=4, width=3, height = 15, text = &#39;A1&#39;, bg = &#39;white&#39;,
fg = &#39;black&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;),command=value_A1)
btnA1.grid(row = 0, column = 5)
root.bind(&#39;&lt;t&gt;&#39;,lambda event:value_A1())
btnGs1 = Button(ABC, height = 6, width = 2, bd = 4, text = &#39;G#\n1&#39;, bg =
&#39;black&#39;, fg = &#39;white&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;),command=value_GS1) #button
c#

btnGs1.place(x=275,y=0)
root.bind(4,lambda event:value_D1())
btnB1= Button(ABC, bd=4, width=3, height = 15, text = &#39;B1&#39;, bg = &#39;white&#39;,
fg = &#39;black&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;),command=value_B1)
btnB1.grid(row = 0, column = 6)
root.bind(&#39;&lt;y&gt;&#39;,lambda event:value_B1())
btnAs1 = Button(ABC, height = 6, width = 2, bd = 4, text = &#39;A#\n1&#39;, bg =
&#39;black&#39;, fg = &#39;white&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;),command=value_AS1) #button
c#
btnAs1.place(x=335,y=0)
root.bind(5,lambda event:value_D1())

#Keys in the second octave

btnC2 = Button(ABC, bd=4, width=3, height = 15, text = &#39;C2&#39;, bg = &#39;white&#39;,
fg = &#39;black&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;))
btnC2.grid(row=0,column=7)
root.bind(&#39;&lt;u&gt;&#39;,lambda event:value_C1())
btnD2 = Button(ABC, bd=4, width=3, height = 15, text = &#39;D2&#39;, bg = &#39;white&#39;,
fg = &#39;black&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;))
btnD2.grid(row = 0, column = 8)
root.bind(&#39;&lt;i&gt;&#39;,lambda event:value_D1())
btnCs2 = Button(ABC, height = 6, width = 2, bd = 4, text = &#39;C#\n2&#39;, bg =
&#39;black&#39;, fg = &#39;white&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;)) #button c#
btnCs2.place(x=445,y=0)
root.bind(8,lambda event:value_D1())
btnE2= Button(ABC, bd=4, width=3, height = 15, text = &#39;E2&#39;, bg = &#39;white&#39;,
fg = &#39;black&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;))

btnE2.grid(row = 0, column = 9)
root.bind(&#39;&lt;o&gt;&#39;,lambda event:value_E1())
btnDs2 = Button(ABC, height = 6, width = 2, bd = 4, text = &#39;D#\n2&#39;, bg =
&#39;black&#39;, fg = &#39;white&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;)) #button d#
btnDs2.place(x=505,y=0)
root.bind(9,lambda event:value_D1())
btnF2= Button(ABC, bd=4, width=3, height = 15, text = &#39;F2&#39;, bg = &#39;white&#39;,
fg = &#39;black&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;))
btnF2.grid(row = 0, column = 10)
root.bind(&#39;&lt;p&gt;&#39;,lambda event:value_F1())
btnG2= Button(ABC, bd=4, width=3, height = 15, text = &#39;G2&#39;, bg = &#39;white&#39;,
fg = &#39;black&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;))
btnG2.grid(row = 0, column = 11)
root.bind(&#39;&lt;[&gt;&#39;,lambda event:value_G1())
btnFs2 = Button(ABC, height = 6, width = 2, bd = 4, text = &#39;F#\n2&#39;, bg =
&#39;black&#39;, fg = &#39;white&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;)) #button c#
btnFs2.place(x=625,y=0)
root.bind(0,lambda event:value_D1())
btnA2= Button(ABC, bd=4, width=3, height = 15, text = &#39;A2&#39;, bg = &#39;white&#39;,
fg = &#39;black&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;))
btnA2.grid(row = 0, column = 12)
root.bind(&#39;&lt;]&gt;&#39;,lambda event:value_A1())
btnGs2 = Button(ABC, height = 6, width = 2, bd = 4, text = &#39;G#\n2&#39;, bg =
&#39;black&#39;, fg = &#39;white&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;)) #button c#
btnGs2.place(x=685,y=0)
root.bind(&#39;-&#39;,lambda event:value_D1())
btnB2= Button(ABC, bd=4, width=3, height = 15, text = &#39;B2&#39;, bg = &#39;white&#39;,
fg = &#39;black&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;))

btnB2.grid(row = 0, column = 13)
root.bind(&#39;&lt;\&gt;&#39;,lambda event:value_B1())
btnAs2 = Button(ABC, height = 6, width = 2, bd = 4, text = &#39;A#\n2&#39;, bg =
&#39;black&#39;, fg = &#39;white&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;)) #button c#
btnAs2.place(x=745,y=0)
root.bind(&#39;&lt;=&gt;&#39;,lambda event:value_D1())

#keys in thrid octave
btnC3 = Button(ABC, bd=4, width=3, height = 15, text = &#39;C3&#39;, bg = &#39;white&#39;,
fg = &#39;black&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;))
btnC3.grid(row=0,column=14)
root.bind(&#39;&lt;z&gt;&#39;,lambda event:value_C1())
btnD3 = Button(ABC, bd=4, width=3, height = 15, text = &#39;D3&#39;, bg = &#39;white&#39;,
fg = &#39;black&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;))
btnD3.grid(row = 0, column = 15)
root.bind(&#39;&lt;x&gt;&#39;,lambda event:value_D1())
btnCs3 = Button(ABC, height = 6, width = 2, bd = 4, text = &#39;C#\n3&#39;, bg =
&#39;black&#39;, fg = &#39;white&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;)) #button c#
btnCs3.place(x=865,y=0)
#root.bind(&#39;&lt;&gt;&#39;,lambda event:value_D1())
btnE3= Button(ABC, bd=4, width=3, height = 15, text = &#39;E3&#39;, bg = &#39;white&#39;,
fg = &#39;black&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;))
btnE3.grid(row = 0, column = 16)
root.bind(&#39;&lt;c&gt;&#39;,lambda event:value_E1())
btnDs3 = Button(ABC, height = 6, width = 2, bd = 4, text = &#39;D#\n3&#39;, bg =
&#39;black&#39;, fg = &#39;white&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;)) #button d#
btnDs3.place(x=925,y=0)
#root.bind(&#39;&lt;&gt;&#39;,lambda event:value_D1())

btnF3= Button(ABC, bd=4, width=3, height = 15, text = &#39;F3&#39;, bg = &#39;white&#39;,
fg = &#39;black&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;))
btnF3.grid(row = 0, column = 17)
root.bind(&#39;&lt;v&gt;&#39;,lambda event:value_F1())
btnG3= Button(ABC, bd=4, width=3, height = 15, text = &#39;G3&#39;, bg = &#39;white&#39;,
fg = &#39;black&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;))
btnG3.grid(row = 0, column = 18)
root.bind(&#39;&lt;b&gt;&#39;,lambda event:value_G1())
btnFs3 = Button(ABC, height = 6, width = 2, bd = 4, text = &#39;F#\n3&#39;, bg =
&#39;black&#39;, fg = &#39;white&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;)) #button c#
btnFs3.place(x=1040,y=0)
#root.bind(&#39;&lt;&gt;&#39;,lambda event:value_1())
btnA3= Button(ABC, bd=4, width=3, height = 15, text = &#39;A3&#39;, bg = &#39;white&#39;,
fg = &#39;black&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;))
btnA3.grid(row = 0, column = 19)
root.bind(&#39;&lt;n&gt;&#39;,lambda event:value_A1())
btnGs3 = Button(ABC, height = 6, width = 2, bd = 4, text = &#39;G#\n3&#39;, bg =
&#39;black&#39;, fg = &#39;white&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;)) #button c#
btnGs3.place(x=1100,y=0)
#root.bind(&#39;&lt;Tab&gt;&#39;,lambda event:value_D1())
btnB3= Button(ABC, bd=4, width=3, height = 15, text = &#39;B3&#39;, bg = &#39;white&#39;,
fg = &#39;black&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;))
btnB3.grid(row = 0, column = 20)
root.bind(&#39;&lt;m&gt;&#39;,lambda event:value_B1())
btnAs3 = Button(ABC, height = 6, width = 2, bd = 4, text = &#39;A#\n3&#39;, bg =
&#39;black&#39;, fg = &#39;white&#39;, font = (&#39;arial&#39;,18,&#39;bold&#39;)) #button c#
btnAs3.place(x=1160,y=0)
#root.bind(&#39;&lt;Tab&gt;&#39;,lambda event:value_D1())

root.mainloop()

def voice_recorder():
&#39;&#39;&#39;
microphone interface
&#39;&#39;&#39;
root2= Tk()
root2.geometry(&#39;1300x700+0+0&#39;)#change this to 1300
root2.configure(background=&quot;Systembuttonface&quot;)
#root.state(&quot;zoomed&quot;)
from playsound import playsound
#connect sql and write path name
def path_saver_sql(name,path):
import mysql.connector as m
try:
con = m.connect(host=&#39;localhost&#39;,user = &#39;root&#39;, password = &#39;root&#39;, db
= &#39;tbdpiano&#39;)
if con.is_connected():
mycursor=con.cursor()
name_song = name
path_file = str(path)
path_list = path_file.split(&#39;\\&#39;)
path_x = &#39;&#39;
for i in path_list:
path_x += i
path_x += &#39;\\\\&#39;
path_x = path_x [:-2]
print(path_x)
q1= &quot;insert into song_info (song_name,path) values
(&#39;%s&#39;,&#39;%s&#39;)&quot;%(name_song, path_x)

print(&quot;Debug:&quot;,q1)
mycursor.execute(q1)
con.commit()
print(&#39;yay&#39;)
except m.Error as e:
print(e)
else:
con.close()
def path_extract(song):
music_file = song+&#39;.wav&#39;
path_to_file = os.path.abspath(music_file)
path_to_file.replace(&#39;\\\\&#39;, &#39;\\\\\\&#39;)
print(path_to_file)
path_saver_sql(song,path_to_file)

def song_recorder():
fs = 44100 # Sample rate
seconds = 10 # Duration of recording
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait() # Wait until recording is finished
file_name = simpledialog.askstring(&quot;Input&quot;, &quot;Recording done\nEnter
the file name&quot;,parent=root)
write(file_name+&#39;.wav&#39;, fs, myrecording) # Save as WAV file
print(&quot;Song recorded&quot;)
path_extract(file_name)
from playsound import playsound
def retrieval():
import mysql.connector as m
try:
con = con = m.connect(host=&#39;localhost&#39;,user = &#39;root&#39;, password =
&#39;root&#39;, db = &#39;tbdpiano&#39;)
if con.is_connected():

mycursor=con.cursor()
song_name = input(&#39;Enter song name: &#39;)
q1 = &quot;select path from song_info where song_name like
&#39;%s&#39;&quot;%(song_name)
mycursor.execute(q1)
path = str(mycursor.fetchone()[0])
path_file = str(path)
path_list = path_file.split(&#39;\\&#39;)
path_x = &#39;&#39;
for i in path_list:
path_x += i
path_x += &#39;\\\\&#39;
path_x = path_x [:-2]
playsound(path)
except m.Error as e:
print(e)
else:
con.close()

microphone=PhotoImage(file=r&quot;C:\Users\shrujanna\Downloads\switch
images\microphone (1).png&quot;)
record_btn=Button(root2,image=microphone,bd=0)
record_btn.place(x=450,y=100)

def btn1():
l4=Label(w,text=&#39;Loading...&#39;,fg=&#39;white&#39;,bg=&#39;black&#39;)
lst4=(&#39;Calibri (Body)&#39;,10,&#39;bold&#39;)
l4.config(font=lst4)
l4.place(x=18,y=210)

import time
r=0
for i in range(100):
progress[&#39;value&#39;]=r
w.update_idletasks()
time.sleep(0.03)
r=r+1
w.destroy()
virtual_piano()
def btn2():
l4=Label(w,text=&#39;Loading...&#39;,fg=&#39;white&#39;,bg=&#39;black&#39;)
lst4=(&#39;Calibri (Body)&#39;,15,&#39;bold&#39;)
l4.config(font=lst4)
l4.place(x=18,y=210)
import time
r=0
for i in range(100):
progress[&#39;value&#39;]=r
w.update_idletasks()
time.sleep(0.03)
r=r+1
w.destroy()
voice_recorder()

progress.place(x=-10,y=235)

Frame(w,width=427,height=241,bg=&#39;black&#39;).place(x=0,y=0)
b1=Button(w,width=23,height=2,text=&#39;VIRTUAL
PIANO&#39;,command=btn1,border=3,fg=&#39;white&#39;,bg=&#39;black&#39;,font=(&quot;times new
roman&quot;,10))
b1.place(x=0,y=195)
b2=Button(w,width=23,height=2,text=&#39;VOICE
RECORDER&#39;,command=btn2,border=3,fg=&#39;white&#39;,bg=&#39;black&#39;,font=(&quot;times
new roman&quot;,10))
b2.place(x=173,y=195)
image=ImageTk.PhotoImage(Image.open(r&quot;C:\Users\shrujanna\Downloads
\switch images\switch images\the cover2 smaller.jpeg&quot;))
label=Label(image=image)
label.pack()

w.mainloop()