import os
import re

DEST_DIR = "src/content/docs/16"

def sanitize_svgs():
    print("🚀 Running Ultimate SVG Sanitizer...")
    files_fixed = 0
    
    for root, dirs, files in os.walk(DEST_DIR):
        for file in files:
            if file.endswith('.svg'):
                filepath = os.path.join(root, file)
                
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    # 1. Strip all XML junk before the <svg> tag
                    content = re.sub(r'^.*?<svg', '<svg', content, flags=re.DOTALL|re.IGNORECASE)
                    
                    # 2. Strip existing width and height to prevent duplicates or percentages
                    content = re.sub(r'\bwidth="[^"]*"', '', content, flags=re.IGNORECASE)
                    content = re.sub(r'\bheight="[^"]*"', '', content, flags=re.IGNORECASE)
                    
                    # 3. Astro STRONGLY prefers hard numbers (pixels). We inject a safe default.
                    new_svg_tag = '<svg width="800" height="600"'
                    content = re.sub(r'<svg', new_svg_tag, content, count=1, flags=re.IGNORECASE)
                    
                    # 4. Remove any embedded scripts that might crash the server renderer
                    content = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL|re.IGNORECASE)
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                        
                    files_fixed += 1
                except Exception as e:
                    print(f"⚠️ Failed to process {file}: {e}")
                    
    print(f"🎉 Done! Fully sanitized {files_fixed} SVGs.")

if __name__ == "__main__":
    sanitize_svgs()