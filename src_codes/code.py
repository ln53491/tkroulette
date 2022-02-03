from subprocess import *
from time import *
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from random import *
from tkinter import *
from PIL import Image, ImageTk
from winsound import *
from simpleaudio import *
import imageio
import threading
global broj_vrtnji
global iznos_vrtnji
iznos_vrtnji = []
broj_vrtnji = [0]
global chip_red
global lista_chipova
lista_chipova = ['ch1', 'ch5', 'ch10', 'ch20', 'ch50', 'ch100', 'ch500', 'ch1000']
chip_red = 0
global paree
global gumbaci
global hak
global ocisceno
global statistika_brojeva
statistika_brojeva = []
ocisceno = 0
hak = 0
global gembaci
gumbaci = {'0':0,
           '1':0,
           '2':0,
           '3':0,
           '4':0,
           '5':0,
           '6':0,
           '7':0,
           '8':0,
           '9':0,
           '10':0,
           '11':0,
           '12':0,
           '13':0,
           '14':0,
           '15':0,
           '16':0,
           '17':0,
           '18':0,
           '19':0,
           '20':0,
           '21':0,
           '22':0,
           '23':0,
           '24':0,
           '25':0,
           '26':0,
           '27':0,
           '28':0,
           '29':0,
           '30':0,
           '31':0,
           '32':0,
           '33':0,
           '34':0,
           '35':0,
           '36':0,
           '1-2-4-5':0,
           '2-3-5-6':0,
           '4-5-7-8':0,
           '5-6-8-9':0,
           '7-8-10-11':0,
           '8-9-11-12':0,
           '10-11-13-14':0,
           '11-12-14-15':0,
           '13-14-16-17':0,
           '14-15-17-18':0,
           '16-17-19-20':0,
           '17-18-20-21':0,
           '19-20-22-23':0,
           '20-21-23-24':0,
           '22-23-25-26':0,
           '23-24-26-27':0,
           '25-26-28-29':0,
           '26-27-29-30':0,
           '28-29-31-32':0,
           '29-30-32-33':0,
           '31-32-34-35':0,
           '32-33-35-36':0,
           'CRVENIMA':0,
           'CRNIMA':0,
           'PARNIMA':0,
           'NEPARNIMA':0,
           '1. TREĆINI':0,
           '2. TREĆINI':0,
           '3. TREĆINI':0,
           '1-18':0,
           '19-36':0,
           '1. REDU':0,
           '2. REDU':0,
           '3. REDU':0,
           '1-2-3':0,
           '4-5-6':0,
           '7-8-9':0,
           '10-11-12':0,
           '13-14-15':0,
           '16-17-18':0,
           '19-20-21':0,
           '22-23-24':0,
           '25-26-27':0,
           '28-29-30':0,
           '31-32-33':0,
           '34-35-36':0,
           '1 do 6':0,
           '4 do 9':0,
           '7 do 12':0,
           '10 do 15':0,
           '13 do 18':0,
           '16 do 21':0,
           '19 do 24':0,
           '22 do 27':0,
           '25 do 30':0,
           '28 do 33':0,
           '31 do 36':0,
           '0-1-2-3':0,
           '1-2':0,
           '2-3':0,
           '4-5':0,
           '5-6':0,
           '7-8':0,
           '8-9':0,
           '10-11':0,
           '11-12':0,
           '13-14':0,
           '14-15':0,
           '16-17':0,
           '17-18':0,
           '19-20':0,
           '20-21':0,
           '22-23':0,
           '23-24':0,
           '25-26':0,
           '26-27':0,
           '28-29':0,
           '29-30':0,
           '31-32':0,
           '32-33':0,
           '34-35':0,
           '35-36':0,
           '0-1-2':0,
           '0-2':0,
           '0-1':0,
           '0-3':0,
           '0-2-3':0,
           '1-4':0,
           '2-5':0,
           '3-6':0,
           '4-7':0,
           '5-8':0,
           '6-9':0,
           '7-10':0,
           '8-11':0,
           '9-12':0,
           '10-13':0,
           '11-14':0,
           '12-15':0,
           '13-16':0,
           '14-17':0,
           '15-18':0,
           '16-19':0,
           '17-20':0,
           '18-21':0,
           '19-22':0,
           '20-23':0,
           '21-24':0,
           '22-25':0,
           '23-26':0,
           '24-27':0,
           '25-28':0,
           '26-29':0,
           '27-30':0,
           '28-31':0,
           '29-32':0,
           '30-33':0,
           '31-34':0,
           '32-35':0,
           '33-36':0}
gembaci = {'0':0,
           '1':0,
           '2':0,
           '3':0,
           '4':0,
           '5':0,
           '6':0,
           '7':0,
           '8':0,
           '9':0,
           '10':0,
           '11':0,
           '12':0,
           '13':0,
           '14':0,
           '15':0,
           '16':0,
           '17':0,
           '18':0,
           '19':0,
           '20':0,
           '21':0,
           '22':0,
           '23':0,
           '24':0,
           '25':0,
           '26':0,
           '27':0,
           '28':0,
           '29':0,
           '30':0,
           '31':0,
           '32':0,
           '33':0,
           '34':0,
           '35':0,
           '36':0,
           '1-2-4-5':0,
           '2-3-5-6':0,
           '4-5-7-8':0,
           '5-6-8-9':0,
           '7-8-10-11':0,
           '8-9-11-12':0,
           '10-11-13-14':0,
           '11-12-14-15':0,
           '13-14-16-17':0,
           '14-15-17-18':0,
           '16-17-19-20':0,
           '17-18-20-21':0,
           '19-20-22-23':0,
           '20-21-23-24':0,
           '22-23-25-26':0,
           '23-24-26-27':0,
           '25-26-28-29':0,
           '26-27-29-30':0,
           '28-29-31-32':0,
           '29-30-32-33':0,
           '31-32-34-35':0,
           '32-33-35-36':0,
           'CRVENIMA':0,
           'CRNIMA':0,
           'PARNIMA':0,
           'NEPARNIMA':0,
           '1. TREĆINI':0,
           '2. TREĆINI':0,
           '3. TREĆINI':0,
           '1-18':0,
           '19-36':0,
           '1. REDU':0,
           '2. REDU':0,
           '3. REDU':0,
           '1-2-3':0,
           '4-5-6':0,
           '7-8-9':0,
           '10-11-12':0,
           '13-14-15':0,
           '16-17-18':0,
           '19-20-21':0,
           '22-23-24':0,
           '25-26-27':0,
           '28-29-30':0,
           '31-32-33':0,
           '34-35-36':0,
           '1 do 6':0,
           '4 do 9':0,
           '7 do 12':0,
           '10 do 15':0,
           '13 do 18':0,
           '16 do 21':0,
           '19 do 24':0,
           '22 do 27':0,
           '25 do 30':0,
           '28 do 33':0,
           '31 do 36':0,
           '0-1-2-3':0,
           '1-2':0,
           '2-3':0,
           '4-5':0,
           '5-6':0,
           '7-8':0,
           '8-9':0,
           '10-11':0,
           '11-12':0,
           '13-14':0,
           '14-15':0,
           '16-17':0,
           '17-18':0,
           '19-20':0,
           '20-21':0,
           '22-23':0,
           '23-24':0,
           '25-26':0,
           '26-27':0,
           '28-29':0,
           '29-30':0,
           '31-32':0,
           '32-33':0,
           '34-35':0,
           '35-36':0,
           '0-1-2':0,
           '0-2':0,
           '0-1':0,
           '0-3':0,
           '0-2-3':0,
           '1-4':0,
           '2-5':0,
           '3-6':0,
           '4-7':0,
           '5-8':0,
           '6-9':0,
           '7-10':0,
           '8-11':0,
           '9-12':0,
           '10-13':0,
           '11-14':0,
           '12-15':0,
           '13-16':0,
           '14-17':0,
           '15-18':0,
           '16-19':0,
           '17-20':0,
           '18-21':0,
           '19-22':0,
           '20-23':0,
           '21-24':0,
           '22-25':0,
           '23-26':0,
           '24-27':0,
           '25-28':0,
           '26-29':0,
           '27-30':0,
           '28-31':0,
           '29-32':0,
           '30-33':0,
           '31-34':0,
           '32-35':0,
           '33-36':0}
global samo_brojevi
samo_brojevi = {'0':0,
           '1':0,
           '2':0,
           '3':0,
           '4':0,
           '5':0,
           '6':0,
           '7':0,
           '8':0,
           '9':0,
           '10':0,
           '11':0,
           '12':0,
           '13':0,
           '14':0,
           '15':0,
           '16':0,
           '17':0,
           '18':0,
           '19':0,
           '20':0,
           '21':0,
           '22':0,
           '23':0,
           '24':0,
           '25':0,
           '26':0,
           '27':0,
           '28':0,
           '29':0,
           '30':0,
           '31':0,
           '32':0,
           '33':0,
           '34':0,
           '35':0,
           '36':0}

def disable_event():
    c1.create_image(1280/2+2, 480/2+1, image=bg2)
    c1.create_text(630, 430,
                       fill='yellow',
                       text = 'Ti si kao mislio izac?',
                       font=("Helvetica",12,'bold'))

def zapocni(e=None):
    PlaySound(None, SND_PURGE)
    r.destroy()

def pare1(e=None):
    global a
    a = pare.get()
    try:
        a = int(a)
        if a<=1000000 and a>0:
            pare.delete(0,END)
            pare.insert(0,'Uplata uspješna!')
            uplati.config(state = DISABLED, relief=RAISED,\
                   cursor="pirate")
            pare.config(state = DISABLED, relief=RAISED,\
                   cursor="pirate")
            start.config(state = NORMAL, relief=RAISED,\
                   cursor="arrow")
            c1.delete(t1)
            start.config(text = "(Spreman sam izgubit ove pare)", relief=RAISED,\
               cursor="circle")
            c1.create_image(1280/2+2, 480/2+1, image=bg2)
        elif a>1000000:
            c1.create_image(1280/2+2, 480/2+1, image=bg2)
            c1.create_text(630, 430,
                       fill='yellow',
                       text = 'Sori lik, maks uplata je jedna milja :/',
                       font=("Helvetica",12,'bold'))
        elif a<=0:
            c1.create_image(1280/2+2, 480/2+1, image=bg2)
            c1.create_text(630, 430,
                       fill='yellow',
                       text = 'Kaj glumis ti?',
                       font=("Helvetica",12,'bold'))
            
    except:
        c1.create_image(1280/2+2, 480/2+1, image=bg2)
        c1.create_text(630, 430,
                       fill='yellow',
                       text = 'Fala kaj si unio normalan broj ono',
                       font=("Helvetica",12,'bold'))
    
klinac = PlaySound('intro\\kazino.wav', SND_LOOP + SND_ASYNC)

r = Tk()
r.iconbitmap("intro\\icon.ico")
c1 = Canvas(r, width=1280, height=480)
c1.pack()
r.protocol("WM_DELETE_WINDOW", disable_event)
bg = ImageTk.PhotoImage(file = 'intro\\realbg.png')
bg2 = ImageTk.PhotoImage(file = 'intro\\bg2.png')
c1.create_image(1280/2+1, 480/2+1, image=bg)
c1.config(cursor="circle")
start = Button(r,
               command = zapocni,
               width=30,
               state=DISABLED,
               activebackground = "red",
               background = "#00771c",
               font=("Calibri",10),
               fg='white',
               relief=RAISED,\
               cursor="pirate")
start_window = c1.create_window(1040/2, 500/2, anchor='nw', window=start)

pare = Entry(c1,
             justify='center',
             background = "yellow",
             fg='black',
             font=("Calibri",10, 'bold'))
c1.create_window(630, 350, window = pare)

t1 = c1.create_text(630, 330, fill='white', text = 'Unesi početni iznos u kunama:')

uplati = Button(r,
                text = 'Uplati',
                width=10,
                activebackground = "red",
                command = pare1,
                background = "#00771c",
                font=("Calibri",10),
                fg='white',
                relief=RAISED,\
               cursor="circle")
uplati_window = c1.create_window(590, 370, anchor='nw', window=uplati)


r.title('TkinteRoulette™')
r.resizable(False, False)
r.mainloop()

sleep(1)

def obrisi(e=None):
    global ocisceno
    global paree
    global chip_red
    global isp
    bb=0
    obavijesti.config(state=NORMAL)
    poss = obavijesti.search('Dobrodošli','1.0', stopindex=END)
    try:
        poss=float(poss)
    except:
        obavijesti.delete('1.0',END)
        obavijesti.insert(END, 'Svi ulozi su obrisani!')
        obavijesti.config(state=DISABLED)
        ocisceno+=1
        for c in gumbaci:
            bb+=gumbaci[c]
        for c in gumbaci:
            gumbaci[c]=0
        ispis_para.config(state=NORMAL)
        paree=paree+bb
        isp=paree
        ispis_para.delete('1.0',END)
        ispis_para.insert(END, paree, 'tag-right')
        ispis_para.config(state=DISABLED)
        c2.itemconfig(ch1, image=ch1_5)
        c2.itemconfig(ch5, image=ch5_5)
        c2.itemconfig(ch10, image=ch10_5)
        c2.itemconfig(ch20, image=ch20_5)
        c2.itemconfig(ch50, image=ch50_5)
        c2.itemconfig(ch100, image=ch100_5)
        c2.itemconfig(ch500, image=ch500_5)
        c2.itemconfig(ch1000, image=ch1000_5)
        c2.tag_bind(ch1, '<Enter>', ch1_1)
        c2.tag_bind(ch1, '<Leave>', ch1_2)
        c2.tag_bind(ch5, '<Enter>', ch5_1)
        c2.tag_bind(ch5, '<Leave>', ch5_2)
        c2.tag_bind(ch10, '<Enter>', ch10_1)
        c2.tag_bind(ch10, '<Leave>', ch10_2)
        c2.tag_bind(ch20, '<Enter>', ch20_1)
        c2.tag_bind(ch20, '<Leave>', ch20_2)
        c2.tag_bind(ch50, '<Enter>', ch50_1)
        c2.tag_bind(ch50, '<Leave>', ch50_2)
        c2.tag_bind(ch100, '<Enter>', ch100_1)
        c2.tag_bind(ch100, '<Leave>', ch100_2)
        c2.tag_bind(ch500, '<Enter>', ch500_1)
        c2.tag_bind(ch500, '<Leave>', ch500_2)
        c2.tag_bind(ch1000, '<Enter>', ch1000_1)
        c2.tag_bind(ch1000, '<Leave>', ch1000_2)

        chip_red=0
    obavijesti.config(state=DISABLED)


def bootleg_obrisi(e=None):
    global ocisceno
    global paree
    global chip_red
    global isp
    bb=0
    obavijesti.config(state=NORMAL)
    poss = obavijesti.search('Dobrodošli','1.0', stopindex=END)
    try:
        poss=float(poss)
    except:
        obavijesti.delete('1.0',END)
        obavijesti.config(state=DISABLED)
        ocisceno+=1
        for c in gumbaci:
            bb+=gumbaci[c]
        for c in gumbaci:
            gumbaci[c]=0
        chip_red=0
    obavijesti.config(state=DISABLED)



def c_1_2_3_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['1-2-3'] = gumbaci['1-2-3']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 1-2-3 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_4_5_6_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['4-5-6'] = gumbaci['4-5-6']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 4-5-6 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_7_8_9_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['7-8-9'] = gumbaci['7-8-9']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 7-8-9 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_10_11_12_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['10-11-12'] = gumbaci['10-11-12']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 10-11-12 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_13_14_15_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['13-14-15'] = gumbaci['13-14-15']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 13-14-15 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_16_17_18_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['16-17-18'] = gumbaci['16-17-18']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 16-17-18 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_19_20_21_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['19-20-21'] = gumbaci['19-20-21']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 19-20-21 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_22_23_24_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['22-23-24'] = gumbaci['22-23-24']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 22-23-24 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_25_26_27_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['25-26-27'] = gumbaci['25-26-27']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 25-26-27 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_28_29_30_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['28-29-30'] = gumbaci['28-29-30']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 28-29-30 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_31_32_33_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['31-32-33'] = gumbaci['31-32-33']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 31-32-33 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_34_35_36_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['34-35-36'] = gumbaci['34-35-36']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 34-35-36 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_1_2_3_4_5_6_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['1 do 6'] = gumbaci['1 do 6']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 1 do 6 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_4_5_6_7_8_9_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['4 do 9'] = gumbaci['4 do 9']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 4 do 9 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_7_8_9_10_11_12_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['7 do 12'] = gumbaci['7 do 12']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 7 do 12 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_10_11_12_13_14_15_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['10 do 15'] = gumbaci['10 do 15']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 10 do 15 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_13_14_15_16_17_18_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['13 do 18'] = gumbaci['13 do 18']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 13 do 18 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_16_17_18_19_20_21_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['16 do 21'] = gumbaci['16 do 21']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 16 do 21 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_19_20_21_22_23_24_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['19 do 24'] = gumbaci['19 do 24']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 19 do 24 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_22_23_24_25_26_27_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['22 do 27'] = gumbaci['22 do 27']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 22 do 27 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_25_26_27_28_29_30_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['25 do 30'] = gumbaci['25 do 30']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 25 do 30 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_28_29_30_31_32_33_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['28 do 33'] = gumbaci['28 do 33']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 28 do 33 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_31_32_33_34_35_36_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['31 do 36'] = gumbaci['31 do 36']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 31 do 36 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_0_1_2_3_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['0-1-2-3'] = gumbaci['0-1-2-3']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 0-1-2-3 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_1_2_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['1-2'] = gumbaci['1-2']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 1-2 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_2_3_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['2-3'] = gumbaci['2-3']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 2-3 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_4_5_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['4-5'] = gumbaci['4-5']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 4-5 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_5_6_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['5-6'] = gumbaci['5-6']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 5-6 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_7_8_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['7-8'] = gumbaci['7-8']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 7-8 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_8_9_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['8-9'] = gumbaci['8-9']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 8-9 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_10_11_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['10-11'] = gumbaci['10-11']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 10-11 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_11_12_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['11-12'] = gumbaci['11-12']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 11-12 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_13_14_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['13-14'] = gumbaci['13-14']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 13-14 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_14_15_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['14-15'] = gumbaci['14-15']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 14-15 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_16_17_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['16-17'] = gumbaci['16-17']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 16-17 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_17_18_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['17-18'] = gumbaci['17-18']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 17-18 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_19_20_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['19-20'] = gumbaci['19-20']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 19-20 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_20_21_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['20-21'] = gumbaci['20-21']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 20-21 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_22_23_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['22-23'] = gumbaci['22-23']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 22-23 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_23_24_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['23-24'] = gumbaci['23-24']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 23-24 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_25_26_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['25-26'] = gumbaci['25-26']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 25-26 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_26_27_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['26-27'] = gumbaci['26-27']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 26-27 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_28_29_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['28-29'] = gumbaci['28-29']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 28-29 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_29_30_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['29-30'] = gumbaci['29-30']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 29-30 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_31_32_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['31-32'] = gumbaci['31-32']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 31-32 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_32_33_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['32-33'] = gumbaci['32-33']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 32-33 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_34_35_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['34-35'] = gumbaci['34-35']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 34-35 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_35_36_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['35-36'] = gumbaci['35-36']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 35-36 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_0_1_2_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['0-1-2'] = gumbaci['0-1-2']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 0-1-2 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_0_2_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['0-2'] = gumbaci['0-2']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 0-2 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_0_1_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['0-1'] = gumbaci['0-1']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 0-1 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_0_3_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['0-3'] = gumbaci['0-3']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 0-3 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_0_2_3_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['0-2-3'] = gumbaci['0-2-3']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 0-2-3 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_1_4_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['1-4'] = gumbaci['1-4']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 1-4 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_2_5_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['2-5'] = gumbaci['2-5']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 2-5 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_3_6_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['3-6'] = gumbaci['3-6']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 3-6 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_4_7_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['4-7'] = gumbaci['4-7']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 4-7 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_5_8_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['5-8'] = gumbaci['5-8']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 5-8 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_6_9_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['6-9'] = gumbaci['6-9']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 6-9 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_7_10_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['7-10'] = gumbaci['7-10']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 7-10 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_8_11_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['8-11'] = gumbaci['8-11']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 8-11 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_9_12_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['9-12'] = gumbaci['9-12']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 9-12 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_10_13_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['10-13'] = gumbaci['10-13']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 10-13 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_11_14_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['11-14'] = gumbaci['11-14']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 11-14 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_12_15_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['12-15'] = gumbaci['12-15']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 12-15 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_13_16_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['13-16'] = gumbaci['13-16']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 13-16 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_14_17_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['14-17'] = gumbaci['14-17']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 14-17 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_15_18_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['15-18'] = gumbaci['15-18']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 15-18 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_16_19_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['16-19'] = gumbaci['16-19']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 16-19 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_17_20_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['17-20'] = gumbaci['17-20']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 17-20 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_18_21_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['18-21'] = gumbaci['18-21']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 18-21 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_19_22_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['19-22'] = gumbaci['19-22']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 19-22 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_20_23_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['20-23'] = gumbaci['20-23']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 20-23 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_21_24_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['21-24'] = gumbaci['21-24']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 21-24 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_22_25_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['22-25'] = gumbaci['22-25']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 22-25 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_23_26_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['23-26'] = gumbaci['23-26']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 23-26 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_24_27_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['24-27'] = gumbaci['24-27']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 24-27 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_25_28_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['25-28'] = gumbaci['25-28']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 25-28 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_26_29_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['26-29'] = gumbaci['26-29']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 26-29 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_27_30_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['27-30'] = gumbaci['27-30']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 27-30 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_28_31_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['28-31'] = gumbaci['28-31']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 28-31 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_29_32_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['29-32'] = gumbaci['29-32']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 29-32 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_30_33_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['30-33'] = gumbaci['30-33']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 30-33 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_31_34_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['31-34'] = gumbaci['31-34']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 31-34 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_32_35_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['32-35'] = gumbaci['32-35']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 32-35 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_33_36_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['33-36'] = gumbaci['33-36']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 33-36 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)



                



def prva_tri_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['1. REDU'] = gumbaci['1. REDU']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 1. REDU ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def druga_tri_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['2. REDU'] = gumbaci['2. REDU']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 2. REDU ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def treca_tri_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['3. REDU'] = gumbaci['3. REDU']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 3. REDU ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)

def crveni_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['CRVENIMA'] = gumbaci['CRVENIMA']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na CRVENIMA ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def crni_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['CRNIMA'] = gumbaci['CRNIMA']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na CRNIMA ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def prva_trecina_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['1. TREĆINI'] = gumbaci['1. TREĆINI']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 1. TREĆINI ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def druga_trecina_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['2. TREĆINI'] = gumbaci['2. TREĆINI']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 2. TREĆINI ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def treca_trecina_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['3. TREĆINI'] = gumbaci['3. TREĆINI']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 3. TREĆINI ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def prvih_18_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['1-18'] = gumbaci['1-18']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 1-18 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def drugih_18_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['19-36'] = gumbaci['19-36']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 19-36 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def even_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['PARNIMA'] = gumbaci['PARNIMA']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na PARNIMA ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def odd_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['NEPARNIMA'] = gumbaci['NEPARNIMA']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na NEPARNIMA ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)

def c_prva_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['2-3-5-6'] = gumbaci['2-3-5-6']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 2-3-5-6 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_druga_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['1-2-4-5'] = gumbaci['1-2-4-5']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 1-2-4-5 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_treca_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['5-6-8-9'] = gumbaci['5-6-8-9']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 5-6-8-9 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_cetvrta_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['4-5-7-8'] = gumbaci['4-5-7-8']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 4-5-7-8 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_peta_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['8-9-11-12'] = gumbaci['8-9-11-12']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 8-9-11-12 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_sesta_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['7-8-10-11'] = gumbaci['7-8-10-11']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 7-8-10-11 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_sedma_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['11-12-14-15'] = gumbaci['11-12-14-15']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 11-12-14-15 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_osma_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['10-11-13-14'] = gumbaci['10-11-13-14']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 10-11-13-14 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_deveta_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['14-15-17-18'] = gumbaci['14-15-17-18']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 14-15-17-18 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_deseta_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['13-14-16-17'] = gumbaci['13-14-16-17']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 13-14-16-17 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_jedanaesta_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['17-18-20-21'] = gumbaci['17-18-20-21']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 17-18-20-21 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_dvanaesta_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['16-17-19-20'] = gumbaci['16-17-19-20']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 16-17-19-20 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_trinaesta_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['20-21-23-24'] = gumbaci['20-21-23-24']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 20-21-23-24 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_cetrnaesta_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['19-20-22-23'] = gumbaci['19-20-22-23']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 19-20-22-23 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_petnaesta_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['23-24-26-27'] = gumbaci['23-24-26-27']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 23-24-26-27 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_sesnaesta_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['22-23-25-26'] = gumbaci['22-23-25-26']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 22-23-25-26 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_sedamnaesta_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['26-27-29-30'] = gumbaci['26-27-29-30']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 26-27-29-30 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_osamnaesta_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['25-26-28-29'] = gumbaci['25-26-28-29']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 25-26-28-29 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_devetnaesta_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['29-30-32-33'] = gumbaci['29-30-32-33']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 29-30-32-33 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_dvadeseta_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['28-29-31-32'] = gumbaci['28-29-31-32']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 28-29-31-32 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_dvadesetprva_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['32-33-35-36'] = gumbaci['32-33-35-36']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 32-33-35-36 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def c_dvadesetdruga_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['31-32-34-35'] = gumbaci['31-32-34-35']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 31-32-34-35 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)


def nula_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['0'] = gumbaci['0']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 0 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
    
def jedan_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['1'] = gumbaci['1']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 1 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)

def dva_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['2'] = gumbaci['2']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 2 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def tri_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['3'] = gumbaci['3']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 3 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def cetiri_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['4'] = gumbaci['4']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 4 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def pet_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['5'] = gumbaci['5']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 5 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def sest_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['6'] = gumbaci['6']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 6 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def sedam_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['7'] = gumbaci['7']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 7 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def osam_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['8'] = gumbaci['8']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 8 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def devet_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['9'] = gumbaci['9']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 9 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def deset_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['10'] = gumbaci['10']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 10 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def jedanaest_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['11'] = gumbaci['11']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 11 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def dvanaest_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['12'] = gumbaci['12']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 12 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def trinaest_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['13'] = gumbaci['13']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 13 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def cetrnaest_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['14'] = gumbaci['14']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 14 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def petnaest_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['15'] = gumbaci['15']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 15 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def sesnaest_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['16'] = gumbaci['16']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 16 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def sedamnaest_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['17'] = gumbaci['17']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 17 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def osamnaest_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['18'] = gumbaci['18']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 18 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def devetnaest_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['19'] = gumbaci['19']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 19 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def d_nula_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['20'] = gumbaci['20']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 20 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def d_jedan_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['21'] = gumbaci['21']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 21 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def d_dva_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['22'] = gumbaci['22']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 22 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def d_tri_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['23'] = gumbaci['23']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 23 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def d_cetiri_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['24'] = gumbaci['24']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 24 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def d_pet_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['25'] = gumbaci['25']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 25 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def d_sest_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['26'] = gumbaci['26']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 26 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def d_sedam_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['27'] = gumbaci['27']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 27 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def d_osam_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['28'] = gumbaci['28']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 28 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def d_devet_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['29'] = gumbaci['29']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 29 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def t_nula_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['30'] = gumbaci['30']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 30 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def t_jedan_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['31'] = gumbaci['31']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 31 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def t_dva_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['32'] = gumbaci['32']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 32 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def t_tri_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['33'] = gumbaci['33']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 33 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def t_cetiri_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['34'] = gumbaci['34']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 34 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def t_pet_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['35'] = gumbaci['35']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 35 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)
def t_sest_klik(e=None):
    global isp
    global paree
    grr = []
    if (int(ispis_para.get('1.0',END))-chip_red)<=-1:
        pass
    else:
        gumbaci['36'] = gumbaci['36']+chip_red
        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        for cc in gumbaci:
            if gumbaci[cc] > 0:
                grr.append(cc)
        paree=paree-chip_red
        for i in range(len(grr)):
            ispis_para.config(state=NORMAL)
            isp=ispis_para.get('1.0',END)
            obavijesti.insert(END, 'Iznos na ')
            obavijesti.insert(END, str(grr[i]), 'broj')
            obavijesti.insert(END, ' je ')
            obavijesti.insert(END, str(gumbaci[grr[i]]), 'iznos')
            if grr[i] != grr[-1]:
                obavijesti.insert(END, '\n')
            else:
                pass
            if (int(isp)-chip_red)<=-1:
                c2.itemconfig(ch1, image=ch1_5)
                c2.itemconfig(ch5, image=ch5_5)
                c2.itemconfig(ch10, image=ch10_5)
                c2.itemconfig(ch20, image=ch20_5)
                c2.itemconfig(ch50, image=ch50_5)
                c2.itemconfig(ch100, image=ch100_5)
                c2.itemconfig(ch500, image=ch500_5)
                c2.itemconfig(ch1000, image=ch1000_5)
                c2.tag_bind(ch1, '<Enter>', ch1_1)
                c2.tag_bind(ch1, '<Leave>', ch1_2)
                c2.tag_bind(ch5, '<Enter>', ch5_1)
                c2.tag_bind(ch5, '<Leave>', ch5_2)
                c2.tag_bind(ch10, '<Enter>', ch10_1)
                c2.tag_bind(ch10, '<Leave>', ch10_2)
                c2.tag_bind(ch20, '<Enter>', ch20_1)
                c2.tag_bind(ch20, '<Leave>', ch20_2)
                c2.tag_bind(ch50, '<Enter>', ch50_1)
                c2.tag_bind(ch50, '<Leave>', ch50_2)
                c2.tag_bind(ch100, '<Enter>', ch100_1)
                c2.tag_bind(ch100, '<Leave>', ch100_2)
                c2.tag_bind(ch500, '<Enter>', ch500_1)
                c2.tag_bind(ch500, '<Leave>', ch500_2)
                c2.tag_bind(ch1000, '<Enter>', ch1000_1)
                c2.tag_bind(ch1000, '<Leave>', ch1000_2)
            else:
                ispis_para.delete('1.0',END)
                ispis_para.insert(END, paree, 'tag-right')
                ispis_para.config(state=DISABLED)
        pos = obavijesti.search('Iznos na 36 ', '1.0', stopindex=END)
        try:
            obavijesti.yview_pickplace(pos)
            obavijesti.config(state=DISABLED)
        except:
            if ocisceno == 0:
                obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, '>----------------------<', 'tag-center')
                obavijesti.insert(END, '\n', 'tag-center')
                obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
                obavijesti.config(state=DISABLED)
            else:
                obavijesti.insert(END, 'Svi ulozi su obrisani!')
                obavijesti.config(state=DISABLED)



