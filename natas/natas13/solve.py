from PIL import Image

imagem = Image.new("RGB", (5, 5), (0, 0, 0))

imagem.save("image.jpg", "JPEG")

