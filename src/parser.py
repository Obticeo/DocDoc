import requests
from langchain_text_splitters import MarkdownHeaderTextSplitter
from pathlib import Path
from tqdm import tqdm
import re
import json
DATA_DIR = Path(__file__).parents[1] / 'data/raw'
print(DATA_DIR,DATA_DIR.exists())
def process_md():
    if not DATA_DIR.exists():
        raise FileNotFoundError(f'Data directory {DATA_DIR} does not exist')
    headers_to_split_on = [('#', 'Header 1'), ('##', 'Header 2'), ('###', 'Header 3')]
    processed_chunks = []
    md_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on, return_each_line=True)
    md_files = DATA_DIR.glob('*.md')
    for md_file in tqdm(md_files):
        with open(md_file, 'r', encoding='utf-8') as f:
            md_text = f.read()
        page_context = ''
        
        md_chunks = md_splitter.split_text(md_text)
        for i, chunk in enumerate(md_chunks):
            chunk_content = chunk.page_content.strip()
            if not chunk_content:
                continue
            h1 = chunk.metadata.get("Header 1", "")
            h2 = chunk.metadata.get("Header 2", "")
            h3 = chunk.metadata.get("Header 3", "")
            hierarchy_trail = " -> ".join([h for h in [h1, h2, h3] if h])
            
            connection_data = f"{(page_context) if page_context else ''}\nSection: {hierarchy_trail}\n\n{chunk_content}"
            chunk_payload = {
                "id": f"{str(md_file)}_chunk_{i}",
                "text": connection_data,
                "metadata": {
                    "file_name": str(md_file),
                    "section_hierarchy": hierarchy_trail,
                    "has_code_block": "```" in chunk_content,
                }
            }
            processed_chunks.append(chunk_payload)
        print(f"⚡ Parsed {md_file} into {len(md_chunks)} structured blocks.")
    print(f"🎉 Analysis Complete. Total chunks formatted: {len(processed_chunks)}")
    return processed_chunks

if __name__ == '__main__':
    chunks = process_md()
    if chunks:
        print("\n🔍 Sample Structure of Chunk 0:")
        print(json.dumps(chunks[1112], indent=2))