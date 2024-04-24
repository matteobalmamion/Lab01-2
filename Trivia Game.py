from random import shuffle
class Domanda():
    def __init__(self,domanda,risposte,punteggio,risposta_corretta):
        self.domanda=domanda
        self.risposte=risposte
        self.punteggio=punteggio
        self.risposta_corretta=risposta_corretta

    def __str__(self):
        return f"{self.domanda} ({self.punteggio})\n{self.risposte[0]} (Risposta corretta)\n{self.risposte[1]}\n{self.risposte[2]}\n{self.risposte[3]}"
class Giocatore():
    def __init__(self,nome,punteggio):
        self.nome=nome
        self.punteggio=punteggio
    def __str__(self):
        return f"{self.nome} {self.punteggio}"
class Gioco():

    def __init__(self):
        self.domande={}
    # legge e memorizza la lista di domande
    def lettura_file(self, nome_file):
        try:
            file = open(nome_file, 'r', encoding='utf-8')
        except FileNotFoundError:
            print("Errore, file non trovato")
        line = " "
        while line != "":
            i = 1
            ask=""
            punteggio=0
            risposta_corretta=""
            risposte=[]
            while i < 7:
                if i == 1:
                    line = file.readline().strip()
                    ask = line
                elif i == 2:
                    line = file.readline().strip()
                    punteggio = (line)
                elif i == 3:
                    line = file.readline().strip()
                    risposta_corretta = line
                    risposte.append(line)
                else:
                    line = file.readline().strip()
                    risposte.append(line)
                i += 1
            domanda=Domanda(ask,risposte,punteggio,risposta_corretta)
            # divide le domande in base alla difficoltà
            if punteggio in self.domande:
                domande_punteggio=self.domande[punteggio]
                domande_punteggio.append(domanda)
            else:
                self.domande[punteggio]=[domanda]
            line = file.readline()

    # propone casualmente una domanda della difficoltà necessaria e stampa le risposte
    def proponi_domanda(self,punteggio):
        lista_domande=self.domande[str(punteggio)]
        shuffle(lista_domande)
        domanda_scelta=lista_domande[0]
        print(f"Livello: {punteggio} {domanda_scelta.domanda}")
        shuffle(domanda_scelta.risposte)
        answers={}
        i=1
        for ans in domanda_scelta.risposte:
            print(f"{i}. {ans}")
            answers[i]=ans
            i+=1
        # il giocatore dà una risposta
        risposta=input("Inserisci la risposta corretta: ")
        if answers[int(risposta)]==domanda_scelta.risposta_corretta:
            print("Risposta corretta")
            return True
        else:
            print(f"Risposta sbagliata! La risposta corretta era: {domanda_scelta.risposta_corretta}")
            return False

    # salva il punteggio nel file aggiornandolo in ordine decrescente di punteggio
    def aggiungi_nickname(self,giocatore,nome_file):
        try:
            file = open(nome_file, 'r', encoding='utf-8')
        except FileNotFoundError:
            print("Errore, file non trovato")
        line=file.readline().split(" ")
        giocatori=[]
        while line != [""]:
            gamer=Giocatore(line[0],line[1].strip())
            giocatori.append(gamer)
            line = file.readline().split(" ")
        file.close()
        try:
            file = open(nome_file, 'w', encoding='utf-8')
        except FileNotFoundError:
            print("Errore, file non trovato")
        cond=False
        for g in giocatori:
            if int(g.punteggio)>int(giocatore.punteggio):
                file.write(f"{g.nome} {g.punteggio}\n")
                continue
            elif cond==True:
                file.write(f"{g.nome} {g.punteggio}\n")
                continue
            else:
                cond=True
                file.write(f"{giocatore.nome} {giocatore.punteggio}\n")
                file.write(f"{g.nome} {g.punteggio}\n")
                continue
        file.close()




    def gioco(self):
        name_file="domande.txt"
        self.lettura_file(name_file)
        risposta=True
        punteggio=0
        # il giocatore dà una risposta, se corretta continua e +1 se sbagliata finisce
        while risposta==True:
            risposta=self.proponi_domanda(punteggio)
            if risposta==True:
                punteggio+=1
            if punteggio>int(max(self.domande)):
                print("Complimenti! Hai vinto")
                risposta=False
        # visualizza il punteggio e chiede di inserire un nome
        print(f"Hai totalizzato {punteggio} punti!")
        nome=input("Inserisci il nickname: ")
        giocatore=Giocatore(nome,punteggio)
        nome_file="punti.txt"
        self.aggiungi_nickname(giocatore,nome_file)



if __name__=="__main__":
    gioco=Gioco()
    gioco.gioco()












