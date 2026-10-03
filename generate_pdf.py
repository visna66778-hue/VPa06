import csv
import os
import subprocess
from weasyprint import HTML


CSV_FILE = "data/products.csv"
TEMPLATE_FILE = "templates/product.html"
OUTPUT_DIR = "output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "products.pdf")


def main():
    # Создаём папку output, если её ещё нет
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Читаем HTML-шаблон
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as file:
        template = file.read()

    # Читаем данные из CSV
    with open(CSV_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        html_parts = []

        for row in reader:
            html = template
            html = html.replace("{{ product }}", row["product"])
            html = html.replace("{{ price }}", row["price"])
            html = html.replace("{{ qty }}", row["qty"])

            html_parts.append(html)

    # Объединяем карточки товаров
    final_html = "".join(html_parts)

    # Создаём PDF
    HTML(string=final_html).write_pdf(OUTPUT_FILE)

    print(f"PDF успешно создан: {OUTPUT_FILE}")

    # Автоматически открываем PDF в Windows
    os.startfile(OUTPUT_FILE)


if __name__ == "__main__":
    main()