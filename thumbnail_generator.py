from PIL import Image, ImageDraw, ImageFont
import os
import re

# Set up
titles = [
    "Fractured Trail",
    "Monologue",
    "Series -1 | Episode -4",
    "Armalakot--April 1, 2022",
    "Ghatichina | SATURDAY | Kayaking",
    "Dashain 2081 | ASMR Kot Mandir | Syangja, Aandhikhola",
    "Dashain 2081 | Syangja Aandhikhola | Dashain Festival",
    "Series -1 | Episode -3",
    "Mardi Base Camp 4500m | Solo Trek",
    "What does it look like if you trek ABC solo? | ASMR TRAVEL",
    "jitey ft. Bimal chhetry | Music from: conscious [prod. By seishil]",
    "ANNAPURNA BASE CAMP | ABC TREK | 4130M",
    "Ghandruk To Germany ft. Kaley ( Ashok )",
    "Series -1 | Episode -2",
    "Ghandruk | Friends",
    "MYSTIC MISTY MONSOON | KORI, NEPAL | 3850M",
    "BACK TO HOME || FROM DHORPATAN || DAY - 04",
    "LAST DAY ON DHORPATAN || DAY -03 || BACK TO BAGLUNG",
    "DHORPATAN || DAY -02 || EXPLORE & HORSE RIDING",
    "DHORPATAN - DAY 2 || Dhorpatan Hunting Reserve",
    "DHORPATAN || DAY -01 || Dhorpatan Hunting Reserve",
    "Kaley dai ko museum yatra || International Mountain Museum",
    "Geet man paryo || Mar-masala Farm Kitchen || How to get there",
    "Birthday wala Nightout || Kalsee Eco Lodge",
    "Random Saturday -#11",
    "Testing #1 - Hero 11",
    "Aarati at lakeside|| Mummy !!",
    "Syangja- snowfall",
    "Dhampus !!",
    "Data Typing at Fewataa!?",
    "Thaple (syangja-biggest statue of buddha)",
    "Roshan Ko Bihey | 2080-01-07",
    "UNBOXING | MACBOOK M2 PRO | 2023",
    "The Road Trip of a Lifetime | Supa Deurali Temple | Nepal to India",
    "Want to be happy? Make good friends !",
    "Pokhara To Lo-Manthang || UPPER MUSTANG",
    "Day 4: Marpha to Tatopani To HOME || UPPER MUSTANG",
    "Day 3: Muktinaath to Dhumba lake To Marpha || UPPER MUSTANG",
    "Self-filming - A Tale to Tell",
    "Day 2: Lo manthang to Korola Border To Muktinath || UPPER MUSTANG",
    "Homebound | 2024",
    "ASMR Travel | Sikles to Sikles Park | Kori Trek",
    "CHANDHIIAAN || SYANGJA || PANCHAULI PUJA",
    "DASHAlN || SYANGJA AANDHIKHOLA || HOMETOWN",
    "CHANGA VLOG 2023 | POKHARA-LAMAGAUN",
    "Dashain || 2080",
    "Guitar Fingerstyle | KISS ME, CLOSE YOUR EYES.",
    "Thaple | Syangja | Biggest Statue of Budhha",
    "Bandipur vol.1",
    "sikles | Hugu | kapuche | Lowest glacial lake - Episode - 1",
    "short pubg experience..!",
    "international mountain musem, pokhara",
    "Asphalt 8 Airborne"
    # ...add remaining titles here
]


# Save to Downloads folder
output_dir = os.path.expanduser("./thumbnails")
os.makedirs(output_dir, exist_ok=True)


# Load Jersey 10 font (make sure you have it or download .ttf file)
font_path = "//Users/bimalchhetry/Downloads/Jersey_10/Jersey10-Regular.ttf"  # ← Change to actual path of Jersey 10
font_size = 100  # Adjust size as needed

try:
    font = ImageFont.truetype(font_path, font_size)
except IOError:
    print("Font file not found. Please make sure 'jersey10.ttf' exists.")
    exit()

# Generate thumbnails
for i, title in enumerate(titles):
    img = Image.new('RGB', (1920, 1080), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Text wrapping logic if too long
    max_width = 1700
    lines = []
    words = title.split()
    line = ""

    for word in words:
        test_line = f"{line} {word}".strip()
        if draw.textlength(test_line, font=font) <= max_width:
            line = test_line
        else:
            lines.append(line)
            line = word
    lines.append(line)

    total_height = sum([draw.textbbox((0, 0), l, font=font)[3] for l in lines]) + 20 * (len(lines) - 1)
    current_y = (1080 - total_height) // 2

    for line in lines:
        text_width = draw.textlength(line, font=font)
        draw.text(((1920 - text_width) / 2, current_y), line, font=font, fill="white")
        current_y += font_size + 20

    # Clean filename
    safe_title = re.sub(r'[\\/*?:"<>|]', "_", title)
    filename = os.path.join(output_dir, f"{safe_title}.png")
    img.save(filename)
print(f"✅ All thumbnails generated in: {os.path.abspath(output_dir)}")


print("✅ All thumbnails generated.")
