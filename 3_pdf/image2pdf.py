import os
import img2pdf
import PyPDF2
from io import BytesIO

path = "/home/sudhanshu/Downloads/"


with open(path + "output.pdf", "wb") as f:
    f.write(img2pdf.convert([i for i in os.listdir(".") if i.endswith(".png")]))

# sh ~/reducepdf.sh UbuntuDocs

# gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4
# -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH
# -sOutputFile=$1small.pdf $1.pdf
