import os
import re

# Where your MDX files and images live
DEST_DIR = "src/content/docs/16"

def clean_svgs():
    print("🚀 Scanning for problematic SVGs...")
    files_fixed = 0
    
    for root, dirs, files in os.walk(DEST_DIR):
        for file in files:
            if file.endswith('.svg'):
                filepath = os.path.join(root, file)
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # 1. Strip everything before the <svg tag (removes XML prologs and comments)
                    # This is the #1 cause of Astro SVG crashes
                    new_content = re.sub(r'^.*?<svg', '<svg', content, flags=re.DOTALL)
                    
                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"🔧 Cleaned junk headers from: {file}")
                        files_fixed += 1
                except Exception as e:
                    print(f"⚠️ Could not process {file}: {e}")
                    
    print(f"🎉 Done! Cleaned {files_fixed} SVG files.")

if __name__ == "__main__":
    clean_svgs()