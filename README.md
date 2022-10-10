#Exatel
- Otrzymane dane są w formacie json
- Aby uruchomić część główną programu za pomocą Dockerfile'a należy będąc
w folderze Exatel uruchomić komendę "docker build --tag='<nazwa_taga>' task/
"
- w celu uruchomienia testów należy użyć tej samej komendy z tym że zamiast
ścieżki "task/" użyć "tests/"

Rozwiązując dane zadanie postanowiłem przyjąć kilka założeń:
- mimo iż użytych fumkcji można użyć do wyciągnięcia innych danych niż tylko
wymaganych z punktu widzenia zadania to nazwy w nich użyte mają
określać działanie kodu tylko dla określonych wymagań w danym momencie (pobranie nazwy regionu)
- jako region przyjąłem nazwę kraju albowiem niektóre z nich powtarzały się
w kolejnych wierszach json'a
- jako ilość pieniędzy zainwestowanych w rany projek przyjąłem klucz "totalamt"