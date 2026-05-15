# Way to run everything together
# Later: add parse, buildIndex, merge in this file
import argparse
import os
import sys

from corpus_io import collect_pages, write_doc_ids
from index import buildPartialIndex

def main():
    # Read command-line options
    parser = argparse.ArgumentParser(description="Indexer milestone 1")
    parser.add_argument("--corpus", required=True, help="Folder with JSON pages, e.g. developer/DEV")
    parser.add_argument("--output", required=True, help="Output folder")
    parser.add_argument("--limit", type=int, default=None, help="Only load this many pages (for testing)")
    parser.add_argument(
        "--docs-per-partial",
        type=int,
        default=5000,
        help="Write one partial index file after every N pages (default 5000).",
    )
    args = parser.parse_args()

    # Load pages as [(doc_id, {"url", "content"}), ...]
    print("Reading corpus...")
    pages = collect_pages(args.corpus, limit=args.limit)
    if len(pages) == 0:
        print("No pages found. Check --corpus path.")
        sys.exit(1)

    # Write doc_ids.txt (one line per page: doc_id + tab + url)
    write_doc_ids(args.output, pages)
    print("Loaded", len(pages), "documents.")
    print("Wrote", os.path.join(args.output, "doc_ids.txt"))

    documents = [page for (doc_id, page) in pages]

    # index.py
    partialsFolder = os.path.join(args.output, "partials")
    print("Building partial index files in:", partialsFolder)
    print("(one partial file every", args.docs_per_partial, "pages)")
    partialPaths = buildPartialIndex(
        documents,
        partialsFolder,
        docsPerPartial=args.docs_per_partial,
    )
    print("Wrote", len(partialPaths), "partial index file(s).")
    if len(partialPaths) < 3 and args.limit is None:
        print(
            "Developer spec wants >= 3 partial files on full corpus.",
            "Use a smaller --docs-per-partial if you only see 1 or 2 files.",
        )

if __name__ == "__main__":
    main()
