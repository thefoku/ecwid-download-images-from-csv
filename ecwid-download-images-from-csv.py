import csv
import os
import requests
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

csvFileName = "example.csv"

# Функция для скачивания картинки по URL
def download_image(url, folder, product_name, row_number, total_rows):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Создаем корректное имя файла
        sanitized_product_name = re.sub(r'[^\w\-_\. ]', '_', product_name)  # Заменяем запрещенные символы на подчеркивания
        file_name = os.path.join(folder, f"{sanitized_product_name}_{url.split('/')[-1]}")
        
        # Добавляем расширение .jpg, если его нет
        if not file_name.lower().endswith('.jpg'):
            file_name += '.jpg'
        
        # Скачиваем и сохраняем файл
        with open(file_name, 'wb') as out_file:
            for chunk in response.iter_content(1024):
                out_file.write(chunk)
        print(f"Строка {row_number} из {total_rows}: скачано {file_name}")
    except requests.exceptions.RequestException as e:
        print(f"Строка {row_number} из {total_rows}: не удалось скачать {url}: {e}")
    except FileNotFoundError as e:
        print(f"Строка {row_number} из {total_rows}: ошибка сохранения {url}: {e}")

# Создаем папку для сохранения изображений, если её нет
output_folder = "downloaded_images"
os.makedirs(output_folder, exist_ok=True)

# Список колонок для чтения ссылок, поменять если колонок меньше
columns = [
    'product_media_main_image_url',
    'product_media_gallery_image_url_1',
    'product_media_gallery_image_url_2',
    'product_media_gallery_image_url_3',
    'product_media_gallery_image_url_4',
    'product_media_gallery_image_url_5',
    'product_media_gallery_image_url_6',
    'product_media_gallery_image_url_7',
    'product_media_gallery_image_url_8',
    'product_media_gallery_image_url_9',
    'product_media_gallery_image_url_10',
    'product_media_gallery_image_url_11',
    'product_media_gallery_image_url_12'
]

# Функция для обработки одной строки CSV
def process_row(row, row_number, total_rows):
    product_name = row.get('product_name', 'unknown_product')
    product_name = product_name.replace(' ', '_')  # Заменяем пробелы на подчеркивания
    for column in columns:
        image_url = row.get(column)
        if image_url:
            download_image(image_url, output_folder, product_name, row_number, total_rows)

# Читаем CSV файл и скачиваем изображения
with open(csvFileName, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)  # Читаем все стexiexitроки в список, чтобы получить общее количество строк
    total_rows = len(rows)

    # Используем ThreadPoolExecutor для многопоточности
    with ThreadPoolExecutor(max_workers=5) as executor:  # Укажите количество потоков (Apple M1 поддерживает до 24 576 потоков, в данном случае можно оставить 5)
        futures = [executor.submit(process_row, row, row_number, total_rows) for row_number, row in enumerate(rows, start=1)]
        for future in as_completed(futures):
            try:
                future.result()  # Получаем результат выполнения потока (если есть)
            except Exception as e:
                print(f"Ошибка: {e}")
