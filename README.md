# Auto-Download ChromeDriver

このPythonスクリプトは、Windows環境で動作するGoogle Chromeと互換性のあるバージョンのChromeDriverを自動的にダウンロードします。具体的には、以下の手順に従って動作します。

1. レジストリからインストール済みのGoogle Chromeのバージョンを取得します。
2. すでにローカルにインストールされているChromeDriverのバージョンを取得します。
3. ChromeのバージョンとChromeDriverのバージョンが一致しない場合、一致するバージョンのChromeDriverをダウンロードします。存在しないバージョンを指定した場合は、バージョン番号を減らしながら再試行します。
4. ダウンロードしたzipファイルを解凍し、chromedriver.exeをスクリプトと同じディレクトリに移動します。

このスクリプトは、Seleniumで自動化を行う際に、常に適切なバージョンのChromeDriverを使用することができます。

This Python script automatically downloads the version of ChromeDriver that is compatible with the version of Google Chrome installed on your Windows environment.

## How it Works

1. **Fetch Chrome Version**: The script first retrieves the version of Google Chrome installed on your system by querying the Windows Registry.

2. **Check ChromeDriver Version**: It then checks the version of ChromeDriver installed in your local environment.

3. **Download Matching ChromeDriver**: If the version of Chrome and ChromeDriver do not match, it attempts to download the version of ChromeDriver that matches the installed Chrome version. If it specifies a version that does not exist, it continues to retry with decremented version numbers until it finds a version that is available.

4. **Unzip and Move ChromeDriver**: Once downloaded, it unzips the downloaded file and moves `chromedriver.exe` to the same directory as the script.

## Why Use This Script

This script ensures that you are always using the correct version of ChromeDriver when running automation with Selenium.
