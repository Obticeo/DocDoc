
import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
from urllib.parse import urlparse
import re
import os
from pathlib import Path

url="https://docs.crawl4ai.com/core/simple-crawling/"
OUTPUT_DIR= Path('./data/raw')
def give_filename(url: str) -> str:
    parsed_url = urlparse(url)
    name = parsed_url.path.strip("/")
    if not name:
        return "index.md"
    name = name.replace("/", "__") 
    return f"{name}.md"

print(give_filename(url))
async def main(root_url):
    browser_config = BrowserConfig()  
    print(f'Getting Table of Contents tree at: {root_url}')
    prefetch_config = CrawlerRunConfig(prefetch=True) 

    async with AsyncWebCrawler(config=browser_config) as crawler:
        root_result = await crawler.arun(url=root_url, config=prefetch_config)
        
        if not root_result.success:
            print(f"Failed to get root documentation TOF. Error: {root_result.error_message}")
            return
        discovered_links = root_result.links.get("internal", [])
        list_of_urls = list({link['href'] for link in discovered_links})
        
        print(f'Scraping the table of contents: Total {len(list_of_urls)}')
        scrape_config = CrawlerRunConfig(
            word_count_threshold=15, 
            excluded_tags=['nav', 'aside'],
            exclude_external_links=True,
            exclude_social_media_links=True
        )
        results = await crawler.arun_many(
            urls=list_of_urls,  
            config=scrape_config,
            max_concurrent=5 
        )

        for result in results:
            if result.success:
                print(result.url)
                filename = give_filename(result.url)
                print(filename)
                filepath = OUTPUT_DIR / filename
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(result.markdown)
                print(f"Saved file: {filename}")
            else:
                print(f"Skipped file: {result.url} (error)")
if __name__ == "__main__":
    asyncio.run(main(url))