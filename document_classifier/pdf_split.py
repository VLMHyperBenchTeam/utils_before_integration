from pdf_image_tools.pdf_utils import pdf_splitter


# Разделение PDF на изображения
result = pdf_splitter("pdf/16716.pdf", zoom_x=2.0, zoom_y=2.0)
if result:
    print(result)  # Успешно обработано страниц: 5 из 5