def c_1_2_3_hov1(e=None):
    c2.itemconfig('jedan', fill='orange')
    c2.itemconfig('dva', fill='orange')
    c2.itemconfig('tri', fill='orange')
def c_1_2_3_hov2(e=None):
    c2.itemconfig('jedan', fill='red')
    c2.itemconfig('dva', fill='black')
    c2.itemconfig('tri', fill='red')
def c_4_5_6_hov1(e=None):
    c2.itemconfig('cetiri', fill='orange')
    c2.itemconfig('pet', fill='orange')
    c2.itemconfig('sest', fill='orange')
def c_4_5_6_hov2(e=None):
    c2.itemconfig('cetiri', fill='black')
    c2.itemconfig('pet', fill='red')
    c2.itemconfig('sest', fill='black')
def c_7_8_9_hov1(e=None):
    c2.itemconfig('sedam', fill='orange')
    c2.itemconfig('osam', fill='orange')
    c2.itemconfig('devet', fill='orange')
def c_7_8_9_hov2(e=None):
    c2.itemconfig('sedam', fill='red')
    c2.itemconfig('osam', fill='black')
    c2.itemconfig('devet', fill='red')
def c_10_11_12_hov1(e=None):
    c2.itemconfig('deset', fill='orange')
    c2.itemconfig('jedanaest', fill='orange')
    c2.itemconfig('dvanaest', fill='orange')
def c_10_11_12_hov2(e=None):
    c2.itemconfig('deset', fill='black')
    c2.itemconfig('jedanaest', fill='black')
    c2.itemconfig('dvanaest', fill='red')
def c_13_14_15_hov1(e=None):
    c2.itemconfig('trinaest', fill='orange')
    c2.itemconfig('cetrnaest', fill='orange')
    c2.itemconfig('petnaest', fill='orange')
def c_13_14_15_hov2(e=None):
    c2.itemconfig('trinaest', fill='black')
    c2.itemconfig('cetrnaest', fill='red')
    c2.itemconfig('petnaest', fill='black')
def c_16_17_18_hov1(e=None):
    c2.itemconfig('sesnaest', fill='orange')
    c2.itemconfig('sedamnaest', fill='orange')
    c2.itemconfig('osamnaest', fill='orange')
def c_16_17_18_hov2(e=None):
    c2.itemconfig('sesnaest', fill='red')
    c2.itemconfig('sedamnaest', fill='black')
    c2.itemconfig('osamnaest', fill='red')
def c_19_20_21_hov1(e=None):
    c2.itemconfig('devetnaest', fill='orange')
    c2.itemconfig('d_nula', fill='orange')
    c2.itemconfig('d_jedan', fill='orange')
def c_19_20_21_hov2(e=None):
    c2.itemconfig('devetnaest', fill='red')
    c2.itemconfig('d_nula', fill='black')
    c2.itemconfig('d_jedan', fill='red')
def c_22_23_24_hov1(e=None):
    c2.itemconfig('d_dva', fill='orange')
    c2.itemconfig('d_tri', fill='orange')
    c2.itemconfig('d_cetiri', fill='orange')
def c_22_23_24_hov2(e=None):
    c2.itemconfig('d_dva', fill='black')
    c2.itemconfig('d_tri', fill='red')
    c2.itemconfig('d_cetiri', fill='black')
def c_25_26_27_hov1(e=None):
    c2.itemconfig('d_pet', fill='orange')
    c2.itemconfig('d_sest', fill='orange')
    c2.itemconfig('d_sedam', fill='orange')
def c_25_26_27_hov2(e=None):
    c2.itemconfig('d_pet', fill='red')
    c2.itemconfig('d_sest', fill='black')
    c2.itemconfig('d_sedam', fill='red')
def c_28_29_30_hov1(e=None):
    c2.itemconfig('d_osam', fill='orange')
    c2.itemconfig('d_devet', fill='orange')
    c2.itemconfig('t_nula', fill='orange')
def c_28_29_30_hov2(e=None):
    c2.itemconfig('d_osam', fill='black')
    c2.itemconfig('d_devet', fill='black')
    c2.itemconfig('t_nula', fill='red')
def c_31_32_33_hov1(e=None):
    c2.itemconfig('t_jedan', fill='orange')
    c2.itemconfig('t_dva', fill='orange')
    c2.itemconfig('t_tri', fill='orange')
def c_31_32_33_hov2(e=None):
    c2.itemconfig('t_jedan', fill='black')
    c2.itemconfig('t_dva', fill='red')
    c2.itemconfig('t_tri', fill='black')
def c_34_35_36_hov1(e=None):
    c2.itemconfig('t_cetiri', fill='orange')
    c2.itemconfig('t_pet', fill='orange')
    c2.itemconfig('t_sest', fill='orange')
def c_34_35_36_hov2(e=None):
    c2.itemconfig('t_cetiri', fill='red')
    c2.itemconfig('t_pet', fill='black')
    c2.itemconfig('t_sest', fill='red')
def c_0_1_2_3_hov1(e=None):
    c2.itemconfig('nula', fill='orange')
    c2.itemconfig('jedan', fill='orange')
    c2.itemconfig('dva', fill='orange')
    c2.itemconfig('tri', fill='orange')
def c_0_1_2_3_hov2(e=None):
    c2.itemconfig('nula', fill='green')
    c2.itemconfig('jedan', fill='red')
    c2.itemconfig('dva', fill='black')
    c2.itemconfig('tri', fill='red')
def c_1_2_3_4_5_6_hov1(e=None):
    c2.itemconfig('jedan', fill='orange')
    c2.itemconfig('dva', fill='orange')
    c2.itemconfig('tri', fill='orange')
    c2.itemconfig('cetiri', fill='orange')
    c2.itemconfig('pet', fill='orange')
    c2.itemconfig('sest', fill='orange')
def c_1_2_3_4_5_6_hov2(e=None):
    c2.itemconfig('jedan', fill='red')
    c2.itemconfig('dva', fill='black')
    c2.itemconfig('tri', fill='red')
    c2.itemconfig('cetiri', fill='black')
    c2.itemconfig('pet', fill='red')
    c2.itemconfig('sest', fill='black')
def c_4_5_6_7_8_9_hov1(e=None):
    c2.itemconfig('sedam', fill='orange')
    c2.itemconfig('osam', fill='orange')
    c2.itemconfig('devet', fill='orange')
    c2.itemconfig('cetiri', fill='orange')
    c2.itemconfig('pet', fill='orange')
    c2.itemconfig('sest', fill='orange')
def c_4_5_6_7_8_9_hov2(e=None):
    c2.itemconfig('sedam', fill='red')
    c2.itemconfig('osam', fill='black')
    c2.itemconfig('devet', fill='red')
    c2.itemconfig('cetiri', fill='black')
    c2.itemconfig('pet', fill='red')
    c2.itemconfig('sest', fill='black')
def c_7_8_9_10_11_12_hov1(e=None):
    c2.itemconfig('sedam', fill='orange')
    c2.itemconfig('osam', fill='orange')
    c2.itemconfig('devet', fill='orange')
    c2.itemconfig('deset', fill='orange')
    c2.itemconfig('jedanaest', fill='orange')
    c2.itemconfig('dvanaest', fill='orange')
def c_7_8_9_10_11_12_hov2(e=None):
    c2.itemconfig('sedam', fill='red')
    c2.itemconfig('osam', fill='black')
    c2.itemconfig('devet', fill='red')
    c2.itemconfig('deset', fill='black')
    c2.itemconfig('jedanaest', fill='black')
    c2.itemconfig('dvanaest', fill='red')
def c_10_11_12_13_14_15_hov1(e=None):
    c2.itemconfig('trinaest', fill='orange')
    c2.itemconfig('cetrnaest', fill='orange')
    c2.itemconfig('petnaest', fill='orange')
    c2.itemconfig('deset', fill='orange')
    c2.itemconfig('jedanaest', fill='orange')
    c2.itemconfig('dvanaest', fill='orange')
def c_10_11_12_13_14_15_hov2(e=None):
    c2.itemconfig('trinaest', fill='black')
    c2.itemconfig('cetrnaest', fill='red')
    c2.itemconfig('petnaest', fill='black')
    c2.itemconfig('deset', fill='black')
    c2.itemconfig('jedanaest', fill='black')
    c2.itemconfig('dvanaest', fill='red')
def c_13_14_15_16_17_18_hov1(e=None):
    c2.itemconfig('trinaest', fill='orange')
    c2.itemconfig('cetrnaest', fill='orange')
    c2.itemconfig('petnaest', fill='orange')
    c2.itemconfig('sesnaest', fill='orange')
    c2.itemconfig('sedamnaest', fill='orange')
    c2.itemconfig('osamnaest', fill='orange')
def c_13_14_15_16_17_18_hov2(e=None):
    c2.itemconfig('trinaest', fill='black')
    c2.itemconfig('cetrnaest', fill='red')
    c2.itemconfig('petnaest', fill='black')
    c2.itemconfig('sesnaest', fill='red')
    c2.itemconfig('sedamnaest', fill='black')
    c2.itemconfig('osamnaest', fill='red')
def c_16_17_18_19_20_21_hov1(e=None):
    c2.itemconfig('devetnaest', fill='orange')
    c2.itemconfig('d_nula', fill='orange')
    c2.itemconfig('d_jedan', fill='orange')
    c2.itemconfig('sesnaest', fill='orange')
    c2.itemconfig('sedamnaest', fill='orange')
    c2.itemconfig('osamnaest', fill='orange')
def c_16_17_18_19_20_21_hov2(e=None):
    c2.itemconfig('devetnaest', fill='red')
    c2.itemconfig('d_nula', fill='black')
    c2.itemconfig('d_jedan', fill='red')
    c2.itemconfig('sesnaest', fill='red')
    c2.itemconfig('sedamnaest', fill='black')
    c2.itemconfig('osamnaest', fill='red')
def c_19_20_21_22_23_24_hov1(e=None):
    c2.itemconfig('devetnaest', fill='orange')
    c2.itemconfig('d_nula', fill='orange')
    c2.itemconfig('d_jedan', fill='orange')
    c2.itemconfig('d_dva', fill='orange')
    c2.itemconfig('d_tri', fill='orange')
    c2.itemconfig('d_cetiri', fill='orange')
def c_19_20_21_22_23_24_hov2(e=None):
    c2.itemconfig('devetnaest', fill='red')
    c2.itemconfig('d_nula', fill='black')
    c2.itemconfig('d_jedan', fill='red')
    c2.itemconfig('d_dva', fill='black')
    c2.itemconfig('d_tri', fill='red')
    c2.itemconfig('d_cetiri', fill='black')
def c_22_23_24_25_26_27_hov1(e=None):
    c2.itemconfig('d_pet', fill='orange')
    c2.itemconfig('d_sest', fill='orange')
    c2.itemconfig('d_sedam', fill='orange')
    c2.itemconfig('d_dva', fill='orange')
    c2.itemconfig('d_tri', fill='orange')
    c2.itemconfig('d_cetiri', fill='orange')
def c_22_23_24_25_26_27_hov2(e=None):
    c2.itemconfig('d_pet', fill='red')
    c2.itemconfig('d_sest', fill='black')
    c2.itemconfig('d_sedam', fill='red')
    c2.itemconfig('d_dva', fill='black')
    c2.itemconfig('d_tri', fill='red')
    c2.itemconfig('d_cetiri', fill='black')
def c_25_26_27_28_29_30_hov1(e=None):
    c2.itemconfig('d_pet', fill='orange')
    c2.itemconfig('d_sest', fill='orange')
    c2.itemconfig('d_sedam', fill='orange')
    c2.itemconfig('d_osam', fill='orange')
    c2.itemconfig('d_devet', fill='orange')
    c2.itemconfig('t_nula', fill='orange')
def c_25_26_27_28_29_30_hov2(e=None):
    c2.itemconfig('d_pet', fill='red')
    c2.itemconfig('d_sest', fill='black')
    c2.itemconfig('d_sedam', fill='red')
    c2.itemconfig('d_osam', fill='black')
    c2.itemconfig('d_devet', fill='black')
    c2.itemconfig('t_nula', fill='red')
def c_28_29_30_31_32_33_hov1(e=None):
    c2.itemconfig('t_jedan', fill='orange')
    c2.itemconfig('t_dva', fill='orange')
    c2.itemconfig('t_tri', fill='orange')
    c2.itemconfig('d_osam', fill='orange')
    c2.itemconfig('d_devet', fill='orange')
    c2.itemconfig('t_nula', fill='orange')
def c_28_29_30_31_32_33_hov2(e=None):
    c2.itemconfig('t_jedan', fill='black')
    c2.itemconfig('t_dva', fill='red')
    c2.itemconfig('t_tri', fill='black')
    c2.itemconfig('d_osam', fill='black')
    c2.itemconfig('d_devet', fill='black')
    c2.itemconfig('t_nula', fill='red')
def c_31_32_33_34_35_36_hov1(e=None):
    c2.itemconfig('t_jedan', fill='orange')
    c2.itemconfig('t_dva', fill='orange')
    c2.itemconfig('t_tri', fill='orange')
    c2.itemconfig('t_cetiri', fill='orange')
    c2.itemconfig('t_pet', fill='orange')
    c2.itemconfig('t_sest', fill='orange')
def c_31_32_33_34_35_36_hov2(e=None):
    c2.itemconfig('t_jedan', fill='black')
    c2.itemconfig('t_dva', fill='red')
    c2.itemconfig('t_tri', fill='black')
    c2.itemconfig('t_cetiri', fill='red')
    c2.itemconfig('t_pet', fill='black')
    c2.itemconfig('t_sest', fill='red')


def c_0_1_2_hov1(e=None):
    c2.itemconfig('nula', fill='orange')
    c2.itemconfig('jedan', fill='orange')
    c2.itemconfig('dva', fill='orange')
def c_0_1_2_hov2(e=None):
    c2.itemconfig('nula', fill='green')
    c2.itemconfig('jedan', fill='red')
    c2.itemconfig('dva', fill='black')
def c_0_2_hov1(e=None):
    c2.itemconfig('nula', fill='orange')
    c2.itemconfig('dva', fill='orange')
def c_0_2_hov2(e=None):
    c2.itemconfig('nula', fill='green')
    c2.itemconfig('dva', fill='black')
def c_0_1_hov1(e=None):
    c2.itemconfig('nula', fill='orange')
    c2.itemconfig('jedan', fill='orange')
def c_0_1_hov2(e=None):
    c2.itemconfig('nula', fill='green')
    c2.itemconfig('jedan', fill='red')
def c_0_3_hov1(e=None):
    c2.itemconfig('nula', fill='orange')
    c2.itemconfig('tri', fill='orange')
def c_0_3_hov2(e=None):
    c2.itemconfig('nula', fill='green')
    c2.itemconfig('tri', fill='red')
def c_0_2_3_hov1(e=None):
    c2.itemconfig('nula', fill='orange')
    c2.itemconfig('tri', fill='orange')
    c2.itemconfig('dva', fill='orange')
def c_0_2_3_hov2(e=None):
    c2.itemconfig('nula', fill='green')
    c2.itemconfig('tri', fill='red')
    c2.itemconfig('dva', fill='black')
def c_1_4_hov1(e=None):
    c2.itemconfig('jedan', fill='orange')
    c2.itemconfig('cetiri', fill='orange')
def c_1_4_hov2(e=None):
    c2.itemconfig('jedan', fill='red')
    c2.itemconfig('cetiri', fill='black')
def c_2_5_hov1(e=None):
    c2.itemconfig('dva', fill='orange')
    c2.itemconfig('pet', fill='orange')
def c_2_5_hov2(e=None):
    c2.itemconfig('dva', fill='black')
    c2.itemconfig('pet', fill='red')
def c_3_6_hov1(e=None):
    c2.itemconfig('tri', fill='orange')
    c2.itemconfig('sest', fill='orange')
def c_3_6_hov2(e=None):
    c2.itemconfig('tri', fill='red')
    c2.itemconfig('sest', fill='black')
def c_4_7_hov1(e=None):
    c2.itemconfig('cetiri', fill='orange')
    c2.itemconfig('sedam', fill='orange')
def c_4_7_hov2(e=None):
    c2.itemconfig('cetiri', fill='black')
    c2.itemconfig('sedam', fill='red')
def c_5_8_hov1(e=None):
    c2.itemconfig('pet', fill='orange')
    c2.itemconfig('osam', fill='orange')
def c_5_8_hov2(e=None):
    c2.itemconfig('pet', fill='red')
    c2.itemconfig('osam', fill='black')
def c_6_9_hov1(e=None):
    c2.itemconfig('sest', fill='orange')
    c2.itemconfig('devet', fill='orange')
def c_6_9_hov2(e=None):
    c2.itemconfig('sest', fill='black')
    c2.itemconfig('devet', fill='red')
def c_7_10_hov1(e=None):
    c2.itemconfig('sedam', fill='orange')
    c2.itemconfig('deset', fill='orange')
def c_7_10_hov2(e=None):
    c2.itemconfig('sedam', fill='red')
    c2.itemconfig('deset', fill='black')
def c_8_11_hov1(e=None):
    c2.itemconfig('osam', fill='orange')
    c2.itemconfig('jedanaest', fill='orange')
def c_8_11_hov2(e=None):
    c2.itemconfig('osam', fill='black')
    c2.itemconfig('jedanaest', fill='black')
def c_9_12_hov1(e=None):
    c2.itemconfig('devet', fill='orange')
    c2.itemconfig('dvanaest', fill='orange')
def c_9_12_hov2(e=None):
    c2.itemconfig('devet', fill='red')
    c2.itemconfig('dvanaest', fill='red')
def c_10_13_hov1(e=None):
    c2.itemconfig('deset', fill='orange')
    c2.itemconfig('trinaest', fill='orange')
def c_10_13_hov2(e=None):
    c2.itemconfig('deset', fill='black')
    c2.itemconfig('trinaest', fill='black')
def c_11_14_hov1(e=None):
    c2.itemconfig('jedanaest', fill='orange')
    c2.itemconfig('cetrnaest', fill='orange')
def c_11_14_hov2(e=None):
    c2.itemconfig('jedanaest', fill='black')
    c2.itemconfig('cetrnaest', fill='red')
def c_12_15_hov1(e=None):
    c2.itemconfig('dvanaest', fill='orange')
    c2.itemconfig('petnaest', fill='orange')
def c_12_15_hov2(e=None):
    c2.itemconfig('dvanaest', fill='red')
    c2.itemconfig('petnaest', fill='black')
def c_13_16_hov1(e=None):
    c2.itemconfig('trinaest', fill='orange')
    c2.itemconfig('sesnaest', fill='orange')
def c_13_16_hov2(e=None):
    c2.itemconfig('trinaest', fill='black')
    c2.itemconfig('sesnaest', fill='red')
def c_14_17_hov1(e=None):
    c2.itemconfig('cetrnaest', fill='orange')
    c2.itemconfig('sedamnaest', fill='orange')
def c_14_17_hov2(e=None):
    c2.itemconfig('cetrnaest', fill='red')
    c2.itemconfig('sedamnaest', fill='black')
def c_15_18_hov1(e=None):
    c2.itemconfig('petnaest', fill='orange')
    c2.itemconfig('osamnaest', fill='orange')
def c_15_18_hov2(e=None):
    c2.itemconfig('petnaest', fill='black')
    c2.itemconfig('osamnaest', fill='red')
def c_16_19_hov1(e=None):
    c2.itemconfig('sesnaest', fill='orange')
    c2.itemconfig('devetnaest', fill='orange')
def c_16_19_hov2(e=None):
    c2.itemconfig('sesnaest', fill='red')
    c2.itemconfig('devetnaest', fill='red')
def c_17_20_hov1(e=None):
    c2.itemconfig('sedamnaest', fill='orange')
    c2.itemconfig('d_nula', fill='orange')
def c_17_20_hov2(e=None):
    c2.itemconfig('sedamnaest', fill='black')
    c2.itemconfig('d_nula', fill='black')
def c_18_21_hov1(e=None):
    c2.itemconfig('osamnaest', fill='orange')
    c2.itemconfig('d_jedan', fill='orange')
def c_18_21_hov2(e=None):
    c2.itemconfig('osamnaest', fill='red')
    c2.itemconfig('d_jedan', fill='red')
def c_19_22_hov1(e=None):
    c2.itemconfig('devetnaest', fill='orange')
    c2.itemconfig('d_dva', fill='orange')
def c_19_22_hov2(e=None):
    c2.itemconfig('devetnaest', fill='red')
    c2.itemconfig('d_dva', fill='black')
def c_20_23_hov1(e=None):
    c2.itemconfig('d_nula', fill='orange')
    c2.itemconfig('d_tri', fill='orange')
def c_20_23_hov2(e=None):
    c2.itemconfig('d_nula', fill='black')
    c2.itemconfig('d_tri', fill='red')
def c_21_24_hov1(e=None):
    c2.itemconfig('d_jedan', fill='orange')
    c2.itemconfig('d_cetiri', fill='orange')
def c_21_24_hov2(e=None):
    c2.itemconfig('d_jedan', fill='red')
    c2.itemconfig('d_cetiri', fill='black')
def c_22_25_hov1(e=None):
    c2.itemconfig('d_dva', fill='orange')
    c2.itemconfig('d_pet', fill='orange')
def c_22_25_hov2(e=None):
    c2.itemconfig('d_dva', fill='black')
    c2.itemconfig('d_pet', fill='red')
def c_23_26_hov1(e=None):
    c2.itemconfig('d_tri', fill='orange')
    c2.itemconfig('d_sest', fill='orange')
def c_23_26_hov2(e=None):
    c2.itemconfig('d_tri', fill='red')
    c2.itemconfig('d_sest', fill='black')
def c_24_27_hov1(e=None):
    c2.itemconfig('d_cetiri', fill='orange')
    c2.itemconfig('d_sedam', fill='orange')
def c_24_27_hov2(e=None):
    c2.itemconfig('d_cetiri', fill='black')
    c2.itemconfig('d_sedam', fill='red')
def c_25_28_hov1(e=None):
    c2.itemconfig('d_pet', fill='orange')
    c2.itemconfig('d_osam', fill='orange')
def c_25_28_hov2(e=None):
    c2.itemconfig('d_pet', fill='red')
    c2.itemconfig('d_osam', fill='black')
def c_26_29_hov1(e=None):
    c2.itemconfig('d_sest', fill='orange')
    c2.itemconfig('d_devet', fill='orange')
def c_26_29_hov2(e=None):
    c2.itemconfig('d_sest', fill='black')
    c2.itemconfig('d_devet', fill='black')
def c_27_30_hov1(e=None):
    c2.itemconfig('d_sedam', fill='orange')
    c2.itemconfig('t_nula', fill='orange')
def c_27_30_hov2(e=None):
    c2.itemconfig('d_sedam', fill='red')
    c2.itemconfig('t_nula', fill='red')
def c_28_31_hov1(e=None):
    c2.itemconfig('d_osam', fill='orange')
    c2.itemconfig('t_jedan', fill='orange')
def c_28_31_hov2(e=None):
    c2.itemconfig('d_osam', fill='black')
    c2.itemconfig('t_jedan', fill='black')
def c_29_32_hov1(e=None):
    c2.itemconfig('d_devet', fill='orange')
    c2.itemconfig('t_dva', fill='orange')
def c_29_32_hov2(e=None):
    c2.itemconfig('d_devet', fill='black')
    c2.itemconfig('t_dva', fill='red')
def c_30_33_hov1(e=None):
    c2.itemconfig('t_nula', fill='orange')
    c2.itemconfig('t_tri', fill='orange')
def c_30_33_hov2(e=None):
    c2.itemconfig('t_nula', fill='red')
    c2.itemconfig('t_tri', fill='black')
def c_31_34_hov1(e=None):
    c2.itemconfig('t_jedan', fill='orange')
    c2.itemconfig('t_cetiri', fill='orange')
def c_31_34_hov2(e=None):
    c2.itemconfig('t_jedan', fill='black')
    c2.itemconfig('t_cetiri', fill='red')
def c_32_35_hov1(e=None):
    c2.itemconfig('t_dva', fill='orange')
    c2.itemconfig('t_pet', fill='orange')
def c_32_35_hov2(e=None):
    c2.itemconfig('t_dva', fill='red')
    c2.itemconfig('t_pet', fill='black')
def c_33_36_hov1(e=None):
    c2.itemconfig('t_tri', fill='orange')
    c2.itemconfig('t_sest', fill='orange')
def c_33_36_hov2(e=None):
    c2.itemconfig('t_tri', fill='black')
    c2.itemconfig('t_sest', fill='red')

def c_1_2_hov1(e=None):
    c2.itemconfig('jedan', fill='orange')
    c2.itemconfig('dva', fill='orange')
def c_1_2_hov2(e=None):
    c2.itemconfig('jedan', fill='red')
    c2.itemconfig('dva', fill='black')
def c_2_3_hov1(e=None):
    c2.itemconfig('dva', fill='orange')
    c2.itemconfig('tri', fill='orange')
def c_2_3_hov2(e=None):
    c2.itemconfig('dva', fill='black')
    c2.itemconfig('tri', fill='red')
def c_4_5_hov1(e=None):
    c2.itemconfig('cetiri', fill='orange')
    c2.itemconfig('pet', fill='orange')
def c_4_5_hov2(e=None):
    c2.itemconfig('cetiri', fill='black')
    c2.itemconfig('pet', fill='red')
def c_5_6_hov1(e=None):
    c2.itemconfig('pet', fill='orange')
    c2.itemconfig('sest', fill='orange')
def c_5_6_hov2(e=None):
    c2.itemconfig('pet', fill='red')
    c2.itemconfig('sest', fill='black')
def c_7_8_hov1(e=None):
    c2.itemconfig('sedam', fill='orange')
    c2.itemconfig('osam', fill='orange')
def c_7_8_hov2(e=None):
    c2.itemconfig('sedam', fill='red')
    c2.itemconfig('osam', fill='black')
def c_8_9_hov1(e=None):
    c2.itemconfig('devet', fill='orange')
    c2.itemconfig('osam', fill='orange')
