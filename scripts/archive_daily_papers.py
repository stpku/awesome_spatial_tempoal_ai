import os
import json
import re
import datetime
import glob

ST_DAILY_REPORT_DIR = "/mnt/d/04_代码/code/ST-dailyreport"
AWESOME_DIR = "/mnt/d/04_代码/code/awesome_spatial_temporal_ai"
PAPERS_JSON_PATH = os.path.join(AWESOME_DIR, "awesomelist", "papers.json")

def find_latest_report():
    # Find all .md files in ST-dailyreport/YYYY/MM/DD/
    # Pattern: ST-dailyreport/202*/0*/2*/geoai_world-model_dashboard_*.md
    # We want the one with the latest date in the filename
    
    # Walk through the directory to find all md files matching the pattern
    md_files = []
    for root, dirs, files in os.walk(ST_DAILY_REPORT_DIR):
        for file in files:
            if file.startswith("geoai_world-model_dashboard_") and file.endswith(".md") and "en_" not in file:
                path = os.path.join(root, file)
                # Extract date from filename
                match = re.search(r"(\d{4}-\d{2}-\d{2})", file)
                if match:
                    date_str = match.group(1)
                    md_files.append((date_str, path))
    
    if not md_files:
        return None
    
    # Sort by date descending
    md_files.sort(key=lambda x: x[0], reverse=True)
    return md_files[0][1]

def parse_papers(md_path):
    print(f"Parsing report: {md_path}")
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find "A. Top Papers" section
    # The section starts with "## A. Top Papers" and ends with "---"
    section_match = re.search(r"## A\. Top Papers(.*?)\n---", content, re.DOTALL)
    if not section_match:
        print("Could not find 'A. Top Papers' section.")
        return []
    
    section_content = section_match.group(1)
    
    # Extract papers
    # Format:
    # 1) **Title**
    # - Link: url (date)
    # - One-line Insight: description
    
    papers = []
    # Split by numbering like "1) ", "2) "
    items = re.split(r"\n\d+\) ", section_content)
    
    for item in items:
        if not item.strip():
            continue
            
        # Extract Title
        title_match = re.search(r"\*\*(.*?)\*\*", item)
        if not title_match:
            continue
        title = title_match.group(1).strip()
        
        # Extract Link
        link_match = re.search(r"- Link: (http[^\s\u4e00-\u9fa5]+)", item)
        url = link_match.group(1).strip() if link_match else ""
        
        # Extract Insight
        insight_match = re.search(r"- \*\*One-line Insight:\*\* (.*)", item)
        if not insight_match:
             insight_match = re.search(r"- One-line Insight: (.*)", item)
             
        description = insight_match.group(1).strip() if insight_match else ""
        
        # Extract Date/Year if available in Link line e.g. (2026-01-23)
        date_match = re.search(r"\((\d{4}-\d{2}-\d{2})\)", item)
        year = int(date_match.group(1)[:4]) if date_match else datetime.date.today().year
        
        # Clean title (remove translated title in brackets if present)
        # Example: "校准的 GEDI 生物量概率插值（Calibrated Probabilistic Interpolation for GEDI Biomass）"
        # We want "Calibrated Probabilistic Interpolation for GEDI Biomass"
        english_title_match = re.search(r"（(.*?)）", title)
        if english_title_match:
            # Check if the part in brackets looks like English (ASCII)
            candidate = english_title_match.group(1)
            if all(ord(c) < 128 for c in candidate.replace(" ", "")):
                title = candidate
        
        paper = {
            "title": title,
            "authors": "Unknown", # Markdown doesn't have authors usually
            "year": year,
            "venue": "arXiv" if "arxiv.org" in url else "Unknown",
            "citations": 0,
            "url": url,
            "description": description,
            "task": [],
            "publisher": "Unknown"
        }
        papers.append(paper)
        
    return papers

def update_json(new_papers):
    if not os.path.exists(PAPERS_JSON_PATH):
        print(f"Error: {PAPERS_JSON_PATH} not found.")
        return

    with open(PAPERS_JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    existing_urls = set(p.get('url') for p in data.get('papers', []))
    existing_titles = set(p.get('title') for p in data.get('papers', []))
    
    added_count = 0
    for paper in new_papers:
        if paper['url'] in existing_urls:
            print(f"Skipping existing URL: {paper['url']}")
            continue
        if paper['title'] in existing_titles:
            print(f"Skipping existing Title: {paper['title']}")
            continue
            
        data['papers'].insert(0, paper) # Add to top
        existing_urls.add(paper['url'])
        added_count += 1
        print(f"Added: {paper['title']}")
        
    if added_count > 0:
        with open(PAPERS_JSON_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Successfully added {added_count} papers to {PAPERS_JSON_PATH}")
    else:
        print("No new papers to add.")

if __name__ == "__main__":
    latest_md = find_latest_report()
    if latest_md:
        papers = parse_papers(latest_md)
        if papers:
            update_json(papers)
        else:
            print("No papers found in the report.")
    else:
        print("No daily report found.")
