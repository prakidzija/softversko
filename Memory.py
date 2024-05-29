#memory igra

from tkinter import *
from tkinter.messagebox import *
import random
import os
import time
from numpy import loadtxt

root=Tk()
root.title('Memory')
root.geometry('1250x750+100+10')

frame=Frame(root)
frame.pack(pady=10)

class player:
   def  __init__(self, username):
       self.username = username
       self.highscore = 0

   def highscore(self):
        print('highscore')

global players, buttons, current_player
players = []
buttons = []



player_file = open ('players.txt', 'r')
player_data = player_file.read().split(' ')
player_file.close()
player_data.pop()
print(player_data)

score_file = open('scores.txt', 'r')
score_data = score_file.read().split(' ')
score_data.pop()
score_file.close()
print(score_data)

countt = 0
for x in player_data:
   playr = player(x)
   playr.highscore = int(score_data[countt])
   players.append(playr)
   countt += 1
   print(x)


def take_name():
   global buttons, add_player, new_player_name, name_button, player_data, score_data
   name = new_player_name.get("1.0", "end-1c")
   if name != '':
     p = player(name)
     plr_file = open('players.txt', 'a')
     plr_file.write(name+' ')
     plr_file.close()

     scr_file = open('scores.txt', 'a')
     scr_file.write(str(0)+' ')
     scr_file.close()
     
     players.append(p)
     player_data.append(p)
     score_data.append(str(0))
     add_player.pack_forget()
     new_player_name.pack_forget()
     name_button.pack_forget()
     for x in buttons:
        x.pack_forget()
     
     add_player = Button(frame, text = 'Novi korisnik', font=("Helvetica 20 bold"), height=2, width=15, fg='blue4', command = lambda: new_player())
     add_player.pack(side = TOP)
     
     display_players()

def new_player():
    global new_player_name, name_button
    new_player_name = Text(frame,  font=("Helvetica",10), height=2, width=16, fg='black')
    new_player_name.pack(side = TOP)
    name_button = Button(frame, text = 'Unesi', font=("Helvetica 20 bold"), height=2, width=7, fg='blue4', command = lambda: take_name())
    name_button.pack(side = TOP) 

a=Label(frame, text=' MEMORI', font=("Helvetica 20 bold"), height=2, width=7, fg='blue4')
a.pack(side = TOP)

add_player = Button(frame, text = 'Novi korisnik', font=("Helvetica 20 bold"), height=2, width=15, fg='blue4', command = lambda: new_player())
add_player.pack(side = TOP)

def carry_player(x):
    global play, current_player
    current_player = x
    add_player.pack_forget()
    for btn in buttons:
        btn.pack_forget()
    play = Button(frame, text = 'Odaberi težinu igre', font=("Helvetica 20 bold"), height=2, width=15, fg='blue4', command = lambda: odaberi_tezinu())
    play.pack(side = TOP)


global count_players
count_players = 0
def display_players():
    global count_players, players
    for x in players:
        button = Button(frame, text = (x.username, x.highscore), font=("Helvetica 20 bold"), height=2, width=15, fg='blue4', command = lambda: carry_player(x))
        button.pack(side = TOP)
        buttons.append(button)


display_players()
    




def odaberi_tezinu():
    global a0
    a0=Label(frame, text='Težina', font=("Helvetica",10), height=2, width=16, fg='black')
    a0.pack(side = TOP)
    tezina()



def tezina():
    global a1, a2, a3
    var = IntVar()
    var.set(1)

    a1=Radiobutton(frame, text="Lagano", variable=var, value=1, command=lambda: pokreni(var.get()))
    a1.pack(side = TOP)

    a2=Radiobutton(frame, text="Srednje", variable=var, value=2, command=lambda: pokreni(var.get()))
    a2.pack(side = TOP)

    a3=Radiobutton(frame, text="Teško", variable=var, value=3, command=lambda: pokreni(var.get()))
    a3.pack(side = TOP)


def pokreni(value):
   global start_time
   a.pack_forget()
   a0.pack_forget()
   a1.pack_forget()
   a2.pack_forget()
   a3.pack_forget()
   play.pack_forget()

   l=Label(frame, text=' MEMORI', font=("Helvetica 20 bold"), height=2, width=7, fg='blue4')
   l.grid(row = 0, column = 2)
    
   if value==1:
       easy()
       start_time = time.time()
   elif value==2:
       medium()
       start_time = time.time()
   elif value==3:
       hard()
       start_time = time.time()


        
counter=0
end1=0
answer=[]
answer1=[]

