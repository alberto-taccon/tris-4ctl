# TRIS
Alberto Taccon, Natan Cavina, Federico Poli

## SUDDIVISONE DEI RUOLI
Taccon: SQL+CODICE
Poli: UN CAZZO 
Cavina: DESCRIZIONE+SCHEMA RELAZIONARE 

## DESCRIZIONE
La parte iniziale "DATABASE CONFIGURATION" serve per instaurare una connesione con il database MySQl attraverso la libreria pymysql, per instaurare la connessione è necessario: l'indirizzo host del server in questo caso 127.0.0.1 , l'user e password  registrato per fare l'accesso al database, il nome del database si desidera utilizzare, la port:3307 che viene usata per instaurare la connessione, "timeout di connessione" indica il tempo di attesa dopo il quale la richiesta di accesso al server viene abbattuta nel nostro caso 5 secondi.
La parte "FUNZIONI" riguarda il funzionamento dal punto di vista del gioco, la prima funzione riceve come argomento "giacca" e tramite un loop stampa la griglia per ogni riga,
