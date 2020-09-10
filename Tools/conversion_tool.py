import tkinter as tk


def process(*args):
    val=ent_value.get()
    #print(val)
    if check(val):
        #print(True)
        end=binCon(int(val))
        lab_results.config(text=str(val)+"-->"+str(end))
    else:
        print(False)
        lab_results.config(text="Invalid Input")

    ent_value.delete(0,tk.END)

def check(a):
    result=True
    for i in a:
        if i!="0" and i!='1':
            result=False
            break

    return result

def binCon(a):
    a=str(a)
    total=0
    place=len(a)-1
    for i in range(len(a)):
        total=total+int(a[i])*(2**(place))
        place=place-1

    return total



root=tk.Tk()

#construct widgets
lab_intruct=tk.Label(root, text="Enter Binary")
ent_value=tk.Entry(root)
lab_results=tk.Label(root, text="--")

#add widgets
lab_intruct.pack()
ent_value.pack()
lab_results.pack()

root.bind("<Return>", process)
root.mainloop()