# Way to run everything together
# Later: add parse, buildIndex, merge in this file
import argparse
import os
import sys

from corpus_io import collect_pages, write_doc_ids
from index import buildIndex, buildPartialIndex

def main():
    # Read command-line options
    parser = argparse.ArgumentParser(description="Indexer milestone 1")
    parser.add_argument("--corpus", required=True, help="Folder with JSON pages, e.g. developer/DEV")
    parser.add_argument("--output", required=True, help="Output folder")
    parser.add_argument("--limit", type=int, default=None, help="Only load this many pages (for testing)")
    parser.add_argument(
        "--memory",
        action="store_true",
        help="Keep inverted index in RAM only (small tests). Default: write partial files to disk.",
    )
    parser.add_argument(
        "--docs-per-partial",
        type=int,
        default=5000,
        help="Write one partial index file after every N pages (default 5000). "
        "Full DEV (~55k pages) -> about 11 partial files.",
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
    corpus_label = os.path.normpath(args.corpus)

    # index.py
    memoryIndex = None
    partialsFolder = None

    if args.memory:
        print("Building in-memory index (--memory)...")
        memoryIndex = buildIndex(documents)
    else:
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
                "Note: developer spec wants >= 3 partial files on full corpus.",
                "Use a smaller --docs-per-partial (e.g. 5000) so RAM spills more often.",
            )

if __name__ == "__main__":
    main()
