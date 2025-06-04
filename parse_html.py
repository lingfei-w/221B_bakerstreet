import sys
import os
from bs4 import BeautifulSoup
import pandas as pd


def parse_html(file_path: str) -> pd.DataFrame:
    """Parse the HTML file and return extracted data as a DataFrame."""
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    data = []
    for tag in soup.find_all(["h1", "h2", "h3", "p", "a"]):
        data.append({"tag": tag.name, "text": tag.get_text(strip=True)})

    return pd.DataFrame(data)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python parse_html.py <path_to_html> [output_file]")
        sys.exit(1)

    html_file = sys.argv[1]
    if not os.path.exists(html_file):
        print(f"File not found: {html_file}")
        sys.exit(1)

    df = parse_html(html_file)
    output_file = sys.argv[2] if len(sys.argv) > 2 else "output.csv"

    if output_file.lower().endswith(".xlsx"):
        df.to_excel(output_file, index=False)
    else:
        df.to_csv(output_file, index=False)

    print(f"Saved extracted data to {output_file}")


if __name__ == "__main__":
    main()
