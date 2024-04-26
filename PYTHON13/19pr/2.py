from PIL import Image

pic = Image.open("19pr\image2.jpg")
con_image = pic.convert("L")
trans_image = con_image.transpose(Image.FLIP_LEFT_RIGHT)

H_W = (400, 300)
new_image = trans_image.resize(H_W)

new_image.save("19pr\image3.jpg")
new_image.show()