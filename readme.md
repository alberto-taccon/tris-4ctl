# TRIS
Alberto Taccon, Natan Cavina, Federico Poli

## SUDDIVISONE DEI RUOLI
Codice python: Alberto Taccon
Schema relazionale + foto: Natan Cavina
Descrizione progetto: Alberto Taccon & Federico Poli

## DESCRIZIONE
Il progetto consiste in una versione del gioco del Tris realizzata in Python ed eseguibile da terminale. Due giocatori inseriscono il proprio nome e codice fiscale, poi si alternano scegliendo le coordinate della casella in cui posizionare il proprio simbolo: il giocatore 1 utilizza `X`, mentre il giocatore 2 utilizza `O`.

Il programma mostra la scacchiera dopo ogni mossa, controlla che le coordinate siano valide e impedisce di occupare una casella già utilizzata. Dopo ogni turno verifica automaticamente tutte le possibili combinazioni di vittoria: righe, colonne e diagonali. Se nessun giocatore riesce a completare una combinazione vincente entro le nove mosse disponibili, la partita termina in pareggio.

Oltre alla logica del gioco, il progetto include il collegamento a un database MySQL. Il database permette di registrare gli utenti, evitare duplicati tramite il codice fiscale, salvare le partite giocate e memorizzare il risultato finale, cioè il vincitore oppure il pareggio. Lo schema relazionale è definito nel file `tris.sql` e contiene le tabelle `users`, `match_users` e `match_results`.

Il sistema permette inoltre di analizzare i dati delle partite salvate: è possibile visualizzare la classifica dei primi 5 o 10 giocatori con il maggior numero di vittorie e consultare le statistiche di un singolo giocatore, tra cui partite giocate, partite vinte, partite perse e win rate.

