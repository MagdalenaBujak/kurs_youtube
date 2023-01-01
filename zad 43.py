waga = float(input("podaj swoją wagę:"))
wzrost = float(input("podaj wzrost w cm: "))
bmi = (waga/((wzrost/100) **2))

if bmi >= 18.5 and bmi <= 24.9:
    print(f"waga prawidłowa, Twoje BMI wynosi {bmi}")
elif bmi > 24.9:
    print(f"Nadwaga!Twoje BMI wynosi {bmi}")
elif bmi < 18.5:
    print(f"Niedowaga! Twoje BMI wynosi {bmi}")