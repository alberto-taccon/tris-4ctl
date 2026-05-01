import pymysql

# ==================================
#      DATABASE CONFIGURATION
# ==================================
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

# ==================================
#             FUNCTIONS
# ==================================
def stampa_scacchiera(scacchiera):
    for riga in scacchiera:
      print(f"{riga[0]} | {riga[1]} | {riga[2]}")

def mossa(scacchiera, mossa_x, mossa_y, n):
    if (scacchiera[mossa_x][mossa_y]) != '_':
        print("Il punto inserito è già occupato. Riprova")
        return False
    if (scacchiera[mossa_x][mossa_y]) == '_':
        if n == 0:
          simbolo = 'X'
        elif n == 1:
          simbolo = 'O'
        scacchiera[mossa_x][mossa_y] = simbolo
        stampa_scacchiera(scacchiera)

def vincita(scacchiera, id_giocatore1, id_giocatore2, conn, id_match):
    # 00 - 01 - 02
    if scacchiera[0][0]==scacchiera[0][1] and scacchiera[0][0] == scacchiera[0][2] and scacchiera[0][0]!='_' and scacchiera[0][1]!='_' and scacchiera[0][2]!='_':
        print(f"\nHa vinto il giocatore {scacchiera[0][0]}")
        inserisci_vittoria(conn, id_match, id_giocatore1 if scacchiera[0][0] == 'X' else id_giocatore2)
        exit()
    # 00 - 10 - 20
    elif scacchiera[0][0]==scacchiera[1][0] and scacchiera[0][0] == scacchiera[2][0] and scacchiera[0][0]!='_' and scacchiera[1][0]!='_' and scacchiera[2][0]!='_':
        print(f"\nHa vinto il giocatore {scacchiera[0][0]}")
        inserisci_vittoria(conn, id_match, id_giocatore1 if scacchiera[0][0] == 'X' else id_giocatore2)
        exit()
    # 00 - 11 - 22 (diagonale 135)
    elif scacchiera[0][0]==scacchiera[1][1] and scacchiera[0][0] == scacchiera[2][2] and scacchiera[0][0]!='_' and scacchiera[1][1]!='_' and scacchiera[2][2]!='_':
        print(f"\nHa vinto il giocatore {scacchiera[0][0]}")
        inserisci_vittoria(conn, id_match, id_giocatore1 if scacchiera[0][0] == 'X' else id_giocatore2)
        exit()
    # 02 - 11 - 20 (diagonale 45)
    elif scacchiera[0][2]==scacchiera[1][1] and scacchiera[0][2] == scacchiera[2][0] and scacchiera[0][2]!='_' and scacchiera[1][1]!='_' and scacchiera[2][0]!='_':
        print(f"\nHa vinto il giocatore {scacchiera[0][2]}")
        inserisci_vittoria(conn, id_match, id_giocatore1 if scacchiera[0][2] == 'X' else id_giocatore2)
        exit()
    # 01 - 11 - 21
    elif scacchiera[0][1]==scacchiera[1][1] and scacchiera[0][1] == scacchiera[2][1] and scacchiera[0][1]!='_' and scacchiera[1][1]!='_' and scacchiera[2][1]!='_':
        print(f"\nHa vinto il giocatore {scacchiera[0][1]}")
        inserisci_vittoria(conn, id_match, id_giocatore1 if scacchiera[0][1] == 'X' else id_giocatore2)
        exit()
    # 02 - 12 - 22
    elif scacchiera[0][2]==scacchiera[1][2] and scacchiera[0][2] == scacchiera[2][2] and scacchiera[0][2]!='_' and scacchiera[1][2]!='_' and scacchiera[2][2]!='_':
        print(f"\nHa vinto il giocatore {scacchiera[0][2]}")
        inserisci_vittoria(conn, id_match, id_giocatore1 if scacchiera[0][2] == 'X' else id_giocatore2)
        exit()
    # 10 - 11 - 12
    elif scacchiera[1][0]==scacchiera[1][1] and scacchiera[1][0] == scacchiera[1][2] and scacchiera[1][0]!='_' and scacchiera[1][1]!='_' and scacchiera[1][2]!='_':
        print(f"\nHa vinto il giocatore {scacchiera[1][0]}")
        inserisci_vittoria(conn, id_match, id_giocatore1 if scacchiera[1][0] == 'X' else id_giocatore2)
        exit()
    # 20 - 21 - 22
    elif scacchiera[2][0]==scacchiera[2][1] and scacchiera[2][0] == scacchiera[2][2] and scacchiera[2][0]!='_' and scacchiera[2][1]!='_' and scacchiera[2][2]!='_':
        print(f"\nHa vinto il giocatore {scacchiera[2][0]}")
        inserisci_vittoria(conn, id_match, id_giocatore1 if scacchiera[2][0] == 'X' else id_giocatore2)
        exit()
    elif z == 9:
        print("Pareggio")
        inserisci_vittoria(conn, id_match, None)
    

