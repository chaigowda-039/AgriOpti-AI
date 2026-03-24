import os
import re

directories = [
    'dashboard_overview',
    'soil_crop_analyzer',
    'irrigation_water_prediction',
    'fleet_management',
    'live_fleet_map'
]

base_dir = r"c:\Users\ASUS\Downloads\agri new\nw"

for d in directories:
    file_path = os.path.join(base_dir, d, 'code.html')
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine sidebar tag, might be <aside> or <nav>
    # Find <header>...</header>
    content = re.sub(r'<header.*?</header>', '', content, flags=re.DOTALL)
    
    # Find sidebar <aside>...</aside> or <nav>...</nav> that has w-64 or left-0 top-0
    content = re.sub(r'<aside\b[^>]*?w-64[^>]*>.*?</aside>', '', content, flags=re.DOTALL)
    content = re.sub(r'<nav\b[^>]*?w-64[^>]*>.*?</nav>', '', content, flags=re.DOTALL)
    
    # Remove ml-64, pl-64, pt-16 from <main>
    content = content.replace('ml-64', '')
    content = content.replace('pl-64', '')
    content = content.replace('pt-16', '')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Processed {d}")
