from services.scrap import run

if __name__ == '__main__':

    # Scraping Data From Gmaps
    url = "https://www.google.com/maps/place/Air+Terjun+Grojogan+Sewu/@-7.6608394,110.8259177,11z/data=!4m13!1m3!2m2!1swisata+jawa+tengah!6e1!3m8!1s0x2e798a3aaef24383:0x3d3da6236af2202a!8m2!3d-7.6608394!4d111.1307883!9m1!1b1!15sChJ3aXNhdGEgamF3YSB0ZW5nYWhaFCISd2lzYXRhIGphd2EgdGVuZ2FokgESdG91cmlzdF9hdHRyYWN0aW9umgEkQ2hkRFNVaE5NRzluUzBWSlEwRm5TVVJYZUhSeGFGOUJSUkFC4AEA!16s%2Fm%2F056n6r1?entry=ttu"
    run(url=url)
