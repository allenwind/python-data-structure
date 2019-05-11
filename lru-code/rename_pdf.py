import os
import pdfrw

def rename_pdf(path):
    os.chdir(path)
    files = os.listdir(".")
    for file in files:
        if file.endswith(".pdf"):
            r = pdfrw.PdfReader(file)
            if r.Info.Title is None:
                continue
            title = r.Info.Title.strip("()").replace(":", " ")
            new_name = os.path.join(path, title + ".pdf")
            try:
                os.rename(file, new_name)
            except Exception as err:
                print(err)

if __name__ == "__main__":
    path = r"C:\Users\Administrator\Desktop\paper"
    rename_pdf(path)
