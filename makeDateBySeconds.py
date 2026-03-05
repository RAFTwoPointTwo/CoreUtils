print("\n ::: Conversion de secondes en Date ::: \n")

sec = -1

while sec < 0:
    try:
        sec = int(input("\n * Entrez une quantité de secondes : "))
    except ValueError:
        print("\n !! Veuillez entrer un entier !! \n")

SECONDS_IN_YEAR = 3600 * 24 * 30 * 12
SECONDS_IN_MONTH = 3600 * 24 * 30
SECONDS_IN_DAY = 3600 * 24
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

TIME_LEFT_AFTER_YEAR = sec % SECONDS_IN_YEAR
TIME_LEFT_AFTER_MONTH = TIME_LEFT_AFTER_YEAR % SECONDS_IN_MONTH
TIME_LEFT_AFTER_DAY = TIME_LEFT_AFTER_MONTH % SECONDS_IN_DAY
TIME_LEFT_AFTER_HOUR = TIME_LEFT_AFTER_DAY % SECONDS_IN_HOUR
TIME_LEFT_AFTER_MINUTE = TIME_LEFT_AFTER_HOUR % SECONDS_IN_MINUTE


years = sec // SECONDS_IN_YEAR
months = TIME_LEFT_AFTER_YEAR // SECONDS_IN_MONTH
days = TIME_LEFT_AFTER_MONTH // SECONDS_IN_DAY
hours = TIME_LEFT_AFTER_DAY // SECONDS_IN_HOUR
minutes = TIME_LEFT_AFTER_HOUR // SECONDS_IN_MINUTE
seconds = TIME_LEFT_AFTER_MINUTE


print(f"\n ::: Le format de cette quantité de secondes en date est : {years:02d} an(s) {months:02d} mois {days:02d} jour(s) {hours:02d} heure(s) {minutes:02d} minute(s) et {seconds:02d} seconde(s) . \n")