def c_8_9_hov2(e=None):
    c2.itemconfig('devet', fill='red')
    c2.itemconfig('osam', fill='black')
def c_10_11_hov1(e=None):
    c2.itemconfig('deset', fill='orange')
    c2.itemconfig('jedanaest', fill='orange')
def c_10_11_hov2(e=None):
    c2.itemconfig('deset', fill='black')
    c2.itemconfig('jedanaest', fill='black')
def c_11_12_hov1(e=None):
    c2.itemconfig('dvanaest', fill='orange')
    c2.itemconfig('jedanaest', fill='orange')
def c_11_12_hov2(e=None):
    c2.itemconfig('dvanaest', fill='red')
    c2.itemconfig('jedanaest', fill='black')
def c_13_14_hov1(e=None):
    c2.itemconfig('trinaest', fill='orange')
    c2.itemconfig('cetrnaest', fill='orange')
def c_13_14_hov2(e=None):
    c2.itemconfig('trinaest', fill='black')
    c2.itemconfig('cetrnaest', fill='red')
def c_14_15_hov1(e=None):
    c2.itemconfig('petnaest', fill='orange')
    c2.itemconfig('cetrnaest', fill='orange')
def c_14_15_hov2(e=None):
    c2.itemconfig('petnaest', fill='black')
    c2.itemconfig('cetrnaest', fill='red')
def c_16_17_hov1(e=None):
    c2.itemconfig('sesnaest', fill='orange')
    c2.itemconfig('sedamnaest', fill='orange')
def c_16_17_hov2(e=None):
    c2.itemconfig('sesnaest', fill='red')
    c2.itemconfig('sedamnaest', fill='black')
def c_17_18_hov1(e=None):
    c2.itemconfig('osamnaest', fill='orange')
    c2.itemconfig('sedamnaest', fill='orange')
def c_17_18_hov2(e=None):
    c2.itemconfig('osamnaest', fill='red')
    c2.itemconfig('sedamnaest', fill='black')
def c_19_20_hov1(e=None):
    c2.itemconfig('devetnaest', fill='orange')
    c2.itemconfig('d_nula', fill='orange')
def c_19_20_hov2(e=None):
    c2.itemconfig('devetnaest', fill='red')
    c2.itemconfig('d_nula', fill='black')
def c_20_21_hov1(e=None):
    c2.itemconfig('d_jedan', fill='orange')
    c2.itemconfig('d_nula', fill='orange')
def c_20_21_hov2(e=None):
    c2.itemconfig('d_jedan', fill='red')
    c2.itemconfig('d_nula', fill='black')
def c_22_23_hov1(e=None):
    c2.itemconfig('d_dva', fill='orange')
    c2.itemconfig('d_tri', fill='orange')
def c_22_23_hov2(e=None):
    c2.itemconfig('d_dva', fill='black')
    c2.itemconfig('d_tri', fill='red')
def c_23_24_hov1(e=None):
    c2.itemconfig('d_cetiri', fill='orange')
    c2.itemconfig('d_tri', fill='orange')
def c_23_24_hov2(e=None):
    c2.itemconfig('d_cetiri', fill='black')
    c2.itemconfig('d_tri', fill='red')
def c_25_26_hov1(e=None):
    c2.itemconfig('d_pet', fill='orange')
    c2.itemconfig('d_sest', fill='orange')
def c_25_26_hov2(e=None):
    c2.itemconfig('d_pet', fill='red')
    c2.itemconfig('d_sest', fill='black')
def c_26_27_hov1(e=None):
    c2.itemconfig('d_sedam', fill='orange')
    c2.itemconfig('d_sest', fill='orange')
def c_26_27_hov2(e=None):
    c2.itemconfig('d_sedam', fill='red')
    c2.itemconfig('d_sest', fill='black')
def c_28_29_hov1(e=None):
    c2.itemconfig('d_osam', fill='orange')
    c2.itemconfig('d_devet', fill='orange')
def c_28_29_hov2(e=None):
    c2.itemconfig('d_osam', fill='black')
    c2.itemconfig('d_devet', fill='black')
def c_29_30_hov1(e=None):
    c2.itemconfig('t_nula', fill='orange')
    c2.itemconfig('d_devet', fill='orange')
def c_29_30_hov2(e=None):
    c2.itemconfig('t_nula', fill='red')
    c2.itemconfig('d_devet', fill='black')
def c_31_32_hov1(e=None):
    c2.itemconfig('t_jedan', fill='orange')
    c2.itemconfig('t_dva', fill='orange')
def c_31_32_hov2(e=None):
    c2.itemconfig('t_jedan', fill='black')
    c2.itemconfig('t_dva', fill='red')
def c_32_33_hov1(e=None):
    c2.itemconfig('t_tri', fill='orange')
    c2.itemconfig('t_dva', fill='orange')
def c_32_33_hov2(e=None):
    c2.itemconfig('t_tri', fill='black')
    c2.itemconfig('t_dva', fill='red')
def c_34_35_hov1(e=None):
    c2.itemconfig('t_cetiri', fill='orange')
    c2.itemconfig('t_pet', fill='orange')
def c_34_35_hov2(e=None):
    c2.itemconfig('t_cetiri', fill='red')
    c2.itemconfig('t_pet', fill='black')
def c_35_36_hov1(e=None):
    c2.itemconfig('t_sest', fill='orange')
    c2.itemconfig('t_pet', fill='orange')
def c_35_36_hov2(e=None):
    c2.itemconfig('t_sest', fill='red')
    c2.itemconfig('t_pet', fill='black')


def c_prva_hov1(e=None):
    c2.itemconfig('dva', fill='orange')
    c2.itemconfig('tri', fill='orange')
    c2.itemconfig('pet', fill='orange')
    c2.itemconfig('sest', fill='orange')
def c_prva_hov2(e=None):
    c2.itemconfig('dva', fill='black')
    c2.itemconfig('tri', fill='red')
    c2.itemconfig('pet', fill='red')
    c2.itemconfig('sest', fill='black')
def c_druga_hov1(e=None):
    c2.itemconfig('jedan', fill='orange')
    c2.itemconfig('dva', fill='orange')
    c2.itemconfig('cetiri', fill='orange')
    c2.itemconfig('pet', fill='orange')
def c_druga_hov2(e=None):
    c2.itemconfig('jedan', fill='red')
    c2.itemconfig('dva', fill='black')
    c2.itemconfig('cetiri', fill='black')
    c2.itemconfig('pet', fill='red')
def c_treca_hov1(e=None):
    c2.itemconfig('pet', fill='orange')
    c2.itemconfig('sest', fill='orange')
    c2.itemconfig('osam', fill='orange')
    c2.itemconfig('devet', fill='orange')
def c_treca_hov2(e=None):
    c2.itemconfig('pet', fill='red')
    c2.itemconfig('sest', fill='black')
    c2.itemconfig('osam', fill='black')
    c2.itemconfig('devet', fill='red')
def c_cetvrta_hov1(e=None):
    c2.itemconfig('cetiri', fill='orange')
    c2.itemconfig('pet', fill='orange')
    c2.itemconfig('sedam', fill='orange')
    c2.itemconfig('osam', fill='orange')
def c_cetvrta_hov2(e=None):
    c2.itemconfig('cetiri', fill='black')
    c2.itemconfig('pet', fill='red')
    c2.itemconfig('sedam', fill='red')
    c2.itemconfig('osam', fill='black')
def c_peta_hov1(e=None):
    c2.itemconfig('osam', fill='orange')
    c2.itemconfig('devet', fill='orange')
    c2.itemconfig('jedanaest', fill='orange')
    c2.itemconfig('dvanaest', fill='orange')
def c_peta_hov2(e=None):
    c2.itemconfig('osam', fill='black')
    c2.itemconfig('devet', fill='red')
    c2.itemconfig('jedanaest', fill='black')
    c2.itemconfig('dvanaest', fill='red')
def c_sesta_hov1(e=None):
    c2.itemconfig('sedam', fill='orange')
    c2.itemconfig('osam', fill='orange')
    c2.itemconfig('deset', fill='orange')
    c2.itemconfig('jedanaest', fill='orange')
def c_sesta_hov2(e=None):
    c2.itemconfig('sedam', fill='red')
    c2.itemconfig('osam', fill='black')
    c2.itemconfig('deset', fill='black')
    c2.itemconfig('jedanaest', fill='black')
def c_sedma_hov1(e=None):
    c2.itemconfig('jedanaest', fill='orange')
    c2.itemconfig('dvanaest', fill='orange')
    c2.itemconfig('cetrnaest', fill='orange')
    c2.itemconfig('petnaest', fill='orange')
def c_sedma_hov2(e=None):
    c2.itemconfig('jedanaest', fill='black')
    c2.itemconfig('dvanaest', fill='red')
    c2.itemconfig('cetrnaest', fill='red')
    c2.itemconfig('petnaest', fill='black')
def c_osma_hov1(e=None):
    c2.itemconfig('deset', fill='orange')
    c2.itemconfig('jedanaest', fill='orange')
    c2.itemconfig('trinaest', fill='orange')
    c2.itemconfig('cetrnaest', fill='orange')
def c_osma_hov2(e=None):
    c2.itemconfig('deset', fill='black')
    c2.itemconfig('jedanaest', fill='black')
    c2.itemconfig('trinaest', fill='black')
    c2.itemconfig('cetrnaest', fill='red')
def c_deveta_hov1(e=None):
    c2.itemconfig('cetrnaest', fill='orange')
    c2.itemconfig('petnaest', fill='orange')
    c2.itemconfig('sedamnaest', fill='orange')
    c2.itemconfig('osamnaest', fill='orange')
def c_deveta_hov2(e=None):
    c2.itemconfig('cetrnaest', fill='red')
    c2.itemconfig('petnaest', fill='black')
    c2.itemconfig('sedamnaest', fill='black')
    c2.itemconfig('osamnaest', fill='red')
def c_deseta_hov1(e=None):
    c2.itemconfig('trinaest', fill='orange')
    c2.itemconfig('cetrnaest', fill='orange')
    c2.itemconfig('sesnaest', fill='orange')
    c2.itemconfig('sedamnaest', fill='orange')
def c_deseta_hov2(e=None):
    c2.itemconfig('trinaest', fill='black')
    c2.itemconfig('cetrnaest', fill='red')
    c2.itemconfig('sesnaest', fill='red')
    c2.itemconfig('sedamnaest', fill='black')
def c_jedanaesta_hov1(e=None):
    c2.itemconfig('sedamnaest', fill='orange')
    c2.itemconfig('osamnaest', fill='orange')
    c2.itemconfig('d_nula', fill='orange')
    c2.itemconfig('d_jedan', fill='orange')
def c_jedanaesta_hov2(e=None):
    c2.itemconfig('sedamnaest', fill='black')
    c2.itemconfig('osamnaest', fill='red')
    c2.itemconfig('d_nula', fill='black')
    c2.itemconfig('d_jedan', fill='red')
def c_dvanaesta_hov1(e=None):
    c2.itemconfig('sesnaest', fill='orange')
    c2.itemconfig('sedamnaest', fill='orange')
    c2.itemconfig('devetnaest', fill='orange')
    c2.itemconfig('d_nula', fill='orange')
def c_dvanaesta_hov2(e=None):
    c2.itemconfig('sesnaest', fill='red')
    c2.itemconfig('sedamnaest', fill='black')
    c2.itemconfig('devetnaest', fill='red')
    c2.itemconfig('d_nula', fill='black')
def c_trinaesta_hov1(e=None):
    c2.itemconfig('d_nula', fill='orange')
    c2.itemconfig('d_jedan', fill='orange')
    c2.itemconfig('d_tri', fill='orange')
    c2.itemconfig('d_cetiri', fill='orange')
def c_trinaesta_hov2(e=None):
    c2.itemconfig('d_nula', fill='black')
    c2.itemconfig('d_jedan', fill='red')
    c2.itemconfig('d_tri', fill='red')
    c2.itemconfig('d_cetiri', fill='black')
def c_cetrnaesta_hov1(e=None):
    c2.itemconfig('devetnaest', fill='orange')
    c2.itemconfig('d_nula', fill='orange')
    c2.itemconfig('d_dva', fill='orange')
    c2.itemconfig('d_tri', fill='orange')
def c_cetrnaesta_hov2(e=None):
    c2.itemconfig('devetnaest', fill='red')
    c2.itemconfig('d_nula', fill='black')
    c2.itemconfig('d_dva', fill='black')
    c2.itemconfig('d_tri', fill='red')
def c_petnaesta_hov1(e=None):
    c2.itemconfig('d_tri', fill='orange')
    c2.itemconfig('d_cetiri', fill='orange')
    c2.itemconfig('d_sest', fill='orange')
    c2.itemconfig('d_sedam', fill='orange')
def c_petnaesta_hov2(e=None):
    c2.itemconfig('d_tri', fill='red')
    c2.itemconfig('d_cetiri', fill='black')
    c2.itemconfig('d_sest', fill='black')
    c2.itemconfig('d_sedam', fill='red')
def c_sesnaesta_hov1(e=None):
    c2.itemconfig('d_dva', fill='orange')
    c2.itemconfig('d_tri', fill='orange')
    c2.itemconfig('d_pet', fill='orange')
    c2.itemconfig('d_sest', fill='orange')
def c_sesnaesta_hov2(e=None):
    c2.itemconfig('d_dva', fill='black')
    c2.itemconfig('d_tri', fill='red')
    c2.itemconfig('d_pet', fill='red')
    c2.itemconfig('d_sest', fill='black')
def c_sedamnaesta_hov1(e=None):
    c2.itemconfig('d_sest', fill='orange')
    c2.itemconfig('d_sedam', fill='orange')
    c2.itemconfig('d_devet', fill='orange')
    c2.itemconfig('t_nula', fill='orange')
def c_sedamnaesta_hov2(e=None):
    c2.itemconfig('d_sest', fill='black')
    c2.itemconfig('d_sedam', fill='red')
    c2.itemconfig('d_devet', fill='black')
    c2.itemconfig('t_nula', fill='red')
def c_osamnaesta_hov1(e=None):
    c2.itemconfig('d_pet', fill='orange')
    c2.itemconfig('d_sest', fill='orange')
    c2.itemconfig('d_osam', fill='orange')
    c2.itemconfig('d_devet', fill='orange')
def c_osamnaesta_hov2(e=None):
    c2.itemconfig('d_pet', fill='red')
    c2.itemconfig('d_sest', fill='black')
    c2.itemconfig('d_osam', fill='black')
    c2.itemconfig('d_devet', fill='black')
def c_devetnaesta_hov1(e=None):
    c2.itemconfig('d_devet', fill='orange')
    c2.itemconfig('t_nula', fill='orange')
    c2.itemconfig('t_dva', fill='orange')
    c2.itemconfig('t_tri', fill='orange')
def c_devetnaesta_hov2(e=None):
    c2.itemconfig('d_devet', fill='black')
    c2.itemconfig('t_nula', fill='red')
    c2.itemconfig('t_dva', fill='red')
    c2.itemconfig('t_tri', fill='black')
def c_dvadeseta_hov1(e=None):
    c2.itemconfig('d_osam', fill='orange')
    c2.itemconfig('d_devet', fill='orange')
    c2.itemconfig('t_jedan', fill='orange')
    c2.itemconfig('t_dva', fill='orange')
def c_dvadeseta_hov2(e=None):
    c2.itemconfig('d_osam', fill='black')
    c2.itemconfig('d_devet', fill='black')
    c2.itemconfig('t_jedan', fill='black')
    c2.itemconfig('t_dva', fill='red')
def c_dvadesetprva_hov1(e=None):
    c2.itemconfig('t_dva', fill='orange')
    c2.itemconfig('t_tri', fill='orange')
    c2.itemconfig('t_pet', fill='orange')
    c2.itemconfig('t_sest', fill='orange')
def c_dvadesetprva_hov2(e=None):
    c2.itemconfig('t_dva', fill='red')
    c2.itemconfig('t_tri', fill='black')
    c2.itemconfig('t_pet', fill='black')
    c2.itemconfig('t_sest', fill='red')
def c_dvadesetdruga_hov1(e=None):
    c2.itemconfig('t_jedan', fill='orange')
    c2.itemconfig('t_dva', fill='orange')
    c2.itemconfig('t_cetiri', fill='orange')
    c2.itemconfig('t_pet', fill='orange')
def c_dvadesetdruga_hov2(e=None):
    c2.itemconfig('t_jedan', fill='black')
    c2.itemconfig('t_dva', fill='red')
    c2.itemconfig('t_cetiri', fill='red')
    c2.itemconfig('t_pet', fill='black')



def nnula1(e=None):
    c2.itemconfig('nula', fill='orange')
def jjedan1(e=None):
    c2.itemconfig('jedan', fill='orange')
def ddva1(e=None):
    c2.itemconfig('dva', fill='orange')
def ttri1(e=None):
    c2.itemconfig('tri', fill='orange')
def ccetiri1(e=None):
    c2.itemconfig('cetiri', fill='orange')
def ppet1(e=None):
    c2.itemconfig('pet', fill='orange')
def ssest1(e=None):
    c2.itemconfig('sest', fill='orange')
def ssedam1(e=None):
    c2.itemconfig('sedam', fill='orange')
def oosam1(e=None):
    c2.itemconfig('osam', fill='orange')
def ddevet1(e=None):
    c2.itemconfig('devet', fill='orange')
def ddeset1(e=None):
    c2.itemconfig('deset', fill='orange')
def jjedanaest1(e=None):
    c2.itemconfig('jedanaest', fill='orange')
def ddvanaest1(e=None):
    c2.itemconfig('dvanaest', fill='orange')
def ttrinaest1(e=None):
    c2.itemconfig('trinaest', fill='orange')
def ccetrnaest1(e=None):
    c2.itemconfig('cetrnaest', fill='orange')
def ppetnaest1(e=None):
    c2.itemconfig('petnaest', fill='orange')
def ssesnaest1(e=None):
    c2.itemconfig('sesnaest', fill='orange')
def ssedamnaest1(e=None):
    c2.itemconfig('sedamnaest', fill='orange')
def oosamnaest1(e=None):
    c2.itemconfig('osamnaest', fill='orange')
def ddevetnaest1(e=None):
    c2.itemconfig('devetnaest', fill='orange')
def dd_nula1(e=None):
    c2.itemconfig('d_nula', fill='orange')
def dd_jedan1(e=None):
    c2.itemconfig('d_jedan', fill='orange')
def dd_dva1(e=None):
    c2.itemconfig('d_dva', fill='orange')
def dd_tri1(e=None):
    c2.itemconfig('d_tri', fill='orange')
def dd_cetiri1(e=None):
    c2.itemconfig('d_cetiri', fill='orange')
def dd_pet1(e=None):
    c2.itemconfig('d_pet', fill='orange')
def dd_sest1(e=None):
    c2.itemconfig('d_sest', fill='orange')
def dd_sedam1(e=None):
    c2.itemconfig('d_sedam', fill='orange')
def dd_osam1(e=None):
    c2.itemconfig('d_osam', fill='orange')
def dd_devet1(e=None):
    c2.itemconfig('d_devet', fill='orange')
def tt_nula1(e=None):
    c2.itemconfig('t_nula', fill='orange')
def tt_jedan1(e=None):
    c2.itemconfig('t_jedan', fill='orange')
def tt_dva1(e=None):
    c2.itemconfig('t_dva', fill='orange')
def tt_tri1(e=None):
    c2.itemconfig('t_tri', fill='orange')
def tt_cetiri1(e=None):
    c2.itemconfig('t_cetiri', fill='orange')
def tt_pet1(e=None):
    c2.itemconfig('t_pet', fill='orange')
def tt_sest1(e=None):
    c2.itemconfig('t_sest', fill='orange')

def nnula2(e=None):
    c2.itemconfig('nula', fill='green')
def jjedan2(e=None):
    c2.itemconfig('jedan', fill='red')
def ddva2(e=None):
    c2.itemconfig('dva', fill='black')
def ttri2(e=None):
    c2.itemconfig('tri', fill='red')
def ccetiri2(e=None):
    c2.itemconfig('cetiri', fill='black')
def ppet2(e=None):
    c2.itemconfig('pet', fill='red')
def ssest2(e=None):
    c2.itemconfig('sest', fill='black')
def ssedam2(e=None):
    c2.itemconfig('sedam', fill='red')
def oosam2(e=None):
    c2.itemconfig('osam', fill='black')
def ddevet2(e=None):
    c2.itemconfig('devet', fill='red')
def ddeset2(e=None):
    c2.itemconfig('deset', fill='black')
def jjedanaest2(e=None):
    c2.itemconfig('jedanaest', fill='black')
def ddvanaest2(e=None):
    c2.itemconfig('dvanaest', fill='red')
def ttrinaest2(e=None):
    c2.itemconfig('trinaest', fill='black')
def ccetrnaest2(e=None):
    c2.itemconfig('cetrnaest', fill='red')
def ppetnaest2(e=None):
    c2.itemconfig('petnaest', fill='black')
def ssesnaest2(e=None):
    c2.itemconfig('sesnaest', fill='red')
def ssedamnaest2(e=None):
    c2.itemconfig('sedamnaest', fill='black')
def oosamnaest2(e=None):
    c2.itemconfig('osamnaest', fill='red')
def ddevetnaest2(e=None):
    c2.itemconfig('devetnaest', fill='red')
def dd_nula2(e=None):
    c2.itemconfig('d_nula', fill='black')
def dd_jedan2(e=None):
    c2.itemconfig('d_jedan', fill='red')
def dd_dva2(e=None):
    c2.itemconfig('d_dva', fill='black')
def dd_tri2(e=None):
    c2.itemconfig('d_tri', fill='red')
def dd_cetiri2(e=None):
    c2.itemconfig('d_cetiri', fill='black')
def dd_pet2(e=None):
    c2.itemconfig('d_pet', fill='red')
def dd_sest2(e=None):
    c2.itemconfig('d_sest', fill='black')
def dd_sedam2(e=None):
    c2.itemconfig('d_sedam', fill='red')
def dd_osam2(e=None):
    c2.itemconfig('d_osam', fill='black')
def dd_devet2(e=None):
    c2.itemconfig('d_devet', fill='black')
def tt_nula2(e=None):
    c2.itemconfig('t_nula', fill='red')
def tt_jedan2(e=None):
    c2.itemconfig('t_jedan', fill='black')
def tt_dva2(e=None):
    c2.itemconfig('t_dva', fill='red')
def tt_tri2(e=None):
    c2.itemconfig('t_tri', fill='black')
def tt_cetiri2(e=None):
    c2.itemconfig('t_cetiri', fill='red')
def tt_pet2(e=None):
    c2.itemconfig('t_pet', fill='black')
def tt_sest2(e=None):
    c2.itemconfig('t_sest', fill='red')
def ttreca_tri1(e=None):
    c2.itemconfig('treca_tri', fill='orange')
    c2.itemconfig('tri', fill='orange')
    c2.itemconfig('sest', fill='orange')
    c2.itemconfig('devet', fill='orange')
    c2.itemconfig('dvanaest', fill='orange')
    c2.itemconfig('petnaest', fill='orange')
    c2.itemconfig('osamnaest', fill='orange')
    c2.itemconfig('d_jedan', fill='orange')
    c2.itemconfig('d_cetiri', fill='orange')
    c2.itemconfig('d_sedam', fill='orange')
    c2.itemconfig('t_nula', fill='orange')
    c2.itemconfig('t_tri', fill='orange')
    c2.itemconfig('t_sest', fill='orange')
def ttreca_tri2(e=None):
    c2.itemconfig('treca_tri', fill='green')
    c2.itemconfig('tri', fill='red')
    c2.itemconfig('sest', fill='black')
    c2.itemconfig('devet', fill='red')
    c2.itemconfig('dvanaest', fill='red')
    c2.itemconfig('petnaest', fill='black')
    c2.itemconfig('osamnaest', fill='red')
    c2.itemconfig('d_jedan', fill='red')
    c2.itemconfig('d_cetiri', fill='black')
    c2.itemconfig('d_sedam', fill='red')
    c2.itemconfig('t_nula', fill='red')
    c2.itemconfig('t_tri', fill='black')
    c2.itemconfig('t_sest', fill='red')
def ddruga_tri1(e=None):
    c2.itemconfig('druga_tri', fill='orange')
    c2.itemconfig('dva', fill='orange')
    c2.itemconfig('pet', fill='orange')
    c2.itemconfig('osam', fill='orange')
    c2.itemconfig('jedanaest', fill='orange')
    c2.itemconfig('cetrnaest', fill='orange')
    c2.itemconfig('sedamnaest', fill='orange')
    c2.itemconfig('d_nula', fill='orange')
    c2.itemconfig('d_tri', fill='orange')
    c2.itemconfig('d_sest', fill='orange')
    c2.itemconfig('d_devet', fill='orange')
    c2.itemconfig('t_dva', fill='orange')
    c2.itemconfig('t_pet', fill='orange')
def ddruga_tri2(e=None):
    c2.itemconfig('druga_tri', fill='green')
    c2.itemconfig('dva', fill='black')
    c2.itemconfig('pet', fill='red')
    c2.itemconfig('osam', fill='black')
    c2.itemconfig('jedanaest', fill='black')
    c2.itemconfig('cetrnaest', fill='red')
    c2.itemconfig('sedamnaest', fill='black')
    c2.itemconfig('d_nula', fill='black')
    c2.itemconfig('d_tri', fill='red')
    c2.itemconfig('d_sest', fill='black')
    c2.itemconfig('d_devet', fill='black')
    c2.itemconfig('t_dva', fill='red')
    c2.itemconfig('t_pet', fill='black')
def pprva_tri1(e=None):
    c2.itemconfig('prva_tri', fill='orange')
    c2.itemconfig('jedan', fill='orange')
    c2.itemconfig('cetiri', fill='orange')
    c2.itemconfig('sedam', fill='orange')
    c2.itemconfig('deset', fill='orange')
    c2.itemconfig('trinaest', fill='orange')
    c2.itemconfig('sesnaest', fill='orange')
    c2.itemconfig('devetnaest', fill='orange')
    c2.itemconfig('d_dva', fill='orange')
    c2.itemconfig('d_pet', fill='orange')
    c2.itemconfig('d_osam', fill='orange')
    c2.itemconfig('t_jedan', fill='orange')
    c2.itemconfig('t_cetiri', fill='orange')
def pprva_tri2(e=None):
    c2.itemconfig('prva_tri', fill='green')
    c2.itemconfig('jedan', fill='red')
    c2.itemconfig('cetiri', fill='black')
    c2.itemconfig('sedam', fill='red')
    c2.itemconfig('deset', fill='black')
    c2.itemconfig('trinaest', fill='black')
    c2.itemconfig('sesnaest', fill='red')
    c2.itemconfig('devetnaest', fill='red')
    c2.itemconfig('d_dva', fill='black')
    c2.itemconfig('d_pet', fill='red')
    c2.itemconfig('d_osam', fill='black')
    c2.itemconfig('t_jedan', fill='black')
    c2.itemconfig('t_cetiri', fill='red')

def prva_tri_hov1(e=None):
    c2.itemconfig('jedan', fill='orange')
    c2.itemconfig('cetiri', fill='orange')
    c2.itemconfig('sedam', fill='orange')
    c2.itemconfig('deset', fill='orange')
    c2.itemconfig('trinaest', fill='orange')
    c2.itemconfig('sesnaest', fill='orange')
    c2.itemconfig('devetnaest', fill='orange')
    c2.itemconfig('d_dva', fill='orange')
    c2.itemconfig('d_pet', fill='orange')
    c2.itemconfig('d_osam', fill='orange')
    c2.itemconfig('t_jedan', fill='orange')
    c2.itemconfig('t_cetiri', fill='orange')

def prva_tri_hov2(e=None):
    c2.itemconfig('prva_tri', fill='green')
    c2.itemconfig('jedan', fill='red')
    c2.itemconfig('cetiri', fill='black')
    c2.itemconfig('sedam', fill='red')
    c2.itemconfig('deset', fill='black')
    c2.itemconfig('trinaest', fill='black')
    c2.itemconfig('sesnaest', fill='red')
    c2.itemconfig('devetnaest', fill='red')
    c2.itemconfig('d_dva', fill='black')
    c2.itemconfig('d_pet', fill='red')
    c2.itemconfig('d_osam', fill='black')
    c2.itemconfig('t_jedan', fill='black')
    c2.itemconfig('t_cetiri', fill='red')

