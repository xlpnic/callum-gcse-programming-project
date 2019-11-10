# This import line tells the computer which python add-ons are needed for it to be able to run the program:
import tkinter as tk

#---------------------------------------------------------------

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # set the title of the main window
        self.title("Programming Project")

        # set size of the main window to 500 pixels tall and 500 pixels wide
        self.geometry("500x500")
 
        # Create a container that will contain each page that you can view in the program
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)   # make one grid cell in the container and make it cover the entire window's height
        container.grid_columnconfigure(0,weight=1) # also make that grid cell cover the entire window's width

        # Create an ARRAY that we will use to store all of the pages that we can view in the program
        self.pages = {}

        # In a FOR LOOP, go through each of our available pages and add them to our page array
        for P in (MainMenuPage, DisplayAsciiArtPage): # for each page
            page = P(container, self) # create the page
            self.pages[P] = page  # store into pages
            page.grid(row=0, column=0, sticky="nsew") # stack the pages in the container's only grid cell
        
        # Call the show page method to show the main menu page when the program first starts.
        self.show_page(MainMenuPage)
 
    # this method/function shows the page that you want to show 
    def show_page(self, name):
        # get the page with this name from our collection of pages and store it in a variable.
        pageToShow = self.pages[name]

        # show the page
        pageToShow.tkraise()
 
#---------------------------------------------------------------

class MainMenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # create the stuff we want to show on the menu page
        label = tk.Label(self, text='Main Menu')

        # When this button is clicked, tell the controller to show the 'Display ASCII Art' page.
        openTheDisplayAsciiPageButton = tk.Button(self, text='Display ASCII Art', command=lambda : controller.show_page(DisplayAsciiArtPage))

        # ley the stuff out where we want it to be ont he menu page
        label.pack(pady=10, padx=10)
        openTheDisplayAsciiPageButton.pack()

#---------------------------------------------------------------

class DisplayAsciiArtPage(tk.Frame):

    # This is the method/function that is called when you click on the 'Display ASCII Art' button.
    def loadFileAndShowAsciiArt(self):
        # Get the file path from the input text box.
        # e.g. C:\Users\nicf\Desktop\dog.txt
        filePath = self.inputTextBox.get()
        #print(filePath)

        # Use the file path to open the file.
        openFile = open(filePath, "r")

        # Read the text of the file and store it in a variable.
        fileText = openFile.read()

        # Print the text out to the terminal / command line.
        #print(fileText)

        # Wipe the display area clean
        self.asciiDisplayArea.delete(1.0, tk.END)

        # Add the text that we have read from the file into the display area.
        self.asciiDisplayArea.insert(tk.END, fileText)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create the stuff we need to show on this page
        label = tk.Label(self, text='Display ASCII Art')
        self.inputTextBox = tk.Entry(self)
        self.asciiDisplayArea = tk.Text(self, height=10, width=10)
        showAsciiButton = tk.Button(self, text="Display ASCII Art", command = self.loadFileAndShowAsciiArt)
        backToMainMenuButton = tk.Button(self, text="Return to Menu", command = lambda: controller.show_page(MainMenuPage))

        # Lay the stuff out on the page in the right places
        label.pack(pady=10, padx=10)
        self.inputTextBox.pack(side="top", fill="x", padx=5)
        self.asciiDisplayArea.pack(side="right", fill="x", expand=True, padx=5)
        showAsciiButton.pack(side="left", padx=5)
        backToMainMenuButton.pack(side="bottom", pady=5)

#---------------------------------------------------------------

# This is the stuff that tells the computer to actually run the program:
if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()

#---------------------------------------------------------------