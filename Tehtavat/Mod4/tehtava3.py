sukupuoli = str(input("Anna sukupuoli: "))
hemoglobiiniarvo = float(input("Anna hemoglobiiniarvo: "))
if sukupuoli == "M":
    if hemoglobiiniarvo < 117:
        print("Alhainen hemoglobiiniarvo")
    elif hemoglobiiniarvo > 195:
        print("Korkea hemoglobiiniarvo")
    else:
        print("Normaali hemoglobiiniarvo")
        
elif sukupuoli == "N":
    if hemoglobiiniarvo < 117:
        print("Alhainen hemoglobiiniarvo")
    elif hemoglobiiniarvo > 175:
        print("Korkea hemoglobiiniarvo")
    else:
        print("Normaali hemoglobiiniarvo")
else:
    print("Virheellinen sukupuoli")