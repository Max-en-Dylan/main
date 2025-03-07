from appJar import gui
from collections import Counter

def calculate_frequency():
    word = app.getEntry("voer woord of zin in:").lower()

    Alphabet = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z'
    ]

    hits = [
        (letter, word.count(letter))
        for letter in Alphabet
        if word.count(letter) > 0
    ]

    result = "\n".join([f"{letter.upper()}: {frequency}" for letter, frequency in hits])

    app.setLabel("resultaat", result)

def show_as_stars():
    word = app.getEntry("voer woord of zin in:").lower()

    Alphabet = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z'
    ]

    hits = [
        (letter, word.count(letter))
        for letter in Alphabet
        if word.count(letter) > 0
    ]

    result = "\n".join([f"{letter.upper()}: {'*' * frequency}" for letter, frequency in hits])

    app.setLabel("resultaat", result)

def show_l_and_h():
    word = app.getEntry("voer woord of zin in:").lower()

    counter = Counter(word)
    hits = [(letter, freq) for letter, freq in counter.items() if letter.isalpha()]

    if hits:
        top_freq = max(hits, key=lambda x: x[1])
        low_freq = min(hits, key=lambda x: x[1])

        res_low = f"De minst voorkomende letter is: {low_freq[0].upper()}, die {low_freq[1]} keer voor komt"
        res_high = f"De meest voorkomende letter is: {top_freq[0].upper()}, die {top_freq[1]} keer voor komt"

        app.setLabel("Low", res_low)
        app.setLabel("High", res_high)
    else:
        app.setLabel("Low", "Geen letters gevonden.")
        app.setLabel("High", "Geen letters gevonden.")

app = gui("Letterfrequentie Teller", "400x300")
app.addLabel("instructie", "Voer een woord of zin in:")
app.addEntry("voer woord of zin in:")
app.addButton("Bereken frequentie", calculate_frequency)
app.addButton("Toon als sterren", show_as_stars)
app.addButton("Toon meest en minst frequent", show_l_and_h)
app.addLabel("resultaat", "")
app.addLabel("Low", "")
app.addLabel("High", "")

app.go()
