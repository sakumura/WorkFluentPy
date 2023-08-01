import os
import requests
import subprocess
import zipfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def version_to_str(version):
    """Converts a version string from '1150579010' to '115.0.5790.10'"""
    return version[:3] + "." + version[3:4] + "." + version[4:8] + "." + version[8:]

def decrement_version(version):
    """Decrements a version string, '115.0.5790.10' to '115.0.5790.9'"""
    return version_to_str(str(int(version.replace('.', '')) - 1))

def get_chrome_version():
    """Gets the Chrome version from the Windows Registry."""
    version = subprocess.run(['reg', 'query', 'HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon', '/v', 'version'], capture_output=True).stdout.decode('utf-8')
    return ''.join(filter(str.isdigit, version))

def get_chromedriver_version():
    """Gets the version of the locally installed ChromeDriver."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    try:
        with webdriver.Chrome(executable_path="./chromedriver.exe", options=chrome_options) as driver:
            return driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
    except:
        return None

def download_chromedriver(version):
    """Downloads the ChromeDriver that matches the given Chrome version."""
    while True:
        download_url = f'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{version}/win64/chromedriver-win64.zip'
        response = requests.get(download_url, stream=True)
        if response.status_code == 200:
            return response
        else:
            version = decrement_version(version)

def extract_and_move_chromedriver():
    """Extracts the downloaded ChromeDriver and moves it to the correct location."""
    with zipfile.ZipFile('chromedriver.zip', 'r') as zip_ref:
        zip_ref.extractall()
    os.rename('./chromedriver-win64/chromedriver.exe', './chromedriver.exe')  # move the file to current directory

def main():
    chrome_version = version_to_str(get_chrome_version())
    current_chromedriver_version = get_chromedriver_version()

    if chrome_version != current_chromedriver_version:
        chromedriver = download_chromedriver(chrome_version)
        with open('chromedriver.zip', 'wb') as file:
            for chunk in chromedriver.iter_content(chunk_size=128):
                file.write(chunk)
        extract_and_move_chromedriver()

if __name__ == '__main__':
    main()
