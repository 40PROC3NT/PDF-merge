import tkinter as tk
from tkinter import filedialog as fd
import PyPDF2
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
import tkinter.font as font


class GUI(object): 
    def __init__(self): 

        self.window=tk.Tk()
        self.window.geometry("400x300")
        self.window.title("Merge PDF App")

        self.font = font.Font(family='Courier', size=10)

        self.window.rowconfigure(4, minsize=50)
        self.window.columnconfigure(1, minsize=50)
        self.window.configure(background='black')

        self.files = None
        self.pdfWriter = None

        frame1 = tk.Frame(master=self.window, width=50, height=50, bg="black")
        frame1.pack()

        self.button1=tk.Button(self.window, text="Select PDF files", bg='#0052cc', fg='#ffffff', width=40, command=self.open_files)
        self.button1['font'] = self.font
        self.button1.pack()

        frame1 = tk.Frame(master=self.window, width=50, height=10, bg="black")
        frame1.pack()

        self.button2=tk.Button(self.window, text="Reset files",  bg='#0052cc', fg='#ffffff', width=40, command=self.reset_files)
        self.button2['font'] = self.font
        self.button2.pack()

        frame2 = tk.Frame(master=self.window, width=50, height=30, bg="black")
        frame2.pack()

        self.button3=tk.Button(self.window, text="Merge PDF files",  bg='#0052cc', fg='#ffffff', width=40, command=self.merge_files)
        self.button3['font'] = self.font
        self.button3.pack()

        frame3 = tk.Frame(master=self.window, width=50, height=30, bg="black")
        frame3.pack()

        self.button4=tk.Button(self.window, text="Save merged PDF",  bg='#0052cc', fg='#ffffff', width=40, command=self.save_file)
        self.button4['font'] = self.font
        self.button4.pack()

        self.window.mainloop() 


    def open_files(self):
        filetypes = (
        ('text files', '*.pdf'),
        ('All files', '*.*'))

        files = fd.askopenfilenames(
        initialdir='C:\\',
        filetypes=filetypes)

        if len(files) == 0:
            self.files = None
        else:
            self.files = files


    def merge_files(self):
        files = self.files

        if self.files is not None:

            # Create a new PdfFileWriter object which represents a blank PDF document
            pdfWriter = PyPDF2.PdfFileWriter()
            # Open the files that have to be merged one by one
            for file in files:
                print(file)

                # Read the files that you have opened
                fp = open(file, 'rb')
                pdf_file = PyPDF2.PdfFileReader(fp)
                
                # Loop through all the pagenumbers for the first document
                for pageNum in range(pdf_file.numPages):
                    pageObj = pdf_file.getPage(pageNum)
                    pdfWriter.addPage(pageObj)

                # Adding blank page    
                if (pdf_file.numPages % 2) != 0 and file != files[-1]:
                    pdfWriter.addBlankPage()

            self.pdfWriter = pdfWriter

            showinfo("Done", "All files are merged successfully!")

        else:
            showinfo("Error", "No files selected! Select files to merge!")

    
    def reset_files(self):
        self.files = None
        self.pdfWriter = None


    def save_file(self):
        if self.pdfWriter is not None:
            pdfWriter = self.pdfWriter
            # Now that you have copied all the pages in both the documents, write them into the a new document
            filename = fd.asksaveasfilename(filetypes=[("PDF Files","*.pdf")], defaultextension = "*.pdf")
            pdfOutputFile = open(filename, "wb")
            pdfWriter.write(pdfOutputFile)
            showinfo("Done", f"File {filename} saved successfully!")
            
            self.files = None
            self.pdfWriter = None

        elif self.files is not None and self.pdfWriter is None:
            showinfo("Error", "You must merge PDF files before save!")
        
        else:
            showinfo("Error", "No files selected! Select files to merge!")


gui = GUI()