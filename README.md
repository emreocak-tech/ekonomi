# Kişisel Finans ve Borsa Analiz Sistemi

Bu proje, kişisel finans yönetimi, güncel döviz kurları, altın fiyatları ve temel borsa analizlerini bir araya getiren bir Python uygulamasıdır. Kullanıcı dostu bir arayüz (PyQt5) ve komut satırı seçenekleri sunar.

## Özellikler

* **Güncel Kur Bilgileri:** Anlık Dolar, Euro ve Gram Altın fiyatlarını görüntüler.
* **Portföy Yönetimi:** Sahip olduğunuz Dolar, Euro, Altın ve TL miktarını bir MySQL veritabanına kaydedebilir, daha sonra görüntüleyebilirsiniz.
* **Hisse Senedi Tahmini:** Belirtilen bir hisse senedinin sembolüne göre basit bir doğrusal regresyon modeli kullanarak gelecekteki değerini tahmin eder.
* **Borsa Analizi:** Önceden tanımlanmış bir veri setini kullanarak Doğal Gaz, Bitcoin ve Ethereum gibi varlıkların tarihsel performansını analiz eder ve grafikler oluşturur. Bu grafikleri PNG veya PDF formatında kaydedebilirsiniz.
* **Ekonomi Haberleri:** Selenium Webdriver kullanarak popüler bir finans sitesinden güncel ekonomi haberlerini çeker.





### English README.md

# Personal Finance and Stock Market Analysis System

This is a Python application that combines personal finance management, live currency rates, gold prices, and fundamental stock market analysis. It offers both a user-friendly graphical interface (PyQt5) and command-line options.

## Features

* **Live Currency Rates:** Displays real-time prices for USD/TRY, EUR/TRY, and Gram Gold.
* **Portfolio Management:** Save your holdings in USD, EUR, Gold, and TRY to a MySQL database and view them later.
* **Stock Prediction:** Predicts the future value of a given stock ticker using a basic linear regression model.
* **Market Analysis:** Analyzes the historical performance of assets like Natural Gas, Bitcoin, and Ethereum from a predefined dataset. It can generate and save plots in PNG or PDF format.
* **Economic News:** Fetches the latest economic news from a popular financial website using Selenium Webdriver.
