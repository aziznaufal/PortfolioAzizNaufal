from PIL import Image, ImageDraw, ImageFont

def generate_icon(size, filename):
    # Create a solid blue background
    img = Image.new('RGB', (size, size), color='#3b82f6')  # Tailwind blue
    draw = ImageDraw.Draw(img)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", size // 2)
    except:
        font = ImageFont.load_default()

    # Text to draw
    text = "$"

    # Get text bounding box (more modern and accurate)
    if hasattr(draw, "textbbox"):
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    else:
        text_width, text_height = draw.textsize(text, font=font)

    # Center the text
    position = ((size - text_width) // 2, (size - text_height) // 2)

    # Draw the text in white
    draw.text(position, text, fill="white", font=font)
    img.save(filename)
    print(f"✅ Icon saved: {filename}")

# Ensure your icons folder exists first!
generate_icon(192, "../finance_tracker/static/icons/icon-192x192.png")
generate_icon(512, "../finance_tracker/static/icons/icon-512x512.png")
