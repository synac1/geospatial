from Tkinter import *
import csv

win=Tk()

def inception(a,b,c):
    
   
    userinput=a.lower()

    
    infile = b+'.csv'

    
    outfile = c+'.csv'
    
    try:
        file=open(infile)
        csv_f=csv.reader(file)# line 98
        inception = next(csv_f)
        print ""#inception
        return csv_f,userinput,infile,outfile
    except UnboundLocalError:""
        
    except IOError:""
         
        
 









def number(first,user):
    #print user
    
   
    list1= []
    for i in first:
        list1.append(i)
    first1=list1[0]
    list = []
    for i in first1:
        list.append([i])
    k = 0
    lench = len(list)

    for i in range(0,lench):
        
        Baselist=list[k]
        
        firstlist1= ','.join(Baselist)
        
        firstlist=firstlist1.lower()#lowercase the entire list
      
        Listoflists=firstlist.split(' ')
        #print Listoflists
        try:
            secondlist = Listoflists.index(user)# se comparan userinput con lista
            if k >=secondlist:
                bn = ','.join(list[k]).title()
                pr = bn.split(' ')
                pop = len(pr)
                if pop==1:
                    acronymum = pr[0][0:3]
                elif pop ==2:
                    acronymum = pr[0][0:3]+pr[1][0:3]
                else:
                    acronymum = pr[0][0:3]+pr[1][0:3]+pr[2][0:3]
                return k, secondlist,acronymum,list
                break
        except ValueError:""
        
        k+=1
#---------------------

aframe= Frame(win, width=400, height=200, bg="khaki")


w=Label(aframe, text="This Program creats a simplified CSV copy")
    
w.pack(side=TOP, padx=7, pady=7)

w=Label(aframe, text="What is the Category?")
w.pack( padx=7, pady=7)
e1=Entry(aframe, cursor="arrow") # first entry which is category
e1.pack( padx=7, pady=7)

w=Label(aframe, text="What is your current filename?")
w.pack( padx=7, pady=7)
e2=Entry(aframe)
e2.pack( padx=7, pady=7)

w=Label(aframe, text="Input the name for the new file!")
w.pack( padx=7, pady=7)
e3=Entry(aframe)
e3.pack( padx=7, pady=7)


w=Label(aframe, text="==> Note: Do not include '.CSV'")

#-------------

    

#----------------
def main():

    try:
        first,user,infile,outfile = inception(e1.get(),e2.get(),e3.get())
        index,index2,header,indexx2 = number(first,user)
   #Esta ok hasta aki
        Arcfile = open(infile)    
        rows = csv.reader(Arcfile)
        out = open(outfile,'wb')
        export = csv.writer(out)    
        print""
        indexx2[4]=[header]
        h=0
        for i in rows:
            
            newfile = [i[index]]
            for i in rows:
                while not(h==1):
                    export.writerow([i[0],i[1],(header)])==()
                    h =h+1
                    for i in rows:
                        export.writerow([i[0],i[1],i[index]])
        print"\nYour new",'"'+outfile+'"',"file is saved and ready!!!"  
        Arcfile.close()
        out.close()
    except TypeError:
        msgError()

     



#---------------------
        






def msgError():
    w1=Label(aframe, text="Check your inputs!")
    w1.pack(side=TOP, padx=7, pady=7)




b = Button(aframe, text="Enter", width=20, command=main)
b.pack(side=LEFT, padx=20, pady=5)
b = Button(aframe, text="Exit", width=20, command=win.destroy)
b.pack(side=LEFT, padx=20, pady=5)



aframe.pack(fill=X, expand=False)



mainloop()
