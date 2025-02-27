from prompt_adapter.prompt_adapter import PromptAdapter
from system_prompt_adapter.system_prompt_adapter import SystemPromptAdapter
import glob
import os
from natsort import natsorted
import pandas as pd


def get_images_paths(directory):
    """
    Возвращает список путей ко всем .png файлам в указанной директории и её поддиректориях.

    :param directory: Путь к директории для поиска файлов.
    :return: Список строк с путями до .png файлов.
    """
    if not os.path.exists(directory):
        raise ValueError(f"Директория не существует: {directory}")

    # Рекурсивный поиск .png файлов
    pattern = os.path.join(directory, "**", "*.png")  # Шаблон для поиска
    images_paths = glob.glob(pattern, recursive=True)
    images_paths = natsorted(images_paths)

    return images_paths


def predict_doc_type(image_path):
    """
    Функция для предсказания типа документа по изображению.
    :param image_path: Путь к изображению.
    :return: Тип документа.
    """
    # ToDo: Реализовать функцию для предсказания типа документа по изображению.
    pass


# Считывание типов документов
system_prompt_adapter = SystemPromptAdapter("document_types.txt")
system_prompt = system_prompt_adapter.get_prompt() # ToDO Чтобы считывался текст с переносами строк, сейчас читается только первая строка
print(system_prompt)

# Считывание промпта из коллекции
current_prompt_collection = "JuliaJu_Qwen2_5-VL-7B_doc_type_ver0_cer_00 copy.csv"
prompt_adapter = PromptAdapter(current_prompt_collection, file_dir="PromptCollection")
page_num_prompt = prompt_adapter.get_prompt("doc", "Тип документа")
print(page_num_prompt)
pages_data = {"src_page_num": [], "page_num": [], "page_topic": []}

# Получение путей к изображениям
image_dir = "images"
images_paths = get_images_paths(image_dir)
total_images = len(images_paths)  # Общее количество изображений
print(f"Найдено изображений: {total_images}")

model_answer = []
for image_path in images_paths:
    print(image_path)
    model_answer.append(predict_doc_type(image_path))
    print(model_answer)

model_answer = ",".join(model_answer)
print(model_answer)