def druga_tri_hov1(e=None):
    c2.itemconfig('dva', fill='orange')
    c2.itemconfig('pet', fill='orange')
    c2.itemconfig('osam', fill='orange')
    c2.itemconfig('jedanaest', fill='orange')
    c2.itemconfig('cetrnaest', fill='orange')
    c2.itemconfig('sedamnaest', fill='orange')
    c2.itemconfig('d_nula', fill='orange')
    c2.itemconfig('d_tri', fill='orange')
    c2.itemconfig('d_sest', fill='orange')
    c2.itemconfig('d_devet', fill='orange')
    c2.itemconfig('t_dva', fill='orange')
    c2.itemconfig('t_pet', fill='orange')

def druga_tri_hov2(e=None):
    c2.itemconfig('dva', fill='black')
    c2.itemconfig('pet', fill='red')
    c2.itemconfig('osam', fill='black')
    c2.itemconfig('jedanaest', fill='black')
    c2.itemconfig('cetrnaest', fill='red')
    c2.itemconfig('sedamnaest', fill='black')
    c2.itemconfig('d_nula', fill='black')
    c2.itemconfig('d_tri', fill='red')
    c2.itemconfig('d_sest', fill='black')
    c2.itemconfig('d_devet', fill='black')
    c2.itemconfig('t_dva', fill='red')
    c2.itemconfig('t_pet', fill='black')

def treca_tri_hov1(e=None):
    c2.itemconfig('tri', fill='orange')
    c2.itemconfig('sest', fill='orange')
    c2.itemconfig('devet', fill='orange')
    c2.itemconfig('dvanaest', fill='orange')
    c2.itemconfig('petnaest', fill='orange')
    c2.itemconfig('osamnaest', fill='orange')
    c2.itemconfig('d_jedan', fill='orange')
    c2.itemconfig('d_cetiri', fill='orange')
    c2.itemconfig('d_sedam', fill='orange')
    c2.itemconfig('t_nula', fill='orange')
    c2.itemconfig('t_tri', fill='orange')
    c2.itemconfig('t_sest', fill='orange')

def treca_tri_hov2(e=None):
    c2.itemconfig('tri', fill='red')
    c2.itemconfig('sest', fill='black')
    c2.itemconfig('devet', fill='red')
    c2.itemconfig('dvanaest', fill='red')
    c2.itemconfig('petnaest', fill='black')
    c2.itemconfig('osamnaest', fill='red')
    c2.itemconfig('d_jedan', fill='red')
    c2.itemconfig('d_cetiri', fill='black')
    c2.itemconfig('d_sedam', fill='red')
    c2.itemconfig('t_nula', fill='red')
    c2.itemconfig('t_tri', fill='black')
    c2.itemconfig('t_sest', fill='red')


def treca_trec1(e=None):
    c2.itemconfig('treca_trecina', fill='orange')
    c2.itemconfig('d_pet', fill='orange')
    c2.itemconfig('d_sest', fill='orange')
    c2.itemconfig('d_sedam', fill='orange')
    c2.itemconfig('d_osam', fill='orange')
    c2.itemconfig('d_devet', fill='orange')
    c2.itemconfig('t_nula', fill='orange')
    c2.itemconfig('t_jedan', fill='orange')
    c2.itemconfig('t_dva', fill='orange')
    c2.itemconfig('t_tri', fill='orange')
    c2.itemconfig('t_cetiri', fill='orange')
    c2.itemconfig('t_pet', fill='orange')
    c2.itemconfig('t_sest', fill='orange')
def treca_trec2(e=None):
    c2.itemconfig('treca_trecina', fill='green')
    c2.itemconfig('d_pet', fill='red')
    c2.itemconfig('d_sest', fill='black')
    c2.itemconfig('d_sedam', fill='red')
    c2.itemconfig('d_osam', fill='black')
    c2.itemconfig('d_devet', fill='black')
    c2.itemconfig('t_nula', fill='red')
    c2.itemconfig('t_jedan', fill='black')
    c2.itemconfig('t_dva', fill='red')
    c2.itemconfig('t_tri', fill='black')
    c2.itemconfig('t_cetiri', fill='red')
    c2.itemconfig('t_pet', fill='black')
    c2.itemconfig('t_sest', fill='red')
def druga_trec1(e=None):
    c2.itemconfig('druga_trecina', fill='orange')
    c2.itemconfig('trinaest', fill='orange')
    c2.itemconfig('cetrnaest', fill='orange')
    c2.itemconfig('petnaest', fill='orange')
    c2.itemconfig('sesnaest', fill='orange')
    c2.itemconfig('sedamnaest', fill='orange')
    c2.itemconfig('osamnaest', fill='orange')
    c2.itemconfig('devetnaest', fill='orange')
    c2.itemconfig('d_nula', fill='orange')
    c2.itemconfig('d_jedan', fill='orange')
    c2.itemconfig('d_dva', fill='orange')
    c2.itemconfig('d_tri', fill='orange')
    c2.itemconfig('d_cetiri', fill='orange')
def druga_trec2(e=None):
    c2.itemconfig('druga_trecina', fill='green')
    c2.itemconfig('trinaest', fill='black')
    c2.itemconfig('cetrnaest', fill='red')
    c2.itemconfig('petnaest', fill='black')
    c2.itemconfig('sesnaest', fill='red')
    c2.itemconfig('sedamnaest', fill='black')
    c2.itemconfig('osamnaest', fill='red')
    c2.itemconfig('devetnaest', fill='red')
    c2.itemconfig('d_nula', fill='black')
    c2.itemconfig('d_jedan', fill='red')
    c2.itemconfig('d_dva', fill='black')
    c2.itemconfig('d_tri', fill='red')
    c2.itemconfig('d_cetiri', fill='black')
def prva_trec1(e=None):
    c2.itemconfig('prva_trecina', fill='orange')
    c2.itemconfig('jedan', fill='orange')
    c2.itemconfig('dva', fill='orange')
    c2.itemconfig('tri', fill='orange')
    c2.itemconfig('cetiri', fill='orange')
    c2.itemconfig('pet', fill='orange')
    c2.itemconfig('sest', fill='orange')
    c2.itemconfig('sedam', fill='orange')
    c2.itemconfig('osam', fill='orange')
    c2.itemconfig('devet', fill='orange')
    c2.itemconfig('deset', fill='orange')
    c2.itemconfig('jedanaest', fill='orange')
    c2.itemconfig('dvanaest', fill='orange')
def prva_trec2(e=None):
    c2.itemconfig('prva_trecina', fill='green')
    c2.itemconfig('jedan', fill='red')
    c2.itemconfig('dva', fill='black')
    c2.itemconfig('tri', fill='red')
    c2.itemconfig('cetiri', fill='black')
    c2.itemconfig('pet', fill='red')
    c2.itemconfig('sest', fill='black')
    c2.itemconfig('sedam', fill='red')
    c2.itemconfig('osam', fill='black')
    c2.itemconfig('devet', fill='red')
    c2.itemconfig('deset', fill='black')
    c2.itemconfig('jedanaest', fill='black')
    c2.itemconfig('dvanaest', fill='red')


def prva_trecina_hov1(e=None):
    c2.itemconfig('jedan', fill='orange')
    c2.itemconfig('dva', fill='orange')
    c2.itemconfig('tri', fill='orange')
    c2.itemconfig('cetiri', fill='orange')
    c2.itemconfig('pet', fill='orange')
    c2.itemconfig('sest', fill='orange')
    c2.itemconfig('sedam', fill='orange')
    c2.itemconfig('osam', fill='orange')
    c2.itemconfig('devet', fill='orange')
    c2.itemconfig('deset', fill='orange')
    c2.itemconfig('jedanaest', fill='orange')
    c2.itemconfig('dvanaest', fill='orange')
def prva_trecina_hov2(e=None):
    c2.itemconfig('prva_trecina', fill='green')
    c2.itemconfig('jedan', fill='red')
    c2.itemconfig('dva', fill='black')
    c2.itemconfig('tri', fill='red')
    c2.itemconfig('cetiri', fill='black')
    c2.itemconfig('pet', fill='red')
    c2.itemconfig('sest', fill='black')
    c2.itemconfig('sedam', fill='red')
    c2.itemconfig('osam', fill='black')
    c2.itemconfig('devet', fill='red')
    c2.itemconfig('deset', fill='black')
    c2.itemconfig('jedanaest', fill='black')
    c2.itemconfig('dvanaest', fill='red')
def druga_trecina_hov1(e=None):
    c2.itemconfig('trinaest', fill='orange')
    c2.itemconfig('cetrnaest', fill='orange')
    c2.itemconfig('petnaest', fill='orange')
    c2.itemconfig('sesnaest', fill='orange')
    c2.itemconfig('sedamnaest', fill='orange')
    c2.itemconfig('osamnaest', fill='orange')
    c2.itemconfig('devetnaest', fill='orange')
    c2.itemconfig('d_nula', fill='orange')
    c2.itemconfig('d_jedan', fill='orange')
    c2.itemconfig('d_dva', fill='orange')
    c2.itemconfig('d_tri', fill='orange')
    c2.itemconfig('d_cetiri', fill='orange')
def druga_trecina_hov2(e=None):
    c2.itemconfig('trinaest', fill='black')
    c2.itemconfig('cetrnaest', fill='red')
    c2.itemconfig('petnaest', fill='black')
    c2.itemconfig('sesnaest', fill='red')
    c2.itemconfig('sedamnaest', fill='black')
    c2.itemconfig('osamnaest', fill='red')
    c2.itemconfig('devetnaest', fill='red')
    c2.itemconfig('d_nula', fill='black')
    c2.itemconfig('d_jedan', fill='red')
    c2.itemconfig('d_dva', fill='black')
    c2.itemconfig('d_tri', fill='red')
    c2.itemconfig('d_cetiri', fill='black')

def treca_trecina_hov1(e=None):
    c2.itemconfig('d_pet', fill='orange')
    c2.itemconfig('d_sest', fill='orange')
    c2.itemconfig('d_sedam', fill='orange')
    c2.itemconfig('d_osam', fill='orange')
    c2.itemconfig('d_devet', fill='orange')
    c2.itemconfig('t_nula', fill='orange')
    c2.itemconfig('t_jedan', fill='orange')
    c2.itemconfig('t_dva', fill='orange')
    c2.itemconfig('t_tri', fill='orange')
    c2.itemconfig('t_cetiri', fill='orange')
    c2.itemconfig('t_pet', fill='orange')
    c2.itemconfig('t_sest', fill='orange')

def treca_trecina_hov2(e=None):
    c2.itemconfig('d_pet', fill='red')
    c2.itemconfig('d_sest', fill='black')
    c2.itemconfig('d_sedam', fill='red')
    c2.itemconfig('d_osam', fill='black')
    c2.itemconfig('d_devet', fill='black')
    c2.itemconfig('t_nula', fill='red')
    c2.itemconfig('t_jedan', fill='black')
    c2.itemconfig('t_dva', fill='red')
    c2.itemconfig('t_tri', fill='black')
    c2.itemconfig('t_cetiri', fill='red')
    c2.itemconfig('t_pet', fill='black')
    c2.itemconfig('t_sest', fill='red')     
    
def prvih_18_t1(e=None):
    c2.itemconfig('prvih_18', fill='orange')
def prvih_18_t2(e=None):
    c2.itemconfig('prvih_18', fill='green')
def drugih_18_t1(e=None):
    c2.itemconfig('drugih_18', fill='orange')
def drugih_18_t2(e=None):
    c2.itemconfig('drugih_18', fill='green')
def even_t1(e=None):
    c2.itemconfig('even', fill='orange')
def even_t2(e=None):
    c2.itemconfig('even', fill='green')
def odd_t1(e=None):
    c2.itemconfig('odd', fill='orange')
def odd_t2(e=None):
    c2.itemconfig('odd', fill='green')
    
def ch1_1(e=None):
    global paree
    ispis_para.config(state=NORMAL)
    xd = int(ispis_para.get('1.0',END))
    ispis_para.config(state=DISABLED)
    if xd>=1:
        c2.itemconfig(ch1, image=ch1_7)
        c2.tag_bind(ch1, '<Button-1>', ch1_klik)
    else:
        c2.config(cursor="x_cursor")
        c2.tag_unbind(ch1, '<Button-1>')
def ch1_2(e=None):
    global paree
    ispis_para.config(state=NORMAL)
    xd = int(ispis_para.get('1.0',END))
    ispis_para.config(state=DISABLED)
    if xd>=1:
        c2.itemconfig(ch1, image=ch1_5)
    else:
        c2.config(cursor="circle")
        c2.tag_bind(ch1, '<Button-1>', ch1_klik)
def ch5_1(e=None):
    ispis_para.config(state=NORMAL)
    xd = int(ispis_para.get('1.0',END))
    ispis_para.config(state=DISABLED)
    global paree
    if xd>=5:
        c2.itemconfig(ch5, image=ch5_7)
        c2.tag_bind(ch5, '<Button-1>', ch5_klik)
    else:
        c2.config(cursor="x_cursor")
        c2.tag_unbind(ch5, '<Button-1>')
def ch5_2(e=None):
    ispis_para.config(state=NORMAL)
    xd = int(ispis_para.get('1.0',END))
    ispis_para.config(state=DISABLED)
    global paree
    if xd>=5:
        c2.itemconfig(ch5, image=ch5_5)
    else:
        c2.config(cursor="circle")
        c2.tag_bind(ch5, '<Button-1>', ch5_klik)
def ch10_1(e=None):
    ispis_para.config(state=NORMAL)
    xd = int(ispis_para.get('1.0',END))
    ispis_para.config(state=DISABLED)
    global paree
    if xd>=10:
        c2.itemconfig(ch10, image=ch10_7)
        c2.tag_bind(ch10, '<Button-1>', ch10_klik)
    else:
        c2.config(cursor="x_cursor")
        c2.tag_unbind(ch10, '<Button-1>')
def ch10_2(e=None):
    ispis_para.config(state=NORMAL)
    xd = int(ispis_para.get('1.0',END))
    ispis_para.config(state=DISABLED)
    global paree
    if xd>=10:
        c2.itemconfig(ch10, image=ch10_5)
    else:
        c2.config(cursor="circle")
        c2.tag_bind(ch10, '<Button-1>', ch10_klik)
def ch20_1(e=None):
    ispis_para.config(state=NORMAL)
    xd = int(ispis_para.get('1.0',END))
    ispis_para.config(state=DISABLED)
    global paree
    if xd>=20:
        c2.itemconfig(ch20, image=ch20_7)
        c2.tag_bind(ch20, '<Button-1>', ch20_klik)
    else:
        c2.config(cursor="x_cursor")
        c2.tag_unbind(ch20, '<Button-1>')
def ch20_2(e=None):
    ispis_para.config(state=NORMAL)
    xd = int(ispis_para.get('1.0',END))
    ispis_para.config(state=DISABLED)
    global paree
    if xd>=20:
        c2.itemconfig(ch20, image=ch20_5)
    else:
        c2.config(cursor="circle")
        c2.tag_bind(ch20, '<Button-1>', ch20_klik)
def ch50_1(e=None):
    ispis_para.config(state=NORMAL)
    xd = int(ispis_para.get('1.0',END))
    ispis_para.config(state=DISABLED)
    global paree
    if xd>=50:
        c2.itemconfig(ch50, image=ch50_7)
        c2.tag_bind(ch50, '<Button-1>', ch50_klik)
    else:
        c2.config(cursor="x_cursor")
        c2.tag_unbind(ch50, '<Button-1>')
def ch50_2(e=None):
    ispis_para.config(state=NORMAL)
    xd = int(ispis_para.get('1.0',END))
    ispis_para.config(state=DISABLED)
    global paree
    if xd>=50:
        c2.itemconfig(ch50, image=ch50_5)
    else:
        c2.config(cursor="circle")
        c2.tag_bind(ch50, '<Button-1>', ch50_klik)
def ch100_1(e=None):
    ispis_para.config(state=NORMAL)
    xd = int(ispis_para.get('1.0',END))
    ispis_para.config(state=DISABLED)
    global paree
    if xd>=100:
        c2.itemconfig(ch100, image=ch100_7)
        c2.tag_bind(ch100, '<Button-1>', ch100_klik)
    else:
        c2.config(cursor="x_cursor")
        c2.tag_unbind(ch100, '<Button-1>')
def ch100_2(e=None):
    ispis_para.config(state=NORMAL)
    xd = int(ispis_para.get('1.0',END))
    ispis_para.config(state=DISABLED)
    global paree
    if xd>=100:
        c2.itemconfig(ch100, image=ch100_5)
    else:
        c2.config(cursor="circle")
        c2.tag_bind(ch100, '<Button-1>', ch100_klik)
def ch500_1(e=None):
    ispis_para.config(state=NORMAL)
    xd = int(ispis_para.get('1.0',END))
    ispis_para.config(state=DISABLED)
    global paree
    if xd>=500:
        c2.itemconfig(ch500, image=ch500_7)
        c2.tag_bind(ch500, '<Button-1>', ch500_klik)
    else:
        c2.config(cursor="x_cursor")
        c2.tag_unbind(ch500, '<Button-1>')
def ch500_2(e=None):
    ispis_para.config(state=NORMAL)
    xd = int(ispis_para.get('1.0',END))
    ispis_para.config(state=DISABLED)
    global paree
    if xd>=500:
        c2.itemconfig(ch500, image=ch500_5)
    else:
        c2.config(cursor="circle")
        c2.tag_bind(ch500, '<Button-1>', ch500_klik)
def ch1000_1(e=None):
    ispis_para.config(state=NORMAL)
    xd = int(ispis_para.get('1.0',END))
    ispis_para.config(state=DISABLED)
    global paree
    if xd>=1000:
        c2.itemconfig(ch1000, image=ch1000_7)
        c2.tag_bind(ch1000, '<Button-1>', ch1000_klik)
    else:
        c2.config(cursor="x_cursor")
        c2.tag_unbind(ch1000, '<Button-1>')
def ch1000_2(e=None):
    ispis_para.config(state=NORMAL)
    xd = int(ispis_para.get('1.0',END))
    ispis_para.config(state=DISABLED)
    global paree
    if xd>=1000:
        c2.itemconfig(ch1000, image=ch1000_5)
    else:
        c2.config(cursor="circle")
        c2.tag_bind(ch1000, '<Button-1>', ch1000_klik)

def ch1_klik(e=None):
    global chip_red
    chip_red = 1
    c2.tag_unbind(ch1, '<Enter>')
    c2.tag_unbind(ch1, '<Leave>')
    c2.itemconfig(ch1, image=ch1_7)
    
    c2.tag_bind(ch5, '<Enter>', ch5_1)
    c2.tag_bind(ch5, '<Leave>', ch5_2)
    c2.tag_bind(ch10, '<Enter>', ch10_1)
    c2.tag_bind(ch10, '<Leave>', ch10_2)
    c2.tag_bind(ch20, '<Enter>', ch20_1)
    c2.tag_bind(ch20, '<Leave>', ch20_2)
    c2.tag_bind(ch50, '<Enter>', ch50_1)
    c2.tag_bind(ch50, '<Leave>', ch50_2)
    c2.tag_bind(ch100, '<Enter>', ch100_1)
    c2.tag_bind(ch100, '<Leave>', ch100_2)
    c2.tag_bind(ch500, '<Enter>', ch500_1)
    c2.tag_bind(ch500, '<Leave>', ch500_2)
    c2.tag_bind(ch1000, '<Enter>', ch1000_1)
    c2.tag_bind(ch1000, '<Leave>', ch1000_2)

    c2.itemconfig(ch5, image=ch5_5)
    c2.itemconfig(ch10, image=ch10_5)
    c2.itemconfig(ch20, image=ch20_5)
    c2.itemconfig(ch50, image=ch50_5)
    c2.itemconfig(ch100, image=ch100_5)
    c2.itemconfig(ch500, image=ch500_5)
    c2.itemconfig(ch1000, image=ch1000_5)
    
def ch5_klik(e=None):
    global chip_red
    chip_red = 5
    c2.tag_unbind(ch5, '<Enter>')
    c2.tag_unbind(ch5, '<Leave>')
    c2.itemconfig(ch5, image=ch5_7)

    c2.tag_bind(ch1, '<Enter>', ch1_1)
    c2.tag_bind(ch1, '<Leave>', ch1_2)
    c2.tag_bind(ch10, '<Enter>', ch10_1)
    c2.tag_bind(ch10, '<Leave>', ch10_2)
    c2.tag_bind(ch20, '<Enter>', ch20_1)
    c2.tag_bind(ch20, '<Leave>', ch20_2)
    c2.tag_bind(ch50, '<Enter>', ch50_1)
    c2.tag_bind(ch50, '<Leave>', ch50_2)
    c2.tag_bind(ch100, '<Enter>', ch100_1)
    c2.tag_bind(ch100, '<Leave>', ch100_2)
    c2.tag_bind(ch500, '<Enter>', ch500_1)
    c2.tag_bind(ch500, '<Leave>', ch500_2)
    c2.tag_bind(ch1000, '<Enter>', ch1000_1)
    c2.tag_bind(ch1000, '<Leave>', ch1000_2)

    c2.itemconfig(ch1, image=ch1_5)
    c2.itemconfig(ch10, image=ch10_5)
    c2.itemconfig(ch20, image=ch20_5)
    c2.itemconfig(ch50, image=ch50_5)
    c2.itemconfig(ch100, image=ch100_5)
    c2.itemconfig(ch500, image=ch500_5)
    c2.itemconfig(ch1000, image=ch1000_5)
    
def ch10_klik(e=None):
    global chip_red
    chip_red = 10
    c2.tag_unbind(ch10, '<Enter>')
    c2.tag_unbind(ch10, '<Leave>')
    c2.itemconfig(ch10, image=ch10_7)
    
    c2.tag_bind(ch1, '<Enter>', ch1_1)
    c2.tag_bind(ch1, '<Leave>', ch1_2)
    c2.tag_bind(ch5, '<Enter>', ch5_1)
    c2.tag_bind(ch5, '<Leave>', ch5_2)
    c2.tag_bind(ch20, '<Enter>', ch20_1)
    c2.tag_bind(ch20, '<Leave>', ch20_2)
    c2.tag_bind(ch50, '<Enter>', ch50_1)
    c2.tag_bind(ch50, '<Leave>', ch50_2)
    c2.tag_bind(ch100, '<Enter>', ch100_1)
    c2.tag_bind(ch100, '<Leave>', ch100_2)
    c2.tag_bind(ch500, '<Enter>', ch500_1)
    c2.tag_bind(ch500, '<Leave>', ch500_2)
    c2.tag_bind(ch1000, '<Enter>', ch1000_1)
    c2.tag_bind(ch1000, '<Leave>', ch1000_2)

    c2.itemconfig(ch1, image=ch1_5)
    c2.itemconfig(ch5, image=ch5_5)
    c2.itemconfig(ch20, image=ch20_5)
    c2.itemconfig(ch50, image=ch50_5)
    c2.itemconfig(ch100, image=ch100_5)
    c2.itemconfig(ch500, image=ch500_5)
    c2.itemconfig(ch1000, image=ch1000_5)
    
def ch20_klik(e=None):
    global chip_red
    chip_red = 20
    c2.tag_unbind(ch20, '<Enter>')
    c2.tag_unbind(ch20, '<Leave>')
    c2.itemconfig(ch20, image=ch20_7)

    c2.tag_bind(ch1, '<Enter>', ch1_1)
    c2.tag_bind(ch1, '<Leave>', ch1_2)
    c2.tag_bind(ch5, '<Enter>', ch5_1)
    c2.tag_bind(ch5, '<Leave>', ch5_2)
    c2.tag_bind(ch10, '<Enter>', ch10_1)
    c2.tag_bind(ch10, '<Leave>', ch10_2)
    c2.tag_bind(ch50, '<Enter>', ch50_1)
    c2.tag_bind(ch50, '<Leave>', ch50_2)
    c2.tag_bind(ch100, '<Enter>', ch100_1)
    c2.tag_bind(ch100, '<Leave>', ch100_2)
    c2.tag_bind(ch500, '<Enter>', ch500_1)
    c2.tag_bind(ch500, '<Leave>', ch500_2)
    c2.tag_bind(ch1000, '<Enter>', ch1000_1)
    c2.tag_bind(ch1000, '<Leave>', ch1000_2)

    c2.itemconfig(ch1, image=ch1_5)
    c2.itemconfig(ch5, image=ch5_5)
    c2.itemconfig(ch10, image=ch10_5)
    c2.itemconfig(ch50, image=ch50_5)
    c2.itemconfig(ch100, image=ch100_5)
    c2.itemconfig(ch500, image=ch500_5)
    c2.itemconfig(ch1000, image=ch1000_5)
    
def ch50_klik(e=None):
    global chip_red
    chip_red = 50
    c2.tag_unbind(ch50, '<Enter>')
    c2.tag_unbind(ch50, '<Leave>')
    c2.itemconfig(ch50, image=ch50_7)

    c2.tag_bind(ch1, '<Enter>', ch1_1)
    c2.tag_bind(ch1, '<Leave>', ch1_2)
    c2.tag_bind(ch5, '<Enter>', ch5_1)
    c2.tag_bind(ch5, '<Leave>', ch5_2)
    c2.tag_bind(ch10, '<Enter>', ch10_1)
    c2.tag_bind(ch10, '<Leave>', ch10_2)
    c2.tag_bind(ch20, '<Enter>', ch20_1)
    c2.tag_bind(ch20, '<Leave>', ch20_2)
    c2.tag_bind(ch100, '<Enter>', ch100_1)
    c2.tag_bind(ch100, '<Leave>', ch100_2)
    c2.tag_bind(ch500, '<Enter>', ch500_1)
    c2.tag_bind(ch500, '<Leave>', ch500_2)
    c2.tag_bind(ch1000, '<Enter>', ch1000_1)
    c2.tag_bind(ch1000, '<Leave>', ch1000_2)

    c2.itemconfig(ch1, image=ch1_5)
    c2.itemconfig(ch5, image=ch5_5)
    c2.itemconfig(ch10, image=ch10_5)
    c2.itemconfig(ch20, image=ch20_5)
    c2.itemconfig(ch100, image=ch100_5)
    c2.itemconfig(ch500, image=ch500_5)
    c2.itemconfig(ch1000, image=ch1000_5)
    
def ch100_klik(e=None):
    global chip_red
    chip_red = 100
    c2.tag_unbind(ch100, '<Enter>')
    c2.tag_unbind(ch100, '<Leave>')
    c2.itemconfig(ch100, image=ch100_7)

    c2.tag_bind(ch1, '<Enter>', ch1_1)
    c2.tag_bind(ch1, '<Leave>', ch1_2)
    c2.tag_bind(ch5, '<Enter>', ch5_1)
    c2.tag_bind(ch5, '<Leave>', ch5_2)
    c2.tag_bind(ch10, '<Enter>', ch10_1)
    c2.tag_bind(ch10, '<Leave>', ch10_2)
    c2.tag_bind(ch20, '<Enter>', ch20_1)
    c2.tag_bind(ch20, '<Leave>', ch20_2)
    c2.tag_bind(ch50, '<Enter>', ch50_1)
    c2.tag_bind(ch50, '<Leave>', ch50_2)
    c2.tag_bind(ch500, '<Enter>', ch500_1)
    c2.tag_bind(ch500, '<Leave>', ch500_2)
    c2.tag_bind(ch1000, '<Enter>', ch1000_1)
    c2.tag_bind(ch1000, '<Leave>', ch1000_2)

    c2.itemconfig(ch1, image=ch1_5)
    c2.itemconfig(ch5, image=ch5_5)
    c2.itemconfig(ch10, image=ch10_5)
    c2.itemconfig(ch20, image=ch20_5)
    c2.itemconfig(ch50, image=ch50_5)
    c2.itemconfig(ch500, image=ch500_5)
    c2.itemconfig(ch1000, image=ch1000_5)
    
