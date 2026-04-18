import re
import glob

talks = []

def parse_md(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # regex to find blocks basically splitting by numbers 1. 2. 3. or # 1.
    blocks = re.split(r'\n#?\s*\d+\.\s*', text)
    
    for block in blocks[1:]:
        line1 = block.strip().split('\n')[0]
        # find title
        title_match = re.search(r'Title:\s*(.*?)(?=Abstract:|$|#)', block, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).replace('\n', ' ').strip() if title_match else ''
        
        # fix line wrap words
        title = re.sub(r'-\s+', '', title)
        title = re.sub(r'\s+', ' ', title)
        
        print("EVT:", line1)
        print("TIT:", title)
        print("---")

for f in sorted(glob.glob('material/*.md')):
    parse_md(f)

