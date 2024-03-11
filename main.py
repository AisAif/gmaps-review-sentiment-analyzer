from services.scrap import run

if __name__ == '__main__':
    
    # Scraping Data From Gmaps
    url = 'https://www.google.com/maps/place/Pasar+Jetak/@-6.784863,111.3781444,13.89z/data=!4m16!1m9!3m8!1s0x2e773c81d9ccb39b:0xecbce8a5501796d1!2sPasar+Sulang!8m2!3d-6.8073457!4d111.3799229!9m1!1b1!16s%2Fg%2F1hm4wbq92!3m5!1s0x2e773cd455970d05:0xf0324592960bba11!8m2!3d-6.7704319!4d111.4241411!16s%2Fg%2F11cmmschm7?entry=ttu'
    run(url=url)