def click(b,num, numbers,x,end):
    global counter, answer, answer1, end1, end_time

    if b["text"]==' ' and counter<2:
        b["text"] =numbers[num]
        answer.append(num)
        answer1.append(b)
        
        counter+=1

    if counter==2:
        if numbers[answer[0]]==numbers[answer[1]]:
            x.config(text="YES")
            for i in answer1:
                i["state"]="disabled"
            counter=0
            answer=[]
            answer1=[]
            end1+=1
        else:
            x.config(text="NO")
            counter=0;
            answer=[]

    if counter==1 and len(answer1)>1:
        i=answer1[0]
        j=answer1[1]
        k=answer1[2]
        i["text"]=" "
        j["text"]=" "
        answer1=[]
        answer1.append(k)

    if end1==end:
        end_time = time.time()
        
        if (round(end_time - start_time) < current_player.highscore) or current_player.highscore == 0:
           current_player.highscore = round(end_time - start_time)
           x.config(text = "NOVI REKORD!  "+str(round(end_time - start_time))+" sekundi")
           score_file = open('scores.txt', 'w')
           for i in players:
              score_file.write(str(i.highscore)+' ')
           score_file.close()
                 

        else:
            x.config(text="VRIJEME RJEŠAVANJA : "+str(round(end_time - start_time))+" sekundi")
        restart()
        

def restart():
    y=askyesno('Restart', 'Želite li ponovo pokrenuti igru?')

    if y==True:
        root.destroy()
        os.startfile("Memory.py")

    else:
        root.destroy()

        


        
def easy():

    numbers=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
    random.shuffle(numbers)
    end=10

    b0=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b0,0, numbers, x, end))
    b1=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b1,1, numbers, x, end))
    b2=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b2,2, numbers, x, end))
    b3=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b3,3, numbers, x, end))
    b4=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b4,4, numbers, x, end))
    b5=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b5,5, numbers, x, end))
    b6=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b6,6, numbers, x, end))
    b7=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b7,7, numbers, x, end))
    b8=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b8,8, numbers, x, end))
    b9=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b9,9, numbers, x, end))
    b10=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b10,10, numbers, x, end))
    b11=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b11,11, numbers, x, end))
    b12=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b12,12, numbers, x, end))
    b13=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b13,13, numbers, x, end))
    b14=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b14,14, numbers, x, end))
    b15=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b15,15, numbers, x, end))
    b16=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b16,16, numbers, x, end))
    b17=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b17,17, numbers, x, end))
    b18=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b18,18, numbers, x, end))
    b19=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b19,19, numbers, x, end))

    
    x=Label(root, text=" ",font=("Helvetica",30), fg='midnight blue')
    x.pack(pady=15)

    b0.grid(row = 1, column = 0)
    b1.grid(row = 1, column = 1)
    b2.grid(row = 1, column = 2)
    b3.grid(row = 1, column = 3)
    b4.grid(row = 1, column = 4)

    b5.grid(row = 2, column = 0)
    b6.grid(row = 2, column = 1)
    b7.grid(row = 2, column = 2)
    b8.grid(row = 2, column = 3)
    b9.grid(row = 2, column = 4)

    b10.grid(row = 3, column = 0)
    b11.grid(row = 3, column = 1)
    b12.grid(row = 3, column = 2)
    b13.grid(row = 3, column = 3)
    b14.grid(row = 3, column = 4)

    b15.grid(row = 4, column = 0)
    b16.grid(row = 4, column = 1)
    b17.grid(row = 4, column = 2)
    b18.grid(row = 4, column = 3)
    b19.grid(row = 4, column = 4)


def medium():
    numbers=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15]
    random.shuffle(numbers)
    end=15

    b0=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b0,0, numbers, x, end))
    b1=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b1,1, numbers, x, end))
    b2=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b2,2, numbers, x, end))
    b3=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b3,3, numbers, x, end))
    b4=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b4,4, numbers, x, end))
    b5=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b5,5, numbers, x, end))
    b6=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b6,6, numbers, x, end))
    b7=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b7,7, numbers, x, end))
    b8=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b8,8, numbers, x, end))
    b9=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b9,9, numbers, x, end))
    b10=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b10,10, numbers, x, end))
    b11=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b11,11, numbers, x, end))
    b12=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b12,12, numbers, x, end))
    b13=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b13,13, numbers, x, end))
    b14=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b14,14, numbers, x, end))
    b15=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b15,15, numbers, x,end))
    b16=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b16,16, numbers, x, end))
    b17=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b17,17, numbers, x, end))
    b18=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b18,18, numbers, x, end))
    b19=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b19,19, numbers, x, end))
    b20=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b20,20, numbers, x, end))
    b21=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b21,21, numbers, x, end))
    b22=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b22,22, numbers, x, end))
    b23=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b23,23, numbers, x, end))
    b24=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b24,24, numbers, x, end))
    b25=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b25,25, numbers, x, end))
    b26=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b26,26, numbers, x, end))
    b27=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b27,27, numbers, x, end))
    b28=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b28,28, numbers, x, end))
    b29=Button(frame, text=' ', font=("Helvetica",30), height=2, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b29,29, numbers, x,end ))

    x=Label(root, text=" ",font=("Helvetica",30), fg='midnight blue')
    x.pack(pady=10)

    b0.grid(row=1, column=0)
    b1.grid(row=1, column=1)
    b2.grid(row=1, column=2)
    b3.grid(row=1, column=3)
    b4.grid(row=1, column=4)
    b5.grid(row=1, column=5)
    
    b6.grid(row=2, column=0)
    b7.grid(row=2, column=1)
    b8.grid(row=2, column=2)
    b9.grid(row=2, column=3)
    b10.grid(row=2, column=4)
    b11.grid(row=2, column=5)
    
    b12.grid(row=3, column=0)
    b13.grid(row=3, column=1)
    b14.grid(row=3, column=2)
    b15.grid(row=3, column=3)
    b16.grid(row=3, column=4)
    b17.grid(row=3, column=5)
    
    b18.grid(row=4, column=0)
    b19.grid(row=4, column=1)
    b20.grid(row=4, column=2)
    b21.grid(row=4, column=3)
    b22.grid(row=4, column=4)
    b23.grid(row=4, column=5)
    
    b24.grid(row=5, column=0)
    b25.grid(row=5, column=1)
    b26.grid(row=5, column=2)
    b27.grid(row=5, column=3)
    b28.grid(row=5, column=4)
    b29.grid(row=5, column=5)


