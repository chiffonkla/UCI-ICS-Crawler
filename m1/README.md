# ICS Search Engine

We are on the **developer** track (full `developer/DEV` corpus, index on disk, partial files + merge).


## What Milestone 1 is about

**Goal:** Build an **inverted index** from the crawled JSON pages and report basic statistics.

An inverted index maps each **word (token)** → **list of postings**. Each posting says which **document** had that word 
and the **term frequency (TF)** in that document. 
We do **not** store tf-idf in the index for M1; ranking comes in later milestones.


## How to Run 

From the **`team`** folder:

```powershell
cd team
pip install -r requirements.txt

# Full developer run (defaults: ../developer/DEV -> ../index/dev-all)
python main.py

# Small test
python main.py --corpus ..\analyst\ANALYST --output ..\index\test --limit 50 --docs-per-partial 8

# Or override paths explicitly
python main.py --corpus ..\developer\DEV --output ..\index\dev-all --docs-per-partial 5000
```

The **output** folder is created automatically. The **corpus** folder must already exist (your crawled JSON).
