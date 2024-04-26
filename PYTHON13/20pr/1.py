from PIL import Image, ImageDraw

img = Image.new('RGB', (650, 200), color='white')
d = ImageDraw.Draw(img)

#буква "В"
d.polygon([(20, 20), (20, 180), (80, 100)], fill='Red')

#буква "И"
d.polygon([(100, 20), (130, 20), (150, 180), (120, 180)], fill='Blue')
d.polygon([(150, 20), (180, 20), (160, 180), (130, 180)], fill='Pink')

#буква "К"
d.line([(200, 20), (200, 180)], fill='Yellow', width=10)
d.line([(200, 100), (300, 20)], fill='Orange', width=15)
d.line([(200, 100), (300, 180)], fill='Blue', width=10)

#буква "Т"
d.line([(320, 20), (380, 20)], fill='Red', width=16)
d.line([(350, 20), (350, 180)], fill='Pink', width=8)

#буква "О"
d.ellipse([(400, 20), (480, 180)], outline='Green', width=10  )

#буква "Р"
d.line([(500, 20), (500, 180)], fill='Red', width=15)
d.arc([(500, 10), (600, 70)], start=180, end=0, fill='black', width=12)
d.arc([(500, 10), (600, 70)], start=0, end=180, fill='yellow', width=12)



img.save('20pr\iname.png')
