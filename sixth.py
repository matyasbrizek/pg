import sys
import requests
import re


def download_url_and_get_all_hrefs(url):
    """
    Funkce stáhne obsah URL předaného v parametru `url` pomocí requests.get().
    Zkontroluje, zda response.status_code je 200. Pokud ano, najde ve staženém
    obsahu všechny výskyty <a href="url">odkaz</a> a vrátí seznam URL pomocí return.
    """
    hrefs = []

    try:
        # Stáhne obsah stránky
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Chyba při stahování URL: Status kód {response.status_code}")

        # Vyhledá všechny odkazy pomocí regulárních výrazů
        content = response.content.decode('utf-8', errors='ignore')  # Dekódování obsahu
        hrefs = re.findall(r'<a\s+href="([^"]+)"', content)  # Hledání odkazů v tagu <a>
    except Exception as e:
        print(f"Chyba při zpracování: {e}")

    return hrefs


if __name__ == "__main__":
    try:
        # Přečíst URL ze vstupu
        if len(sys.argv) < 2:
            raise ValueError("Nebyla poskytnuta URL jako argument příkazového řádku.")
        
        url = sys.argv[1]
        all_hrefs = download_url_and_get_all_hrefs(url)
        print(all_hrefs)
    except Exception as e:
        print(f"Program skončil chybou: {e}")