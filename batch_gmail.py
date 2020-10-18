import yagmail

mails = ["laterzacarbonaiareservations@gmail.com",
"milleluci.milleluci@gmail.com",
"montenero@kapuziner.it",
"monza23@taiyosrl.it",
"navigli@aibalestrari.it",
"ocagiulivamilano@hotmail.it",
"parrillamexicana@live.com",
"pontdeferr@gmail.com",
"prenotazione@bon-wei.it",
"prenotazioni@ipesciolini.com",
"prenotazionidongio@gmail.com",
"restaurantharu33@gmail.com",
"ristdonjuan@hotmail.com",
"ristocittadrago@libero.it",
"ristoranteoasimilano@gmail.com",
"ristorantewarsa@gmail.com",
"ristorantewarsa@gmail.com",
"rugantinoprenotazioni@gmail.com",
"sales@ristorantenewdelhi.it",
"sciusciamare@gmail.com",
"spinuiliemarius03@yahoo.com",
"tavernagrecastelios@gmail.com",
"time.sas@tiscali.it",
"trattoriamilanese1933@gmail.com",
"vietnamonamour@gmail.com",
"xier.rutilia@hotmail.it"]

body = """
Buongiorno, 

siamo Gabriele ed Irene, dei vostri assidui e soddisfatti clienti :)

vi scriviamo perchè siete tra i nostri ristoranti milanesi di fiducia e vorremmo chiedere la vostra disponibilità a rispondere ad un brevissimo questionario di 8 domande a crocette, utile alla nostra ricerca.\n
Da qualche tempo infatti stiamo conducendo un’analisi sull'impatto ambientale dei contenitori monouso nell'industria del food delivery, con l'obiettivo di creare un’alternativa sostenibile, che sia più pratica e meno costosa per i ristoranti e i consumatori.\n
Per il nostro studio, l'opinione e l'esperienza dei ristoratori sono di estrema importanza e vi saremmo davvero grati se poteste aiutarci, rispondendo alle brevi domande che vi riportiamo al link qui sotto.

Grazie mille e al prossimo ordine!

dei vostri fan :)

Irene e Gabriele

https://docs.google.com/forms/d/1g3xetTExHmbSGiQVeypRZZr925I8NUc3HEdgyVScTaQ/edit"""

yag = yagmail.SMTP("gabriele.simeone@gmail.com")

if __name__ == "__main__":

	yagmail.register('gabriele.simeone@gmail.com', 'Mangio 4 uovar?')

	for receiver in mails:
		yag.send(
		to=receiver,
		cc="irene.stuni@gmail.com",
		subject="Qualche breve domanda da dei vostri clienti fidati.",
		contents=body)
