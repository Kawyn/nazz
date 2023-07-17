label prologue_II: 

    show dorian at left
    with Shake((0, 0, 0, 0), 0.2, dist=15)


    dorian "NAZZ!!"
    nazz "O, nie!"
    dorian "Muszę przerwać waszą poważną rozmowę, ale..."
    nazz "Czyżby już wszystkie dziewczyny odrzuciły Twoje zaloty więc łapiesz się brzytwy?"
    dorian "Co?"
    dorian "NIE!"
    dorian "Żadna jeszcze nie była wstanie oprzeć się moim zalotą!"

    show cynthia at right
    with dissolve

    cynthia "To prawda..."
    cynthia "Twoje krasne oczy... "
    nazz "CO?!"
    dorian "CO?!"
    cynthia "Co “CO”?!"
    cynthia "Ja nic nie mówiłam..."
    dorian "..."
    dorian "Nie o tym teraz!"
    dorian "Jest sprawa Nazz. Zgubiłem coś Twojego w ogrodzie... i musisz to odzyskać!?"
    nazz "Co!? Kto pozwolił Ci ruszać moje rzeczy!?"
    dorian "Cynthia..."
    cynthia "To nie prawda!"
    dorian "Pra..."
    nazz "Nie będę po to szła. Czemu mam iść po coś co Ty zgubiłeś!?"
    dorian "Bo Ty chcesz to odzyskać?"
    nazz "Ale to Ty to  zgubiłeś!"
    dorian "No nic... nie pozostawiasz mi wyboru..."
    narrator "Dorian usiadł na wolnym krześle przy Cynthii i wstrzymał oddech."
    menu:
        
        "He? Jak to niby ma mnie przekonać, abym to Ja poszła?":
            narrator "Dorian uśmiechnął się i wstrzymał wykonywanie niecnego planu by objaśnić Nazz jego geniusz."
            dorian "Gdy stracę przytomność nie będę w stanie samemu chodzić. Czyż nie?"
            nazz "No..."
            dorian "To oznacza, że ty będziesz jedyną osobą mogącą wyruszyć na wyprawę by odzyskać Twoją rzecz!"
            narrator "Dorian ponownie wstrzymał oddech, będąc dumnym ze swojego planu."
            cynthia "Muszę przyznać... Dorian jest..."
            cynthia "Geniuszem!"
        
        "...":
            dorian "..."

    menu: 
        "...":
            dorian "..."
        "Dobra... Już idę!":
            jump lost
        
    menu: 
        "...":
            dorian "..."
        "Dobra... Już idę!":
            jump lost
        
    menu: 
        "...":
            jump won
        "Dobra... Już idę!":
            jump lost

label won:

    play sound "minecraft death.mp3"
    hide dorian
    with Shake((0, 0, 0, 0), 0.2, dist=15)

    narrator "Dorian osunął się na krześle, nieprzytomny. Zapewne w swojej głowie właśnie rozkoszował się zwycięstwem"
  
    nazz "No nic... zaraz wrócę."
    nazz "Patrz go w między czasie, by nic głupszego nie zrobił."
  
    show cynthia at center
    with dissolve

    cynthia "Nie musisz się martwić!"

    cynthia "Przy mnie będzie bezpieczny niczym..."
    cynthia "Niczym ta karafka!"
  
    narrator "Cynthia podniosła butelkę ze stołu i nalała sobie blado-zieloną zawartość." 

    jump prologue_III

label lost:

    dorian "Kolejne zwycięstwo!"
    dorian "Ale z drugiej strony — nie okazałem pełnej dominacji..."
    dorian "Połowiczne zwycięstwo!"

    nazz "Eh..."
    nazz "Pogadamy jutro... bez świadków!"

    jump prologue_III