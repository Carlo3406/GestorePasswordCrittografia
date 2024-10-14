import ctypes
import sys
import os

#Parte principale del codice
# /////////////////////////////////////////////////////////////////////////////////////////////////////
def main():


 # Ottieni il percorso del desktop dell'utente
 desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

 # Definisci il percorso della cartella "GestoreSetting"
 folder_path = os.path.join(desktop_path, 'GestoreSetting')

 # Verifica se la cartella esiste
 if not os.path.exists(folder_path):
     # Se non esiste, crea la cartella
     os.makedirs(folder_path)
     print(f'Cartella "{folder_path}" creata con successo.')
 else:
     print(f'La cartella "{folder_path}" esiste già.')


# /////////////////////////////////////////////////////////////////////////////////////////////////////

def is_admin():
    """Verifica se lo script è eseguito come amministratore"""
    try:
        # è una funzione della libreria ctypes è verifica se l'utente è admin
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == "__main__":
    if is_admin():
        # Inserisci qui il tuo codice che necessita di permessi amministrativi
        print("Esecuzione con privilegi di amministratore!")
        main()
        # Aggiungi una pausa per impedire la chiusura immediata dello script
        input("Premi Invio per uscire...")
    else:
        # Riavvia lo script con privilegi elevati
        print("Richiesta esecuzione come amministratore...")
        #è una funzione di os che è usata per ottenere il percorso assoluto dello script python
        script_path = os.path.abspath(sys.argv[0])
        try:
            #è una chiamata alla funzione di ctypes per eseguire lo script con privilegi di amministratore
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, script_path, None, 1
            )
        except Exception as e:
            print(f"Errore durante il tentativo di eseguire con privilegi elevati: {e}")
        # Aggiungi una pausa per vedere il messaggio di errore
        input("Premi Invio per chiudere...")
