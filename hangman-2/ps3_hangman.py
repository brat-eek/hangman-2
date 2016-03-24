# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
import pyglet
import sqlite3
import os
import threading 
import serial

def worker():
	os.system("aplay -q  correctguess.wav");

def wrong():
	os.system("aplay -q wrongs.wav");

def win():
	os.system("aplay -q applause.wav");

def lost():
	os.system("aplay -q arrow.wav");
 	
conn=sqlite3.connect("once.db")
cur=conn.cursor()

print 'Please enter your name : '
naam=raw_input()

	
WORDLIST_FILENAME = "words.txt"

def loadWords():
    
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded on deck."
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    ns=''
    for i in secretWord:
        if i not in ns:
            ns=ns+i
    size=len(ns)
    for j in lettersGuessed:
        if size==0:
            return True
        if j in ns:
            size-=1
            
    if size==0:
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    s=''
    for i in secretWord:
        if i in lettersGuessed:
            s=s+i+' '
        else:
            s=s+'__ '
            
    return s



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    s=string.ascii_lowercase
    for i in lettersGuessed:
        cut=s.index(i)
        s=s[0:cut]+s[cut+1:]
        
    return s
    
def pstate1():
    for i in range(60):
	print ''
    
    print '                                                                (((((())))))'
    print '                                                                |          |'
    print '                                                                |  @   @   |'
    print '                                                                |   ___    |'
    print '                                                                [__________]'                 
    for i in range(10):
	print ''
    for i in range(10):
        print ''


def pstate2():
    for i in range(60):
	print ''
    print '                                                                (((((())))))'
    print '                                                                |          |'
    print '                                                                |  @   @   |'
    print '                                                                |   ___    |'
    print '                                                                [__________]'                 
    print '                                                                     ||'
    print '                                                                     || '
    print '                                                                     ||  '
    print '                                                                     ||   '
    print '                                                                     ||    '
    print '                                                                     ||     '
    print '                                                                     ||      '
    
   
    for i in range(5):
	print ''
    for i in range(10):
        print ''
 
def pstate3():
    for i in range(60):
	print ''
    print '                                                                (((((())))))'
    print '                                                                |          |'
    print '                                                                |  @   @   |'
    print '                                                                |   ___    |'
    print '                                                                [__________]'                 
    print '                                                                    /||\\'
    print '                                                                   / || \\'
    print '                                                                  /  ||  \\'
    print '                                                                 /   ||   \\'
    print '                                                                     ||      '
    print '                                                                     ||       '
    print '                                                                     ||        '
    for i in range(5):
	print ''
    for i in range(10):
        print ''


def pstate4():
    for i in range(60):
	print ''
    print '                                                                (((((())))))'
    print '                                                                |          |'
    print '                                                                |  @   @   |'
    print '                                                                |          |'
    print '                                                                [__________]'                 
    print '                                                                    /||\\'
    print '                                                                   / || \\'
    print '                                                                  /  ||  \\'
    print '                                                                 /   ||   \\'
    print '                                                                     ||      '
    print '                                                                     ||       '
    print '                                                                     ||        '
    print '                                                                    /  \\'
    print '                                                                   /    \\'
    print '                                                                  /      \\'
    print '                                                               __/        \\__'
    print '                                                              (__)         (__)'
    
    
    for i in range(10):
        print ''
def pstate5():
    for i in range(60):
	print ''

	print ''
	print '                                             ----------------------------------------'
    print '                                             |                  (((((())))))        D    '
    print '                                             |                  |          |        E    '
    print '                                             |                  |  @   @   |        A    '
    print '                                             |                  |          |        D    '
    print '                                             |                  [__________]             '         
    print '                        SHOOT           ------------         >>---------------->>>'        
    print '                                             |                      /||\\'
    print '                                             |                     / || \\'
    print '                                             |                    /  ||  \\'
    print '                                             |                   /   ||   \\'
    print '                                             |                       ||      '
    print '                                             |                       ||       '
    print '                                             |                       ||        '
    print '                                             |                      /  \\'
    print '                                             |                     /    \\'
    print '                                             |                    /      \\'
    print '                                             |                 __/        \\__'
    print '                                             |                (__)         (__)'
    

    for i in range(10):
        print ''
def pstatewin():
    for i in range(60):
	print ''

    print ''
    print '                                                                (((((())))))'
    print '                                                                |          |'
    print '                                                                |  @   ;   |'
    print '                                                                |    <>    |'
    print '                           \\     /     /\\       \\     /         \\__________/'                 
    print '                            \\   /     /  \\       \\   /          /\\  /||\\'
    print '                             \\ /     /    \\       \\ /          [] \\/ || \\'
    print '                              |     /------\\       |                 ||  \\'
    print '                              |    /        \\      |                 ||   \\'
    print '                              |   /          \\     |                 ||      '
    print '                                                                    /  \\'
    print '                                                                   /    \\'
    print '                                                                  /      \\'
    print '                                                               __/        \\__'
    print '                                                              (__)         (__)'

    for i in range(10):
        print ''
