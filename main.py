# Way to run everything together
# Later: add parse, buildIndex, merge in this file
import argparse
import os
import sys

from corpus_io import collect_pages, write_doc_ids

def main():
    # Read command-line options
    parser = argparse.ArgumentParser(description="Load crawl JSON and write doc_ids.txt")
    parser.add_argument("--corpus", required=True, help="Folder with JSON pages, e.g. developer/DEV")
    parser.add_argument("--output", required=True, help="Folder to write doc_ids.txt into")
    parser.add_argument("--limit", type=int, default=None, help="Only load this many pages (for testing)")
    args = parser.parse_args()

    # Load pages as [(doc_id, {"url", "content"}), ...]
    pages = collect_pages(args.corpus, limit=args.limit)
    if len(pages) == 0:
        print("No pages found. Check --corpus path.")
        sys.exit(1)

    # Write doc_ids.txt (one line per page: doc_id + tab + url)
    write_doc_ids(args.output, pages)
    print("Loaded", len(pages), "documents.")
    print("Wrote", os.path.join(args.output, "doc_ids.txt"))

if __name__ == "__main__":
    main()
