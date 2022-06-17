

def split_space(str):
    list = str.split(" ")
    return list


#split string to list by comma and split list to list by dot
def split_comma_dot(str): 
    list = str.split(",")
    list2 = []
    for i in list:
        list2.append(i.split("."))
    list3=[]
    for i in list2:
        for j in i:
            list3.append(j)
    return list3

#find in string by list
def find_in_string_by_list(str,list):
    for i in list:
        if i in str:
            return True
    return False
#find in string by word
def find_in_string_by_word(str,word):
    if word in str:
        return True
    else:
        return False
# find index of element in list by list
def find_index_by_list(list1,list2):
    list3=[]
    for i in range (len(list1)):
        for j in range (len(list1[i])):
            if list1[i][j] in list2:
                list3.append(j)        
    return list3
def find_index_of_element_in_list(list,element):
    for i in range (len(list[-1])):
        if element == list[-1][i]:
            return i
#find list in list
def find_list(list1,list2):
    for i in list2:
        for j in i:
            if j in list1:
                return True
    return False    

#find number text in list
def get_number(list):
    num=[] 
    for i in list:
        for j in i:
            if j.isdigit():
                num.append(j)
    return num
def get_index_of_number(list):
    lst=[]
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j].isdigit():
                lst.append(j)
    return lst

#vòng lặp tách từng phần tử của chuỗi trong list
def split_element_in_string(list):
    for i in range (len(list)):
        list[i] = list[i].split(" ")
    #del space in list
    for i in range (len(list)):
        for j in range (len(list[i])-1):
            if list[i][j] == '':
                del list[i][j]
    return list


#get input data in keyboard
def get_input():   
    str = input("Nhập vào đề tài: ")
    return str
#xác định toán hạng
def get_math(all):
    if find_in_string_by_list(all[-2],div_word)==True:
        math = "/"
    elif find_in_string_by_list(all[-2],mul_word)==True:
        math = "*"
    elif find_in_string_by_list(all[-2],sub_word)==True:
        math = "-"
    elif find_in_string_by_list(all[-2],add_word)==True:
        math = "+"
    else:
        if find_in_string_by_list(all[-1],div_word)==True:
            math = "/"
        elif find_in_string_by_list(all[-1],mul_word)==True:
            math = "*"
        
        elif find_in_string_by_list(all[-1],sub_word)==True:
            math = "-"
        elif find_in_string_by_list(all[-1],add_word)==True:
            math = "+"
        
        else:
            math = "error"
    return math    
    
#get element in list form index to end
def get_element_to_end(list,idx):
    list2=[]
    for i in range(idx+1,len(list)):
        list2.append(list[i])
    return list2
#get element in list form start to index
def get_element_to_start(list,idx):
    list2=[]
    for i in range(0,idx):
        list2.append(list[i])
    return list2
#get element in list form index to end
def get_element_to_end_for_az(list,idx):
    list2=[]
    for i in range(idx+1,len(list)-1):
        list2.append(list[i])
    return list2
#get element in list form start to index
def get_element_to_start_for_az(list,idx):
    list2=[]
    for i in range(0,idx):
        list2.append(list[i+1])
    return list2
#add data in list to string
def add_data_in_list_to_string(list):
    str=""
    for i in list:
        str+=i+" " 
    return str



    
data1="Khối lớp ba có 345 học sinh, khối lớp bốn có ít hơn khối lớp ba là 24 học sinh. Hỏi khối lớp bốn có bao nhiêu học sinh ?"
split_word=["có","được","trong","cho","là","đi"]
question_word=["nhiêu","mấy"]
sub_word=["ít","ít hơn","thua","ăn","bớt","thả"]
add_word=["nhiều","nhiều hơn","thắng","tổng","thêm","cả hai"]
div_word=["chia","lấy","đều","lần"]
mul_word=["mỗi"]
data2="Trên bàn có 4 đĩa cam, mỗi đĩa có 3 quả. Hỏi trên bàn có bao nhiêu quả cam ?"
data3="Cô giáo có 40 cái bút, thưởng đều cho 4 tổ. Hỏi mỗi tổ được thưởng bao nhiêu cái bút ?"
data4="Một thanh gỗ dài 12 cm, bố em cưa bớt đi 2 cm. Hỏi thanh gỗ còn lại dài bao nhiêu cm ?"


