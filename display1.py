from cProfile import label
import math
from pydoc import text
from tkinter import *
import tkinter
from math3 import *


#root1.config(bg="#ff0000")
temp=0
data=""
macth=""
all1=[]
all2=[]
lst_number=[]
calc=""
az=""
root1 = Tk()
#root1.geometry("500x500")
root1.title("Toán 1 Phép Tính")
#create a text box and pack it
label=Label(root1,text="Nhập đề toán cần tính:",font=("Arial", 15), fg="red")
label.grid(row=0,column=0,padx=10)
text_box = Text(root1, width=50, height=5, borderwidth=2, relief="solid", padx=10, pady=10)
text_box.grid(row=1, column=0, padx=10)

    



def tinh():
    data= text_box.get("1.0",END)
    all1,macth,all2,a,b,c,lst_number,calc,az=main1(data)
    if lst_number==[]:
        label0=Label(root1,text="Chuỗi nhập vào không hợp lệ!",font=("Arial", 20), fg="red")
        label0.grid(row=3,column=0,padx=10)
        return
    label0=Label(root1,text="---------------------------------")
    label0.grid(row=3,column=0,padx=10)
    label1 = Label(root1, text="Tóm Tắt:", font=("Arial", 15), fg="red")
    label1.grid(row=4, column=0, padx=10)
    label2 = Label(root1, text="-"+a, font=("Arial", 12))
    label2.grid(row=5, column=0, padx=10)
    label3 = Label(root1, text="-"+b, font=("Arial", 12))
    label3.grid(row=6, column=0, padx=10)
    label4 = Label(root1, text="- Câu hỏi:"+c, font=("Arial", 12))
    label4.grid(row=7, column=0, padx=10)
    label5= Label(root1,text="---------------------------------")
    label5.grid(row=8,column=0,padx=10)
    label6 = Label(root1, text="Giải:", font=("Arial", 15), fg="red")
    label6.grid(row=9, column=0, padx=10)
    label7 = Label(root1, text=calc, font=("Arial", 12))
    label7.grid(row=10, column=0, padx=10)
    label8 = Label(root1, text="Vậy "+az,font=("Arial", 12))
    label8.grid(row=11, column=0, padx=10)
    label9= Label(root1,text="---------------------------------")
    label9.grid(row=12,column=0,padx=10)
    button1 = Button(root1, text="Hiển thị kết quả từng bước làm", command=showdetail )

    button1.grid(row=13, column=0, padx=10)

    def hidetinh():
        label0.grid_forget()
        label1.grid_forget()
        label2.grid_forget()
        label3.grid_forget()
        label4.grid_forget()
        label5.grid_forget()
        label6.grid_forget()
        label7.grid_forget()
        label8.grid_forget()
        label9.grid_forget()
        button1.grid_forget()
        button = Button(root1, text="Tính Toán", command=tinh )
        button.grid(row=2, column=0, padx=10)
    
    button = Button(root1, text="Làm mới", command=hidetinh )
    button.grid(row=2, column=0, padx=10)


    return data,macth,calc,az,all1,all2,lst_number




button = Button(root1, text="Tính toán", command=tinh )
button.grid(row=2, column=0, padx=10)

def showdetail():
    data,macth,calc,az,all1,all2,lst_number=tinh()
    for i in range (10):
        lb=Label(root1,text="|")
        lb.grid(row=i+1,column=1,padx=10)
    lb0=Label(root1,text="Các bước làm:",font=("Arial", 15), fg="red")
    lb0.grid(row=1,column=2,padx=10)
    lb1=Label(root1,text="Bước 1:Tách chuỗi thành list bởi dấu phẩy và dấu chấm:",font=("Arial", 15), fg="red")
    lb1.grid(row=2,column=2,padx=10)    #tach chuoi thanh list
    lb2=Label(root1,text=all1,font=("Arial", 12))
    lb2.grid(row=3,column=2,padx=10)
    lb3=Label(root1,text="Bước 2:Tách chuỗi thành list bởi dấu cách:",font=("Arial", 15), fg="red")
    lb3.grid(row=4,column=2,padx=10)
    lb4=Label(root1,text=all2,font=("Arial", 12))
    lb4.grid(row=5,column=2,padx=10)
    lb5=Label(root1,text="Bước 3:Lấy các số và thêm vào list:",font=("Arial", 15), fg="red")
    lb5.grid(row=6,column=2,padx=10)
    lb6=Label(root1,text=("Các số đề cho: ",lst_number),font=("Arial", 12))
    lb6.grid(row=7,column=2,padx=10)
    lb7=Label(root1,text="Bước 4:Xác định toán tử:",font=("Arial", 15), fg="red")
    lb7.grid(row=8,column=2,padx=10)
    lb8=Label(root1,text="Toán tử của bài toán: "+"'"+macth+"'",font=("Arial", 12))
    lb8.grid(row=9,column=2,padx=10)
    lb9=Label(root1,text="Bước 5:Tính toán:",font=("Arial", 15), fg="red")
    lb9.grid(row=10,column=2,padx=10)
    lb10=Label(root1,text=calc,font=("Arial", 12))
    lb10.grid(row=11,column=2,padx=10)
    def HideResult():
        lb0.grid_forget()
        lb1.grid_forget()
        lb2.grid_forget()
        lb3.grid_forget()
        lb4.grid_forget()
        lb5.grid_forget()
        lb6.grid_forget()
        lb7.grid_forget()
        lb8.grid_forget()
        lb9.grid_forget()
        lb10.grid_forget()
        btn.grid_forget()
    btn=Button(root1,text="Ẩn chi tiết",command=HideResult)
    btn.grid(row=12,column=2,padx=10)

        



#create a button to click
#create a label to display the result

#get data form keyboard by text entry



root1.mainloop()