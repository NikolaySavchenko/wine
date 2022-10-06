# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Установите необходимые библиотеки. Для этого используйте команду:

`pip install -r requirements.txt`

- Запустите сайт командой

`python3 main.py file_address`

Где `file_address` - адрес файла с данными по напиткам.
Требования к файлу с данными: файл Excel, содержит следующие столбцы: `Категория`, `Название`, `Сорт`, `Цена`, `Картинка`, `Акция`.
Допускаются пустые ячейки.
`Картинка` - название картинки продукта, например `belaya_ledi.png`, сама картинка находится в папке `images`.

- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
