class PDFReader:
    def open(self):
        print ("PDF Reader opening...")

class ImageViewer:
    def open(self):
        print ("Image Viewer opening...")

pdf=PDFReader()
image=ImageViewer()

pdf.open()
image.open()