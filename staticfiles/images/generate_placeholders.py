from PIL import Image, ImageDraw, ImageFont
import os

# Create images directory if it doesn't exist
os.makedirs('amaron_store/store/static/images', exist_ok=True)

# Image dimensions
width, height = 1200, 400

# Colors
colors = [
    ('#1a5276', '#3498db'),  # Blue theme
    ('#7d3c98', '#9b59b6'),  # Purple theme
    ('#196f3d', '#27ae60'),  # Green theme
]

# Text for each image
texts = [
    ('Premium Quality Batteries', 'Powering your vehicles with reliability'),
    ('Expert Service Support', 'Professional maintenance and care'),
    ('Wide Range of Products', 'For all your automotive needs'),
]

# Generate images
for i, ((bg_color, text_color), (title, subtitle)) in enumerate(zip(colors, texts)):
    # Create new image
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Add text
    title_font = ImageFont.truetype("arial.ttf", 40)
    subtitle_font = ImageFont.truetype("arial.ttf", 24)
    
    # Calculate text positions
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    
    title_width = title_bbox[2] - title_bbox[0]
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    
    title_x = (width - title_width) // 2
    subtitle_x = (width - subtitle_width) // 2
    
    # Draw text
    draw.text((title_x, height//2 - 50), title, fill=text_color, font=title_font)
    draw.text((subtitle_x, height//2 + 20), subtitle, fill=text_color, font=subtitle_font)
    
    # Save image
    img.save(f'amaron_store/store/static/images/battery{i+1}.jpg')

print("Placeholder images generated successfully!") 