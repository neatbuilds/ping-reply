#!/usr/bin/env python3
"""
Generate PingReply feature graphic (1024x500) for Google Play Store
Improved version with better visual design
"""

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("ERROR: Pillow not installed. Install with: pip install pillow")
    exit(1)

# Create image with better quality
width, height = 1024, 500
img = Image.new('RGB', (width, height), color='#0B0B0F')
draw = ImageDraw.Draw(img, 'RGBA')

# ============================================================
# BACKGROUND GRADIENT
# ============================================================
# Gradient from dark blue-grey to darker blue-grey
for y in range(height):
    ratio = y / height
    # Interpolate from #0B0B0F to #1B1B25
    r = int(0x0B + (0x1B - 0x0B) * ratio)
    g = int(0x0B + (0x1B - 0x0B) * ratio)
    b = int(0x0F + (0x25 - 0x0F) * ratio)
    draw.line([(0, y), (width, y)], fill=(r, g, b))

# ============================================================
# DECORATIVE GLOWS
# ============================================================
# Orange glow (top left)
glow_x, glow_y = -100, -100
for r in range(400, 50, 15):
    alpha = int(40 * (1 - (r - 50) / 350))
    color = (255, 107, 43, alpha)
    draw.ellipse(
        [(glow_x - r, glow_y - r), (glow_x + r, glow_y + r)],
        fill=color
    )

# Purple glow (bottom right)
glow_x2, glow_y2 = width + 100, height + 50
for r in range(350, 50, 15):
    alpha = int(35 * (1 - (r - 50) / 300))
    color = (99, 102, 241, alpha)
    draw.ellipse(
        [(glow_x2 - r, glow_y2 - r), (glow_x2 + r, glow_y2 + r)],
        fill=color
    )

# ============================================================
# FONTS
# ============================================================
try:
    # Try system fonts
    bold_font_64 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 64)
    bold_font_48 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
    regular_font_20 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    regular_font_16 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
except:
    # Fallback to default
    bold_font_64 = ImageFont.load_default()
    bold_font_48 = ImageFont.load_default()
    regular_font_20 = ImageFont.load_default()
    regular_font_16 = ImageFont.load_default()

# ============================================================
# LEFT SECTION - TEXT CONTENT
# ============================================================
left_margin = 60
text_top = 60

# Logo badge
badge_size = 60
badge_x = left_margin
badge_y = text_top

# Draw orange badge
draw.rounded_rectangle(
    [(badge_x, badge_y), (badge_x + badge_size, badge_y + badge_size)],
    radius=12,
    fill=(255, 107, 43, 255)
)

# "PR" text in badge
try:
    pr_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
except:
    pr_font = bold_font_48

draw.text(
    (badge_x + 12, badge_y + 10),
    "PR",
    font=pr_font,
    fill=(255, 255, 255, 255)
)

# ============================================================
# MAIN HEADLINE
# ============================================================
headline_y = text_top + badge_size + 20

# "Never miss a"
draw.text(
    (left_margin, headline_y),
    "Never miss a",
    font=bold_font_64,
    fill=(238, 238, 240, 255)
)

# "chance to reply" (in orange)
draw.text(
    (left_margin, headline_y + 60),
    "chance to reply",
    font=bold_font_64,
    fill=(255, 107, 43, 255)
)

# ============================================================
# SUBTITLE
# ============================================================
subtitle_y = headline_y + 140

draw.text(
    (left_margin, subtitle_y),
    "Auto-reply to missed calls with SMS",
    font=regular_font_20,
    fill=(122, 122, 140, 255)
)

draw.text(
    (left_margin, subtitle_y + 30),
    "Privacy-first • Offline • No accounts",
    font=regular_font_20,
    fill=(122, 122, 140, 255)
)

# ============================================================
# RIGHT SECTION - PHONE MOCKUP
# ============================================================
phone_x = 670
phone_y = 80
phone_w = 220
phone_h = 340

# Phone outer shadow
shadow_offset = 3
draw.rounded_rectangle(
    [(phone_x + shadow_offset, phone_y + shadow_offset),
     (phone_x + phone_w + shadow_offset, phone_y + phone_h + shadow_offset)],
    radius=20,
    fill=(0, 0, 0, 100)
)

# Phone body
draw.rounded_rectangle(
    [(phone_x, phone_y), (phone_x + phone_w, phone_y + phone_h)],
    radius=20,
    fill=(19, 19, 26, 255),
    outline=(255, 255, 255, 50),
    width=2
)

# Notch/status bar
notch_h = 28
draw.rectangle(
    [(phone_x, phone_y), (phone_x + phone_w, phone_y + notch_h)],
    fill=(11, 11, 15, 255)
)

# Screen area
screen_x = phone_x + 12
screen_y = phone_y + notch_h + 8
screen_w = phone_w - 24
screen_h = phone_h - notch_h - 20

draw.rounded_rectangle(
    [(screen_x, screen_y), (screen_x + screen_w, screen_y + screen_h)],
    radius=12,
    fill=(27, 27, 37, 255)
)

# Phone content - icon
icon_y = screen_y + 40
draw.text(
    (screen_x + screen_w // 2 - 20, icon_y),
    "📱",
    font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40) if 'ImageFont' else regular_font_20,
    fill=(255, 255, 255, 255)
)

# Phone content - "Service Active" text
text_y = icon_y + 50
draw.text(
    (screen_x + 20, text_y),
    "Service",
    font=regular_font_16,
    fill=(238, 238, 240, 255)
)

draw.text(
    (screen_x + 20, text_y + 28),
    "Active",
    font=regular_font_16,
    fill=(238, 238, 240, 255)
)

draw.text(
    (screen_x + 20, text_y + 60),
    "Auto-replying",
    font=regular_font_16,
    fill=(122, 122, 140, 200)
)

draw.text(
    (screen_x + 20, text_y + 82),
    "to calls",
    font=regular_font_16,
    fill=(122, 122, 140, 200)
)

# CTA Button on phone
btn_w = 90
btn_h = 32
btn_x = screen_x + (screen_w - btn_w) // 2
btn_y = screen_y + screen_h - 50

draw.rounded_rectangle(
    [(btn_x, btn_y), (btn_x + btn_w, btn_y + btn_h)],
    radius=8,
    fill=(255, 107, 43, 255)
)

draw.text(
    (btn_x + 15, btn_y + 6),
    "Get Free",
    font=regular_font_16,
    fill=(255, 255, 255, 255)
)

# ============================================================
# SAVE IMAGE
# ============================================================
output_path = '/home/ricardo/Homespace/1_Projects/ping-reply/assets/feature-graphic.png'
img.save(output_path, 'PNG', quality=95)

print(f"✓ Feature graphic created: {output_path}")
print(f"  Dimensions: 1024×500 (Play Store requirement)")
print(f"  Design: Modern dark theme with orange accent")
print(f"  Ready for Google Play Console upload!")
