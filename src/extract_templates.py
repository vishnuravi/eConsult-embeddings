import os
from docx import Document


def extract_text_from_docx(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        if para.text.strip():  # Avoid empty lines
            full_text.append(para.text.strip())
    return "\n".join(full_text)


def extract_all_templates(directory_path):
    templates = {}
    for filename in os.listdir(directory_path):
        if filename.endswith(".docx"):
            file_path = os.path.join(directory_path, filename)
            text = extract_text_from_docx(file_path)
            templates[filename] = text
    return templates


if __name__ == "__main__":
    templates_dir = "templates"  # Folder where you placed the .docx files
    templates = extract_all_templates(templates_dir)

    # Save extracted templates to a text file (optional)
    with open("extracted_templates.txt", "w", encoding="utf-8") as f:
        for filename, content in templates.items():
            f.write(f"--- {filename} ---\n")
            f.write(content + "\n\n")

    print("Templates extracted successfully. Check 'extracted_templates.txt' for output.")