# ==================================
#             FUNCTIONS DB
# ==================================
def esegui_dml(connection, query, params):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        connection.commit()
        return cursor.lastrowid


def inserisci_utente(connection, x, y):
    if duplicati_check(connection, y) == True:
        print(f"L'utente è già inserito nel database.")
        return cerca_id_utente(connection, y)
    elif duplicati_check(connection, y) == False:
        query = "INSERT INTO users (nome, CF) VALUES (%s, %s)"
        params = (x, y)
        return esegui_dml(connection, query, params)

def duplicati_check(connection, cf):
    query = "SELECT 1 FROM users WHERE CF = %s LIMIT 1"
    params = (cf,)
    cursor = connection.cursor()
    cursor.execute(query, params)
    if cursor.fetchone():
        return True
    else:        
        return False

def cerca_id_utente(connection, cf):
    query = "SELECT id_user FROM users WHERE CF = %s LIMIT 1"
    params = (cf,)
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        riga = cursor.fetchone()
        return riga[0] if riga else None

def inserisci_match_users(connection, id_giocatore1, id_giocatore2):
    query = "INSERT INTO match_users (id_user_1, id_user_2, date) VALUES (%s, %s, NOW())"
    params = (id_giocatore1, id_giocatore2)
    return esegui_dml(connection, query, params)

def inserisci_match_results(connection, id_m_u, id_user_vincitore=None):
    query = "INSERT INTO match_results (id_m_u, id_user_vincitore) VALUES (%s, %s)"
    params = (id_m_u, id_user_vincitore)
    return esegui_dml(connection, query, params)

def inserisci_vittoria(connection, id_match, cf):
    query = "UPDATE match_results SET id_user_vincitore = %s WHERE id_match_results = %s"
    params = (cf, id_match)
    return esegui_dml(connection, query, params)

def leggi_coordinata(nome):
    while True:
        try:
            coordinata = int(input(f"Inserisci la coordinata {nome}: "))
        except ValueError:
            print("Inserisci un numero intero tra 0 e 2.")
            continue

        if coordinata >= 0 and coordinata <= 2:
            return coordinata
        print("La coordinata inserita è oltre il limite.")
    
# =================================
#              MAIN
# =================================
def main():
    # ==================================
    #            DECLARATION
    # ==================================
    global scacchiera 
    scacchiera = [['_','_','_'],['_','_','_'],['_','_','_']]
    # n=0
    # z=0
    global n,z  
    n,z = 0,0 # ho chiesto a chatgpt se si potesse fare in altro modo(è molto più bello)

    conn = None

    try:
        try:
            conn = get_connection()
            print("Connessione riuscita.")
        except pymysql.MySQLError as exc:
            print(f"Database non raggiungibile, la partita non verrà salvata: {exc}")

        print("Benvenuto al gioco del tris!")
        print("Il giocatore 1 è X, il giocatore 2 è O.")
        nome_giocatore1 = input("Inserisci il nome del giocatore 1: ")
        cf_giocatore1 = input("Inserisci il codice fiscale del giocatore 1: ")
        nome_giocatore2 = input("Inserisci il nome del giocatore 2: ")
        cf_giocatore2 = input("Inserisci il codice fiscale del giocatore 2: ")

        id_giocatore1 = None
        id_giocatore2 = None
        id_match_results = None
        if conn:
            id_giocatore1 = inserisci_utente(conn, nome_giocatore1, cf_giocatore1)
            id_giocatore2 = inserisci_utente(conn, nome_giocatore2, cf_giocatore2)
            id_m_u = inserisci_match_users(conn, id_giocatore1, id_giocatore2)
            id_match_results = inserisci_match_results(conn, id_m_u)

        print(f"\nIl giocatore 1 è {nome_giocatore1}({cf_giocatore1}) e il giocatore 2 è {nome_giocatore2}({cf_giocatore2}) .")
        while z<9:
            if n == 0:
                f="X"
            else:        
                f="O"

            print(f"\nTURNO DEL GIOCATORE {f}")
            while True:
                mossa_x = leggi_coordinata("x")
                mossa_y = leggi_coordinata("y")
                
                if mossa(scacchiera, mossa_x, mossa_y, n) == False:
                    continue
                else:
                    break
            if n==0:
                n = n + 1
            else:
                n = n - 1
            z = z + 1

            vincita(scacchiera, id_giocatore1, id_giocatore2, conn, id_match_results)
    except pymysql.MySQLError as exc:
        if conn:
            conn.rollback()
        print(f"Errore database: {exc}")

    finally:
        if conn:
            conn.close()
            print("\nConnessione chiusa.")


if __name__ == "__main__":
    main()
