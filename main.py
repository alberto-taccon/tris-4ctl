import pymysql

scacchiera = [['_','_','_'],['_','_','_'],['_','_','_']]
n=0
z=0

DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "4CTL_tacco.a.201208",
    "password": "forzamilan22522",
    "database": "4CTL_tacco.a.201208",
    "port": 3307,
    "cursorclass": pymysql.cursors.Cursor,
    "connect_timeout": 5,
}


def get_connection():
    """
    Crea e restituisce una connessione al database.
    """
    return pymysql.connect(**DB_CONFIG)

# ============================================================================================
def stampa_scacchiera(scacchiera):
    for riga in scacchiera:
      print(f"{riga[0]} | {riga[1]} | {riga[2]}")

def mossa(scacchiera, mossa_x, mossa_y, n):
    if (scacchiera[mossa_x][mossa_y]) != '_':
        print("Il punto inserito è già occupato. Riprova")
    if (scacchiera[mossa_x][mossa_y]) == '_':
        if n == 0:
          simbolo = 'X'
        elif n == 1:
          simbolo = 'O'
        scacchiera[mossa_x][mossa_y] = simbolo
        stampa_scacchiera(scacchiera)


def vincita(scacchiera):
    # 00 - 01 - 02
    if scacchiera[0][0]==scacchiera[0][1] and scacchiera[0][0] == scacchiera[0][2] and scacchiera[0][0]!='_':
        print(f"\nHa vinto il giocatore {scacchiera[0][0]}")
        exit()
    # 00 - 10 - 20
    elif scacchiera[0][0]==scacchiera[1][0] and scacchiera[0][0] == scacchiera[2][0]:
        print(f"\nHa vinto il giocatore {scacchiera[0][0]}")
        exit()
    # 00 - 11 - 22 (diagonale 135)
    elif scacchiera[0][0]==scacchiera[1][1] and scacchiera[0][0] == scacchiera[2][2]:
        print(f"\nHa vinto il giocatore {scacchiera[0][0]}")
        exit()
    # 02 - 11 - 20 (diagonale 45)
    elif scacchiera[0][2]==scacchiera[1][1] and scacchiera[0][2] == scacchiera[2][0]:
        print(f"\nHa vinto il giocatore {scacchiera[0][2]}")
        exit()
    # 01 - 11 - 21
    elif scacchiera[0][1]==scacchiera[1][1] and scacchiera[0][1] == scacchiera[2][1]:
        print(f"\nHa vinto il giocatore {scacchiera[0][1]}")
        exit()
    # 02 - 12 - 22
    elif scacchiera[0][2]==scacchiera[1][2] and scacchiera[0][2] == scacchiera[2][2]:
        print(f"\nHa vinto il giocatore {scacchiera[0][2]}")
        exit()
    # 10 - 11 - 12
    elif scacchiera[1][0]==scacchiera[1][1] and scacchiera[1][0] == scacchiera[1][2]:
        print(f"\nHa vinto il giocatore {scacchiera[1][0]}")
        exit()
    # 20 - 21 - 22
    elif scacchiera[2][0]==scacchiera[2][1] and scacchiera[2][0] == scacchiera[2][2]:
        print(f"\nHa vinto il giocatore {scacchiera[2][0]}")
        exit()
    if z == 9:
        print("Pareggio")
    


while z<9:
    print(f"\nTURNO DEL GIOCATORE {n}")
    while True:
        mossa_x = int(input("Inserisci la coordinata x: "))
        if mossa_x >= 0 and mossa_x <= 2:
            break
        else:
            print("La coordinata inserita è oltre i limite.")
    while True:
        mossa_y = int(input("Inserisci la coordinata y: "))
        if mossa_y >= 0 and mossa_y <= 2:
            break
        else:
            print("La coordinata inserita è oltre i limite.")
    mossa(scacchiera, mossa_x, mossa_y, n)
    if n==0:
        n = n + 1
    else:
        n = n - 1

    z = z + 1



vincita(scacchiera)

