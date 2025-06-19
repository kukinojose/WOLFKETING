import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Ruta al chromedriver
CHROMEDRIVER_PATH = r"C:\Users\PC\Desktop\TT\web wolfketing\images\8c776b7b01ccb5d8556755bc25a8e17d/chromedriver.exe"

# URL de búsqueda en Pixabay (negocios digitales, vertical)
URL = "https://pixabay.com/es/photos/search/negocios%20digitales/?orientation=vertical"

# Carpeta donde guardar imágenes
SAVE_DIR = r"C:\Users\PC\Desktop\TT\web wolfketing\images"
os.makedirs(SAVE_DIR, exist_ok=True)

def download_image(url, path):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(path, "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Descargada: {path}")
        else:
            print(f"Error al descargar {url}: status {response.status_code}")
    except Exception as e:
        print(f"Error al descargar {url}: {e}")

def main():
    options = Options()
    # options.add_argument("--headless")  # Descomenta para no abrir ventana
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(URL)
    time.sleep(5)  # Esperar a que cargue la página

    # Scroll para cargar más imágenes (modifica si quieres más)
    for _ in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    # Localizar todas las imágenes (tienen clase 'preview')
    images = driver.find_elements(By.CSS_SELECTOR, "img.preview")

    print(f"Encontradas {len(images)} imágenes.")

    for i, img in enumerate(images):
        src = img.get_attribute("src")
        if src:
            # Cambiar URL para obtener la imagen más grande (normalmente reemplazando /thumb/ por /photo/)
            high_res_url = src.replace("/thumb/", "/photo/")
            ext = high_res_url.split(".")[-1].split("?")[0]
            filename = os.path.join(SAVE_DIR, f"negocios_{i+1}.{ext}")
            download_image(high_res_url, filename)

    driver.quit()

if __name__ == "__main__":
    main()
