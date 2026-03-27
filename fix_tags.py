import os
import re

DEST_DIR = "src/content/docs/16"

def fix_fake_components():
    print("🚀 Scanning for class names disguised as React components...")
    
    # This regex looks for `<` followed by a Capital letter, 
    # then any characters, ending with `>`.
    # It replaces them with &lt;ClassName&gt;
    pattern = re.compile(r'<([A-Z][a-zA-Z0-9_]*\b[^>]*)>')
    
    files_fixed = 0
    
    for root, dirs, files in os.walk(DEST_DIR):
        for file in files:
            if file.endswith('.mdx'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace <ClassName> with &lt;ClassName&gt;
                new_content, subs = pattern.subn(r'&lt;\1&gt;', content)
                
                if subs > 0:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"🔧 Escaped {subs} class name(s) in: {file}")
                    files_fixed += 1
                    
    print(f"🎉 Done! Fixed code tags in {files_fixed} files.")

if __name__ == "__main__":
    fix_fake_components()