def hangman(secretWord):
    
    print 'Please select your talent level:'
    print 'press S to begin the game'
    
    a=raw_input()
    if a=='S':
        guess=5
    else:
        guess=5
    print 'Welcome to the game, Hangman!'
    size=len(secretWord)
    s=string.ascii_lowercase
    print "I'm thinking of a word that is "+str(size)+" letters long."
    print '-------------'
    
    for i in range(44):
        print ''
    l=[]
    state=0
    while guess>0:
        print 'You have '+str(guess)+' guesses left.'
        print 'Available letters:',s
        print 'Please guess a letter:',
	#ser=serial.Serial('/dev/ttyACM0',9600)
	
	#c=ser.readline()
	
        c=raw_input()
	#d = threading.Thread(name='daemon', target=worker)
	#d.setDaemon(True);
	#d.start();
        c=c.lower()
        if c not in l:
            l.append(c)
            if c in secretWord:
		if state==0:
	    	    for i in range(45):
			print ''
		elif state==1:
	    	    pstate1()
		elif state==2:
	    	    pstate2()
		elif state==3:
	    	    pstate3()
		else:
	    	    pstate4()
		#else:
		    #for i in range(40):
		     #   print ''
    	    	    #print 'now ur soul is playing from heaven'
		
                print 'Good guess:'
		d=threading.Thread(name='daemon',target=worker)
		d.setDaemon(True);
		d.start();
		#d.join();
                print '                                                               '+getGuessedWord(secretWord,l)
            else:
                guess-=1
		state+=1
		if state==0:
	    	    for i in range(45):
			print ''
		elif state==1:
	    	    pstate1()
		elif state==2:
	            pstate2()
		elif state==3:
	            pstate3()
		else:
	    	    pstate4()
		#else:
		    #for i in range(40):
		        #print ''
    	    	    #print 'ur kidnapped......better win orelse i will throw ur headless body on ur screen'
                #print 'Oops! That letter is not in my word:'
		#w=threading.Thread(name='daemon',target=wrong)
		#w.setDaemon(True);
		#w.start();
		#w.join();
                print '                                                               '+getGuessedWord(secretWord,l)
            print '-------------'
            cut=s.index(c)
            s=s[0:cut]+s[cut+1:]
        else:
	    if state==0:
	        for i in range(45):
		    print ''
	    elif state==1:
	        pstate1()
	    elif state==2:
	        pstate2()
	    elif state==3:
	        pstate3()
	    else:
	        pstate4()
	    #else:
		#for i in range(40):
		  #  print ''
    	    	#print 'now ur soul is playing from heaven'
            print "Oops! You've already guessed that letter:"
	    u=threading.Thread(name='daemon',target=wrong)
	    u.setDaemon(True);
	    u.start();
            print '                                                                   '+getGuessedWord(secretWord,l)
            print '-------------'
            #d.join();
	    #w.join();
	    #p.join();
	    #t.join();
        if isWordGuessed(secretWord,l):
	    pstatewin()
            print '                                                 Congratulations, you won!'
	    p=threading.Thread(name='daemon',target=win)
            p.setDaemon(True);
            p.start();
	    print '                                                word u guessed right was',secretWord
	    cur.execute("SELECT wins FROM leader_board WHERE name='"+naam+"'")
	    num2=cur.fetchall()
	    for j in num2:
	        lst2=list(j)
		if a==1:
		    lst2[0]=lst2[0]+1
		else:
		    lst2[0]=lst2[0]+2
		j=tuple(lst2)
		cur.execute("UPDATE leader_board SET wins="+str(j[0])+" WHERE name='"+naam+"'")
            break
    if guess==0:
	pstate5()
	t=threading.Thread(name='daemon',target=lost)
	t.setDaemon(True);
	t.start();
        print '                                         Sorry, you ran out of guesses. The word was',secretWord
    cur.execute("SELECT played FROM leader_board WHERE name='"+naam+"'")
    num=cur.fetchall()
    for i in num:
        lst=list(i)
        lst[0]=lst[0]+1
        i=tuple(lst)
        cur.execute("UPDATE leader_board SET played="+str(i[0])+" WHERE name='"+naam+"'")
    cur.execute("SELECT wins FROM leader_board WHERE name='"+naam+"'")
    num2=cur.fetchall()
    for j in num2:
	print '                                                             Your efficiency is :',
	print ((j[0]*100)/i[0]),
	print '%'

    cur.execute("SELECT * FROM leader_board ORDER BY wins DESC")
    res=cur.fetchall()
    for i in res:
        print i





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
conn.commit()
conn.close()