def hard():
    numbers=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21]
    random.shuffle(numbers)
    end=21

    b0=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b0,0, numbers, x, end))
    b1=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b1,1, numbers, x, end))
    b2=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b2,2, numbers, x, end))
    b3=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b3,3, numbers, x,end))
    b4=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b4,4, numbers, x, end))
    b5=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b5,5, numbers, x, end))
    b6=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b6,6, numbers, x, end))
    b7=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b7,7, numbers, x, end))
    b8=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b8,8, numbers, x, end))
    b9=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b9,9, numbers, x, end))
    b10=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b10,10, numbers, x, end))
    b11=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b11,11, numbers, x, end))
    b12=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b12,12, numbers, x, end))
    b13=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b13,13, numbers, x, end))
    b14=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b14,14, numbers, x, end))
    b15=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b15,15, numbers, x, end))
    b16=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b16,16, numbers, x, end))
    b17=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b17,17, numbers, x, end))
    b18=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b18,18, numbers, x, end))
    b19=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b19,19, numbers, x, end))
    b20=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b20,20, numbers, x, end))
    b21=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b21,21, numbers, x, end))
    b22=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b22,22, numbers, x, end))
    b23=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b23,23, numbers, x, end))
    b24=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b24,24, numbers, x, end))
    b25=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b25,25, numbers, x, end))
    b26=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b26,26, numbers, x,end))
    b27=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b27,27, numbers, x, end))
    b28=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b28,28, numbers, x, end))
    b29=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b29,29, numbers, x, end))
    b30=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b30,30, numbers, x, end))
    b31=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b31,31, numbers, x,end))
    b32=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b32,32, numbers, x, end))
    b33=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b33,33, numbers, x, end))
    b34=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b34,34, numbers, x, end))
    b35=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b35,35, numbers, x, end))
    b36=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b36,36, numbers, x, end))
    b37=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b37,37, numbers, x, end))
    b38=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b38,38, numbers, x, end))
    b39=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b39,39, numbers, x, end))
    b40=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b40,40, numbers, x, end))
    b41=Button(frame, text=' ', font=("Helvetica",30), height=1, width=7, bg='midnight blue', fg='mint cream', command=lambda: click(b41,41, numbers, x, end))

    x=Label(root, text=" ", font=("Helvetica",30), fg='midnight blue')
    x.pack(pady=10)

    b0.grid(row=1, column=0)
    b1.grid(row=1, column=1)
    b2.grid(row=1, column=2)
    b3.grid(row=1, column=3)
    b4.grid(row=1, column=4)
    b5.grid(row=1, column=5)
    b6.grid(row=1, column=6)
    
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)
    b10.grid(row=2, column=3)
    b11.grid(row=2, column=4)    
    b12.grid(row=2, column=5)
    b13.grid(row=2, column=6)
    
    b14.grid(row=3, column=0)
    b15.grid(row=3, column=1)
    b16.grid(row=3, column=2)
    b17.grid(row=3, column=3)    
    b18.grid(row=3, column=4)
    b19.grid(row=3, column=5)
    b20.grid(row=3, column=6)
    
    b21.grid(row=4, column=0)
    b22.grid(row=4, column=1)
    b23.grid(row=4, column=2)    
    b24.grid(row=4, column=3)
    b25.grid(row=4, column=4)
    b26.grid(row=4, column=5)
    b27.grid(row=4, column=6)
    
    b28.grid(row=5, column=0)
    b29.grid(row=5, column=1)
    b30.grid(row=5, column=2)
    b31.grid(row=5, column=3)
    b32.grid(row=5, column=4)
    b33.grid(row=5, column=5)
    b34.grid(row=5, column=6)
    
    b35.grid(row=6, column=0)
    b36.grid(row=6, column=1)
    b37.grid(row=6, column=2)
    b38.grid(row=6, column=3)
    b39.grid(row=6, column=4)
    b40.grid(row=6, column=5)
    b41.grid(row=6, column=6)

    



root.mainloop()
