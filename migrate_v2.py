import os
import re
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# ================= CONFIGURATION =================
# Updated to match the double-build folder in your structure.txt
SOURCE_DIR = "build/build/docs-idrs/16" 
DEST_DIR = "src/content/docs/16"
# =================================================

def clean_antora_html(soup):
    """Isolates main content from Antora UI."""
    article = soup.find('article', class_='doc')
    if not article:
        return None

    # Extract Title for Frontmatter
    h1 = article.find('h1')
    title = h1.get_text().strip() if h1 else "Untitled"
    if h1:
        h1.decompose()

    # Remove Pagination (Next/Prev links)
    pagination = article.find('nav', class_='pagination')
    if pagination:
        pagination.decompose()

    # Convert Admonitions (Note, Warning, etc.) to Starlight syntax
    for admonition in article.find_all('div', class_='admonitionblock'):
        admonition_type = "note"
        classes = admonition.get('class', [])
        if 'tip' in classes: admonition_type = 'tip'
        elif 'warning' in classes: admonition_type = 'caution'
        elif 'important' in classes: admonition_type = 'danger'
        
        content_cell = admonition.find('td', class_='content')
        if content_cell:
            new_text = f"\n:::{admonition_type}\n{content_cell.get_text().strip()}\n:::\n"
            admonition.replace_with(BeautifulSoup(new_text, "html.parser"))

    return title, article

def process_directory():
    print(f"🚀 Starting migration from {SOURCE_DIR}...")
    
    for root, _, files in os.walk(SOURCE_DIR):
        for file in files:
            if not file.endswith(".html"):
                continue
                
            # Calculate paths
            source_path = os.path.join(root, file)
            # Maintain the subfolder structure (e.g., developer-guide-idrs16/)
            relative_path = os.path.relpath(source_path, SOURCE_DIR)
            dest_path = os.path.join(DEST_DIR, relative_path).replace('.html', '.mdx')
            
            # Read and parse HTML
            with open(source_path, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
                
            result = clean_antora_html(soup)
            if not result:
                print(f"⏭️ Skipping {relative_path} (No content found)")
                continue
                
            title, cleaned_html = result
            
            # Convert to Markdown
            markdown_content = md(str(cleaned_html), heading_style="atx")
            markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content) # Cleanup spacing
            
            # Create Frontmatter
            frontmatter = f"---\ntitle: \"{title}\"\n---\n\n"
            final_output = frontmatter + markdown_content
            
            # Save file
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            with open(dest_path, 'w', encoding='utf-8') as f:
                f.write(final_output)
                
            print(f"✅ Converted: {relative_path}")

if __name__ == "__main__":
    if not os.path.exists(SOURCE_DIR):
        print(f"❌ Error: Source folder '{SOURCE_DIR}' not found. Check your path.")
    else:
        process_directory()
        print("🎉 Migration Complete!")