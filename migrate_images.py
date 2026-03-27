import os
import shutil
import re

# ================= CONFIGURATION =================
SOURCE_DIR = "build/build/docs-idrs/16" 
DEST_DIR = "src/content/docs/16"
# =================================================

def migrate_images():
    print("🚀 Starting image migration...")
    
    # STEP 1: Copy and rename the _images folders
    for root, dirs, files in os.walk(SOURCE_DIR):
        if '_images' in dirs:
            src_images_path = os.path.join(root, '_images')
            # Calculate where this folder belongs in the Astro directory
            rel_path = os.path.relpath(root, SOURCE_DIR)
            # Rename '_images' to 'images' for the destination
            dest_images_path = os.path.normpath(os.path.join(DEST_DIR, rel_path, 'images'))
            
            # Remove old destination folder if it exists to prevent conflicts
            if os.path.exists(dest_images_path):
                shutil.rmtree(dest_images_path)
                
            shutil.copytree(src_images_path, dest_images_path)
            print(f"📁 Copied: {src_images_path} -> {dest_images_path}")

    # STEP 2: Update the links inside the .mdx files
    for root, dirs, files in os.walk(DEST_DIR):
        for file in files:
            if file.endswith('.mdx'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Regex replace: changes `_images/filename.png` to `images/filename.png`
                new_content = re.sub(r'_images/', 'images/', content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"🔗 Updated links in: {file}")

    print("🎉 Image Migration Complete!")

if __name__ == "__main__":
    migrate_images()