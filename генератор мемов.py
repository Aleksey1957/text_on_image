from PIL import Image, ImageDraw, ImageFont

print('Генератор мемов запущен!')

top_text = input('Введите верхний текст: ')
bottom_text = input('Введите верхний текст: ')

print(top_text, bottom_text)

print('Список картинок:')
print('1. Кот в ресторане')
print('2. Кот в очках')

choice = input('Введите номер нужной картинки: ')

image = ''

if choice == '1':
    image = "Кот в ресторане.png"
elif choice == '2':
    image = 'Кот в очках.png'

image_file = Image.open(image)     #открыть файл
width, height = image_file.size    #размер картинки
draw = ImageDraw.Draw(image_file)   #метод для добавления текста
font = ImageFont.truetype('arial.ttf', size=70)     #шрифт и размер текста

text = draw.textbbox((0, 0), top_text, font)     #место где будет текст
text_width = text[2]   #ширина

draw.text(((width - text_width) / 2, 10), top_text, font=font, fill='black')    #параметры текста и отрисовка

text = draw.textbbox((0, 0), bottom_text, font)
text_width = text[2]
text_height = text[3]

draw.text(((width - text_width) / 2, height - text_height - 10), bottom_text, font=font, fill='black')

image_file.save('new_image.png')