def ch500_klik(e=None):
    global chip_red
    chip_red = 500
    c2.tag_unbind(ch500, '<Enter>')
    c2.tag_unbind(ch500, '<Leave>')
    c2.itemconfig(ch500, image=ch500_7)

    c2.tag_bind(ch1, '<Enter>', ch1_1)
    c2.tag_bind(ch1, '<Leave>', ch1_2)
    c2.tag_bind(ch5, '<Enter>', ch5_1)
    c2.tag_bind(ch5, '<Leave>', ch5_2)
    c2.tag_bind(ch10, '<Enter>', ch10_1)
    c2.tag_bind(ch10, '<Leave>', ch10_2)
    c2.tag_bind(ch20, '<Enter>', ch20_1)
    c2.tag_bind(ch20, '<Leave>', ch20_2)
    c2.tag_bind(ch50, '<Enter>', ch50_1)
    c2.tag_bind(ch50, '<Leave>', ch50_2)
    c2.tag_bind(ch100, '<Enter>', ch100_1)
    c2.tag_bind(ch100, '<Leave>', ch100_2)
    c2.tag_bind(ch1000, '<Enter>', ch1000_1)
    c2.tag_bind(ch1000, '<Leave>', ch1000_2)

    c2.itemconfig(ch1, image=ch1_5)
    c2.itemconfig(ch5, image=ch5_5)
    c2.itemconfig(ch10, image=ch10_5)
    c2.itemconfig(ch20, image=ch20_5)
    c2.itemconfig(ch50, image=ch50_5)
    c2.itemconfig(ch100, image=ch100_5)
    c2.itemconfig(ch1000, image=ch1000_5)
    
def ch1000_klik(e=None):
    global chip_red
    chip_red = 1000
    c2.tag_unbind(ch1000, '<Enter>')
    c2.tag_unbind(ch1000, '<Leave>')
    c2.itemconfig(ch1000, image=ch1000_7)

    c2.tag_bind(ch1, '<Enter>', ch1_1)
    c2.tag_bind(ch1, '<Leave>', ch1_2)
    c2.tag_bind(ch5, '<Enter>', ch5_1)
    c2.tag_bind(ch5, '<Leave>', ch5_2)
    c2.tag_bind(ch10, '<Enter>', ch10_1)
    c2.tag_bind(ch10, '<Leave>', ch10_2)
    c2.tag_bind(ch20, '<Enter>', ch20_1)
    c2.tag_bind(ch20, '<Leave>', ch20_2)
    c2.tag_bind(ch50, '<Enter>', ch50_1)
    c2.tag_bind(ch50, '<Leave>', ch50_2)
    c2.tag_bind(ch100, '<Enter>', ch100_1)
    c2.tag_bind(ch100, '<Leave>', ch100_2)
    c2.tag_bind(ch500, '<Enter>', ch500_1)
    c2.tag_bind(ch500, '<Leave>', ch500_2)

    c2.itemconfig(ch1, image=ch1_5)
    c2.itemconfig(ch5, image=ch5_5)
    c2.itemconfig(ch10, image=ch10_5)
    c2.itemconfig(ch20, image=ch20_5)
    c2.itemconfig(ch50, image=ch50_5)
    c2.itemconfig(ch100, image=ch100_5)
    c2.itemconfig(ch500, image=ch500_5)

def zatvorii(e=None):
    zatvori.destroy()
    c2.delete(brojine_windows)
    c2.delete(zeleno)
    janko.destroy()
    bar1.get_tk_widget().place(x=5330,y=3453)
    line2.get_tk_widget().place(x=5330,y=3453)

def statika(e=None):
    global gembaci
    global samo_brojevi
    global broj_vrtnji
    global iznos_vrtnji
    global bar1
    global line2
    global janko
    global brojine
    global brojine_windows
    data1 = {'Brojevi': [int(t) for t in samo_brojevi],
         'Ponavljanje': [samo_brojevi[t] for t in samo_brojevi]
        }
    color_dict ={'0':'green',
                 '1':'red',
                 '2':'black',
                 '3':'red',
                 '4':'black',
                 '5':'red',
                 '6':'black',
                 '7':'red',
                 '8':'black',
                 '9':'red',
                 '10':'black',
                 '11':'black',
                 '12':'red',
                 '13':'black',
                 '14':'red',
                 '15':'black'}
    df1 = DataFrame(data1,columns=['Brojevi','Ponavljanje'])
    figure1 = plt.Figure(figsize=(6,5), dpi=100)
    figure1.patch.set_facecolor('green')
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, c2)
    bar1.get_tk_widget().place(x=-25,y=-17)
    df1 = df1[['Brojevi','Ponavljanje']].groupby('Brojevi').sum()
    df1.plot(kind='bar', legend=False, ax=ax1, color=['r','g','r','g','r','g','r','g','r','g','r','g','r','g','r','g','r','g','r','g','r','g','r','g','r','g','r','g'])
    ax1.set_title('Broj ponavljanja brojeva')

    data2 = {'Broj vrtnji': broj_vrtnji,
         'Stanje para': iznos_vrtnji
        }
    df2 = DataFrame(data2,columns=['Broj vrtnji','Stanje para'])

    figure2 = plt.Figure(figsize=(5,5), dpi=100)
    figure2.patch.set_facecolor('green')
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, r1)
    line2.get_tk_widget().place(x=790,y=-17)
    df2 = df2[['Broj vrtnji','Stanje para']].groupby('Broj vrtnji').sum()
    df2.plot(kind='line', legend=False, ax=ax2, color='r',marker='o', fontsize=10)
    ax2.set_title('Stanje para po vrtnjama')
    global zeleno
    zeleno = c2.create_rectangle(500, 0, 900, 484,
                    fill="green")
    global zatvori
    zatvori = Button(r1,
                activebackground = "#00FF00",
                background = "green",
                text='Natrag',
                font=('Arial', 10,'bold'),
                relief=RAISED,\
                cursor="circle",
                fg='white',
                command = zatvorii)
    zatvori_window = c2.create_window(644, 450,
                                         width = 59,
                                         height = 30,
                                         anchor='nw',
                                         window=zatvori)
    janko=Label(c2)
    janko.place(x=595,y=20)
    janko.config(borderwidth=0, highlightthickness=0)
    janko.config(text='Posljedni brojevi',bg='green',font=('Arial', 15,'bold'))
    brojine = Text(r1,
                   width=15,
                   font=("Calibri",50,'bold'),
                   fg='white',
                   background='#0B4709',
                   relief=RAISED,\
                   cursor="circle")
    brojine_windows = c2.create_window(635, 50, width = 75, height = 379, anchor='nw', window=brojine)
    brojine.config(state=NORMAL)
    brojine.delete('1.0', END)
    brojine.tag_config('crv', foreground='#DB1F1F',justify='center')
    brojine.tag_config('crn', foreground='black',justify='center')
    brojine.tag_config('nula', foreground='#00FF00',justify='center')
    for i in range(len(statistika_brojeva)):
        if statistika_brojeva[i] in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
            brojine.insert(END,str(statistika_brojeva[i]),'crv')
        elif statistika_brojeva[i] in [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]:
            brojine.insert(END,str(statistika_brojeva[i]),'crn')
        elif statistika_brojeva[i]==0:
            brojine.insert(END,str(statistika_brojeva[i]),'nula')
        if statistika_brojeva[i]!=statistika_brojeva[-1]:
            brojine.insert(END,'\n')
        else:
            pass
    try:
        brojine.yview_pickplace(END)
    except:
        pass
    brojine.config(state=DISABLED)
        

def pomocc(e=None):
    global pomoc_slika
    global pomoc_gumb
    global my_label
    global mylabel
    global novi
    novi = Label(c2)
    novi.place(x=0,y=0)
    novi.config(image=holp)
    novi.image = holp
    
    izbrisi.config(state=DISABLED)
    helpp.config(state=DISABLED)
    statistic.config(state=DISABLED)
    vrti.config(state=DISABLED)
    pomoc_gumb = Button(r1,
                activebackground = "#00FF00",
                background = "green",
                text='Natrag',
                font=('Arial', 10,'bold'),
                relief=RAISED,\
                cursor="circle",
                fg='white',
                command = makni)
    pomoc_gumb_window = c2.create_window(10, 445,
                                         width = 59,
                                         height = 30,
                                         anchor='nw',
                                         window=pomoc_gumb)
    c2.config(width=475,height=480)

def makni(e=None):
    global mylabel
    global my_label
    global novi
    pomoc_gumb.destroy()
    novi.place_forget()
    izbrisi.config(state=NORMAL)
    helpp.config(state=NORMAL)
    statistic.config(state=NORMAL)
    vrti.config(state=NORMAL)
    c2.config(width=1280,height=480)
    
def startt(label):
    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image

def stream(label):
    global prozorr
    global gumbaci
    global trumbaci
    global broj_vrtnji
    global iznos_vrtnji
    global finalan_broj
    global ukupno
    global paree
    global gembaci
    global my_label
    crveni = [1,3,5,7,9,12,14,16,18,
              19,21,23,25,27,30,32,34,36]
    crni = [2,4,6,8,10,11,13,15,17,
            20,22,24,26,28,29,31,33,35]
    parni = [2,4,6,8,10,12,14,16,18,
             20,22,24,26,28,30,32,34,36]
    neparni = [1,3,5,7,9,11,13,15,17,
               19,21,23,25,27,29,31,33,35]
    prvih_12st = [1,2,3,4,5,6,7,8,9,10,11,12]
    drugih_12st = [13,14,15,16,17,18,19,20,21,22,23,24]
    trecih_12st = [25,26,27,28,29,30,31,32,33,34,35,36]
    prva_trechina = [1,4,7,10,13,16,19,22,25,28,31,34]
    druga_trechina = [2,5,8,11,14,17,20,23,26,29,32,35]
    treca_trechina = [3,6,9,12,15,18,21,24,27,30,33,36]
    prvih_osamnaest = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    drugih_osamnaest = [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36] 
    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image
    vrti.config(state=NORMAL)
    helpp.config(state=NORMAL)
    izbrisi.config(state=NORMAL)
    statistic.config(state=NORMAL)
    c2.delete(prozorr)
    c2.tag_bind(ch1, '<Enter>', ch1_1)
    c2.tag_bind(ch1, '<Leave>', ch1_2)
    c2.tag_bind(ch5, '<Enter>', ch5_1)
    c2.tag_bind(ch5, '<Leave>', ch5_2)
    c2.tag_bind(ch10, '<Enter>', ch10_1)
    c2.tag_bind(ch10, '<Leave>', ch10_2)
    c2.tag_bind(ch20, '<Enter>', ch20_1)
    c2.tag_bind(ch20, '<Leave>', ch20_2)
    c2.tag_bind(ch50, '<Enter>', ch50_1)
    c2.tag_bind(ch50, '<Leave>', ch50_2)
    c2.tag_bind(ch100, '<Enter>', ch100_1)
    c2.tag_bind(ch100, '<Leave>', ch100_2)
    c2.tag_bind(ch500, '<Enter>', ch500_1)
    c2.tag_bind(ch500, '<Leave>', ch500_2)
    c2.tag_bind(ch1000, '<Enter>', ch1000_1)
    c2.tag_bind(ch1000, '<Leave>', ch1000_2)
    if finalan_broj == 0:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['0']*=36
        gembaci['0']+=1
    if finalan_broj == 1:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['1']*=36
        gembaci['1']+=1
    if finalan_broj == 2:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['2']*=36
        gembaci['2']+=1
    if finalan_broj == 3:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['3']*=36
        gembaci['3']+=1
    if finalan_broj == 4:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['4']*=36
        gembaci['4']+=1
    if finalan_broj == 5:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['5']*=36
        gembaci['5']+=1
    if finalan_broj == 6:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['6']*=36
        gembaci['6']+=1
    if finalan_broj == 7:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['7']*=36
        gembaci['7']+=1
    if finalan_broj == 8:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['8']*=36
        gembaci['8']+=1
    if finalan_broj == 9:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['9']*=36
        gembaci['9']+=1
    if finalan_broj == 10:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['10']*=36
        gembaci['10']+=1
    if finalan_broj == 11:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['11']*=36
        gembaci['11']+=1
    if finalan_broj == 12:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['12']*=36
        gembaci['12']+=1
    if finalan_broj == 13:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['13']*=36
        gembaci['13']+=1
    if finalan_broj == 14:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['14']*=36
        gembaci['14']+=1
    if finalan_broj == 15:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['15']*=36
        gembaci['15']+=1
    if finalan_broj == 16:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['16']*=36
        gembaci['16']+=1
    if finalan_broj == 17:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['17']*=36
        gembaci['17']+=1
    if finalan_broj == 18:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['18']*=36
        gembaci['18']+=1
    if finalan_broj == 19:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['19']*=36
        gembaci['19']+=1
    if finalan_broj == 20:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['20']*=36
        gembaci['20']+=1
    if finalan_broj == 21:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['21']*=36
        gembaci['21']+=1
    if finalan_broj == 22:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['22']*=36
        gembaci['22']+=1
    if finalan_broj == 23:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['23']*=36
        gembaci['23']+=1
    if finalan_broj == 24:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['24']*=36
        gembaci['24']+=1
    if finalan_broj == 25:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['25']*=36
        gembaci['25']+=1
    if finalan_broj == 26:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['26']*=36
        gembaci['26']+=1
    if finalan_broj == 27:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['27']*=36
        gembaci['27']+=1
    if finalan_broj == 28:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['28']*=36
        gembaci['28']+=1
    if finalan_broj == 29:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['29']*=36
        gembaci['29']+=1
    if finalan_broj == 30:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['30']*=36
        gembaci['30']+=1
    if finalan_broj == 31:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['31']*=36
        gembaci['31']+=1
    if finalan_broj == 32:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['32']*=36
        gembaci['32']+=1
    if finalan_broj == 33:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['33']*=36
        gembaci['33']+=1
    if finalan_broj == 34:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['34']*=36
        gembaci['34']+=1
    if finalan_broj == 35:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['35']*=36
        gembaci['35']+=1
    if finalan_broj == 36:
        samo_brojevi[str(finalan_broj)]+=1
        gumbaci['36']*=36
        gembaci['36']+=1
    if finalan_broj in crveni:
        gumbaci['CRVENIMA']*=2
        gembaci['CRVENIMA']+=1
    if finalan_broj in crni:
        gumbaci['CRNIMA']*=2
        gembaci['CRNIMA']+=1
    if finalan_broj in prvih_osamnaest:
        gumbaci['1-18']*=2
        gembaci['1-18']+=1
    if finalan_broj in drugih_osamnaest:
        gumbaci['19-36']*=2
        gembaci['19-36']+=1
    if finalan_broj in parni:
        gumbaci['PARNIMA']*=2
        gembaci['PARNIMA']+=1
    if finalan_broj in neparni:
        gumbaci['NEPARNIMA']*=2
        gembaci['NEPARNIMA']+=1
    if finalan_broj in prvih_12st:
        gumbaci['1. TREĆINI']*=3
        gembaci['1. TREĆINI']+=1
    if finalan_broj in drugih_12st:
        gumbaci['2. TREĆINI']*=3
        gembaci['2. TREĆINI']+=1
    if finalan_broj in trecih_12st:
        gumbaci['3. TREĆINI']*=3
        gembaci['3. TREĆINI']+=1
    if finalan_broj in prva_trechina:
        gumbaci['1. REDU']*=3
        gembaci['1. REDU']+=1
    if finalan_broj in druga_trechina:
        gumbaci['2. REDU']*=3
        gembaci['2. REDU']+=1
    if finalan_broj in treca_trechina:
        gumbaci['3. REDU']*=3
        gembaci['3. REDU']+=1
    if finalan_broj in [1,2,4,5]:
        gumbaci['1-2-4-5']*=9
        gembaci['1-2-4-5']+=1
    if finalan_broj in [2,3,5,6]:
        gumbaci['2-3-5-6']*=9
        gembaci['2-3-5-6']+=1
    if finalan_broj in [4,5,7,8]:
        gumbaci['4-5-7-8']*=9
        gembaci['4-5-7-8']+=1
    if finalan_broj in [5,6,8,9]:
        gumbaci['5-6-8-9']*=9
        gembaci['5-6-8-9']+=1
    if finalan_broj in [7,8,10,11]:
        gumbaci['7-8-10-11']*=9
        gembaci['7-8-10-11']+=1
    if finalan_broj in [8,9,11,12]:
        gumbaci['8-9-11-12']*=9
        gembaci['8-9-11-12']+=1
    if finalan_broj in [10,11,13,14]:
        gumbaci['10-11-13-14']*=9
        gembaci['10-11-13-14']+=1
    if finalan_broj in [11,12,14,15]:
        gumbaci['11-12-14-15']*=9
        gembaci['11-12-14-15']+=1
    if finalan_broj in [13,14,16,17]:
        gumbaci['13-14-16-17']*=9
        gembaci['13-14-16-17']+=1
    if finalan_broj in [14,15,17,18]:
        gumbaci['14-15-17-18']*=9
        gembaci['14-15-17-18']+=1
    if finalan_broj in [16,17,19,20]:
        gumbaci['16-17-19-20']*=9
        gembaci['16-17-19-20']+=1
    if finalan_broj in [17,18,20,21]:
        gumbaci['17-18-20-21']*=9
        gembaci['17-18-20-21']+=1
    if finalan_broj in [19,20,22,23]:
        gumbaci['19-20-22-23']*=9
        gembaci['19-20-22-23']+=1
    if finalan_broj in [20,21,23,24]:
        gumbaci['20-21-23-24']*=9
        gembaci['20-21-23-24']+=1
    if finalan_broj in [22,23,25,26]:
        gumbaci['22-23-25-26']*=9
        gembaci['22-23-25-26']+=1
    if finalan_broj in [23,24,26,27]:
        gumbaci['23-24-26-27']*=9
        gembaci['23-24-26-27']+=1
    if finalan_broj in [25,26,28,29]:
        gumbaci['25-26-28-29']*=9
        gembaci['25-26-28-29']+=1
    if finalan_broj in [26,27,29,30]:
        gumbaci['26-27-29-30']*=9
        gembaci['26-27-29-30']+=1
    if finalan_broj in [28,29,31,32]:
        gumbaci['28-29-31-32']*=9
        gembaci['28-29-31-32']+=1
    if finalan_broj in [29,30,32,33]:
        gumbaci['29-30-32-33']*=9
        gembaci['29-30-32-33']+=1
    if finalan_broj in [31,32,34,35]:
        gumbaci['31-32-34-35']*=9
        gembaci['31-32-34-35']+=1
    if finalan_broj in [32,33,35,36]:
        gumbaci['32-33-35-36']*=9
        gembaci['32-33-35-36']+=1
    if finalan_broj in [1,2,3]:
        gumbaci['1-2-3']*=12
        gembaci['1-2-3']+=1
    if finalan_broj in [4,5,6]:
        gumbaci['4-5-6']*=12
        gembaci['4-5-6']+=1
    if finalan_broj in [7,8,9]:
        gumbaci['7-8-9']*=12
        gembaci['7-8-9']+=1
    if finalan_broj in [10,11,12]:
        gumbaci['10-11-12']*=12
        gembaci['10-11-12']+=1
    if finalan_broj in [13,14,15]:
        gumbaci['13-14-15']*=12
        gembaci['13-14-15']+=1
    if finalan_broj in [16,17,18]:
        gumbaci['16-17-18']*=12
        gembaci['16-17-18']+=1
    if finalan_broj in [19,20,21]:
        gumbaci['19-20-21']*=12
        gembaci['19-20-21']+=1
    if finalan_broj in [22,23,24]:
        gumbaci['22-23-24']*=12
        gembaci['22-23-24']+=1
    if finalan_broj in [25,26,27]:
        gumbaci['25-26-27']*=12
        gembaci['25-26-27']+=1
    if finalan_broj in [28,29,30]:
        gumbaci['28-29-30']*=12
        gembaci['28-29-30']+=1
    if finalan_broj in [31,32,33]:
        gumbaci['31-32-33']*=12
        gembaci['31-32-33']+=1
    if finalan_broj in [34,35,36]:
        gumbaci['34-35-36']*=12
        gembaci['34-35-36']+=1
    if finalan_broj in [1,2,3,4,5,6]:
        gumbaci['1 do 6']*=6
        gembaci['1 do 6']+=1
    if finalan_broj in [4,5,6,7,8,9]:
        gumbaci['4 do 9']*=6
        gembaci['4 do 9']+=1
    if finalan_broj in [7,8,9,10,11,12]:
        gumbaci['7 do 12']*=6
        gembaci['7 do 12']+=1
    if finalan_broj in [10,11,12,13,14,15]:
        gumbaci['10 do 15']*=6
        gembaci['10 do 15']+=1
    if finalan_broj in [13,14,15,16,17,18]:
        gumbaci['13 do 18']*=6
        gembaci['13 do 18']+=1
    if finalan_broj in [16,17,18,19,20,21]:
        gumbaci['16 do 21']*=6
        gembaci['16 do 21']+=1
    if finalan_broj in [19,20,21,22,23,24]:
        gumbaci['19 do 24']*=6
        gembaci['19 do 24']+=1
    if finalan_broj in [22,23,24,25,26,27]:
        gumbaci['22 do 27']*=6
        gembaci['22 do 27']+=1
    if finalan_broj in [25,26,27,28,29,30]:
        gumbaci['25 do 30']*=6
        gembaci['25 do 30']+=1
    if finalan_broj in [28,29,30,31,32,33]:
        gumbaci['28 do 33']*=6
        gembaci['28 do 33']+=1
    if finalan_broj in [31,32,33,34,35,36]:
        gumbaci['31 do 36']*=6
        gembaci['31 do 36']+=1
    if finalan_broj in [0,1,2,3]:
        gumbaci['0-1-2-3']*=9
        gembaci['0-1-2-3']+=1
    if finalan_broj in [1,2]:
        gumbaci['1-2']*=18
        gembaci['1-2']+=1
    if finalan_broj in [2,3]:
        gumbaci['2-3']*=18
        gembaci['2-3']+=1
    if finalan_broj in [4,5]:
        gumbaci['4-5']*=18
        gembaci['4-5']+=1
    if finalan_broj in [5,6]:
        gumbaci['5-6']*=18
        gembaci['5-6']+=1
    if finalan_broj in [7,8]:
        gumbaci['7-8']*=18
        gembaci['7-8']+=1
    if finalan_broj in [8,9]:
        gumbaci['8-9']*=18
        gembaci['8-9']+=1
    if finalan_broj in [10,11]:
        gumbaci['10-11']*=18
        gembaci['10-11']+=1
    if finalan_broj in [11,12]:
        gumbaci['11-12']*=18
        gembaci['11-12']+=1
    if finalan_broj in [13,14]:
        gumbaci['13-14']*=18
        gembaci['13-14']+=1
    if finalan_broj in [14,15]:
        gumbaci['14-15']*=18
        gembaci['14-15']+=1
    if finalan_broj in [16,17]:
        gumbaci['16-17']*=18
        gembaci['16-17']+=1
    if finalan_broj in [17,18]:
        gumbaci['17-18']*=18
        gembaci['17-18']+=1
    if finalan_broj in [19,20]:
        gumbaci['19-20']*=18
        gembaci['19-20']+=1
    if finalan_broj in [20,21]:
        gumbaci['20-21']*=18
        gembaci['20-21']+=1
    if finalan_broj in [22,23]:
        gumbaci['22-23']*=18
        gembaci['22-23']+=1
    if finalan_broj in [23,24]:
        gumbaci['23-24']*=18
        gembaci['23-24']+=1
    if finalan_broj in [25,26]:
        gumbaci['25-26']*=18
        gembaci['25-26']+=1
    if finalan_broj in [26,27]:
        gumbaci['26-27']*=18
        gembaci['26-27']+=1
    if finalan_broj in [28,29]:
        gumbaci['28-29']*=18
        gembaci['28-29']+=1
    if finalan_broj in [29,30]:
        gumbaci['29-30']*=18
        gembaci['29-30']+=1
    if finalan_broj in [31,32]:
        gumbaci['31-32']*=18
        gembaci['31-32']+=1
    if finalan_broj in [32,33]:
        gumbaci['32-33']*=18
        gembaci['32-33']+=1
    if finalan_broj in [34,35]:
        gumbaci['34-35']*=18
        gembaci['34-35']+=1
    if finalan_broj in [35,36]:
        gumbaci['35-36']*=18
        gembaci['35-36']+=1
    if finalan_broj in [0,1,2]:
        gumbaci['0-1-2']*=12
        gembaci['0-1-2']+=1
    if finalan_broj in [0,2]:
        gumbaci['0-2']*=18
        gembaci['0-2']+=1
    if finalan_broj in [0,1]:
        gumbaci['0-1']*=18
        gembaci['0-1']+=1
    if finalan_broj in [0,3]:
        gumbaci['0-3']*=18
        gembaci['0-3']+=1
    if finalan_broj in [0,2,3]:
        gumbaci['0-2-3']*=12
        gembaci['0-2-3']+=1
    if finalan_broj in [1,4]:
        gumbaci['1-4']*=18
        gembaci['1-4']+=1
    if finalan_broj in [2,5]:
        gumbaci['2-5']*=18
        gembaci['2-5']+=1
    if finalan_broj in [3,6]:
        gumbaci['3-6']*=18
        gembaci['3-6']+=1
    if finalan_broj in [4,7]:
        gumbaci['4-7']*=18
        gembaci['4-7']+=1
    if finalan_broj in [5,8]:
        gumbaci['5-8']*=18
        gembaci['5-8']+=1
    if finalan_broj in [6,9]:
        gumbaci['6-9']*=18
        gembaci['6-9']+=1
    if finalan_broj in [7,10]:
        gumbaci['7-10']*=18
        gembaci['7-10']+=1
    if finalan_broj in [8,11]:
        gumbaci['8-11']*=18
        gembaci['8-11']+=1
    if finalan_broj in [9,12]:
        gumbaci['9-12']*=18
        gembaci['9-12']+=1
    if finalan_broj in [10,13]:
        gumbaci['10-13']*=18
        gembaci['10-13']+=1
    if finalan_broj in [11,14]:
        gumbaci['11-14']*=18
        gembaci['11-14']+=1
    if finalan_broj in [12,15]:
        gumbaci['12-15']*=18
        gembaci['12-15']+=1
    if finalan_broj in [13,16]:
        gumbaci['13-16']*=18
        gembaci['13-16']+=1
    if finalan_broj in [14,17]:
        gumbaci['14-17']*=18
        gembaci['14-17']+=1
    if finalan_broj in [15,18]:
        gumbaci['15-18']*=18
        gembaci['15-18']+=1
    if finalan_broj in [16,19]:
        gumbaci['16-19']*=18
        gembaci['16-19']+=1
    if finalan_broj in [17,20]:
        gumbaci['17-20']*=18
        gembaci['17-20']+=1
    if finalan_broj in [18,21]:
        gumbaci['18-21']*=18
        gembaci['18-21']+=1
    if finalan_broj in [19,22]:
        gumbaci['19-22']*=18
        gembaci['19-22']+=1
    if finalan_broj in [20,23]:
        gumbaci['20-23']*=18
        gembaci['20-23']+=1
    if finalan_broj in [21,24]:
        gumbaci['21-24']*=18
        gembaci['21-24']+=1
    if finalan_broj in [22,25]:
        gumbaci['22-25']*=18
        gembaci['22-25']+=1
    if finalan_broj in [23,26]:
        gumbaci['23-26']*=18
        gembaci['23-26']+=1
    if finalan_broj in [24,27]:
        gumbaci['24-27']*=18
        gembaci['24-27']+=1
    if finalan_broj in [25,28]:
        gumbaci['25-28']*=18
        gembaci['25-28']+=1
    if finalan_broj in [26,29]:
        gumbaci['26-29']*=18
        gembaci['26-29']+=1
    if finalan_broj in [27,30]:
        gumbaci['27-30']*=18
        gembaci['27-30']+=1
    if finalan_broj in [28,31]:
        gumbaci['28-31']*=18
        gembaci['28-31']+=1
    if finalan_broj in [29,32]:
        gumbaci['29-32']*=18
        gembaci['29-32']+=1
    if finalan_broj in [30,33]:
        gumbaci['30-33']*=18
        gembaci['30-33']+=1
    if finalan_broj in [31,34]:
        gumbaci['31-34']*=18
        gembaci['31-34']+=1
    if finalan_broj in [32,35]:
        gumbaci['32-35']*=18
        gembaci['32-35']+=1
    if finalan_broj in [33,36]:
        gumbaci['33-36']*=18
        gembaci['33-36']+=1
    profit=0
    spusio=0
    ispis_para.config(state=NORMAL)
    for c in trumbaci:
        if trumbaci[c]==gumbaci[c]:
            spusio+=gumbaci[c]
            gumbaci[c]=0
    for c in gumbaci:
        profit+=gumbaci[c]
    bootleg_obrisi()
    obavijesti.config(state=NORMAL)
    if profit==0:
        if int(ispis_para.get('1.0',END))==0:
            obavijesti.delete('1.0', END)
            obavijesti.insert(END, 'Prokockao si sve pare!', 'broj')
            obavijesti.insert(END, '\nKad si spreman, vrati se\ns djetetovim bubregom :)')
            label.place_forget()
            my_label.place_forget()
            jukic = Label(c2)
            jukic.place(x=1,y=0)
            jukic.config(image=genss, relief=RAISED,\
                cursor="pirate")
            vrti.config(state=NORMAL)
            vrti.config(text=':(((((((', state=DISABLED)
            helpp.config(state=DISABLED)
            izbrisi.config(state=DISABLED)
            prozorr = c2.create_image(1280/3+500, 480/3+5, image=proz)
            PlaySound(None, SND_PURGE)
            gotovo_je = PlaySound('intro\\gotovo_je.wav', SND_ASYNC)
        else:
            obavijesti.delete('1.0', END)
            obavijesti.insert(END, 'Bravo!', 'broj')
            obavijesti.insert(END, '\nIzgubio si sve što se ima za izgubit!\nJesi ponosan?')
            bruhhh = WaveObject.from_wave_file('intro\\bruhh.wav').play()
    elif profit>0:
        obavijesti.delete('1.0', END)
        obavijesti.insert(END, 'Tvoj gubitak: ')
        obavijesti.insert(END, spusio, 'crv')
        obavijesti.insert(END, '\nTvoj dobitak: ')
        obavijesti.insert(END, profit, 'iznos')
        woww = WaveObject.from_wave_file('intro\\wow.wav').play()
    obavijesti.config(state=DISABLED)
    money = int(ispis_para.get('1.0',END))
    paree+=profit
    money+=profit
    ispis_para.delete('1.0',END)
    ispis_para.insert(END, str(money), 'tag-right')
    iznos_vrtnji.append(int(ispis_para.get('1.0',END)))
    ispis_para.config(state=DISABLED)
    broj_vrtnji.append(broj_vrtnji[-1]+1)

