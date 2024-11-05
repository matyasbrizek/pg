import sys

# Definice úvodních binárních sekvencí obrázkových souborů
jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'

def read_header(file_name, header_length):
    """
    Tato funkce načte binární soubor z cesty file_name,
    z něj přečte prvních header_length bytů a ty vrátí pomocí return
    """
    with open(file_name, "rb") as img_file:
        header = img_file.read(header_length)
    return header

def is_jpeg(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanou hlavičkou v proměnné jpeg_header
    """
    # načti hlavičku souboru
    header = read_header(file_name, len(jpeg_header))

    # vyhodnoť zda je soubor jpeg
    return header.startswith(jpeg_header)

def is_gif(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku gif,
    tu srovná s definovanými hlavičkami v proměnných gif_header1 a gif_header2
    """
    # načti hlavičku souboru
    header = read_header(file_name, len(gif_header1))

    # vyhodnoť zda je soubor gif
    return header == gif_header1 or header == gif_header2

def is_png(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku png,
    tu srovná s definovanou hlavičkou v proměnné png_header
    """
    # načti hlavičku souboru
    header = read_header(file_name, len(png_header))

    # vyhodnoť zda je soubor png
    return header.startswith(png_header)

def print_file_type(file_name):
    """
    Funkce vypíše typ souboru - tuto funkci není třeba upravovat
    """
    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu jpeg')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu gif')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu png')
    else:
        print(f'Soubor {file_name} je neznámého typu')

if __name__ == '__main__':
    # Přidej try-catch blok, odchyť obecnou výjimku Exception a vypiš ji
    try:
        file_name = sys.argv[1]
        print_file_type(file_name)
    except IndexError:
        print("Nebyly zadany soubory")
    except FileNotFoundError:
        print("Soubor neexistuje")
    except Exception as e:
        print(f"Nastala neočekávaná chyba: {e}")