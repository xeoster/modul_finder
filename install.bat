@echo off
echo Başlatılıyor...

:: Paketleri yüklemek için döngü
for %%p in (
pandas==2.2.3
random
selenium
selenium.webdriver.chrome.service
selenium.webdriver.chrome.options
pywhatkit
pyautogui
numpy==2.2.0
bs4
smtplib
docx
docx.shared
docx.enum.section
email.mime.multipart
email.mime.base
email
email.mime.text
) do (
    pip install %%p
)

echo Tüm işlemler tamamlandı!
pause
