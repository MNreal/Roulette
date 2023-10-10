import numpy as np;
import random as rd;
import time;
import string as str;
import sys;

bool = False;
list = [ 0, 00, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36];
list1 = ["R", "S"];
b = input ("was ist deine Zahl?");
d = input ("Was ist deine Farbe?");
F1 = ("R");
F2 = ("S");






a = input("Drehen?");

if (a == "j" or a =="J" or a == "Ja" or a == "ja" ):
    print ("Scheibe dreht sich...");

    time.sleep(3);

    print ("Dreht sich noch...");

    time.sleep(2);

    c = (np.random.randint(1, 36));
    e = [F1, F2];
    f = (rd.choice(e));
    print (rd.choice(f));
    print (c);

    if (b == c and f == d):
        print ("Du hast gewonnen");

    elif (b != c and f != d):
        print("Du hast verloren");

    elif (b != c and f == d):
        print("Du hast bei Farbe gewonnen");
    
    elif (b == c and f != d):
        print ("Du hast bei Zahl gewonnen");

    elif ( d != "Rot" or d!= "rot" or d != "Schwarz" or d != "schwarz"):
        print ("exit");


else:
    print ("exit");
