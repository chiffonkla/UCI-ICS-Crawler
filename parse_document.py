from bs4 import BeautifulSoup

def tokenize(text):
    tokens = []
    current = ""
    for ch in text:
        if ch.isalnum() and ch.isascii():
            current = current + ch.lower()
        else:
            if current != "":
                tokens.append(current)
                current = ""
    if current != "":
        tokens.append(current)
    return tokens

def Parse(document):
    if isinstance(document, dict):
        html = document.get("content", "")
    else:
        html = str(document)

    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style"]):
        tag.decompose()

    text = soup.get_text(" ", strip=True)

    return tokenize(text)