def vrti_klik(e=None):
    global gumbaci
    global ukupno
    global trumbaci
    global prozorr
    global finalan_broj
    global video
    global sve_animacije
    global statistika_brojeva
    trumbaci = dict()
    ukupno = 0
    
    for c in gumbaci:
        ukupno+=gumbaci[c]
        trumbaci[c]=gumbaci[c]
    if ukupno!=0:
        finalan_broj = randint(0,36)
        statistika_brojeva.append(finalan_broj)

        c2.itemconfig(ch1, image=ch1_5)
        c2.itemconfig(ch5, image=ch5_5)
        c2.itemconfig(ch10, image=ch10_5)
        c2.itemconfig(ch20, image=ch20_5)
        c2.itemconfig(ch50, image=ch50_5)
        c2.itemconfig(ch100, image=ch100_5)
        c2.itemconfig(ch500, image=ch500_5)
        c2.itemconfig(ch1000, image=ch1000_5)
        c2.tag_unbind(ch1, '<Enter>')
        c2.tag_unbind(ch1, '<Leave>')
        c2.tag_unbind(ch5, '<Enter>')
        c2.tag_unbind(ch5, '<Leave>')
        c2.tag_unbind(ch10, '<Enter>')
        c2.tag_unbind(ch10, '<Leave>')
        c2.tag_unbind(ch20, '<Enter>')
        c2.tag_unbind(ch20, '<Leave>')
        c2.tag_unbind(ch50, '<Enter>')
        c2.tag_unbind(ch50, '<Leave>')
        c2.tag_unbind(ch100, '<Enter>')
        c2.tag_unbind(ch100, '<Leave>')
        c2.tag_unbind(ch500, '<Enter>')
        c2.tag_unbind(ch500, '<Leave>')
        c2.tag_unbind(ch1000, '<Enter>')
        c2.tag_unbind(ch1000, '<Leave>')

        vrti.config(state=DISABLED)
        helpp.config(state=DISABLED)
        izbrisi.config(state=DISABLED)
        statistic.config(state=DISABLED)

        prozorr = c2.create_image(1280/3+500, 480/3+5, image=proz)

        video = imageio.get_reader(sve_animacije[finalan_broj])
        global mylabel
        mylabel = Label(c2)
        mylabel.place(x=3,y=2)
        mylabel.config(borderwidth=0, highlightthickness=0)

        thread = threading.Thread(target=stream, args=(mylabel,))
        thread.daemon = 1
        thread.start()

        obavijesti.config(state=NORMAL)
        obavijesti.delete('1.0', END)
        obavijesti.insert(END, 'Rula se vrtiiiiii...')


r1 = Tk()
c2 = Canvas(r1, width=1280, height=480)
c2.pack()
bg1 = ImageTk.PhotoImage(file = 'main\\bg.png')
c2.create_image(1280/2+1, 480/2+1, image=bg1)
c2.config(cursor="circle")

c2.create_rectangle(474, 1280, 490, 0,
                    outline="yellow",
                    fill="black")
c2.pack(fill=BOTH, expand=1)


global holp

holp = ImageTk.PhotoImage(file = 'main\\help.png')

nula = c2.create_rectangle(550, 24, 593, 238,
                           fill="green",
                           tags="nula",
                           activefill='orange')
nnula = c2.create_text(572, 131,
                      text='0',
                      font=("Bodoni MT Black", 20),
                      fill='white')

c_0_3 = c2.create_rectangle(593, 48, 598, 68,
                      fill='green',
                      tags="c_0_3",
                            activefill='orange')
c_0_2 = c2.create_rectangle(593, 121, 598, 141,
                      fill='green',
                      tags="c_0_2",
                            activefill='orange')
c_0_1 = c2.create_rectangle(593, 194, 598, 214,
                      fill='green',
                      tags="c_0_1",
                            activefill='orange')
c_0_2_3 = c2.create_rectangle(593, 84, 598, 104,
                      fill='green',
                      tags="c_0_2_3",
                            activefill='orange')
c_0_1_2 = c2.create_rectangle(593, 157, 598, 177,
                      fill='green',
                      tags="c_0_2_3",
                            activefill='orange')

c_3_6 = c2.create_rectangle(641, 48, 646, 68,
                      fill='green',
                      tags="c_3_6",
                            activefill='orange')
c_2_5 = c2.create_rectangle(641, 121, 646, 141,
                      fill='green',
                      tags="c_2_5",
                            activefill='orange')
c_1_4 = c2.create_rectangle(641, 194, 646, 214,
                      fill='green',
                      tags="c_1_4",
                            activefill='orange')

c_6_9 = c2.create_rectangle(689, 48, 694, 68,
                      fill='green',
                      tags="c_6_9",
                            activefill='orange')
c_5_8 = c2.create_rectangle(689, 121, 694, 141,
                      fill='green',
                      tags="c_5_8",
                            activefill='orange')
c_4_7 = c2.create_rectangle(689, 194, 694, 214,
                      fill='green',
                      tags="c_4_7",
                            activefill='orange')

c_9_12 = c2.create_rectangle(737, 48, 742, 68,
                      fill='green',
                      tags="c_9_12",
                            activefill='orange')
c_8_11 = c2.create_rectangle(737, 121, 742, 141,
                      fill='green',
                      tags="c_8_11",
                            activefill='orange')
c_7_10 = c2.create_rectangle(737, 194, 742, 214,
                      fill='green',
                      tags="c_7_10",
                            activefill='orange')

c_12_15 = c2.create_rectangle(785, 48, 790, 68,
                      fill='green',
                      tags="c_12_15",
                            activefill='orange')
c_11_14 = c2.create_rectangle(785, 121, 790, 141,
                      fill='green',
                      tags="c_11_14",
                            activefill='orange')
c_10_13 = c2.create_rectangle(785, 194, 790, 214,
                      fill='green',
                      tags="c_10_13",
                            activefill='orange')

c_15_18 = c2.create_rectangle(833, 48, 838, 68,
                      fill='green',
                      tags="c_15_18",
                            activefill='orange')
c_14_17 = c2.create_rectangle(833, 121, 838, 141,
                      fill='green',
                      tags="c_14_17",
                            activefill='orange')
c_13_16 = c2.create_rectangle(833, 194, 838, 214,
                      fill='green',
                      tags="c_13_16",
                            activefill='orange')

c_18_21 = c2.create_rectangle(881, 48, 886, 68,
                      fill='green',
                      tags="c_18_21",
                            activefill='orange')
c_17_20 = c2.create_rectangle(881, 121, 886, 141,
                      fill='green',
                      tags="c_17_20",
                            activefill='orange')
c_16_19 = c2.create_rectangle(881, 194, 886, 214,
                      fill='green',
                      tags="c_16_19",
                            activefill='orange')

c_21_24 = c2.create_rectangle(929, 48, 934, 68,
                      fill='green',
                      tags="c_21_24",
                            activefill='orange')
c_20_23 = c2.create_rectangle(929, 121, 934, 141,
                      fill='green',
                      tags="c_20_23",
                            activefill='orange')
c_19_22 = c2.create_rectangle(929, 194, 934, 214,
                      fill='green',
                      tags="c_19_22",
                            activefill='orange')

c_24_27 = c2.create_rectangle(977, 48, 982, 68,
                      fill='green',
                      tags="c_24_27",
                            activefill='orange')
c_23_26 = c2.create_rectangle(977, 121, 982, 141,
                      fill='green',
                      tags="c_23_26",
                            activefill='orange')
c_22_25 = c2.create_rectangle(977, 194, 982, 214,
                      fill='green',
                      tags="c_22_25",
                            activefill='orange')

c_27_30 = c2.create_rectangle(1025, 48, 1030, 68,
                      fill='green',
                      tags="c_27_30",
                            activefill='orange')
c_26_29 = c2.create_rectangle(1025, 121, 1030, 141,
                      fill='green',
                      tags="c_26_29",
                            activefill='orange')
c_25_28 = c2.create_rectangle(1025, 194, 1030, 214,
                      fill='green',
                      tags="c_25_28",
                            activefill='orange')

c_30_33 = c2.create_rectangle(1073, 48, 1078, 68,
                      fill='green',
                      tags="c_30_33",
                            activefill='orange')
c_29_32 = c2.create_rectangle(1073, 121, 1078, 141,
                      fill='green',
                      tags="c_29_32",
                            activefill='orange')
c_28_31 = c2.create_rectangle(1073, 194, 1078, 214,
                      fill='green',
                      tags="c_28_31",
                            activefill='orange')

c_33_36 = c2.create_rectangle(1121, 48, 1126, 68,
                      fill='green',
                      tags="c_33_36",
                            activefill='orange')
c_32_35 = c2.create_rectangle(1121, 121, 1126, 141,
                      fill='green',
                      tags="c_32_35",
                            activefill='orange')
c_31_34 = c2.create_rectangle(1121, 194, 1126, 214,
                      fill='green',
                      tags="c_31_34",
                            activefill='orange')

tri = c2.create_rectangle(598, 24, 641, 92,
                          fill="red",
                          tags="tri",
                           activefill='orange')
ttri = c2.create_text(620, 58,
                      text='3',
                      font=("Bodoni MT Black", 20),
                      fill='white')
dva = c2.create_rectangle(598, 97, 641, 165,
                          fill="black",
                          tags="dva",
                           activefill='orange')
ddva = c2.create_text(620, 131,
                      text='2',
                      font=("Bodoni MT Black", 20),
                      fill='white')
jedan = c2.create_rectangle(598, 170, 641, 238,
                            fill="red",
                            tags="jedan",
                           activefill='orange')
jjedan = c2.create_text(620, 204,
                      text='1',
                      font=("Bodoni MT Black", 20),
                      fill='white')
sest = c2.create_rectangle(646, 24, 689, 92,
                          fill="black",
                          tags="sest",
                           activefill='orange')
ssest = c2.create_text(668, 58,
                      text='6',
                      font=("Bodoni MT Black", 20),
                      fill='white')
pet = c2.create_rectangle(646, 97, 689, 165,
                          fill="red",
                          tags="pet",
                           activefill='orange')
ppet = c2.create_text(668, 131,
                      text='5',
                      font=("Bodoni MT Black", 20),
                      fill='white')
cetiri = c2.create_rectangle(646, 170, 689, 238,
                            fill="black",
                            tags="cetiri",
                           activefill='orange')
ccetiri = c2.create_text(668, 204,
                      text='4',
                      font=("Bodoni MT Black", 20),
                      fill='white')
devet = c2.create_rectangle(694, 24, 737, 92,
                          fill="red",
                          tags="devet",
                           activefill='orange')
ddevet = c2.create_text(716, 58,
                      text='9',
                      font=("Bodoni MT Black", 20),
                      fill='white')
osam = c2.create_rectangle(694, 97, 737, 165,
                          fill="black",
                          tags="osam",
                           activefill='orange')
oosam = c2.create_text(716, 131,
                      text='8',
                      font=("Bodoni MT Black", 20),
                      fill='white')
sedam = c2.create_rectangle(694, 170, 737, 238,
                            fill="red",
                            tags="sedam",
                           activefill='orange')
ssedam = c2.create_text(716, 204,
                      text='7',
                      font=("Bodoni MT Black", 20),
                      fill='white')
dvanaest = c2.create_rectangle(742, 24, 785, 92,
                          fill="red",
                          tags="dvanaest",
                           activefill='orange')
ddvanaest = c2.create_text(764, 58,
                      text='12',
                      font=("Bodoni MT Black", 20),
                      fill='white')
jedanaest = c2.create_rectangle(742, 97, 785, 165,
                          fill="black",
                          tags="jedanaest",
                           activefill='orange')
jjedanaest = c2.create_text(764, 131,
                      text='11',
                      font=("Bodoni MT Black", 20),
                      fill='white')
deset = c2.create_rectangle(742, 170, 785, 238,
                            fill="black",
                            tags="deset",
                           activefill='orange')
ddeset = c2.create_text(764, 204,
                      text='10',
                      font=("Bodoni MT Black", 20),
                      fill='white')
petnaest = c2.create_rectangle(790, 24, 833, 92,
                          fill="black",
                          tags="petnaest",
                           activefill='orange')
ppetnaest = c2.create_text(812, 58,
                      text='15',
                      font=("Bodoni MT Black", 20),
                      fill='white')
cetrnaest = c2.create_rectangle(790, 97, 833, 165,
                          fill="red",
                          tags="cetrnaest",
                           activefill='orange')
ccetrnaest = c2.create_text(812, 131,
                      text='14',
                      font=("Bodoni MT Black", 20),
                      fill='white')
trinaest = c2.create_rectangle(790, 170, 833, 238,
                            fill="black",
                            tags="trinaest",
                           activefill='orange')
ttrinaest = c2.create_text(812, 204,
                      text='13',
                      font=("Bodoni MT Black", 20),
                      fill='white')
osamnaest = c2.create_rectangle(838, 24, 881, 92,
                          fill="red",
                          tags="osamnaest",
                           activefill='orange')
oosamnaest = c2.create_text(860, 58,
                      text='18',
                      font=("Bodoni MT Black", 20),
                      fill='white')
sedamnaest = c2.create_rectangle(838, 97, 881, 165,
                          fill="black",
                          tags="sedamnaest",
                           activefill='orange')
ssedamnaest = c2.create_text(860, 131,
                      text='17',
                      font=("Bodoni MT Black", 20),
                      fill='white')
sesnaest = c2.create_rectangle(838, 170, 881, 238,
                            fill="red",
                            tags="sesnaest",
                           activefill='orange')
ssesnaest = c2.create_text(860, 204,
                      text='16',
                      font=("Bodoni MT Black", 20),
                      fill='white')
d_jedan = c2.create_rectangle(886, 24, 929, 92,
                          fill="red",
                          tags="d_jedan",
                           activefill='orange')
dd_jedan = c2.create_text(908, 58,
                      text='21',
                      font=("Bodoni MT Black", 20),
                      fill='white')
d_nula = c2.create_rectangle(886, 97, 929, 165,
                          fill="black",
                          tags="d_nula",
                           activefill='orange')
dd_nula = c2.create_text(908, 131,
                      text='20',
                      font=("Bodoni MT Black", 20),
                      fill='white')
devetnaest = c2.create_rectangle(886, 170, 929, 238,
                            fill="red",
                            tags="devetnaest",
                           activefill='orange')
ddevetnaest = c2.create_text(908, 204,
                      text='19',
                      font=("Bodoni MT Black", 20),
                      fill='white')
d_cetiri = c2.create_rectangle(934, 24, 977, 92,
                          fill="black",
                          tags="d_cetiri",
                           activefill='orange')
dd_cetiri = c2.create_text(956, 58,
                      text='24',
                      font=("Bodoni MT Black", 20),
                      fill='white')
d_tri = c2.create_rectangle(934, 97, 977, 165,
                          fill="red",
                          tags="d_tri",
                           activefill='orange')
dd_tri = c2.create_text(956, 131,
                      text='23',
                      font=("Bodoni MT Black", 20),
                      fill='white')
d_dva = c2.create_rectangle(934, 170, 977, 238,
                            fill="black",
                            tags="d_dva",
                           activefill='orange')
dd_dva = c2.create_text(956, 204,
                      text='22',
                      font=("Bodoni MT Black", 20),
                      fill='white')
d_sedam = c2.create_rectangle(982, 24, 1025, 92,
                          fill="red",
                          tags="d_sedam",
                           activefill='orange')
dd_sedam = c2.create_text(1004, 58,
                      text='27',
                      font=("Bodoni MT Black", 20),
                      fill='white')
d_sest = c2.create_rectangle(982, 97, 1025, 165,
                          fill="black",
                          tags="d_sest",
                           activefill='orange')
dd_sest = c2.create_text(1004, 131,
                      text='26',
                      font=("Bodoni MT Black", 20),
                      fill='white')
d_pet = c2.create_rectangle(982, 170, 1025, 238,
                            fill="red",
                            tags="d_pet",
                           activefill='orange')
dd_pet = c2.create_text(1004, 204,
                      text='25',
                      font=("Bodoni MT Black", 20),
                      fill='white')
t_nula = c2.create_rectangle(1030, 24, 1073, 92,
                          fill="red",
                          tags="t_nula",
                           activefill='orange')
tt_nula = c2.create_text(1052, 58,
                      text='30',
                      font=("Bodoni MT Black", 20),
                      fill='white')
d_devet = c2.create_rectangle(1030, 97, 1073, 165,
                          fill="black",
                          tags="d_devet",
                           activefill='orange')
dd_devet = c2.create_text(1052, 131,
                      text='29',
                      font=("Bodoni MT Black", 20),
                      fill='white')
d_osam = c2.create_rectangle(1030, 170, 1073, 238,
                            fill="black",
                            tags="d_osam",
                           activefill='orange')
dd_osam = c2.create_text(1052, 204,
                      text='28',
                      font=("Bodoni MT Black", 20),
                      fill='white')
t_tri = c2.create_rectangle(1078, 24, 1121, 92,
                          fill="black",
                          tags="t_tri",
                           activefill='orange')
tt_tri = c2.create_text(1100, 58,
                      text='33',
                      font=("Bodoni MT Black", 20),
                      fill='white')
t_dva = c2.create_rectangle(1078, 97, 1121, 165,
                          fill="red",
                          tags="t_dva",
                           activefill='orange')
tt_dva = c2.create_text(1100, 131,
                      text='32',
                      font=("Bodoni MT Black", 20),
                      fill='white')
t_jedan = c2.create_rectangle(1078, 170, 1121, 238,
                            fill="black",
                            tags="t_jedan",
                           activefill='orange')
tt_jedan = c2.create_text(1100, 204,
                      text='31',
                      font=("Bodoni MT Black", 20),
                      fill='white')
t_sest = c2.create_rectangle(1126, 24, 1169, 92,
                          fill="red",
                          tags="t_sest",
                           activefill='orange')
tt_sest = c2.create_text(1148, 58,
                      text='36',
                      font=("Bodoni MT Black", 20),
                      fill='white')
t_pet = c2.create_rectangle(1126, 97, 1169, 165,
                          fill="black",
                          tags="t_pet",
                           activefill='orange')
tt_pet = c2.create_text(1148, 131,
                      text='35',
                      font=("Bodoni MT Black", 20),
                      fill='white')
t_cetiri = c2.create_rectangle(1126, 170, 1169, 238,
                            fill="red",
                            tags="t_cetiri",
                           activefill='orange')
tt_cetiri = c2.create_text(1148, 204,
                      text='34',
                      font=("Bodoni MT Black", 20),
                      fill='white')
treca_tri = c2.create_rectangle(1174, 24, 1217, 92,
                          fill="green",
                          tags="treca_tri",
                           activefill='orange')
ttreca_tri = c2.create_text(1196, 58+2,
                      text='2:1',
                      font=("Bodoni MT Black", 20),
                      fill='white',
                      angle=270)
druga_tri = c2.create_rectangle(1174, 97, 1217, 165,
                          fill="green",
                          tags="druga_tri",
                           activefill='orange')
ddruga_tri = c2.create_text(1196, 131+2,
                      text='2:1',
                      font=("Bodoni MT Black", 20),
                      fill='white',
                      angle=270)
prva_tri = c2.create_rectangle(1174, 170, 1217, 238,
                            fill="green",
                            tags="prva_tri",
                           activefill='orange')
pprva_tri = c2.create_text(1196, 204+2,
                      text='2:1',
                      tags='pprva_tri',
                      font=("Bodoni MT Black", 20),
                      fill='white',
                      angle=270)


c_2_3 = c2.create_rectangle(610, 92, 630, 97,
                      fill='green',
                      tags="c_2_3",
                           activefill='orange')
c_1_2 = c2.create_rectangle(610, 165, 630, 170,
                      fill='green',
                      tags="c_1_2",
                           activefill='orange')
c_5_6 = c2.create_rectangle(658, 92, 678, 97,
                      fill='green',
                      tags="c_5_6",
                           activefill='orange')
c_4_5 = c2.create_rectangle(658, 165, 678, 170,
                      fill='green',
                      tags="c_4_5",
                           activefill='orange')
c_8_9 = c2.create_rectangle(706, 92, 726, 97,
                      fill='green',
                      tags="c_8_9",
                           activefill='orange')
c_7_8 = c2.create_rectangle(706, 165, 726, 170,
                      fill='green',
                      tags="c_7_8",
                           activefill='orange')
c_11_12 = c2.create_rectangle(754, 92, 774, 97,
                      fill='green',
                      tags="c_11_12",
                           activefill='orange')
c_10_11 = c2.create_rectangle(754, 165, 774, 170,
                      fill='green',
                      tags="c_10_11",
                           activefill='orange')
c_14_15 = c2.create_rectangle(802, 92, 822, 97,
                      fill='green',
                      tags="c_14_15",
                           activefill='orange')
c_13_14 = c2.create_rectangle(802, 165, 822, 170,
                      fill='green',
                      tags="c_13_14",
                           activefill='orange')
c_17_18 = c2.create_rectangle(850, 92, 870, 97,
                      fill='green',
                      tags="c_17_18",
                           activefill='orange')
c_16_17 = c2.create_rectangle(850, 165, 870, 170,
                      fill='green',
                      tags="c_16_17",
                           activefill='orange')
c_20_21 = c2.create_rectangle(898, 92, 918, 97,
                      fill='green',
                      tags="c_20_21",
                           activefill='orange')
c_19_20 = c2.create_rectangle(898, 165, 918, 170,
                      fill='green',
                      tags="c_19_20",
                           activefill='orange')
c_23_24 = c2.create_rectangle(946, 92, 966, 97,
                      fill='green',
                      tags="c_23_24",
                           activefill='orange')
c_22_23 = c2.create_rectangle(946, 165, 966, 170,
                      fill='green',
                      tags="c_22_23",
                           activefill='orange')
c_26_27 = c2.create_rectangle(994, 92, 1014, 97,
                      fill='green',
                      tags="c_26_27",
                           activefill='orange')
c_25_26 = c2.create_rectangle(994, 165, 1014, 170,
                      fill='green',
                      tags="c_25_26",
                           activefill='orange')
c_29_30 = c2.create_rectangle(1042, 92, 1062, 97,
                      fill='green',
                      tags="c_29_30",
                           activefill='orange')
c_28_29 = c2.create_rectangle(1042, 165, 1062, 170,
                      fill='green',
                      tags="c_28_29",
                           activefill='orange')
c_32_33 = c2.create_rectangle(1090, 92, 1110, 97,
                      fill='green',
                      tags="c_32_33",
                           activefill='orange')
c_31_32 = c2.create_rectangle(1090, 165, 1110, 170,
                      fill='green',
                      tags="c_31_32",
                           activefill='orange')
c_35_36 = c2.create_rectangle(1138, 92, 1158, 97,
                      fill='green',
                      tags="c_35_36",
                           activefill='orange')
c_34_35 = c2.create_rectangle(1138, 165, 1158, 170,
                      fill='green',
                      tags="c_34_35",
                           activefill='orange')


c_1_2_3 = c2.create_rectangle(610, 238, 630, 243,
                      fill='green',
                      tags="c_1_2_3",
                           activefill='orange')
c_4_5_6 = c2.create_rectangle(658, 238, 678, 243,
                      fill='green',
                      tags="c_4_5_6",
                           activefill='orange')
c_7_8_9 = c2.create_rectangle(706, 238, 726, 243,
                      fill='green',
                      tags="c_7_8_9",
                           activefill='orange')
c_10_11_12 = c2.create_rectangle(754, 238, 774, 243,
                      fill='green',
                      tags="c_10_11_12",
                           activefill='orange')
c_13_14_15 = c2.create_rectangle(802, 238, 822, 243,
                      fill='green',
                      tags="c_13_14_15",
                           activefill='orange')
c_16_17_18 = c2.create_rectangle(850, 238, 870, 243,
                      fill='green',
                      tags="c_16_17_18",
                           activefill='orange')
c_19_20_21 = c2.create_rectangle(898, 238, 918, 243,
                      fill='green',
                      tags="c_19_20_21",
                           activefill='orange')
c_22_23_24 = c2.create_rectangle(946, 238, 966, 243,
                      fill='green',
                      tags="c_22_23_24",
                           activefill='orange')
c_25_26_27 = c2.create_rectangle(994, 238, 1014, 243,
                      fill='green',
                      tags="c_25_26_27",
                           activefill='orange')
c_28_29_30 = c2.create_rectangle(1042, 238, 1062, 243,
                      fill='green',
                      tags="c_28_29_30",
                           activefill='orange')
c_31_32_33 = c2.create_rectangle(1090, 238, 1110, 243,
                      fill='green',
                      tags="c_31_32_33",
                           activefill='orange')
c_34_35_36 = c2.create_rectangle(1138, 238, 1158, 243,
                      fill='green',
                      tags="c_34_35_36",
                           activefill='orange')


c_0_1_2_3 = c2.create_rectangle(586, 238, 606, 243,
                      fill='green',
                      tags="c_0_1_2_3",
                           activefill='orange')
c_1_2_3_4_5_6 = c2.create_rectangle(634, 238, 654, 243,
                      fill='green',
                      tags="c_1_2_3_4_5_6",
                           activefill='orange')
c_4_5_6_7_8_9 = c2.create_rectangle(682, 238, 702, 243,
                      fill='green',
                      tags="c_4_5_6_7_8_9",
                           activefill='orange')
c_7_8_9_10_11_12 = c2.create_rectangle(730, 238, 750, 243,
                      fill='green',
                      tags="c_7_8_9_10_11_12",
                           activefill='orange')
c_10_11_12_13_14_15 = c2.create_rectangle(778, 238, 798, 243,
                      fill='green',
                      tags="c_10_11_12_13_14_15",
                           activefill='orange')
c_13_14_15_16_17_18 = c2.create_rectangle(826, 238, 846, 243,
                      fill='green',
                      tags="c_13_14_15_16_17_18",
                           activefill='orange')
c_16_17_18_19_20_21 = c2.create_rectangle(874, 238, 894, 243,
                      fill='green',
                      tags="c_16_17_18_19_20_21",
                           activefill='orange')
c_19_20_21_22_23_24 = c2.create_rectangle(922, 238, 942, 243,
                      fill='green',
                      tags="c_19_20_21_22_23_24",
                           activefill='orange')
c_22_23_24_25_26_27 = c2.create_rectangle(970, 238, 990, 243,
                      fill='green',
                      tags="c_22_23_24_25_26_27",
                           activefill='orange')
