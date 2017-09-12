from tkinter import  *
from random import   *

okno=Tk()
okno.title("Snake")
rys=Canvas(okno,width=600,height=400)

rys.pack()

kolory=["black","peach puff","orange","red","blue","yellow","silver","gold","purple","green","pink","grey","brown","lime","violet","dark green","light blue","dark red","light green"]
class Snake(object):
	def __init__(self,szerokosc,wysokosc):
		self.col=False
		self.szerokosc=szerokosc
		self.wysokosc=wysokosc
		self.snake=[[szerokosc/2,wysokosc/2],[szerokosc/2+1,wysokosc/2],[szerokosc/2+2,wysokosc/2]]
		self.kierunek=0
		self.kierunki=[[0,1],[1,0],[0,-1],[-1,0]]
		self.rozmiar=10
		self.jablko=[randint(1,szerokosc-2),randint(1,wysokosc-2)]
		self.t=200
		
	def rysuj_pixel(self,x,y,color):
		rys.create_rectangle(x,y,x+self.rozmiar,y+self.rozmiar,fill=color)
		
	def rysuj(self):
		rys.delete("all")
		if self.col==True:
			rys.create_text(self.szerokosc/2*self.rozmiar,self.wysokosc/2*self.rozmiar,text="koniec gry\n wynik = "+str(len(self.snake)))
		for i in range(self.szerokosc):
			self.rysuj_pixel(i*self.rozmiar,0,color="brown")
			self.rysuj_pixel(i*self.rozmiar,self.rozmiar*(self.wysokosc-1),color="brown")
		for i in range(1,self.wysokosc-1):
			self.rysuj_pixel(0,i*self.rozmiar,color="brown")
			self.rysuj_pixel(self.rozmiar*(self.szerokosc-1),i*self.rozmiar,color="brown")
		for i in self.snake:
			self.rysuj_pixel(i[0]*self.rozmiar,i[1]*self.rozmiar,"green")
		self.rysuj_pixel(self.jablko[0]*self.rozmiar,self.jablko[1]*self.rozmiar,"red")
		
	def jedz(self):
		if self.snake[0][0]==self.jablko[0] and self.snake[0][1]==self.jablko[1]:
			self.snake.append([0,0])
			self.jablko=[randint(1,self.szerokosc-2),randint(1,self.wysokosc-2)]

		
	def idz(self):
		for i in range(len(self.snake)-1,0,-1):
			self.snake[i][0]=self.snake[i-1][0]
			self.snake[i][1]=self.snake[i-1][1]
		self.snake[0][0] = self.snake[0][0] + self.kierunki[self.kierunek][0]
		self.snake[0][1] = self.snake[0][1] + self.kierunki[self.kierunek][1]	
		self.kolizja()
		self.jedz()
		self.rysuj()
	
	def wlewo(self):
		self.kierunek=self.kierunek+1
		if self.kierunek==4:
			self.kierunek=0
	def wprawo(self):
		self.kierunek=self.kierunek-1
		if self.kierunek==-1:
			self.kierunek=3
	def kolizja(self):
		for i in range(1,len(self.snake)):
			if self.snake[0][0]==self.snake[i][0] and self.snake[0][1]==self.snake[i][1]:
				self.col=True
		if self.snake[0][0]==0 or self.snake[0][0]==self.szerokosc-1 or self.snake[0][1]==0 or self.snake[0][1]==self.wysokosc-1:
			self.col=True
	def reset(self):
		self.col=False
		self.snake=[[self.szerokosc/2,self.wysokosc/2],[self.szerokosc/2+1,self.wysokosc/2],[self.szerokosc/2+2,self.wysokosc/2]]
		self.kierunek=0
		self.jablko=[randint(1,self.szerokosc-2),randint(1,self.wysokosc-2)]
		self.kierunki=[[0,1],[1,0],[0,-1],[-1,0]]
		self.rozmiar=10
		self.t=200
		okno.after(self.t,idz)


		

def latwy():
	gra.t=400
	
gra=Snake(60,40)	

def latwy():
	gra.t=400

def sredni():
	gra.t=200

def trudny():
	gra.t=100
	
def pauza():
	if gra.t==10000000000000:
		gra.t=200
	else:
		gra.t=10000000000000

	
pasekmenu=Menu(okno)
menu=Menu(pasekmenu,tearoff=0)
menu2=Menu(pasekmenu,tearoff=0)
pasekmenu.add_cascade(label="gra",menu=menu)
menu.add_command(label="nowa gra",command=gra.reset)
#menu.add_command(label="pauza",command=pauza)
menu.add_command(label="wyjscie",command=okno.quit)
pasekmenu.add_cascade(label="poziom trudnosci",menu=menu2)
menu2.add_command(label="latwy",command=latwy)
menu2.add_command(label="sredni",command=sredni)
menu2.add_command(label="trudny",command=trudny)


okno.config(menu=pasekmenu)


gra.rysuj()

def idz():
	gra.idz()
	if not gra.col:
		okno.after(gra.t,idz)

def lewo(przycisk):
	gra.wlewo()
	
def prawo(przycisk):
	gra.wprawo()	


okno.after(gra.t,idz)


okno.bind("<Left>",lewo)
okno.bind("<Right>",prawo)













































































okno.mainloop()