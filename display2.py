from cProfile import label
import math
from pydoc import text
from tkinter import *
import tkinter
from math3_2 import *

root2 = Tk()
#root2.geometry("500x500")
root2.title("Toán 2 Phép Tính")
#root2.config(bg="#ff0000")
data=""
macth=""
all1=[]
all2=[]
lst_number=[]
calc=""
az=""

#create a text box and pack it
label=Label(root2,text="Nhập đề toán 2 phép tính cần tính:",font=("Arial", 15), fg="red")
label.grid(row=0,column=0,padx=10)
text_box = Text(root2, width=50, height=5, borderwidth=2, relief="solid", padx=10, pady=10)
text_box.grid(row=1, column=0, padx=10)

    



def tinh():
    data= text_box.get("1.0",END)
    calc1,calc2,a,b,c,az1,az2,az3=main2(data)
   
    label0=Label(root2,text="---------------------------------")
    label0.grid(row=3,column=0,padx=10)
    label1 = Label(root2, text="Tóm Tắt:", font=("Arial", 15), fg="red")
    label1.grid(row=4, column=0, padx=10)
    label2 = Label(root2, text="-"+a, font=("Arial", 12))
    label2.grid(row=5, column=0, padx=10)
    label3 = Label(root2, text="-"+b, font=("Arial", 12))
    label3.grid(row=6, column=0, padx=10)
    label4 = Label(root2, text="- Câu hỏi:"+c, font=("Arial", 12))
    label4.grid(row=7, column=0, padx=10)
    label5= Label(root2,text="---------------------------------")
    label5.grid(row=8,column=0,padx=10)
    label6 = Label(root2, text="Giải:", font=("Arial", 15), fg="red")
    label6.grid(row=9, column=0, padx=10)
    label7 = Label(root2, text=az1, font=("Arial", 12))
    label7.grid(row=10, column=0, padx=10)
    label8 = Label(root2, text=calc1, font=("Arial", 12))
    label8.grid(row=11, column=0, padx=10)
    label9 = Label(root2, text=az2, font=("Arial", 12))
    label9.grid(row=12, column=0, padx=10)
    label10 = Label(root2, text=calc2, font=("Arial", 12))
    label10.grid(row=13, column=0, padx=10)
    label11 = Label(root2, text="Vậy "+az3,font=("Arial", 12))
    label11.grid(row=14, column=0, padx=10)
    label12= Label(root2,text="---------------------------------")
    label12.grid(row=15,column=0,padx=10)
    
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
        label10.grid_forget()
        label11.grid_forget()
        label12.grid_forget()

        button = Button(root2, text="Tính Toán", command=tinh )
        button.grid(row=2, column=0, padx=10)
    
    button = Button(root2, text="Làm mới", command=hidetinh )
    button.grid(row=2, column=0, padx=10)

button = Button(root2, text="Tính toán", command=tinh )
button.grid(row=2, column=0, padx=10)

# def showdetail():
#     data,macth,calc,az,all1,all2,lst_number=tinh()
#     for i in range (10):
#         lb=Label(root2,text="|")
#         lb.grid(row=i+1,column=1,padx=10)
#     lb0=Label(root2,text="Các bước làm:",font=("Arial", 15), fg="red")
#     lb0.grid(row=1,column=2,padx=10)
#     lb1=Label(root2,text="Bước 1:Tách chuỗi thành list bởi dấu phẩy và dấu chấm:",font=("Arial", 15), fg="red")
#     lb1.grid(row=2,column=2,padx=10)    #tach chuoi thanh list
#     lb2=Label(root2,text=all1,font=("Arial", 12))
#     lb2.grid(row=3,column=2,padx=10)
#     lb3=Label(root2,text="Bước 2:Tách chuỗi thành list bởi dấu cách:",font=("Arial", 15), fg="red")
#     lb3.grid(row=4,column=2,padx=10)
#     lb4=Label(root2,text=all2,font=("Arial", 12))
#     lb4.grid(row=5,column=2,padx=10)
#     lb5=Label(root2,text="Bước 3:Lấy các số và thêm vào list:",font=("Arial", 15), fg="red")
#     lb5.grid(row=6,column=2,padx=10)
#     lb6=Label(root2,text=("Các số đề cho: ",lst_number),font=("Arial", 12))
#     lb6.grid(row=7,column=2,padx=10)
#     lb7=Label(root2,text="Bước 4:Xác định toán tử:",font=("Arial", 15), fg="red")
#     lb7.grid(row=8,column=2,padx=10)
#     lb8=Label(root2,text="Toán tử của bài toán: "+"'"+macth+"'",font=("Arial", 12))
#     lb8.grid(row=9,column=2,padx=10)
#     lb9=Label(root2,text="Bước 5:Tính toán:",font=("Arial", 15), fg="red")
#     lb9.grid(row=10,column=2,padx=10)
#     lb10=Label(root2,text=calc,font=("Arial", 12))
#     lb10.grid(row=11,column=2,padx=10)
#     def HideResult():
#         lb0.grid_forget()
#         lb1.grid_forget()
#         lb2.grid_forget()
#         lb3.grid_forget()
#         lb4.grid_forget()
#         lb5.grid_forget()
#         lb6.grid_forget()
#         lb7.grid_forget()
#         lb8.grid_forget()
#         lb9.grid_forget()
#         lb10.grid_forget()
#         btn.grid_forget()
#     btn=Button(root2,text="Ẩn chi tiết",command=HideResult)
#     btn.grid(row=12,column=2,padx=10)

        



#create a button to click
#create a label to display the result

#get data form keyboard by text entry



root2.mainloop()