c_25_26_27_28_29_30 = c2.create_rectangle(1018, 238, 1038, 243,
                      fill='green',
                      tags="c_25_26_27_28_29_30",
                           activefill='orange')
c_28_29_30_31_32_33 = c2.create_rectangle(1066, 238, 1086, 243,
                      fill='green',
                      tags="c_28_29_30_31_32_33",
                           activefill='orange')
c_31_32_33_34_35_36 = c2.create_rectangle(1114, 238, 1134, 243,
                      fill='green',
                      tags="c_31_32_33_34_35_36",
                           activefill='orange')


c_prva = c2.create_rectangle(634, 92, 654, 97,
                      fill='green',
                      tags="c_prva",
                           activefill='orange')
c_druga = c2.create_rectangle(634, 165, 654, 170,
                      fill='green',
                      tags="c_druga",
                           activefill='orange')
c_treca = c2.create_rectangle(682, 92, 702, 97,
                      fill='green',
                      tags="c_treca",
                           activefill='orange')
c_cetvrta = c2.create_rectangle(682, 165, 702, 170,
                      fill='green',
                      tags="c_cetvrta",
                           activefill='orange')
c_peta = c2.create_rectangle(730, 92, 750, 97,
                      fill='green',
                      tags="c_peta",
                           activefill='orange')
c_sesta = c2.create_rectangle(730, 165, 750, 170,
                      fill='green',
                      tags="c_sesta",
                           activefill='orange')
c_sedma = c2.create_rectangle(778, 92, 798, 97,
                      fill='green',
                      tags="c_sedma",
                           activefill='orange')
c_osma = c2.create_rectangle(778, 165, 798, 170,
                      fill='green',
                      tags="c_osma",
                           activefill='orange')
c_deveta = c2.create_rectangle(826, 92, 846, 97,
                      fill='green',
                      tags="c_deveta",
                           activefill='orange')
c_deseta = c2.create_rectangle(826, 165, 846, 170,
                      fill='green',
                      tags="c_deseta",
                           activefill='orange')
c_jedanaesta = c2.create_rectangle(874, 92, 894, 97,
                      fill='green',
                      tags="c_jedanaesta",
                           activefill='orange')
c_dvanaesta = c2.create_rectangle(874, 165, 894, 170,
                      fill='green',
                      tags="c_dvanaesta",
                           activefill='orange')
c_trinaesta = c2.create_rectangle(922, 92, 942, 97,
                      fill='green',
                      tags="c_trinaesta",
                           activefill='orange')
c_cetrnaesta = c2.create_rectangle(922, 165, 942, 170,
                      fill='green',
                      tags="c_cetrnaesta",
                           activefill='orange')
c_petnaesta = c2.create_rectangle(970, 92, 990, 97,
                      fill='green',
                      tags="c_petnaesta",
                           activefill='orange')
c_sesnaesta = c2.create_rectangle(970, 165, 990, 170,
                      fill='green',
                      tags="c_sesnaesta",
                           activefill='orange')
c_sedamnaesta = c2.create_rectangle(1018, 92, 1038, 97,
                      fill='green',
                      tags="c_sedamnaesta",
                           activefill='orange')
c_osamnaesta = c2.create_rectangle(1018, 165, 1038, 170,
                      fill='green',
                      tags="c_osamnaesta",
                           activefill='orange')
c_devetnaesta = c2.create_rectangle(1066, 92, 1086, 97,
                      fill='green',
                      tags="c_devetnaesta",
                           activefill='orange')
c_dvadeseta = c2.create_rectangle(1066, 165, 1086, 170,
                      fill='green',
                      tags="c_dvadeseta",
                           activefill='orange')
c_dvadesetprva = c2.create_rectangle(1114, 92, 1134, 97,
                      fill='green',
                      tags="c_dvadesetprva",
                           activefill='orange')
c_dvadesetdruga = c2.create_rectangle(1114, 165, 1134, 170,
                      fill='green',
                      tags="c_dvadesetadruga",
                           activefill='orange')
prva_trecina = c2.create_rectangle(598, 243, 785, 286,
                           fill="green",
                           tags="prva_trecina",
                           activefill='orange')
prva_trec = c2.create_text(691, 264,
                      text='1st 12',
                      font=("Bodoni MT Black", 20),
                      fill='white')
druga_trecina = c2.create_rectangle(790, 243, 977, 286,
                           fill="green",
                           tags="druga_trecina",
                           activefill='orange')
druga_trec = c2.create_text(883, 264,
                      text='2nd 12',
                      font=("Bodoni MT Black", 20),
                      fill='white')
treca_trecina = c2.create_rectangle(982, 243, 1169, 286,
                           fill="green",
                           tags="treca_trecina",
                           activefill='orange')
treca_trec = c2.create_text(1075, 264,
                      text='3rd 12',
                      font=("Bodoni MT Black", 20),
                      fill='white')
prvih_18 = c2.create_rectangle(598, 291, 691, 334,
                           fill="green",
                           tags="prvih_18",
                           activefill='orange')
prvih_18_t = c2.create_text(644, 312,
                      text='1-18',
                      font=("Bodoni MT Black", 20),
                      fill='white')
drugih_18 = c2.create_rectangle(1078, 291, 1169, 334,
                           fill="green",
                           tags="drugih_18",
                           activefill='orange')
drugih_18_t = c2.create_text(1123, 312,
                      text='19-36',
                      font=("Bodoni MT Black", 20),
                      fill='white')
even = c2.create_rectangle(696, 291, 785, 334,
                           fill="green",
                           tags="even",
                           activefill='orange')
even_t = c2.create_text(741, 312,
                      text='EVEN',
                      font=("Bodoni MT Black", 20),
                      fill='white')
odd = c2.create_rectangle(982, 291, 1073, 334,
                           fill="green",
                           tags="odd",
                           activefill='orange')
odd_t = c2.create_text(1027, 312,
                      text='ODD',
                      font=("Bodoni MT Black", 20),
                      fill='white')
crveni = c2.create_rectangle(790, 291, 881, 334,
                           fill="red",
                           tags="crveni",
                             activefill='orange')
crni = c2.create_rectangle(886, 291, 977, 334,
                           fill="black",
                           tags="crni",
                           activefill='orange')


c2.tag_bind(nula, '<Button-1>', nula_klik)
c2.tag_bind(nnula, '<Button-1>', nula_klik)
c2.tag_bind(jedan, '<Button-1>', jedan_klik)
c2.tag_bind(jjedan, '<Button-1>', jedan_klik)
c2.tag_bind(dva, '<Button-1>', dva_klik)
c2.tag_bind(ddva, '<Button-1>', dva_klik)
c2.tag_bind(tri, '<Button-1>', tri_klik)
c2.tag_bind(ttri, '<Button-1>', tri_klik)
c2.tag_bind(cetiri, '<Button-1>', cetiri_klik)
c2.tag_bind(ccetiri, '<Button-1>', cetiri_klik)
c2.tag_bind(pet, '<Button-1>', pet_klik)
c2.tag_bind(ppet, '<Button-1>', pet_klik)
c2.tag_bind(sest, '<Button-1>', sest_klik)
c2.tag_bind(ssest, '<Button-1>', sest_klik)
c2.tag_bind(sedam, '<Button-1>', sedam_klik)
c2.tag_bind(ssedam, '<Button-1>', sedam_klik)
c2.tag_bind(osam, '<Button-1>', osam_klik)
c2.tag_bind(oosam, '<Button-1>', osam_klik)
c2.tag_bind(devet, '<Button-1>', devet_klik)
c2.tag_bind(ddevet, '<Button-1>', devet_klik)
c2.tag_bind(deset, '<Button-1>', deset_klik)
c2.tag_bind(ddeset, '<Button-1>', deset_klik)
c2.tag_bind(jedanaest, '<Button-1>', jedanaest_klik)
c2.tag_bind(jjedanaest, '<Button-1>', jedanaest_klik)
c2.tag_bind(dvanaest, '<Button-1>', dvanaest_klik)
c2.tag_bind(ddvanaest, '<Button-1>', dvanaest_klik)
c2.tag_bind(trinaest, '<Button-1>', trinaest_klik)
c2.tag_bind(ttrinaest, '<Button-1>', trinaest_klik)
c2.tag_bind(cetrnaest, '<Button-1>', cetrnaest_klik)
c2.tag_bind(ccetrnaest, '<Button-1>', cetrnaest_klik)
c2.tag_bind(petnaest, '<Button-1>', petnaest_klik)
c2.tag_bind(ppetnaest, '<Button-1>', petnaest_klik)
c2.tag_bind(sesnaest, '<Button-1>', sesnaest_klik)
c2.tag_bind(ssesnaest, '<Button-1>', sesnaest_klik)
c2.tag_bind(sedamnaest, '<Button-1>', sedamnaest_klik)
c2.tag_bind(ssedamnaest, '<Button-1>', sedamnaest_klik)
c2.tag_bind(osamnaest, '<Button-1>', osamnaest_klik)
c2.tag_bind(oosamnaest, '<Button-1>', osamnaest_klik)
c2.tag_bind(devetnaest, '<Button-1>', devetnaest_klik)
c2.tag_bind(ddevetnaest, '<Button-1>', devetnaest_klik)
c2.tag_bind(d_nula, '<Button-1>', d_nula_klik)
c2.tag_bind(dd_nula, '<Button-1>', d_nula_klik)
c2.tag_bind(d_jedan, '<Button-1>', d_jedan_klik)
c2.tag_bind(dd_jedan, '<Button-1>', d_jedan_klik)
c2.tag_bind(d_dva, '<Button-1>', d_dva_klik)
c2.tag_bind(dd_dva, '<Button-1>', d_dva_klik)
c2.tag_bind(d_tri, '<Button-1>', d_tri_klik)
c2.tag_bind(dd_tri, '<Button-1>', d_tri_klik)
c2.tag_bind(d_cetiri, '<Button-1>', d_cetiri_klik)
c2.tag_bind(dd_cetiri, '<Button-1>', d_cetiri_klik)
c2.tag_bind(d_pet, '<Button-1>', d_pet_klik)
c2.tag_bind(dd_pet, '<Button-1>', d_pet_klik)
c2.tag_bind(d_sest, '<Button-1>', d_sest_klik)
c2.tag_bind(dd_sest, '<Button-1>', d_sest_klik)
c2.tag_bind(d_sedam, '<Button-1>', d_sedam_klik)
c2.tag_bind(dd_sedam, '<Button-1>', d_sedam_klik)
c2.tag_bind(d_osam, '<Button-1>', d_osam_klik)
c2.tag_bind(dd_osam, '<Button-1>', d_osam_klik)
c2.tag_bind(d_devet, '<Button-1>', d_devet_klik)
c2.tag_bind(dd_devet, '<Button-1>', d_devet_klik)
c2.tag_bind(t_nula, '<Button-1>', t_nula_klik)
c2.tag_bind(tt_nula, '<Button-1>', t_nula_klik)
c2.tag_bind(t_jedan, '<Button-1>', t_jedan_klik)
c2.tag_bind(tt_jedan, '<Button-1>', t_jedan_klik)
c2.tag_bind(t_dva, '<Button-1>', t_dva_klik)
c2.tag_bind(tt_dva, '<Button-1>', t_dva_klik)
c2.tag_bind(t_tri, '<Button-1>', t_tri_klik)
c2.tag_bind(tt_tri, '<Button-1>', t_tri_klik)
c2.tag_bind(t_cetiri, '<Button-1>', t_cetiri_klik)
c2.tag_bind(tt_cetiri, '<Button-1>', t_cetiri_klik)
c2.tag_bind(t_pet, '<Button-1>', t_pet_klik)
c2.tag_bind(tt_pet, '<Button-1>', t_pet_klik)
c2.tag_bind(t_sest, '<Button-1>', t_sest_klik)
c2.tag_bind(tt_sest, '<Button-1>', t_sest_klik)



c2.tag_bind(c_prva, '<Button-1>', c_prva_klik)
c2.tag_bind(c_druga, '<Button-1>', c_druga_klik)
c2.tag_bind(c_treca, '<Button-1>', c_treca_klik)
c2.tag_bind(c_cetvrta, '<Button-1>', c_cetvrta_klik)
c2.tag_bind(c_peta, '<Button-1>', c_peta_klik)
c2.tag_bind(c_sesta, '<Button-1>', c_sesta_klik)
c2.tag_bind(c_sedma, '<Button-1>', c_sedma_klik)
c2.tag_bind(c_osma, '<Button-1>', c_osma_klik)
c2.tag_bind(c_deveta, '<Button-1>', c_deveta_klik)
c2.tag_bind(c_deseta, '<Button-1>', c_deseta_klik)
c2.tag_bind(c_jedanaesta, '<Button-1>', c_jedanaesta_klik)
c2.tag_bind(c_dvanaesta, '<Button-1>', c_dvanaesta_klik)
c2.tag_bind(c_trinaesta, '<Button-1>', c_trinaesta_klik)
c2.tag_bind(c_cetrnaesta, '<Button-1>', c_cetrnaesta_klik)
c2.tag_bind(c_petnaesta, '<Button-1>', c_petnaesta_klik)
c2.tag_bind(c_sesnaesta, '<Button-1>', c_sesnaesta_klik)
c2.tag_bind(c_sedamnaesta, '<Button-1>', c_sedamnaesta_klik)
c2.tag_bind(c_osamnaesta, '<Button-1>', c_osamnaesta_klik)
c2.tag_bind(c_devetnaesta, '<Button-1>', c_devetnaesta_klik)
c2.tag_bind(c_dvadeseta, '<Button-1>', c_dvadeseta_klik)
c2.tag_bind(c_dvadesetprva, '<Button-1>', c_dvadesetprva_klik)
c2.tag_bind(c_dvadesetdruga, '<Button-1>', c_dvadesetdruga_klik)


c2.tag_bind(prva_tri, '<Enter>', prva_tri_hov1)
c2.tag_bind(prva_tri, '<Leave>', prva_tri_hov2)
c2.tag_bind(druga_tri, '<Enter>', druga_tri_hov1)
c2.tag_bind(druga_tri, '<Leave>', druga_tri_hov2)
c2.tag_bind(treca_tri, '<Enter>', treca_tri_hov1)
c2.tag_bind(treca_tri, '<Leave>', treca_tri_hov2)

c2.tag_bind(prva_trecina, '<Enter>', prva_trecina_hov1)
c2.tag_bind(prva_trecina, '<Leave>', prva_trecina_hov2)
c2.tag_bind(druga_trecina, '<Enter>', druga_trecina_hov1)
c2.tag_bind(druga_trecina, '<Leave>', druga_trecina_hov2)
c2.tag_bind(treca_trecina, '<Enter>', treca_trecina_hov1)
c2.tag_bind(treca_trecina, '<Leave>', treca_trecina_hov2)

c2.tag_bind(prva_tri, '<Button-1>', prva_tri_klik)
c2.tag_bind(pprva_tri, '<Button-1>', prva_tri_klik)
c2.tag_bind(druga_tri, '<Button-1>', druga_tri_klik)
c2.tag_bind(ddruga_tri, '<Button-1>', druga_tri_klik)
c2.tag_bind(treca_tri, '<Button-1>', treca_tri_klik)
c2.tag_bind(ttreca_tri, '<Button-1>', treca_tri_klik)


c2.tag_bind(crveni, '<Button-1>', crveni_klik)
c2.tag_bind(crni, '<Button-1>', crni_klik)
c2.tag_bind(prva_trecina, '<Button-1>', prva_trecina_klik)
c2.tag_bind(prva_trec, '<Button-1>', prva_trecina_klik)
c2.tag_bind(druga_trecina, '<Button-1>', druga_trecina_klik)
c2.tag_bind(druga_trec, '<Button-1>', druga_trecina_klik)
c2.tag_bind(treca_trecina, '<Button-1>', treca_trecina_klik)
c2.tag_bind(treca_trec, '<Button-1>', treca_trecina_klik)
c2.tag_bind(prvih_18, '<Button-1>', prvih_18_klik)
c2.tag_bind(prvih_18_t, '<Button-1>', prvih_18_klik)
c2.tag_bind(drugih_18, '<Button-1>', drugih_18_klik)
c2.tag_bind(drugih_18_t, '<Button-1>', drugih_18_klik)
c2.tag_bind(even, '<Button-1>', even_klik)
c2.tag_bind(even_t, '<Button-1>', even_klik)
c2.tag_bind(odd, '<Button-1>', odd_klik)
c2.tag_bind(odd_t, '<Button-1>', odd_klik)


c2.tag_bind(c_1_2_3, '<Button-1>', c_1_2_3_klik)
c2.tag_bind(c_4_5_6, '<Button-1>', c_4_5_6_klik)
c2.tag_bind(c_7_8_9, '<Button-1>', c_7_8_9_klik)
c2.tag_bind(c_10_11_12, '<Button-1>', c_10_11_12_klik)
c2.tag_bind(c_13_14_15, '<Button-1>', c_13_14_15_klik)
c2.tag_bind(c_16_17_18, '<Button-1>', c_16_17_18_klik)
c2.tag_bind(c_19_20_21, '<Button-1>', c_19_20_21_klik)
c2.tag_bind(c_22_23_24, '<Button-1>', c_22_23_24_klik)
c2.tag_bind(c_25_26_27, '<Button-1>', c_25_26_27_klik)
c2.tag_bind(c_28_29_30, '<Button-1>', c_28_29_30_klik)
c2.tag_bind(c_31_32_33, '<Button-1>', c_31_32_33_klik)
c2.tag_bind(c_34_35_36, '<Button-1>', c_34_35_36_klik)
c2.tag_bind(c_1_2_3_4_5_6, '<Button-1>', c_1_2_3_4_5_6_klik)
c2.tag_bind(c_4_5_6_7_8_9, '<Button-1>', c_4_5_6_7_8_9_klik)
c2.tag_bind(c_7_8_9_10_11_12, '<Button-1>', c_7_8_9_10_11_12_klik)
c2.tag_bind(c_10_11_12_13_14_15, '<Button-1>', c_10_11_12_13_14_15_klik)
c2.tag_bind(c_13_14_15_16_17_18, '<Button-1>', c_13_14_15_16_17_18_klik)
c2.tag_bind(c_16_17_18_19_20_21, '<Button-1>', c_16_17_18_19_20_21_klik)
c2.tag_bind(c_19_20_21_22_23_24, '<Button-1>', c_19_20_21_22_23_24_klik)
c2.tag_bind(c_22_23_24_25_26_27, '<Button-1>', c_22_23_24_25_26_27_klik)
c2.tag_bind(c_25_26_27_28_29_30, '<Button-1>', c_25_26_27_28_29_30_klik)
c2.tag_bind(c_28_29_30_31_32_33, '<Button-1>', c_28_29_30_31_32_33_klik)
c2.tag_bind(c_31_32_33_34_35_36, '<Button-1>', c_31_32_33_34_35_36_klik)
c2.tag_bind(c_0_1_2_3, '<Button-1>', c_0_1_2_3_klik)
c2.tag_bind(c_1_2, '<Button-1>', c_1_2_klik)
c2.tag_bind(c_2_3, '<Button-1>', c_2_3_klik)
c2.tag_bind(c_4_5, '<Button-1>', c_4_5_klik)
c2.tag_bind(c_5_6, '<Button-1>', c_5_6_klik)
c2.tag_bind(c_7_8, '<Button-1>', c_7_8_klik)
c2.tag_bind(c_8_9, '<Button-1>', c_8_9_klik)
c2.tag_bind(c_10_11, '<Button-1>', c_10_11_klik)
c2.tag_bind(c_11_12, '<Button-1>', c_11_12_klik)
c2.tag_bind(c_13_14, '<Button-1>', c_13_14_klik)
c2.tag_bind(c_14_15, '<Button-1>', c_14_15_klik)
c2.tag_bind(c_16_17, '<Button-1>', c_16_17_klik)
c2.tag_bind(c_17_18, '<Button-1>', c_17_18_klik)
c2.tag_bind(c_19_20, '<Button-1>', c_19_20_klik)
c2.tag_bind(c_20_21, '<Button-1>', c_20_21_klik)
c2.tag_bind(c_22_23, '<Button-1>', c_22_23_klik)
c2.tag_bind(c_23_24, '<Button-1>', c_23_24_klik)
c2.tag_bind(c_25_26, '<Button-1>', c_25_26_klik)
c2.tag_bind(c_26_27, '<Button-1>', c_26_27_klik)
c2.tag_bind(c_28_29, '<Button-1>', c_28_29_klik)
c2.tag_bind(c_29_30, '<Button-1>', c_29_30_klik)
c2.tag_bind(c_31_32, '<Button-1>', c_31_32_klik)
c2.tag_bind(c_32_33, '<Button-1>', c_32_33_klik)
c2.tag_bind(c_34_35, '<Button-1>', c_34_35_klik)
c2.tag_bind(c_35_36, '<Button-1>', c_35_36_klik)
c2.tag_bind(c_0_1_2, '<Button-1>', c_0_1_2_klik)
c2.tag_bind(c_0_2, '<Button-1>', c_0_2_klik)
c2.tag_bind(c_0_1, '<Button-1>', c_0_1_klik)
c2.tag_bind(c_0_3, '<Button-1>', c_0_3_klik)
c2.tag_bind(c_0_2_3, '<Button-1>', c_0_2_3_klik)
c2.tag_bind(c_1_4, '<Button-1>', c_1_4_klik)
c2.tag_bind(c_2_5, '<Button-1>', c_2_5_klik)
c2.tag_bind(c_3_6, '<Button-1>', c_3_6_klik)
c2.tag_bind(c_4_7, '<Button-1>', c_4_7_klik)
c2.tag_bind(c_5_8, '<Button-1>', c_5_8_klik)
c2.tag_bind(c_6_9, '<Button-1>', c_6_9_klik)
c2.tag_bind(c_7_10, '<Button-1>', c_7_10_klik)
c2.tag_bind(c_8_11, '<Button-1>', c_8_11_klik)
c2.tag_bind(c_9_12, '<Button-1>', c_9_12_klik)
c2.tag_bind(c_10_13, '<Button-1>', c_10_13_klik)
c2.tag_bind(c_11_14, '<Button-1>', c_11_14_klik)
c2.tag_bind(c_12_15, '<Button-1>', c_12_15_klik)
c2.tag_bind(c_13_16, '<Button-1>', c_13_16_klik)
c2.tag_bind(c_14_17, '<Button-1>', c_14_17_klik)
c2.tag_bind(c_15_18, '<Button-1>', c_15_18_klik)
c2.tag_bind(c_16_19, '<Button-1>', c_16_19_klik)
c2.tag_bind(c_17_20, '<Button-1>', c_17_20_klik)
c2.tag_bind(c_18_21, '<Button-1>', c_18_21_klik)
c2.tag_bind(c_19_22, '<Button-1>', c_19_22_klik)
c2.tag_bind(c_20_23, '<Button-1>', c_20_23_klik)
c2.tag_bind(c_21_24, '<Button-1>', c_21_24_klik)
c2.tag_bind(c_22_25, '<Button-1>', c_22_25_klik)
c2.tag_bind(c_23_26, '<Button-1>', c_23_26_klik)
c2.tag_bind(c_24_27, '<Button-1>', c_24_27_klik)
c2.tag_bind(c_25_28, '<Button-1>', c_25_28_klik)
c2.tag_bind(c_26_29, '<Button-1>', c_26_29_klik)
c2.tag_bind(c_27_30, '<Button-1>', c_27_30_klik)
c2.tag_bind(c_28_31, '<Button-1>', c_28_31_klik)
c2.tag_bind(c_29_32, '<Button-1>', c_29_32_klik)
c2.tag_bind(c_30_33, '<Button-1>', c_30_33_klik)
c2.tag_bind(c_31_34, '<Button-1>', c_31_34_klik)
c2.tag_bind(c_32_35, '<Button-1>', c_32_35_klik)
c2.tag_bind(c_33_36, '<Button-1>', c_33_36_klik)


c2.tag_bind(c_1_2_3, '<Enter>', c_1_2_3_hov1)
c2.tag_bind(c_1_2_3, '<Leave>', c_1_2_3_hov2)
c2.tag_bind(c_4_5_6, '<Enter>', c_4_5_6_hov1)
c2.tag_bind(c_4_5_6, '<Leave>', c_4_5_6_hov2)
c2.tag_bind(c_7_8_9, '<Enter>', c_7_8_9_hov1)
c2.tag_bind(c_7_8_9, '<Leave>', c_7_8_9_hov2)
c2.tag_bind(c_10_11_12, '<Enter>', c_10_11_12_hov1)
c2.tag_bind(c_10_11_12, '<Leave>', c_10_11_12_hov2)
c2.tag_bind(c_13_14_15, '<Enter>', c_13_14_15_hov1)
c2.tag_bind(c_13_14_15, '<Leave>', c_13_14_15_hov2)
c2.tag_bind(c_16_17_18, '<Enter>', c_16_17_18_hov1)
c2.tag_bind(c_16_17_18, '<Leave>', c_16_17_18_hov2)
c2.tag_bind(c_19_20_21, '<Enter>', c_19_20_21_hov1)
c2.tag_bind(c_19_20_21, '<Leave>', c_19_20_21_hov2)
c2.tag_bind(c_22_23_24, '<Enter>', c_22_23_24_hov1)
c2.tag_bind(c_22_23_24, '<Leave>', c_22_23_24_hov2)
c2.tag_bind(c_25_26_27, '<Enter>', c_25_26_27_hov1)
c2.tag_bind(c_25_26_27, '<Leave>', c_25_26_27_hov2)
c2.tag_bind(c_28_29_30, '<Enter>', c_28_29_30_hov1)
c2.tag_bind(c_28_29_30, '<Leave>', c_28_29_30_hov2)
c2.tag_bind(c_31_32_33, '<Enter>', c_31_32_33_hov1)
c2.tag_bind(c_31_32_33, '<Leave>', c_31_32_33_hov2)
c2.tag_bind(c_34_35_36, '<Enter>', c_34_35_36_hov1)
c2.tag_bind(c_34_35_36, '<Leave>', c_34_35_36_hov2)
c2.tag_bind(c_1_2_3_4_5_6, '<Enter>', c_1_2_3_4_5_6_hov1)
c2.tag_bind(c_1_2_3_4_5_6, '<Leave>', c_1_2_3_4_5_6_hov2)
c2.tag_bind(c_4_5_6_7_8_9, '<Enter>', c_4_5_6_7_8_9_hov1)
c2.tag_bind(c_4_5_6_7_8_9, '<Leave>', c_4_5_6_7_8_9_hov2)
c2.tag_bind(c_7_8_9_10_11_12, '<Enter>', c_7_8_9_10_11_12_hov1)
c2.tag_bind(c_7_8_9_10_11_12, '<Leave>', c_7_8_9_10_11_12_hov2)
c2.tag_bind(c_10_11_12_13_14_15, '<Enter>', c_10_11_12_13_14_15_hov1)
c2.tag_bind(c_10_11_12_13_14_15, '<Leave>', c_10_11_12_13_14_15_hov2)
c2.tag_bind(c_13_14_15_16_17_18, '<Enter>', c_13_14_15_16_17_18_hov1)
c2.tag_bind(c_13_14_15_16_17_18, '<Leave>', c_13_14_15_16_17_18_hov2)
c2.tag_bind(c_16_17_18_19_20_21, '<Enter>', c_16_17_18_19_20_21_hov1)
c2.tag_bind(c_16_17_18_19_20_21, '<Leave>', c_16_17_18_19_20_21_hov2)
c2.tag_bind(c_19_20_21_22_23_24, '<Enter>', c_19_20_21_22_23_24_hov1)
c2.tag_bind(c_19_20_21_22_23_24, '<Leave>', c_19_20_21_22_23_24_hov2)
c2.tag_bind(c_22_23_24_25_26_27, '<Enter>', c_22_23_24_25_26_27_hov1)
c2.tag_bind(c_22_23_24_25_26_27, '<Leave>', c_22_23_24_25_26_27_hov2)
c2.tag_bind(c_25_26_27_28_29_30, '<Enter>', c_25_26_27_28_29_30_hov1)
c2.tag_bind(c_25_26_27_28_29_30, '<Leave>', c_25_26_27_28_29_30_hov2)
c2.tag_bind(c_28_29_30_31_32_33, '<Enter>', c_28_29_30_31_32_33_hov1)
c2.tag_bind(c_28_29_30_31_32_33, '<Leave>', c_28_29_30_31_32_33_hov2)
c2.tag_bind(c_31_32_33_34_35_36, '<Enter>', c_31_32_33_34_35_36_hov1)
c2.tag_bind(c_31_32_33_34_35_36, '<Leave>', c_31_32_33_34_35_36_hov2)
c2.tag_bind(c_0_1_2_3, '<Enter>', c_0_1_2_3_hov1)
c2.tag_bind(c_0_1_2_3, '<Leave>', c_0_1_2_3_hov2)

