import pymupdf
import os


def convert_pdf_to_images(pdf_path, output_folder, zoom_x=2.0, zoom_y=2.0):
    """
    Конвертирует страницы PDF в изображения и сохраняет их в указанную папку.

    Args:
        pdf_path (str): Путь к PDF-файлу.
        output_folder (str): Папка для сохранения изображений.
        zoom_x (float): Коэффициент масштабирования по горизонтали. По умолчанию 2.0.
        zoom_y (float): Коэффициент масштабирования по вертикали. По умолчанию 2.0.

    Returns:
        str или None: Сообщение об успешном завершении или None в случае ошибки.
    """

    try:
        # Чтение PDF-документа
        doc = pymupdf.open(pdf_path)
        print(f"Количество страниц в документе: {len(doc)}")

        # Создание папки для сохранения изображений, если она не существует
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Матрица для масштабирования
        mat = pymupdf.Matrix(zoom_x, zoom_y)

        # Концертациям каждой страницы в изображение
        for page in doc:
            pix = page.get_pixmap(matrix=mat)  # С использованием масштабирования matrix=mat
            output_path = os.path.join(output_folder, f"page-{page.number}.png")
            pix.save(output_path)

        print(f"Изображения сохранены в папку: {output_folder}")
        return f"Успешно сохранено {len(doc)} страниц."

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


# Пример использования
if __name__ == "__main__":
    pdf_path = "test.pdf"
    output_folder = "images"
    result = convert_pdf_to_images(pdf_path, output_folder)
    if result:
        print(result)