def main1(data):

    #tách từng câu vào list
    all= split_comma_dot(data)
    all1=all
    math = get_math(all)
    print("Chuỗi sau khi đã tách ra bơi dấu '.' và ',':\n",all)
    all=split_element_in_string(all)
    all2=all
    print("Chuỗi sau khi đã tách ra từng từ: \n",all)
    #lấy số nguyên trong get_number
    lst_number = get_number(all)

    #lấy toán tử trong get_math
    

    #get index of split word to list
    idx_split=find_index_by_list(all,split_word)
    print("danh sách index của từ điệm trong chuỗi: \n",idx_split) 
    if len(idx_split)<2:
        idx_split=get_index_of_number(all)
    
    #
    print("danh sách index của từ điệm trong chuỗi: \n",idx_split) 
    
    
    #find a
    a=""
    #lấy từng phần tử từ đầu đến index của từ đệm đầu tiên, đưa vào danh sách
    a+=add_data_in_list_to_string(get_element_to_start(all[0],idx_split[0]))
    a+="= "
    #lấy từng phần tử từ index của từ đệm thứ 2 đến vị trí cuối cùng của danh sánh, rồi add vào chuỗi
    a+=add_data_in_list_to_string(get_element_to_end(all[0],idx_split[0]))   
    #find b
    b=""
    #lấy từng phần tử trong câu thứ 2 của danh sách ban đầu vì câu thứ 2 đã đủ nghĩa
    b+=add_data_in_list_to_string(all[1])
    #find câu hỏi
    #lấy vị trí của các từ để hỏi
    idx_az=find_index_by_list(all,question_word)[0]
    c=""
    c+= add_data_in_list_to_string(get_element_to_start_for_az(all[-1],idx_az-2))
    c+="? " 
    c+= add_data_in_list_to_string(get_element_to_end_for_az(all[-1],idx_az))


    
    #tính toán
    calc=""
    if math == "+":
        result = int(lst_number[0]) + int(lst_number[1])
        calc+=str(lst_number[0])+" + "+str(lst_number[1])+" = "+str(int(result))
    elif math == "-":
        result = int(lst_number[0]) - int(lst_number[1])
        calc+=str(lst_number[0])+" - "+str(lst_number[1])+" = "+str(int(result))
    elif math == "*":
        result = int(lst_number[0]) * int(lst_number[1])
        calc+=str(lst_number[0])+" * "+str(lst_number[1])+" = "+str(int(result))
    elif math == "/":
        result = int(lst_number[0]) / int(lst_number[1])
        calc+=str(lst_number[0])+" / "+str(lst_number[1])+" = "+str(int(result))
    else:
        result = "Thuật toán chưa phát triển cho dạng toán này! =))"


    #get index of element in list
    
    az=""
    az+= add_data_in_list_to_string(get_element_to_start_for_az(all[-1],idx_az-2))
    az+=str(int(result))+" " 
    az+= add_data_in_list_to_string(get_element_to_end_for_az(all[-1],idx_az))


    # print("Tóm tắt: \n-",a)
    # print("-",b)
    # print("- Câu hỏi:",c)
    # print("các số đề cho: ",lst_number)
    # print("Toán tử của bài toán: ","'",math,"'")
    # print("Tính toán: ",calc)
    # print("Câu trả lời: \n",az)
    return all1,math,all2,a,b,c,lst_number,calc,az



   


if __name__ == "__main__":
    main1(data4)
    