c2.tag_bind(c_1_2, '<Enter>', c_1_2_hov1)
c2.tag_bind(c_1_2, '<Leave>', c_1_2_hov2)
c2.tag_bind(c_2_3, '<Enter>', c_2_3_hov1)
c2.tag_bind(c_2_3, '<Leave>', c_2_3_hov2)
c2.tag_bind(c_4_5, '<Enter>', c_4_5_hov1)
c2.tag_bind(c_4_5, '<Leave>', c_4_5_hov2)
c2.tag_bind(c_5_6, '<Enter>', c_5_6_hov1)
c2.tag_bind(c_5_6, '<Leave>', c_5_6_hov2)
c2.tag_bind(c_7_8, '<Enter>', c_7_8_hov1)
c2.tag_bind(c_7_8, '<Leave>', c_7_8_hov2)
c2.tag_bind(c_8_9, '<Enter>', c_8_9_hov1)
c2.tag_bind(c_8_9, '<Leave>', c_8_9_hov2)
c2.tag_bind(c_10_11, '<Enter>', c_10_11_hov1)
c2.tag_bind(c_10_11, '<Leave>', c_10_11_hov2)
c2.tag_bind(c_11_12, '<Enter>', c_11_12_hov1)
c2.tag_bind(c_11_12, '<Leave>', c_11_12_hov2)
c2.tag_bind(c_13_14, '<Enter>', c_13_14_hov1)
c2.tag_bind(c_13_14, '<Leave>', c_13_14_hov2)
c2.tag_bind(c_14_15, '<Enter>', c_14_15_hov1)
c2.tag_bind(c_14_15, '<Leave>', c_14_15_hov2)
c2.tag_bind(c_16_17, '<Enter>', c_16_17_hov1)
c2.tag_bind(c_16_17, '<Leave>', c_16_17_hov2)
c2.tag_bind(c_17_18, '<Enter>', c_17_18_hov1)
c2.tag_bind(c_17_18, '<Leave>', c_17_18_hov2)
c2.tag_bind(c_19_20, '<Enter>', c_19_20_hov1)
c2.tag_bind(c_19_20, '<Leave>', c_19_20_hov2)
c2.tag_bind(c_20_21, '<Enter>', c_20_21_hov1)
c2.tag_bind(c_20_21, '<Leave>', c_20_21_hov2)
c2.tag_bind(c_22_23, '<Enter>', c_22_23_hov1)
c2.tag_bind(c_22_23, '<Leave>', c_22_23_hov2)
c2.tag_bind(c_23_24, '<Enter>', c_23_24_hov1)
c2.tag_bind(c_23_24, '<Leave>', c_23_24_hov2)
c2.tag_bind(c_25_26, '<Enter>', c_25_26_hov1)
c2.tag_bind(c_25_26, '<Leave>', c_25_26_hov2)
c2.tag_bind(c_26_27, '<Enter>', c_26_27_hov1)
c2.tag_bind(c_26_27, '<Leave>', c_26_27_hov2)
c2.tag_bind(c_28_29, '<Enter>', c_28_29_hov1)
c2.tag_bind(c_28_29, '<Leave>', c_28_29_hov2)
c2.tag_bind(c_29_30, '<Enter>', c_29_30_hov1)
c2.tag_bind(c_29_30, '<Leave>', c_29_30_hov2)
c2.tag_bind(c_31_32, '<Enter>', c_31_32_hov1)
c2.tag_bind(c_31_32, '<Leave>', c_31_32_hov2)
c2.tag_bind(c_32_33, '<Enter>', c_32_33_hov1)
c2.tag_bind(c_32_33, '<Leave>', c_32_33_hov2)
c2.tag_bind(c_34_35, '<Enter>', c_34_35_hov1)
c2.tag_bind(c_34_35, '<Leave>', c_34_35_hov2)
c2.tag_bind(c_35_36, '<Enter>', c_35_36_hov1)
c2.tag_bind(c_35_36, '<Leave>', c_35_36_hov2)


c2.tag_bind(c_prva, '<Enter>', c_prva_hov1)
c2.tag_bind(c_prva, '<Leave>', c_prva_hov2)
c2.tag_bind(c_druga, '<Enter>', c_druga_hov1)
c2.tag_bind(c_druga, '<Leave>', c_druga_hov2)
c2.tag_bind(c_treca, '<Enter>', c_treca_hov1)
c2.tag_bind(c_treca, '<Leave>', c_treca_hov2)
c2.tag_bind(c_cetvrta, '<Enter>', c_cetvrta_hov1)
c2.tag_bind(c_cetvrta, '<Leave>', c_cetvrta_hov2)
c2.tag_bind(c_peta, '<Enter>', c_peta_hov1)
c2.tag_bind(c_peta, '<Leave>', c_peta_hov2)
c2.tag_bind(c_sesta, '<Enter>', c_sesta_hov1)
c2.tag_bind(c_sesta, '<Leave>', c_sesta_hov2)
c2.tag_bind(c_sedma, '<Enter>', c_sedma_hov1)
c2.tag_bind(c_sedma, '<Leave>', c_sedma_hov2)
c2.tag_bind(c_osma, '<Enter>', c_osma_hov1)
c2.tag_bind(c_osma, '<Leave>', c_osma_hov2)
c2.tag_bind(c_deveta, '<Enter>', c_deveta_hov1)
c2.tag_bind(c_deveta, '<Leave>', c_deveta_hov2)
c2.tag_bind(c_deseta, '<Enter>', c_deseta_hov1)
c2.tag_bind(c_deseta, '<Leave>', c_deseta_hov2)
c2.tag_bind(c_jedanaesta, '<Enter>', c_jedanaesta_hov1)
c2.tag_bind(c_jedanaesta, '<Leave>', c_jedanaesta_hov2)
c2.tag_bind(c_dvanaesta, '<Enter>', c_dvanaesta_hov1)
c2.tag_bind(c_dvanaesta, '<Leave>', c_dvanaesta_hov2)
c2.tag_bind(c_trinaesta, '<Enter>', c_trinaesta_hov1)
c2.tag_bind(c_trinaesta, '<Leave>', c_trinaesta_hov2)
c2.tag_bind(c_cetrnaesta, '<Enter>', c_cetrnaesta_hov1)
c2.tag_bind(c_cetrnaesta, '<Leave>', c_cetrnaesta_hov2)
c2.tag_bind(c_petnaesta, '<Enter>', c_petnaesta_hov1)
c2.tag_bind(c_petnaesta, '<Leave>', c_petnaesta_hov2)
c2.tag_bind(c_sesnaesta, '<Enter>', c_sesnaesta_hov1)
c2.tag_bind(c_sesnaesta, '<Leave>', c_sesnaesta_hov2)
c2.tag_bind(c_sedamnaesta, '<Enter>', c_sedamnaesta_hov1)
c2.tag_bind(c_sedamnaesta, '<Leave>', c_sedamnaesta_hov2)
c2.tag_bind(c_osamnaesta, '<Enter>', c_osamnaesta_hov1)
c2.tag_bind(c_osamnaesta, '<Leave>', c_osamnaesta_hov2)
c2.tag_bind(c_devetnaesta, '<Enter>', c_devetnaesta_hov1)
c2.tag_bind(c_devetnaesta, '<Leave>', c_devetnaesta_hov2)
c2.tag_bind(c_dvadeseta, '<Enter>', c_dvadeseta_hov1)
c2.tag_bind(c_dvadeseta, '<Leave>', c_dvadeseta_hov2)
c2.tag_bind(c_dvadesetprva, '<Enter>', c_dvadesetprva_hov1)
c2.tag_bind(c_dvadesetprva, '<Leave>', c_dvadesetprva_hov2)
c2.tag_bind(c_dvadesetdruga, '<Enter>', c_dvadesetdruga_hov1)
c2.tag_bind(c_dvadesetdruga, '<Leave>', c_dvadesetdruga_hov2)


c2.tag_bind(c_0_1_2, '<Enter>', c_0_1_2_hov1)
c2.tag_bind(c_0_1_2, '<Leave>', c_0_1_2_hov2)
c2.tag_bind(c_0_2, '<Enter>', c_0_2_hov1)
c2.tag_bind(c_0_2, '<Leave>', c_0_2_hov2)
c2.tag_bind(c_0_1, '<Enter>', c_0_1_hov1)
c2.tag_bind(c_0_1, '<Leave>', c_0_1_hov2)
c2.tag_bind(c_0_3, '<Enter>', c_0_3_hov1)
c2.tag_bind(c_0_3, '<Leave>', c_0_3_hov2)
c2.tag_bind(c_0_2_3, '<Enter>', c_0_2_3_hov1)
c2.tag_bind(c_0_2_3, '<Leave>', c_0_2_3_hov2)
c2.tag_bind(c_1_4, '<Enter>', c_1_4_hov1)
c2.tag_bind(c_1_4, '<Leave>', c_1_4_hov2)
c2.tag_bind(c_2_5, '<Enter>', c_2_5_hov1)
c2.tag_bind(c_2_5, '<Leave>', c_2_5_hov2)
c2.tag_bind(c_3_6, '<Enter>', c_3_6_hov1)
c2.tag_bind(c_3_6, '<Leave>', c_3_6_hov2)
c2.tag_bind(c_4_7, '<Enter>', c_4_7_hov1)
c2.tag_bind(c_4_7, '<Leave>', c_4_7_hov2)
c2.tag_bind(c_5_8, '<Enter>', c_5_8_hov1)
c2.tag_bind(c_5_8, '<Leave>', c_5_8_hov2)
c2.tag_bind(c_6_9, '<Enter>', c_6_9_hov1)
c2.tag_bind(c_6_9, '<Leave>', c_6_9_hov2)
c2.tag_bind(c_7_10, '<Enter>', c_7_10_hov1)
c2.tag_bind(c_7_10, '<Leave>', c_7_10_hov2)
c2.tag_bind(c_8_11, '<Enter>', c_8_11_hov1)
c2.tag_bind(c_8_11, '<Leave>', c_8_11_hov2)
c2.tag_bind(c_9_12, '<Enter>', c_9_12_hov1)
c2.tag_bind(c_9_12, '<Leave>', c_9_12_hov2)
c2.tag_bind(c_10_13, '<Enter>', c_10_13_hov1)
c2.tag_bind(c_10_13, '<Leave>', c_10_13_hov2)
c2.tag_bind(c_11_14, '<Enter>', c_11_14_hov1)
c2.tag_bind(c_11_14, '<Leave>', c_11_14_hov2)
c2.tag_bind(c_12_15, '<Enter>', c_12_15_hov1)
c2.tag_bind(c_12_15, '<Leave>', c_12_15_hov2)
c2.tag_bind(c_13_16, '<Enter>', c_13_16_hov1)
c2.tag_bind(c_13_16, '<Leave>', c_13_16_hov2)
c2.tag_bind(c_14_17, '<Enter>', c_14_17_hov1)
c2.tag_bind(c_14_17, '<Leave>', c_14_17_hov2)
c2.tag_bind(c_15_18, '<Enter>', c_15_18_hov1)
c2.tag_bind(c_15_18, '<Leave>', c_15_18_hov2)
c2.tag_bind(c_16_19, '<Enter>', c_16_19_hov1)
c2.tag_bind(c_16_19, '<Leave>', c_16_19_hov2)
c2.tag_bind(c_17_20, '<Enter>', c_17_20_hov1)
c2.tag_bind(c_17_20, '<Leave>', c_17_20_hov2)
c2.tag_bind(c_18_21, '<Enter>', c_18_21_hov1)
c2.tag_bind(c_18_21, '<Leave>', c_18_21_hov2)
c2.tag_bind(c_19_22, '<Enter>', c_19_22_hov1)
c2.tag_bind(c_19_22, '<Leave>', c_19_22_hov2)
c2.tag_bind(c_20_23, '<Enter>', c_20_23_hov1)
c2.tag_bind(c_20_23, '<Leave>', c_20_23_hov2)
c2.tag_bind(c_21_24, '<Enter>', c_21_24_hov1)
c2.tag_bind(c_21_24, '<Leave>', c_21_24_hov2)
c2.tag_bind(c_22_25, '<Enter>', c_22_25_hov1)
c2.tag_bind(c_22_25, '<Leave>', c_22_25_hov2)
c2.tag_bind(c_23_26, '<Enter>', c_23_26_hov1)
c2.tag_bind(c_23_26, '<Leave>', c_23_26_hov2)
c2.tag_bind(c_24_27, '<Enter>', c_24_27_hov1)
c2.tag_bind(c_24_27, '<Leave>', c_24_27_hov2)
c2.tag_bind(c_25_28, '<Enter>', c_25_28_hov1)
c2.tag_bind(c_25_28, '<Leave>', c_25_28_hov2)
c2.tag_bind(c_26_29, '<Enter>', c_26_29_hov1)
c2.tag_bind(c_26_29, '<Leave>', c_26_29_hov2)
c2.tag_bind(c_27_30, '<Enter>', c_27_30_hov1)
c2.tag_bind(c_27_30, '<Leave>', c_27_30_hov2)
c2.tag_bind(c_28_31, '<Enter>', c_28_31_hov1)
c2.tag_bind(c_28_31, '<Leave>', c_28_31_hov2)
c2.tag_bind(c_29_32, '<Enter>', c_29_32_hov1)
c2.tag_bind(c_29_32, '<Leave>', c_29_32_hov2)
c2.tag_bind(c_30_33, '<Enter>', c_30_33_hov1)
c2.tag_bind(c_30_33, '<Leave>', c_30_33_hov2)
c2.tag_bind(c_31_34, '<Enter>', c_31_34_hov1)
c2.tag_bind(c_31_34, '<Leave>', c_31_34_hov2)
c2.tag_bind(c_32_35, '<Enter>', c_32_35_hov1)
c2.tag_bind(c_32_35, '<Leave>', c_32_35_hov2)
c2.tag_bind(c_33_36, '<Enter>', c_33_36_hov1)
c2.tag_bind(c_33_36, '<Leave>', c_33_36_hov2)



c2.tag_bind(nnula, '<Enter>', nnula1)
c2.tag_bind(nnula, '<Leave>', nnula2)
c2.tag_bind(jjedan, '<Enter>', jjedan1)
c2.tag_bind(jjedan, '<Leave>', jjedan2)
c2.tag_bind(ddva, '<Enter>', ddva1)
c2.tag_bind(ddva, '<Leave>', ddva2)
c2.tag_bind(ttri, '<Enter>', ttri1)
c2.tag_bind(ttri, '<Leave>', ttri2)
c2.tag_bind(ccetiri, '<Enter>', ccetiri1)
c2.tag_bind(ccetiri, '<Leave>', ccetiri2)
c2.tag_bind(ppet, '<Enter>', ppet1)
c2.tag_bind(ppet, '<Leave>', ppet2)
c2.tag_bind(ssest, '<Enter>', ssest1)
c2.tag_bind(ssest, '<Leave>', ssest2)
c2.tag_bind(ssedam, '<Enter>', ssedam1)
c2.tag_bind(ssedam, '<Leave>', ssedam2)
c2.tag_bind(oosam, '<Enter>', oosam1)
c2.tag_bind(oosam, '<Leave>', oosam2)
c2.tag_bind(ddevet, '<Enter>', ddevet1)
c2.tag_bind(ddevet, '<Leave>', ddevet2)
c2.tag_bind(ddeset, '<Enter>', ddeset1)
c2.tag_bind(ddeset, '<Leave>', ddeset2)
c2.tag_bind(jjedanaest, '<Enter>', jjedanaest1)
c2.tag_bind(jjedanaest, '<Leave>', jjedanaest2)
c2.tag_bind(ddvanaest, '<Enter>', ddvanaest1)
c2.tag_bind(ddvanaest, '<Leave>', ddvanaest2)
c2.tag_bind(ttrinaest, '<Enter>', ttrinaest1)
c2.tag_bind(ttrinaest, '<Leave>', ttrinaest2)
c2.tag_bind(ccetrnaest, '<Enter>', ccetrnaest1)
c2.tag_bind(ccetrnaest, '<Leave>', ccetrnaest2)
c2.tag_bind(ppetnaest, '<Enter>', ppetnaest1)
c2.tag_bind(ppetnaest, '<Leave>', ppetnaest2)
c2.tag_bind(ssesnaest, '<Enter>', ssesnaest1)
c2.tag_bind(ssesnaest, '<Leave>', ssesnaest2)
c2.tag_bind(ssedamnaest, '<Enter>', ssedamnaest1)
c2.tag_bind(ssedamnaest, '<Leave>', ssedamnaest2)
c2.tag_bind(oosamnaest, '<Enter>', oosamnaest1)
c2.tag_bind(oosamnaest, '<Leave>', oosamnaest2)
c2.tag_bind(ddevetnaest, '<Enter>', ddevetnaest1)
c2.tag_bind(ddevetnaest, '<Leave>', ddevetnaest2)
c2.tag_bind(dd_nula, '<Enter>', dd_nula1)
c2.tag_bind(dd_nula, '<Leave>', dd_nula2)
c2.tag_bind(dd_jedan, '<Enter>', dd_jedan1)
c2.tag_bind(dd_jedan, '<Leave>', dd_jedan2)
c2.tag_bind(dd_dva, '<Enter>', dd_dva1)
c2.tag_bind(dd_dva, '<Leave>', dd_dva2)
c2.tag_bind(dd_tri, '<Enter>', dd_tri1)
c2.tag_bind(dd_tri, '<Leave>', dd_tri2)
c2.tag_bind(dd_cetiri, '<Enter>', dd_cetiri1)
c2.tag_bind(dd_cetiri, '<Leave>', dd_cetiri2)
c2.tag_bind(dd_pet, '<Enter>', dd_pet1)
c2.tag_bind(dd_pet, '<Leave>', dd_pet2)
c2.tag_bind(dd_sest, '<Enter>', dd_sest1)
c2.tag_bind(dd_sest, '<Leave>', dd_sest2)
c2.tag_bind(dd_sedam, '<Enter>', dd_sedam1)
c2.tag_bind(dd_sedam, '<Leave>', dd_sedam2)
c2.tag_bind(dd_osam, '<Enter>', dd_osam1)
c2.tag_bind(dd_osam, '<Leave>', dd_osam2)
c2.tag_bind(dd_devet, '<Enter>', dd_devet1)
c2.tag_bind(dd_devet, '<Leave>', dd_devet2)
c2.tag_bind(tt_nula, '<Enter>', tt_nula1)
c2.tag_bind(tt_nula, '<Leave>', tt_nula2)
c2.tag_bind(tt_jedan, '<Enter>', tt_jedan1)
c2.tag_bind(tt_jedan, '<Leave>', tt_jedan2)
c2.tag_bind(tt_dva, '<Enter>', tt_dva1)
c2.tag_bind(tt_dva, '<Leave>', tt_dva2)
c2.tag_bind(tt_tri, '<Enter>', tt_tri1)
c2.tag_bind(tt_tri, '<Leave>', tt_tri2)
c2.tag_bind(tt_cetiri, '<Enter>', tt_cetiri1)
c2.tag_bind(tt_cetiri, '<Leave>', tt_cetiri2)
c2.tag_bind(tt_pet, '<Enter>', tt_pet1)
c2.tag_bind(tt_pet, '<Leave>', tt_pet2)
c2.tag_bind(tt_sest, '<Enter>', tt_sest1)
c2.tag_bind(tt_sest, '<Leave>', tt_sest2)
c2.tag_bind(ttreca_tri, '<Enter>', ttreca_tri1)
c2.tag_bind(ttreca_tri, '<Leave>', ttreca_tri2)
c2.tag_bind(ddruga_tri, '<Enter>', ddruga_tri1)
c2.tag_bind(ddruga_tri, '<Leave>', ddruga_tri2)
c2.tag_bind(pprva_tri, '<Enter>', pprva_tri1)
c2.tag_bind(pprva_tri, '<Leave>', pprva_tri2)
c2.tag_bind(treca_trec, '<Enter>', treca_trec1)
c2.tag_bind(treca_trec, '<Leave>', treca_trec2)
c2.tag_bind(druga_trec, '<Enter>', druga_trec1)
c2.tag_bind(druga_trec, '<Leave>', druga_trec2)
c2.tag_bind(prva_trec, '<Enter>', prva_trec1)
c2.tag_bind(prva_trec, '<Leave>', prva_trec2)
c2.tag_bind(prvih_18_t, '<Enter>', prvih_18_t1)
c2.tag_bind(prvih_18_t, '<Leave>', prvih_18_t2)
c2.tag_bind(drugih_18_t, '<Enter>', drugih_18_t1)
c2.tag_bind(drugih_18_t, '<Leave>', drugih_18_t2)
c2.tag_bind(even_t, '<Enter>', even_t1)
c2.tag_bind(even_t, '<Leave>', even_t2)
c2.tag_bind(odd_t, '<Enter>', odd_t1)
c2.tag_bind(odd_t, '<Leave>', odd_t2)




ch1_5 = ImageTk.PhotoImage(file = 'icons\\1.png')
ch1_7 = ImageTk.PhotoImage(file = 'icons\\11.png')
ch1 = c2.create_image(550, 380, image=ch1_5)

c2.tag_bind(ch1, '<Enter>', ch1_1)
c2.tag_bind(ch1, '<Leave>', ch1_2)
c2.tag_bind(ch1, '<Button-1>', ch1_klik)

ch5_5 = ImageTk.PhotoImage(file = 'icons\\5.png')
ch5_7 = ImageTk.PhotoImage(file = 'icons\\55.png')
ch5 = c2.create_image(550, 440, image=ch5_5)

c2.tag_bind(ch5, '<Enter>', ch5_1)
c2.tag_bind(ch5, '<Leave>', ch5_2)
c2.tag_bind(ch5, '<Button-1>', ch5_klik)

ch10_5 = ImageTk.PhotoImage(file = 'icons\\10.png')
ch10_7 = ImageTk.PhotoImage(file = 'icons\\1010.png')
ch10 = c2.create_image(610, 380, image=ch10_5)

c2.tag_bind(ch10, '<Enter>', ch10_1)
c2.tag_bind(ch10, '<Leave>', ch10_2)
c2.tag_bind(ch10, '<Button-1>', ch10_klik)

ch20_5 = ImageTk.PhotoImage(file = 'icons\\20.png')
ch20_7 = ImageTk.PhotoImage(file = 'icons\\2020.png')
ch20 = c2.create_image(610, 440, image=ch20_5)

c2.tag_bind(ch20, '<Enter>', ch20_1)
c2.tag_bind(ch20, '<Leave>', ch20_2)
c2.tag_bind(ch20, '<Button-1>', ch20_klik)

ch50_5 = ImageTk.PhotoImage(file = 'icons\\50.png')
ch50_7 = ImageTk.PhotoImage(file = 'icons\\5050.png')
ch50 = c2.create_image(670, 380, image=ch50_5)

c2.tag_bind(ch50, '<Enter>', ch50_1)
c2.tag_bind(ch50, '<Leave>', ch50_2)
c2.tag_bind(ch50, '<Button-1>', ch50_klik)

ch100_5 = ImageTk.PhotoImage(file = 'icons\\100.png')
ch100_7 = ImageTk.PhotoImage(file = 'icons\\100100.png')
ch100 = c2.create_image(670, 440, image=ch100_5)

c2.tag_bind(ch100, '<Enter>', ch100_1)
c2.tag_bind(ch100, '<Leave>', ch100_2)
c2.tag_bind(ch100, '<Button-1>', ch100_klik)

ch500_5 = ImageTk.PhotoImage(file = 'icons\\500.png')
ch500_7 = ImageTk.PhotoImage(file = 'icons\\500500.png')
ch500 = c2.create_image(730, 380, image=ch500_5)

c2.tag_bind(ch500, '<Enter>', ch500_1)
c2.tag_bind(ch500, '<Leave>', ch500_2)
c2.tag_bind(ch500, '<Button-1>', ch500_klik)

ch1000_5 = ImageTk.PhotoImage(file = 'icons\\1000.png')
ch1000_7 = ImageTk.PhotoImage(file = 'icons\\10001000.png')
ch1000 = c2.create_image(730, 440, image=ch1000_5)

c2.tag_bind(ch1000, '<Enter>', ch1000_1)
c2.tag_bind(ch1000, '<Leave>', ch1000_2)
c2.tag_bind(ch1000, '<Button-1>', ch1000_klik)


vrti = Button(r1,
                text = '--- VRTI! ---',
                activebackground = "#00FF00",
                background = "#003300",
                font=("Algerian",25),
                fg='yellow',
                relief=RAISED,\
                cursor="circle",
                command = vrti_klik)
vrti_window = c2.create_window(790, 353, width = 189, height = 50, anchor='nw', window=vrti)

gumak = PhotoImage(file = 'icons\\eraser.png')
halp = PhotoImage(file = 'icons\\help.png')
stat = PhotoImage(file = 'icons\\stat.png') 

izbrisi = Button(r1,
                activebackground = "#00FF00",
                background = "#003300",
                image = gumak,
                relief=RAISED,\
                cursor="circle",
                command = obrisi)
izbrisi_window = c2.create_window(790, 412, width = 60, height = 50, anchor='nw', window=izbrisi)

helpp = Button(r1,
                activebackground = "#00FF00",
                background = "#003300",
                image = halp,
                relief=RAISED,\
                cursor="circle",
                command = pomocc)
helpp_window = c2.create_window(920, 412, width = 59, height = 50, anchor='nw', window=helpp)

statistic = Button(r1,
                activebackground = "#00FF00",
                background = "#003300",
                image = stat,
                relief=RAISED,\
                cursor="circle",
                command = statika)
statistic_window = c2.create_window(855, 412, width = 60, height = 50, anchor='nw', window=statistic)



ispis_para = Text(r1,
                   width=15,
                   font=("Arial",18, 'bold'),
                   fg='#00FF00',
                   background='black',
                   relief=RAISED,\
                   cursor="circle")
ispis_para_window = c2.create_window(1015, 430, width = 225, height = 30, anchor='nw', window=ispis_para)


obavijesti = Text(r1,
                   width=15,
                   font=("Calibri",11,'bold'),
                   fg='white',
                   background='black',
                   relief=RAISED,\
                   cursor="circle")
obavijesti_windows = c2.create_window(1015, 353, width = 225, height = 67, anchor='nw', window=obavijesti)



ispis_para.tag_configure('tag-right', justify='right')
ispis_para.insert(END, str(a), 'tag-right')
ispis_para.config(state=DISABLED)

obavijesti.tag_config('broj', foreground='yellow')
obavijesti.tag_config('iznos', foreground='#00FF00')
obavijesti.tag_config('crv', foreground='red')

obavijesti.tag_config('ostali', foreground='#3399FF')
global genss
obavijesti.delete('1.0',END)
obavijesti.tag_configure('tag-center', justify='center')
obavijesti.insert(END, 'Dobrodošli u TkinteRoulette!', 'tag-center')
obavijesti.insert(END, '\n', 'tag-center')
obavijesti.insert(END, '>----------------------<', 'tag-center')
obavijesti.insert(END, '\n', 'tag-center')
obavijesti.insert(END, 'Za pomoć, kliknite na upitnik.', 'tag-center')
proz = ImageTk.PhotoImage(file = 'main\\prozirno.png')
genss = ImageTk.PhotoImage(file = 'rula/jux.png')
obavijesti.config(state=DISABLED)

paree=int(a)
iznos_vrtnji.append(int(a))

global my_label

video = imageio.get_reader("rula/start.mp4")


my_label = Label(c2)
my_label.place(x=3,y=2)
my_label.config(borderwidth=0, highlightthickness=0)

thread = threading.Thread(target=startt, args=(my_label,))
thread.daemon = 1
thread.start()
marijo = PlaySound('intro\\mario_bg.wav', SND_LOOP + SND_ASYNC)

global sve_animacije
sve_animacije = ['rula/'+str(i)+'.mp4' for i in range(0,37)]
r1.iconbitmap("intro/icon.ico")
r1.title('TkinteRoulette™')
r1.resizable(False, False)
r1.mainloop()








