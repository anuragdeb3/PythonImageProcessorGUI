from PIL import ImageTk
from PIL import Image as PilImage
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog


class ImageCompressor(Tk):
    def __init__(self, winTitle, xSize, ySize, *args):
        super(ImageCompressor, self).__init__()
        if args:
            self.configure(bg=args)
        self.geometry(f'{xSize}x{ySize}')
        self.title(winTitle)
        self.resizable(False, False)
        self.compressFile = Label(self, text="1. Choose Your Image", font=("Courier", 10))
        self.compressFile.place(x=25, y=15)
        self.compressFile = Button(text="Upload Image", command=self.GetImageFile)
        self.compressFile.place(x=300, y=10)

        self.chooseQuality = Label(self, text="2. Choose Image quality", font=("Courier", 10))
        self.chooseQuality.place(x=25, y=60)

        self.scaleValue = Scale(self, from_=0, to=100, orient=HORIZONTAL)
        self.scaleValue.place(x=300, y=55)

        self.compressFile = Label(self, text="3. Choose which folder to save to", font=("Courier", 10))
        self.compressFile.place(x=25, y=100)
        self.saveFolder = Button(text="Choose folder", command=self.SavedFolder)
        self.saveFolder.place(x=300, y=100)

        self.imageNameLabel = Label(text="4. Enter new file name(without extension)")
        self.imageNameLabel.place(x=25, y=160)
        self.imageName = Entry(self, bd=3)
        self.imageName.place(x=300, y=165)

        self.compressImageBtn = Button(text="5. Compress Image", command=self.CompressImage, bd=5)
        self.compressImageBtn.place(x=190, y=200)

        self.compressImageBtn = Button(text="6. Exit", command=self.close, bd=5)
        self.compressImageBtn.place(x=220, y=250)

        self.saveFolder = Label(self, text="(ɔ) Anu", font=("Courier", 10),fg='#4287f5')
        self.saveFolder.place(x=400, y=380)




        self.mainloop()

    def GetImageFile(self):
        self.compressLocation = filedialog.askopenfilename()

        if self.compressLocation:
           # messagebox.showinfo("File", self.compressLocation)
            self.compressFile = Label(self, text="Image Path Chosen:  " + self.compressLocation, font=("Courier", 10),fg='#4287f5')
            self.compressFile.place(x=25, y=35)
        else:
            messagebox.showwarning("Error", "No image selected")

    def SavedFolder(self):
        self.saveTo = filedialog.askdirectory()


        if self.saveTo:
            #messagebox.showinfo("Save to:", self.saveTo)
            self.saveFolder = Label(self, text="Image Save Directory Chosen: " + self.saveTo, font=("Courier", 10),fg='#4287f5')
            self.saveFolder.place(x=25, y=130)
        else:
            messagebox.showwarning("Error", "No folder selected")

    def CompressImage(self):
        self.scaleNum = self.scaleValue.get()
        try:
            self.imageToCompress = PilImage.open(self.compressLocation)
            self.getImageExtension = self.compressLocation.rsplit(".", 1)
            self.imageExtension = self.getImageExtension[1]
            self.imageEntryName = self.imageName.get()
            self.imageToCompress.save(f"{self.saveTo}/{self.imageEntryName}.{self.imageExtension}",
                                      quality=self.scaleNum)
            messagebox.showinfo("Successful", f"Compressed image saved to {self.saveTo}")
        except:
            messagebox.showwarning("Error", "Something went wrong. Redo the Steps in Ascending Order")

    def close(self):
             #self.destroy()
             self.quit()

MyNewGUI = ImageCompressor("Anu Image Compressor", 600, 405)

