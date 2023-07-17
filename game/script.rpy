# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character(None, what_xalign=0.5, what_text_align=0.5, what_size=28)

define nazz = Character("Nazz")
define cynthia = Character("Cynthia")
define dorian = Character("Dorian")

label start:
    
    pause

    scene black

    play music 'audio/music theory fur elise.mp3' fadein 2 volume 0.3

    queue music 'audio/music theory rush e.mp3' volume 0.3
    queue music 'audio/music theory fur elise.mp3' volume 0.3
    queue music 'audio/music theory rush e.mp3' volume 0.3

    pause 1.85

    scene bg banquet at center
    play sound "glass.mp3"

    with Shake((0, 0, 0, 0), 0.2, dist=15)
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png"to the images
    # directory.


    # These display lines of dialogue.

    narrator "Uderzenie kieliszka — z niezbyt starannych obliczeń Nazz wynikało, że siódmego — o blat, byłoby zapewne słychać na drugim końcu sali, gdyby muzykanci nie grali właśnie... tego co im serce podpowie?..."
    narrator "Patrząc na to ile wypili — ciężko było grać coś innego."
    nazz "Nigdy Cię nie zrozumiem... Za dwa dni mamy egzamin, a ty pijesz jakby jutra nie było."
  
    show cynthia
    with dissolve
    
    narrator "Cynthia przyłożyła grzbiet dłoni do ust — widać było, że potrzebowała jeszcze chwili by pozbierać się po tym co właśnie wypiła."
    cynthia "Przecież dwa dni to sporo czasu..."
    cynthia "Poza tym co niby lepszego mam do roboty?"
    cynthia "Mam się uczyć? Teraz — na balu?"
    menu:
        "Oczywiście, że masz się uczyć!":
            nazz "Nie po to przynosiłam skrypty, by z nich teraz nie skorzystać!"
            cynthia "Co? Czy ty naprawdę..."
            narrator "Po rzuceniu wzrokiem na torbę przy krześle Nazz — z której wystawały pergaminy, Cynthia wybuchła śmiechem... każdy wybuchłby śmiechem."
            nazz "Z czego się niby śmiejesz!? Może niektórym zależy na przyszłości?"
            cynthia "Mhh..."
            cynthia "Nie!"
            cynthia "Nikomu nie zależy."

        "Nieee?":
            cynthia "Szkoda... Miałam naprawdę chęć pouczyć się o... o tym co aktualnie mamy..."
            nazz "Nie miałaś! Nawet nie wiesz co aktualnie mamy."
            cynthia "To prawda... Nie miałam."
   
    cynthia "..."
    cynthia "W ogóle, kto wymyślił ten bal?"
    cynthia "W sensie..."
    cynthia "Dlaczego on jest? "
    cynthia "Przecież nic ważnego się nie dzieje."
    cynthia "..."
    nazz "Przecież, na zaproszeniu miałaś, że Lyra urodziny..."
    cynthia "Na moje urodziny nie było gargantuicznej imprezy!"
    cynthia "Ha! GARGANTUICZNEJ!"
    nazz "..."
    nazz "Może zaprosiła nas wszystkich tutaj z jakiegoś nikczemnego powodu..."
    nazz "Może chce nas wszystkie otruć..."
    cynthia "Dlaczego niby chciałby nas otruć!?"
    nazz "Dlatego, że jest złą wiedźmą, która potrzebuje krwi do przeprowadzenia tajemnych rytuałów, które..."
    cynthia "A co jeżeli nie jest wiedźmą, lecz szalonym alchemikiem, a nasza krew jest jej potrzebna na bazę do różnego rodzaju napojów!"
    nazz "Krwawe napoje powiadasz?"
    cynthia "Krwawe napoje powiadam."
    cynthia "..."
    cynthia "Nie..."
    cynthia "To nie ma sensu... "
    cynthia "A może..."
    nazz "A morze jest głębokie i szerokie!"
    cynthia "Nie śmieszne..."
    narrator "Zapadła cisza"
    cynthia "Czekaj chwilę..."
    cynthia "To jest impreza urodzinowa?"
    cynthia "Czy to znaczy, że miałam kupić prezent?"
    nazz "..."
    cynthia "Ale jestem okropna..."
    cynthia "Z drugiej strony..."
    cynthia "Będzie miałą tyle prezentów, że pewnie nie zauważy, że brakuje mojego..."
    nazz "Ha! Jesteś kompletnie przewidywalna!"
    cynthia "Hm?"
    nazz "Wiedziałam, że nic nie kupisz, więc — dałam jej “nasz” prezent..."
    cynthia "URATOWANA!"
    nazz "Jutro się rozliczymy."
    cynthia "Co, z czego?"
    nazz "Wisisz mi za “nasz” prezent."
    cynthia "..."
    cynthia "No nic..."
    cynthia "Trzeba opić bycie uratowanym! "
    cynthia "Trzeba opić zwycięstwo!"
    cynthia "Zapewne kosztowne zwycięstwo..."
    nazz "Bardzo kosztowne..."
    cynthia "Eh..."
    narrator "Zamaszystym ruchem Cynthia chwyciła karafkę stojącą przy niej i swoimi brwiami spytała się Nazz czy nie chce może z nią skosztować zielonego płynu."
    menu: 
        "Niech będzie...":
            narrator "Dziewczyna nalała sobie po brzegi, chwyciła za szkło, a następnie podniosła je do ust... i odstawiła na stół."
            cynthia "Czy Ty powiedziałaś, że reflektujesz na napój?"
            cynthia "Ha! REFLEKTUJESZ!"
            nazz "..."
            nazz "Też w to nie wierzę, ale.. chyba możesz mi nalać?"
            cynthia "W sumie to spytałam, tylko z grzeczności..."
            cynthia "Dobra gdzie masz szkło!"
            narrator "Niczym zawodowy oberżysta — lub moczymorda — Cynthia polała Nazz nic nie żałując."
            cynthia "To co?"
            cynthia "Szybko, bo szkłem przejdzie!"
            narrator "Zamaszystym ruchem Cynthia wlała płyn w swe gardło."
            narrator "Trochę z mniejszą gracją, lecz równie zamaszyście, Nazz uczyniła to samo."
            nazz "Ekhm!"
        
        "Wiesz, że nie trawię tego...":
            cynthia "Ale zawsze warto próbować!"
            cynthia "No nic..."
            narrator "Szybkim ruchem Cynthia wlała płyn w swe gardło."
    
    jump prologue_II