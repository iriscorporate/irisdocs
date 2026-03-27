import os
import re

# Where your MDX files live
DEST_DIR = "src/content/docs/16"

def fix_mdx_links():
    print("🚀 Scanning for broken MDX links...")
    
    # This regex looks for anything starting with http:// or https:// wrapped in < >
    pattern = re.compile(r'<(https?://[^>]+)>')
    
    files_fixed = 0
    
    for root, dirs, files in os.walk(DEST_DIR):
        for file in files:
            if file.endswith('.mdx'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace <url> with [url](url)
                new_content, subs = pattern.subn(r'[\1](\1)', content)
                
                if subs > 0:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"🔧 Fixed {subs} link(s) in: {file}")
                    files_fixed += 1
                    
    print(f"🎉 Done! Fixed links in {files_fixed} files.")

if __name__ == "__main__":
    fix_mdx_links()