import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QFormLayout, QMessageBox, QComboBox,QCheckBox
from PyQt5.QtGui import QIcon
import sys
import mysql.connector
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yfinance as yf
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
plt.style.use("seaborn-v0_8-darkgrid")
conn=mysql.connector.connect("KULLANICI KENDİ BİLGİLERİNİ GİRMELİDİR!")
cursor=conn.cursor()
ert=datetime.datetime.now()
def logla(mesaj):
    with open("hata_dosyam.txt","a+",encoding="utf-8") as file:
        file.write("\n" + " " + "Hata Açıklaması : " + " " + mesaj + "Hatanın Alındığı Tarih" + " " + str(ert))
class System:
    def dolar_tl(self):
        url = "https://v6.exchangerate-api.com/v6/KULLANICI KENDİ API key BİLGİSİNİ GİRMELİDİR!/latest/USD"
        cevap = requests.get(url)
        if cevap.status_code==200:
            data = cevap.json()
            print(f"1 DOLAR =  {data['conversion_rates']['TRY']} TL'DİR.")
        else:
            print(f"API servisine ulaşılamadı ❗, Hata Kodu : {cevap.status_code}")
    def euro_tl(self):
        url = "https://v6.exchangerate-api.com/v6/KULLANICI KENDİ API key BİLGİSİNİ GİRMELİDİR!/latest/EUR"
        cevap=requests.get(url=url)
        if cevap.status_code==200:
            data=cevap.json()
            print(f"1 EURO = {data['conversion_rates']['TRY']} TL'DİR.")
        else:
            print(f"API servisine ulaşılamadı❗ , Hata Kodu : {cevap.status_code}")
    def altın_tl(self):
        url="https://tr.investing.com/currencies/gau-try-historical-data"
        driver=webdriver.Edge()
        driver.get(url=url)
        driver.maximize_window()
        ürün_fiyat=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]')))
        time.sleep(3)
        print(f"1 Gram Altın : {ürün_fiyat.text} TL'dir")
    def uygulama_çalıştır(self):
        app=QApplication(sys.argv)
        window=QWidget()
        vbox=QVBoxLayout()
        check_box=QCheckBox("Kullanıcı Sözleşmesini Okudum , Onaylıyorum")
        form_layout=QFormLayout()
        def kaydetme_fonksiyonum():
            isim=user_input.text().strip()
            dolar=user_input2.text().strip()
            euro=user_input3.text().strip()
            altın=user_input4.text().strip()
            tl=user_input5.text().strip()
            zaman=datetime.datetime.now()
            if not check_box.isChecked():
                QMessageBox.warning(window,"Hata","Kullanıcı Sözleşmesini Kabul Etmededen Giriş Yapamazsınız❗")
            else:
                if not isim:
                    QMessageBox.warning(window,"Hata","Bu Alan Boş Bırakılamaz!")
                elif not dolar.isdigit():
                    QMessageBox.warning(window,"Hata","Lütfen Sayı Değeri Giriniz!")
                elif not euro.isdigit():
                    QMessageBox.warning(window,"Hata","Lütfen Sayı Giriniz!")
                elif not altın.isdigit():
                    QMessageBox.warning(window,"Hata","Lütfen Sayı Değeri Giriniz!")
                else:
                    QMessageBox.information(window,"Giriş Başarılı",f"Merhaba {isim} 👋, Verileriniz Kaydedildi!")
                    sql_sorgum="INSERT INTO param(İsim,Dolar,Euro,Altın,TL,Zaman) VALUES (%s,%s,%s,%s,%s,%s)"
                    values=(isim,dolar,euro,altın,tl,zaman)
                    try:
                        cursor.execute(sql_sorgum,values)
                        conn.commit()
                    except Exception as v:
                        QMessageBox.warning(window,"Hata❗",f"Veritabanı Bağlantısı Hatası , Hata Kodu {v}")
        user_input=QLineEdit()
        user_input2=QLineEdit()
        user_input3 =QLineEdit()
        user_input4=QLineEdit()
        user_input5=QLineEdit()
        form_layout.addRow("İsminizi Giriniz : ",user_input)
        form_layout.addRow("Kaydetmek İstediğiniz Dolar Miktarını Giriniz : ",user_input2)
        form_layout.addRow("Kaydetmek İstediğiniz Euro miktarını Giriniz : ",user_input3)
        form_layout.addRow("Kaydetmek İstediğiniz Çeyrek Altını Tane Olarak Giriniz : ",user_input4)
        form_layout.addRow("Kaydetmek İstediğiniz TL Miktarını Giriniz : ",user_input5)
        buton=QPushButton("Gönder")
        vbox.addLayout(form_layout)
        vbox.addWidget(buton)
        buton.clicked.connect(kaydetme_fonksiyonum)
        vbox.addWidget(check_box)
        window.setLayout(vbox)
        window.setWindowTitle("Kişisel Finans Sistemim")
        window.setWindowIcon(QIcon("kişisel finans hakkı.png"))
        buton.setStyleSheet("""
            background-color: #007ACC;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
        """)
        user_input.setStyleSheet("""
            border: 2px solid gray;
            padding: 5px;
            font-size: 14px;
            border-radius: 4px;
        """)
        user_input2.setStyleSheet("""
            border: 2px solid gray;
            padding: 5px;
            font-size: 14px;
            border-radius: 4px;
        """)
        user_input3.setStyleSheet("""
            border: 2px solid gray;
            padding: 5px;
            font-size: 14px;
            border-radius: 4px;
        """)
        user_input4.setStyleSheet("""
            border: 2px solid gray;
            padding: 5px;
            font-size: 14px;
            border-radius: 4px;
        """)
        user_input5.setStyleSheet("""
            border: 2px solid gray;
            padding: 5px;
            font-size: 14px;
            border-radius: 4px;
        """)
        check_box.setStyleSheet("""
            border: 2px solid gray;
            padding: 5px;
            font-size: 14px;
            border-radius: 4px;
        """)
        window.showMaximized()
        sys.exit(app.exec_())
    def sıralama_fonksiyonum(self):
        sql_sorgum="SELECT * FROM param"
        cursor.execute(sql_sorgum)
        veriler=cursor.fetchall()
        for veri in veriler:
            print(veri)
        conn.commit()
        conn.close()
    def borsa_tahmin(self):
        sembol_al=input("Şirketin Sembolünü Giriniz : ")
        veri=yf.download(sembol_al,period="30d",interval="1d")
        kapanış=veri["Close"].dropna().reset_index(drop=True)
        X = np.array(range(len(kapanış))).reshape(-1, 1)
        Y = kapanış.values.reshape(-1, 1)
        model=LinearRegression()
        model.fit(X,Y)
        bugun = len(kapanış)
        tahmin = model.predict([[bugun]])
        tahminler=model.predict(X)
        gerçek=Y
        hata=np.sqrt(mean_squared_error(gerçek,tahminler))
        print(f"Modelin Doğruluk Oranı : {hata}")
        print(f"{sembol_al} hissesinin  tahmini değeri {tahmin}")
    def borsa_analiz(self):
        df = pd.read_csv("C:/Users\emre_\Downloads/archive (6)\Stock Market Dataset.csv")
        def doğal_gaz():
            ortalama=df["Natural_Gas_Price"].mean()
            print(f"Doğal Gazın Ortalama Fiyatı : {ortalama}")
            son_otuz_değer=df["Natural_Gas_Price"].tail(30)
            plt.bar(son_otuz_değer,df["Date"].tail(30),color="Red",linewidth=1)
            plt.grid(True)
            plt.title("DOĞAL GAZ FİYATLARI",color="Black",fontsize=20)
            plt_filename="doğal_gaz.png"
            plt.savefig(plt_filename)
            try:
                karar=int(input("Bu görseli PDF dosya haline getirmek istiyorsanız  1 , istemiyorsanız 0 tuşlayınız : "))
                if karar==1:
                    pdf_filename="dogalgaz.pdf"
                    c=canvas.Canvas(pdf_filename)
                    c.setFont("Times-Roman",16)
                    c.drawString(150,792,"Doğal Gaz Fiyatları")
                    ımg=ImageReader(plt_filename)
                    c.drawImage(ımg,100,150,width=400,height=200)
                    c.drawString(25,400,"Doğal gaz fiyatları, öngörülmesi zor birçok faktöre bağlıdır. Yatırımcılar ve tüketiciler için enerji çeşitlendirmesi ve verimlilik önemli hale gelmiştir. Güncel verileri takip etmek için EIA (ABD Enerji Bilgi İdaresi), IEA (Uluslararası Enerji Ajansı) ve BOTAŞ raporları incelenmelidir.")
                    c.setFont("Helvetica", 12)
                    c.drawString(0, 250, f"BU DOSYANIN OLUSTURULMA ZAMANI {datetime.datetime.now()}")
                    c.save()
                elif karar==0:
                    print("png Dosyası Oluşturuluyor...")
                    time.sleep(3)
                    plt.show()
            except ValueError as v:
                print(f"Lütfen Belirtilen Değerleri Tuşlayınız❗")
                logla("Kullanıcı Belirtlen İşlem Numrasını Girmedi.")
        def btc():
            df["Bitcoin_Price"] = df["Bitcoin_Price"].str.replace(",", "").astype(float)
            ortalama=df["Bitcoin_Price"].mean(numeric_only=True)
            en_yüksek_fiyat=df.nlargest(1,"Bitcoin_Price")[["Date","Bitcoin_Price"]]
            en_düşük_fiyat=df.nsmallest(1,"Bitcoin_Price")[["Date","Bitcoin_Price"]]
            print(f"BTC'nin Ortalama Değeri : {ortalama} Dolar'dır")
            print(f"BTC'nin En Yüksek Değeri : {en_yüksek_fiyat['Bitcoin_Price'].values} ,  Tarih : {en_yüksek_fiyat['Date'].values}")
            print(f"BTC'nin En Düşük Değeri : {en_düşük_fiyat['Bitcoin_Price'].values} ,  Tarih : {en_düşük_fiyat['Date'].values}")
            plt.bar(df["Bitcoin_Price"].tail(30) , df["Date"].tail(30), color="Red", linewidth=300000)
            plt.title("BİTCOİN SON ÇEYREK DEĞERLERİ",color="Black",fontsize=20)
            plt.grid(True)
            plt_filename="bitcoin.png"
            plt.savefig(plt_filename)
            try:
                karar=int(input("Bu Görseli pdf Dosya Halinde Görmek İstiyorsanız  1 , İstemiyorsanız 0 Tuşlayınız : "))
                if karar==1:
                    pdf="bitcoin.pdf"
                    c=canvas.Canvas(pdf)
                    c.setFont("Times-Roman",16)
                    c.drawString(150,792,"BITCOIN GRAFIK")
                    ımg=ImageReader(plt_filename)
                    c.drawImage(ımg,100,150,width=400,height=200)
                    c.drawString(150,400,"Bitcoin fiyatları, küresel likidite, risk algısı ve ETF onayları gibi makro faktörlerden etkileniyor. Kısa vadede yükseliş eğiliminde olsa da aşırı volatilite ve düzenleme riskleri dikkat edilmesi gereken unsurlar. Uzun vadede benimsenme artışı ve arz kısıtı (halving) fiyatları destekleyebilir.")
                    c.save()
                    print("PDF dosya oluştruldu!")
                elif karar==0:
                    print("png Dosyası Hazırlanıyor...")
                    plt.show()
            except ValueError as v:
                print(f"Lütfen Belirtilen Değerleri Giriniz  , Hata Kodu : {v}")
                logla("Kullanıcı Belirtlen İşlem Numrasını Girmedi.")
        def ethereum():
            df["Ethereum_Price"] = df["Ethereum_Price"].str.replace(",", "").astype(float)
            ortalama=df["Ethereum_Price"].mean()
            en_yüksek_değer=df.nlargest(1,"Ethereum_Price")[["Date","Ethereum_Price"]]
            en_düşük_değer=df.nsmallest(1,"Ethereum_Price")[["Date","Ethereum_Price"]]
            print(f"Ethereum Ortalama Değeri : {ortalama} Dolar'dır")
            print(f"ETH'nin En Yüksek Değeri {en_yüksek_değer['Ethereum_Price']} , Tarih : {en_yüksek_değer['Date']}")
            print(f"ETH'nin En Düşük Değeri {en_düşük_değer['Ethereum_Price']} , Tarih : {en_düşük_değer['Date']}")
            plt.bar(df["Date"],df["Ethereum_Price"],color="Red",linewidth=3)
            plt.title("ETH GRAFİK",color="Black",fontsize=20)
            plt_filename="eth.png"
            plt.savefig(plt_filename)
            try:
                karar=int(input("Bu Dosyayı PDF şeklinde İstiyorsanız 1 , İstemiyorsanız 0 Tuşlayınız : "))
                if karar==1:
                    pdf="eth.pdf"
                    c=canvas.Canvas(pdf)
                    c.setFont("Times-Roman",16)
                    c.drawString(150,792,"ETH ANALİZ")
                    ımg=ImageReader(plt_filename)
                    c.drawImage(ımg,400,200,width=200,height=100)
                    c.drawString(150,600,"Teknolojik Üstünlük: Ethereum, akıllı kontratlar ve merkeziyetsiz uygulamalar (dApps) geliştirmeye olanak sağlayan öncü bir blok zinciri platformudur, bu özelliğiyle kripto dünyasında kritik bir rol oynamaktadır.ETH 2.0 Geçişi: Proof-of-Stake (PoS) konsensüs mekanizmasına geçişle birlikte ölçeklenebilirlik ve enerji verimliliği sorunlarını çözmeyi hedefleyen Ethereum, bu süreçte ağ güvenliğini ve kullanıcı deneyimini artırmaktadır.DeFi ve NFT Merkezi: Ethereum, merkeziyetsiz finans (DeFi) ve NFT ekosistemlerinin temel taşı olarak kabul edilir, ancak yüksek işlem ücretleri (gas fee) ve rakip blok zincirlerinin yükselişi nedeniyle rekabet baskısı altındadır.")
                    c.setFont("Helvetica", 12)
                    c.drawString(0, 250, f"BU DOSYANIN OLUSTURULMA ZAMANI {datetime.datetime.now()}")
                    c.save()
                    print("PDF dosyanız oluşturuldu!")
                elif karar==0:
                    print("Matplotlib Kütüphanesi Hazırlanıyor...")
                    time.sleep(3)
                    plt.show()
            except ValueError as v:
                print(f"Lütfen Belirlenen Değerleri Giriniz , Hata Kodu  :{v}")
                logla("Kullanıcı Belirtlen İşlem Numrasını Girmedi.")
        print("Borsa Analiz Fonksiyonuna Hoşgeldiniz😂".center(50, "*"))
        print("Yapabilecekleriniz:\n1=Doğal Gaz Fiyatları ve Analizi\n2=Bitcoin Fiyatları ve Analizi₿\n3=ETH Fiyatları ve Analizi")
        try:
            qwe = int(input("Yapmak İstediğiniz İşlemin Numarasını Giriniz : "))
            if qwe == 1:
                doğal_gaz()
            elif qwe == 2:
                btc()
            elif qwe == 3:
                ethereum()
            else:
                print("Lütfen Belirtilen İşlem Numaralarını Giriniz!")
        except ValueError as v:
            print(f"Lütfen Belirtilen Değerleri Giriniz ❗,  Hata Kodu : {v}")
            logla("Kullanıcı Belirtlen İşlem Numrasını Girmedi.")
    def ekonomi_haber(self):
        url="https://tr.investing.com/"
        driver = webdriver.Edge()
        driver.get(url=url)
        driver.maximize_window()
        time.sleep(10000)
