#!/usr/bin/env python3
"""
Generate PingReply feature graphic (1024x500) for Google Play Store
"""

try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
except ImportError:
    print("ERROR: Pillow not installed. Install with: pip install pillow")
    exit(1)

# Create image
width, height = 1024, 500
img = Image.new('RGB', (width, height), color='#0B0B0F')
draw = ImageDraw.Draw(img, 'RGBA')

# Gradient background (approximated with rectangles)
for y in range(height):
    ratio = y / height
    r = int(11 + (27 - 11) * ratio)
    g = int(11 + (27 - 11) * ratio)
    b = int(15 + (37 - 15) * ratio)
    draw.line([(0, y), (width, y)], fill=(r, g, b, 255))

# Add gradient mesh (circles with transparency)
# Orange glow (top-left)
for radius in range(300, 0, 20):
    alpha = int(30 * (1 - radius / 300))
    color = (255, 107, 43, alpha)
    draw.ellipse([(-200, -200), (-200 + 2*radius, -200 + 2*radius)], fill=color)

# Purple glow (bottom-right)
for radius in range(250, 0, 20):
    alpha = int(20 * (1 - radius / 250))
    color = (99, 102, 241, alpha)
    draw.ellipse([(width - 200, height - 150), (width - 200 + 2*radius, height - 150 + 2*radius)], fill=color)

# Try to load fonts (fallback to default if not available)
try:
    title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 56)
    text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    feature_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
except:
    title_font = ImageFont.load_default()
    text_font = ImageFont.load_default()
    feature_font = ImageFont.load_default()

# Left section - text
left_x = 60
top_y = 80

# Logo badge
logo_size = 56
logo_x = left_x
logo_y = top_y
draw.rectangle([logo_x, logo_y, logo_x + logo_size, logo_y + logo_size],
               fill=(255, 107, 43, 255), outline=(255, 155, 92, 200))
draw.text((logo_x + 14, logo_y + 10), "PR", font=title_font, fill=(255, 255, 255, 255))

# Title
title_y = top_y + logo_size + 20
draw.text((left_x, title_y), "Never miss a", font=title_font, fill=(238, 238, 240, 255))
draw.text((left_x, title_y + 50), "chance to reply", font=title_font, fill=(255, 107, 43, 255))

# Subtitle
subtitle_y = title_y + 110
draw.text((left_x, subtitle_y), "Automatically respond to missed calls with SMS.",
         font=text_font, fill=(122, 122, 140, 255))
draw.text((left_x, subtitle_y + 25), "Privacy-first, offline, no accounts.",
         font=text_font, fill=(122, 122, 140, 255))

# Features
features = [
    "✓ Privacy first — no data collection",
    "✓ Works offline — no internet needed",
    "✓ Fully customizable — your messages"
]
feature_y = subtitle_y + 70
for feature in features:
    draw.text((left_x, feature_y), feature, font=feature_font, fill=(238, 238, 240, 255))
    feature_y += 25

# Right section - phone mockup
phone_x = 650
phone_y = 110
phone_w = 180
phone_h = 280

# Phone body
draw.rounded_rectangle([phone_x, phone_y, phone_x + phone_w, phone_y + phone_h],
                       radius=16, fill=(19, 19, 26, 255), outline=(255, 255, 255, 30))

# Notch
notch_w = 80
notch_x = phone_x + (phone_w - notch_w) // 2
draw.rounded_rectangle([notch_x, phone_y, notch_x + notch_w, phone_y + 12],
                       radius=8, fill=(11, 11, 15, 255))

# Screen
screen_x = phone_x + 8
screen_y = phone_y + 20
screen_w = phone_w - 16
screen_h = phone_h - 28
draw.rounded_rectangle([screen_x, screen_y, screen_x + screen_w, screen_y + screen_h],
                       radius=12, fill=(27, 27, 37, 255))

# Phone content
draw.text((screen_x + 20, screen_y + 40), "📱", font=ImageFont.load_default())
draw.text((screen_x + 15, screen_y + 80), "Service", font=feature_font, fill=(238, 238, 240, 255))
draw.text((screen_x + 20, screen_y + 100), "Active", font=feature_font, fill=(238, 238, 240, 255))
draw.text((screen_x + 10, screen_y + 130), "Auto-replying", font=feature_font, fill=(122, 122, 140, 200))
draw.text((screen_x + 15, screen_y + 145), "to calls", font=feature_font, fill=(122, 122, 140, 200))

# Button on phone
btn_h = 20
btn_x = screen_x + (screen_w - 80) // 2
btn_y = screen_y + screen_h - 40
draw.rounded_rectangle([btn_x, btn_y, btn_x + 80, btn_y + btn_h],
                       radius=6, fill=(255, 107, 43, 255))
draw.text((btn_x + 20, btn_y + 2), "Get Free", font=feature_font, fill=(255, 255, 255, 255))

# Save
output_path = '/home/ricardo/Homespace/1_Projects/ping-reply/assets/feature-graphic.png'
img.save(output_path, 'PNG')
print(f"✓ Feature graphic created: {output_path}")
print(f"  Size: 1024×500 (Play Store requirement)")
print(f"  Ready for upload to Google Play Console!")
