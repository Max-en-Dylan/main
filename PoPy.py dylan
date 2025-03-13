from appJar import gui

def bereken_bmi():
    try:
        gewicht = float(app.getEntry("Gewicht (kg)"))
        lengte = float(app.getEntry("Lengte (m)"))
        bmi = gewicht / (lengte ** 2)
        bmi = round(bmi, 2)
        
        if bmi < 18.5:
            advies = "Je hebt ondergewicht. Probeer gezond aan te komen."
        elif 18.5 <= bmi < 25:
            advies = "Je hebt een gezond gewicht. Goed bezig!"
        elif 25 <= bmi < 30:
            advies = "Je hebt overgewicht. Meer beweging en een gezond dieet kunnen helpen."
        else:
            advies = "Je hebt obesitas. Overleg met een arts voor advies."
        
        app.setLabel("resultaat", f"Je BMI is {bmi}. {advies}")
    except:
        app.setLabel("resultaat", "Fout: Voer geldige getallen in.")

def bereken_bmr():
    try:
        geslacht = app.getOptionBox("Geslacht")
        gewicht = float(app.getEntry("Gewicht (kg)"))
        lengte = float(app.getEntry("Lengte (cm)"))
        leeftijd = int(app.getEntry("Leeftijd"))

        if geslacht == "Man":
            bmr = 88.36 + (13.4 * gewicht) + (4.8 * lengte) - (5.7 * leeftijd)
        else:
            bmr = 447.6 + (9.2 * gewicht) + (3.1 * lengte) - (4.3 * leeftijd)

        bmr = round(bmr, 2)
        app.setLabel("resultaat", f"Je dagelijkse caloriebehoefte (BMR) is {bmr} kcal.")
    except:
        app.setLabel("resultaat", "Fout: Voer geldige getallen in.")

def bereken_water():
    try:
        gewicht = float(app.getEntry("Gewicht (kg)"))
        water = gewicht * 0.03  
        water = round(water, 2)
        app.setLabel("resultaat", f"Je moet dagelijks ongeveer {water} liter water drinken.")
    except:
        app.setLabel("resultaat", "Fout: Voer geldige getallen in.")


app = gui("Gezondheids Calculator", "400x400")
app.setBg("#f0f0f0")
app.setFont(14)

app.addLabel("titel", "Gezondheids Calculator", 0, 0, 2)
app.addLabel("sub", "Kies een berekening:", 1, 0, 2)


app.addLabelEntry("Gewicht (kg)", 2, 0, 2)
app.addLabelEntry("Lengte (m)", 3, 0, 2)
app.addLabelEntry("Lengte (cm)", 4, 0, 2)
app.addLabelEntry("Leeftijd", 5, 0, 2)


app.addLabel("geslacht_label", "Geslacht:", 6, 0)
app.addOptionBox("Geslacht", ["Man", "Vrouw"], 6, 1)


app.addButton("Bereken BMI", bereken_bmi, 7, 0)
app.addButton("Bereken BMR", bereken_bmr, 8, 0)
app.addButton("Bereken Waterinname", bereken_water, 9, 0)


app.addLabel("resultaat", " Resultaat komt hier...", 10, 0, 2)


app.go()
