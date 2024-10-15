from PIL import Image, ImageDraw

def create_palette_image(colors, filename) :

    image = Image.new("RGB", (730, 110), color="#28231D")
    draw = ImageDraw.Draw(image)

    rectangles = [
        (10, 10, 90, 50),
        (100, 10, 180, 50),
        (190, 10, 270, 50),
        (280, 10, 360, 50),
        (370, 10, 450, 50),
        (460, 10, 540, 50),
        (550, 10, 630, 50),
        (640, 10, 720 ,50),
        (10, 60, 90, 100),
        (100, 60, 180, 100), 
        (190, 60, 270, 100),
        (280, 60, 360, 100),
        (370, 60, 450, 100),
        (460, 60, 540, 100),
        (550, 60, 630, 100),
        (640, 60, 720 ,100)
    ]

    for color, rect in zip(colors, rectangles):
        draw.rectangle(rect, fill=color)

    image.save(f"{filename}.png")
