def download_image(image_url):
    import requests
    from pathlib import Path

    dir_path = Path("downloaded_images/")
    dir_path.mkdir(parents=True, exist_ok=True)

    image_name = image_url[image_url.rfind("/")+1:]
    image_path = str(dir_path) + "/" + image_name


    with requests.get(image_url, stream=True) as response:
        response.raise_for_status()
        with open(image_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
            file.flush()
    print(f"Finished downloading \"{image_url}\" to \"{image_path}\".\n")

def main():

    import requests
    from bs4 import BeautifulSoup

    # root_url = "https://www.stiga.pl/"

    # url = f"{root_url}sklep/koszenie-trawnika/agregaty-tnace/agregaty-tnace-park-villa"
    
    url = "url = https://www.stiga.pl/sklep/koszenie-trawnika/agregaty-tnace/agregaty-tnace-park-villa/agregat-park-105-el-combi-qf"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    for product in soup.findAll("div", {"class": "owl-item"}):
        image_url = product.find("img")["data-src"]
        download_image(image_url)

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
>>>>>>> Updating code
