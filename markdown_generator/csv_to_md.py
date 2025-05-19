import os

# Output directory for markdown files
output_dir = "../_publications"
os.makedirs(output_dir, exist_ok=True)

# Generate markdown files from CSV
for index, row in df.iterrows():
    year = str(row["Year"])
    date = f"{year}-01-01"
    title = row["Title"]
    slug = title.lower().replace(" ", "-").replace(",", "").replace(":", "").replace(".", "").strip()
    filename = f"{date}-{slug[:50]}.md"  # Truncate filename for safety
    filepath = os.path.join(output_dir, filename)

    authors = row["Authors"]
    venue = row["Publication"]
    citation_parts = [authors, f"({year})", title, venue]
    if not pd.isna(row["Volume"]):
        citation_parts.append(f"Vol. {row['Volume']}")
    if not pd.isna(row["Number"]):
        citation_parts.append(f"No. {row['Number']}")
    if not pd.isna(row["Pages"]):
        citation_parts.append(f"pp. {row['Pages']}")
    if not pd.isna(row["Publisher"]):
        citation_parts.append(row["Publisher"])

    citation = ". ".join(str(p).strip() for p in citation_parts if str(p).strip())

    with open(filepath, "w", encoding="utf-8") as f:
        f.write('---\n')
        f.write(f'title: "{title}"\n')
        f.write(f'collection: publications\n')
        f.write(f'permalink: /publication/{slug}\n')
        f.write(f'date: {date}\n')
        f.write(f'venue: "{venue}"\n')
        f.write(f'authors: "{authors}"\n')
        f.write(f'paperurl: ""\n')
        f.write(f'citation: "{citation}"\n')
        f.write('---\n')

# Output path for download
output_dir