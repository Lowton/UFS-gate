from sys import argv
import random
import math
from tkinter import *  

val_range = 0    # диапазон числа
secret = 0       # угадываемое число
guesses = 0      # число попыток
limits = 0       # макс. число попыток

def new_game():
    global secret, guesses, limits
    msg[ 'text' ] = ' ' * 100 + \
        '\nНовая игра, диапазон: [ 0...{} ]\n'.format( val_range )
    secret = random.randrange( 0,val_range )
    guesses = 0
    limits = int( math.ceil( math.log( val_range, 2 ) ) )
    
def input_guess( event ):
    global guesses
    if guesses < 0 :            # признак завершённой игры
        msg[ 'text' ] += 'Начните новую игру...\n'
        ent.delete( 0, END )
        return
    try :
        value = int( ent.get() )
    except ValueError:
        msg[ 'text' ] += 'Ошибка: значение должно быть целочисленным!\n'
        ent.delete( 0, END )
        return;
    ent.delete( 0, END )
    guesses += 1
    if value < secret :
         msg[ 'text' ] += '{} - это меньше ...\n'.format( value )
    elif value > secret :
        msg[ 'text' ] += '{} - это больше ...\n'.format( value )
    else :
        msg[ 'text' ] += 'Игрок выиграл!\n'
        guesses = -1             # признак завершённой игры
        return
    if guesses >= limits :        
        msg[ 'text' ] += 'Компьютер выиграл! Загадно было {}\n'.format( secret )
        guesses = -1             # признак завершённой игры
        return
        
root = Tk()
root.title( 'Угадай число!' )    # окно пиложения
root.geometry( '500x240' )
Label( root, text='Вводите следующее число...' ).pack( side=TOP )
ent = Entry( root, width=10 )    # поле ввода
ent.pack( side=TOP )
ent.focus() # избавить от необходимости выполнять щелчок мышью для фокуса
ent.bind( '<Return>', input_guess )
Button( root, text=' Новая игра ', command=new_game ).pack( side=BOTTOM )
msg = Message( root, bg='white', fg='black', width=400, borderwidth=0 )
msg.pack( side=TOP )             # окно результата

val_range = ( len( argv ) > 1 and int( argv[ 1 ] ) ) or 100 # параметр - диапазон
new_game()
root.mainloop()
