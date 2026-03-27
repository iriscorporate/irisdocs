import os
import re

DEST_DIR = "src/content/docs/16"

def fix_all_svg_dimensions():
    print("🚀 Scanning all SVGs for missing dimensions...")
    files_fixed = 0
    
    for root, dirs, files in os.walk(DEST_DIR):
        for file in files:
            if file.endswith('.svg'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Find the opening <svg ... > tag
                svg_tag_match = re.search(r'<svg[^>]*>', content)
                
                if svg_tag_match:
                    svg_tag = svg_tag_match.group(0)
                    
                    # If it's missing width or height, inject them!
                    if 'width=' not in svg_tag or 'height=' not in svg_tag:
                        # Safely insert width and height right after <svg
                        new_svg_tag = svg_tag.replace('<svg', '<svg width="100%" height="100%"')
                        
                        # Replace the old tag with the new tag in the file
                        new_content = content.replace(svg_tag, new_svg_tag)
                        
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                            
                        print(f"🔧 Fixed dimensions for: {file}")
                        files_fixed += 1
                        
    print(f"🎉 Done! Injected dimensions into {files_fixed} SVG files.")

if __name__ == "__main__":
    fix_all_svg_dimensions()