def main():
    system=System()
    print("YATIRIMCIDOSTUM Uygulamasına Hoşgeldiniz🥰".center(50,"*"))
    print("Yapabilecekleriniz:\n1=Dolar/TL Değeri💵\n2=Euro/TL Değeri💶\n3=Gram Altın Değeri🪙\n4=Portföyünüzü Veritabanına Kaydetme📓\n5=Portföy Görüntüleme🔎\n6=Hisse Tahmin Etme (Temel Seviye)\n7=Borsa Analiz📈\n8=Ekonomi Haberleri📰\n9=Sistemden Çıkış")
    while True:
        try:
            decision=int(input("Yapmak İstediğiniz İşlemin Numarasını Giriniz : "))
            if decision==1:
                system.dolar_tl()
            elif decision==2:
                system.euro_tl()
            elif decision==3:
                system.altın_tl()
            elif decision==4:
                system.uygulama_çalıştır()
            elif decision==5:
                system.sıralama_fonksiyonum()
            elif decision==6:
                system.borsa_tahmin()
            elif decision==7:
                system.borsa_analiz()
            elif decision==8:
                system.ekonomi_haber()
            elif decision==9:
                print("Sistemden Çıkılıyor...")
                print("Sistemden Çıkıldı✔️ ")
                time.sleep(3)
                quit()
            else:
                print("Lütfen Belirtilen Değerleri Giriniz❗")
        except ValueError as v:
            print(f"Lütfen Belirtilen Değerleri Giriniz ,  Hata Kodu : {v}")
            logla("Kullanıcı Belirtlen İşlem Numrasını Girmedi.")
        finally:
            print("Sistem Düzgün Şekilde Çalışıyor✅")
if __name__=="__main__":
    main()
