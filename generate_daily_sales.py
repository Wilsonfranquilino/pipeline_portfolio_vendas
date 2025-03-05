import pandas as pd
import random
from datetime import datetime, timedelta
import names
import os
from pandas.tseries.offsets import BDay

products = [
    (101, "Mouse Sem Fio", "Periféricos", 25.99), (102, "Teclado Mecânico", "Periféricos", 85.00),
    (103, "Monitor 24\"", "Eletrônicos", 299.90), (104, "Impressora Laser", "Escritório", 450.00),
    (105, "Notebook i5", "Eletrônicos", 3200.00), (106, "Cadeira Ergonômica", "Escritório", 199.90),
    (107, "Webcam HD", "Periféricos", 45.50), (108, "HD Externo 1TB", "Eletrônicos", 250.00),
    (109, "Mesa de Escritório", "Escritório", 150.00), (110, "Fone de Ouvido", "Periféricos", 35.00),
    (111, "Monitor 27\"", "Eletrônicos", 399.90), (112, "Roteador Wi-Fi", "Eletrônicos", 120.00),
    (113, "Caneta Esferográfica", "Escritório", 1.50), (114, "SSD 500GB", "Eletrônicos", 180.00),
    (115, "Cabo HDMI", "Periféricos", 15.00), (116, "Notebook i7", "Eletrônicos", 4500.00),
    (117, "Mousepad", "Periféricos", 9.90), (118, "Teclado Bluetooth", "Periféricos", 65.00),
    (119, "Monitor 32\"", "Eletrônicos", 599.90), (120, "Cartucho de Tinta", "Escritório", 39.90),
    (121, "Hub USB", "Periféricos", 29.90), (122, "Carregador Portátil", "Eletrônicos", 89.90),
    (123, "Luminária de Mesa", "Escritório", 45.00), (124, "Pendrive 64GB", "Eletrônicos", 35.00),
    (125, "Caixa de Som Bluetooth", "Eletrônicos", 120.00), (126, "Adaptador HDMI", "Periféricos", 19.90),
    (127, "Papel A4 500un", "Escritório", 25.00), (128, "Smartphone Básico", "Eletrônicos", 799.90),
    (129, "Estante de Livros", "Escritório", 250.00), (130, "Microfone USB", "Periféricos", 75.00),
    (131, "Smart TV 50\"", "Eletrônicos", 2200.00), (132, "Suporte de Monitor", "Escritório", 59.90),
    (133, "Cabo USB-C", "Periféricos", 12.50), (134, "Tablet 10\"", "Eletrônicos", 999.90),
    (135, "Organizador de Mesa", "Escritório", 34.90), (136, "Headset Gamer", "Periféricos", 150.00),
    (137, "Projetor", "Eletrônicos", 850.00), (138, "Grampeador", "Escritório", 15.00),
    (139, "Mouse Gamer", "Periféricos", 99.90), (140, "Smartwatch", "Eletrônicos", 299.00),
    (141, "Calculadora", "Escritório", 19.90), (142, "Placa de Vídeo", "Eletrônicos", 1500.00),
    (143, "Teclado Sem Fio", "Periféricos", 55.00), (144, "HD SSD 1TB", "Eletrônicos", 400.00),
    (145, "Caderno 200 Folhas", "Escritório", 12.00), (146, "Adaptador VGA", "Periféricos", 22.00),
    (147, "TV 42\"", "Eletrônicos", 1800.00), (148, "Porta Canetas", "Escritório", 8.90),
    (149, "Caixa de Som Portátil", "Eletrônicos", 79.90), (150, "Filtro de Linha", "Periféricos", 39.90)
]
regions = ["Sudeste", "Nordeste", "Sul", "Centro-Oeste", "Norte"]
payment_methods = ["Cartão", "Boleto", "Pix", "Dinheiro"]
customers = [(1000 + i, names.get_full_name()) for i in range(5000)]

today = datetime.now()
start_date = today - BDay(60)

csv_path = "sales.csv"
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    df = df[df['sale_date'] >= start_date]
    last_id = df['sale_id'].max()
else:
    df = pd.DataFrame()
    last_id = 0

new_data = []
for i in range(1, random.randint(200, 250)):
    product = random.choice(products)
    price = product[3] * (1 + random.uniform(-0.1, 0.1)) if random.random() < 0.05 else product[3]
    customer = random.choice(customers)
    customer_name = customer[1] if random.random() > 0.02 else names.get_full_name()
    customer_region = random.choice(regions) if random.random() > 0.02 else random.choice(regions)
    quantity = random.randint(1, 10) if random.random() > 0.01 else None
    sale_id = last_id + i
    new_data.append({
        "sale_id": sale_id,
        "product_id": product[0],
        "product_name": product[1],
        "category": product[2],
        "quantity": quantity,
        "price": price,
        "customer_id": customer[0],
        "customer_name": customer_name,
        "region": customer_region,
        "sale_date": today.strftime("%Y-%m-%d"),
        "payment_method": random.choice(payment_methods)
    })

df_new = pd.DataFrame(new_data)
df_combined = pd.concat([df, df_new], ignore_index=True)
df_combined.to_csv(csv_path, index=False)
print(f"Atualizado sales.csv: {len(df_new)} novas linhas, total {len(df_combined)} linhas (60 dias úteis).")