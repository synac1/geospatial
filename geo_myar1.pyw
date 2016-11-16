# This is goingg to be a gui for Geo-Myar
from Tkinter import *
import webbrowser
import os
def OpenUrl(url):
    webbrowser.open_new(url)

##
def makeFolder(name):
    np=r'C:\Users\Public\Documents\\'+name
    newpath= str(np)
    if not os.path.exists(newpath): os.makedirs(newpath)
    
def folderGUI():
    ##window
    def makeentry():
        print e.get()
        return makeFolder(e.get())
    frameFolder = Frame(width=300, height=276, bg="KHAKI")

    w=Label(frameFolder, text="Enter name of folder")
    
    w.pack(side=LEFT, padx=7, pady=7)

    e=Entry(frameFolder)
    e.pack(side=LEFT, padx=7, pady=7)
    b=Button(frameFolder, text="OK",width=2, command=makeentry)
    b.pack(side="left", padx=7, pady=7)
    
    frameFolder.pack()
    def makePath():
        if e.get()!= "":
            np='C:\Users\Public\Documents\\'+ e.get()
            
            w1.insert(INSERT, np)
            
    
        
        
    w1=Text(frameFolder, cursor="pencil",width=40, height=3)
    w1.insert(INSERT, "")

    w1.pack(side=BOTTOM)
    b1=Button(frameFolder, text="Show path",width=10, command=makePath )
    b1.pack(side=BOTTOM, pady=5)

    

###...............
    
#folderGUI()
def aprogram():
    os.startfile("ahora1.pyw")
def arcMap():
    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\ArcGIS\\ArcMap 10.2.2.lnk")

    
##
    
master = Tk()

Label(text="Geo_MYAR").pack()

##
url = 'http://factfinder2.census.gov/faces/nav/jsf/pages/guided_search.xhtml'
##
url1='http://www.census.gov/geo/maps-data/data/tiger-line.html'
##
separator = Frame(height=2, bd=1, relief=SUNKEN)

##Label
master.configure(background="khaki")


##Separator
separator.pack(fill=X, padx=5, pady=5)
###Toolbar
toolbar = Frame(master)



b = Button(toolbar, text="Create Folder", width=20, command=folderGUI)
b.pack(side=LEFT,padx=20, pady=5)

b = Button(toolbar, text="Get Census Data", width=20,command=lambda aurl=url:OpenUrl(aurl))
b.pack(side=LEFT, padx=20, pady=5)


b = Button(toolbar, text="Get Shapefile", width=20,command=lambda aurl=url1:OpenUrl(aurl))
b.pack(side=LEFT, padx=20, pady=5)
b = Button(toolbar, text="Open csv editor", width=20, command=aprogram)
b.pack(side=LEFT, padx=20, pady=5)
b = Button(toolbar, text="Open Arcmap", width=20, command=arcMap)
b.pack(side=LEFT, padx=20, pady=5)

toolbar.pack(side=TOP, fill=X)




mainloop()

