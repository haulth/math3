# từng phần tử trong list được chia thành 2 phần tử trong list
def get_element_to_end(list,idx):
    list2=[]
    for i in range(idx+1,len(list)):
        list2.append(list[i])
    return list2
#get element in list form start to index
def get_element_to_start(list,idx):
    list2=[]
    for i in range(0,idx-1):
        list2.append(list[i])
    return list2
#get element in list form index to end
def get_element_to_end_for_az1(list,idx):
    list2=[]
    for i in range(idx+1,len(list)-1):
        list2.append(list[i])
    return list2
def get_element_to_start_for_az1(list,idx):
    list2=[]
    for i in range(0,idx-1):
        list2.append(list[i+1])
    return list2
def get_element_to_end_for_az2(list,idx):
    list2=[]
    for i in range(idx+1,len(list)-1):
        list2.append(list[i])
    return list2
#get element in list form start to index
def get_element_to_start_for_az2(list,idx):
    list2=[]
    for i in range(0,idx-2):
        list2.append(list[i+1])
    return list2
def find_index_of_element_in_list(list,element):
    for i in range (len(list)):
        if element == list[i]:
            return i
def find_index_by_list(list1,list2):
    for i in range (len(list1)):
        if list1[i] in list2:
            return i
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
# get index of element in string and replace it with space
def get_index_of_element_in_string(str):
    idx= str.index("/")
    str = str.replace(str[idx]," ")
    return str
#find in string by list
def find_in_string_by_list(str,list):
    for i in list:
            if i in str:
                return True
    return False
def split_element_in_string(list):    
    for i in range (len(list)):
        list[i] = list[i].split(" ")
    #del space in list
    for i in range (len(list)):
        for j in range (len(list[i])-1):
            if list[i][j] == '':
                del list[i][j]

    return list

def find_exist_and_remove(str):
    f=str
    lst_f=f.split(" ")
    for i in range (len(lst_f)):
        for j in range (len(lst_f[i+1:-1])):
            if lst_f[i] == lst_f[j]:
                del lst_f[j]
    s=add_data_in_list_to_string(lst_f)
    return s
               
def add_data_in_list_to_string(list):
    str=""
    for i in list:
        str+=i+" " 
    return str


def get_number(list):
    num=[] 
    for i in list:
        for j in i:
            if j.isdigit():
                num.append(j)
    return num
def find_flask(str):
    if str.find("/") != -1:
        d = get_index_of_element_in_string(str)
        print(d)
    else:
        d=str
    return d
data1="Một cửa hàng có 1242 cái áo, cửa hàng đã bán 1/6 số áo. Hỏi cửa hàng đó còn lại bao nhiêu cái áo ?"
data2="Em có 5 nhãn vở, bạn Trang có nhiều hơn em 3 cái. Hỏi cả hai bạn có bao nhiêu cái nhãn vở ?"
data3="Lớp 3A trồng được 42 cây, lớp 3B trồng được gấp 4 lần số cây của lớp 3A. hỏi cả hai lớp trồng được bao nhiêu cây ?"
data4="Can thứ nhất có 18 lít dầu. Số dầu ở can thứ hai gấp 3 lần số dầu ở can thứ nhất. hỏi can thứ nhất ít hơn can thứ hai bao nhiêu lít dầu ?"
sub_word1=["ít hơn","rời đi","giảm"]
sub_word2=["mỗi","còn lại","ít hơn"]
add_word1=["cả hai","nhiều hơn","tổng"]
div_word1=["lần"]
mul_word1=["gấp","mỗi"]
buffer_word=["hơn","bằng","ít","được","gấp","1","có","chứa"]
question_word=["nhiêu", "mấy"]
math=[]

def main2(data):
    #del / in string
    d=find_flask(data)
    #split string to list by comma and split list to list by dot
    list1 = split_comma_dot(d)
    list_cd=list1.copy()
    print(list1)
    #get match 
    tomtat=split_comma_dot(data)
    listTT=split_element_in_string(tomtat)

    #split string to list by space
    list2= split_element_in_string(list1)
    print(list2)
    #get number in list
    lst_num=get_number(list2)
    print(lst_num)
    #get math
    #1
    if len(lst_num)>2 and lst_num[1]=='1':
        math.append("/")
        lst_num.remove(lst_num[1])
    else:
        if find_in_string_by_list(list_cd[1],mul_word1)==True:
            math.append("*")      
        elif find_in_string_by_list(list_cd[1],div_word1)==True:
            math.append("/")
        elif find_in_string_by_list(list_cd[1],sub_word1)==True:
            math.append("-")
        elif find_in_string_by_list(list_cd[1],add_word1)==True:
            math.append("+")        
        else:
            math.append("error")
    print("toán tử phép tính thứ nhất",math)
    #2
    print(list_cd[2])
    if find_in_string_by_list(list_cd[2],sub_word2)==True:
            math.append("-")
    elif find_in_string_by_list(list_cd[2],add_word1)==True:
            math.append("+")
    else:
        math.append("error")
    print("toán tử phép tính thứ một và hai",math)
    lst_result=[]
    calc1=""
    #phép tính thứ nhất
    if math[0]=="/":
        lst_result.append(abs(int(int(lst_num[0])/int(lst_num[1]))))
        calc1+=str(lst_num[0])+" / "+str(lst_num[1])+" = "+str(lst_result[0])
    elif math[0]=="*":
        lst_result.append(abs(int(int(lst_num[0])*int(lst_num[1]))))
        calc1+=str(lst_num[0])+" * "+str(lst_num[1])+" = "+str(lst_result[0])
    elif math[0]=="-":
        lst_result.append(abs(int(int(lst_num[0])-int(lst_num[1]))))
        calc1+=str(lst_num[0])+" - "+str(lst_num[1])+" = "+str(lst_result[0])
    elif math[0]=="+":
        lst_result.append(abs(int(int(lst_num[0])+int(lst_num[1]))))
        calc1+=str(lst_num[0])+" + "+str(lst_num[1])+" = "+str(lst_result[0])
    else:
        lst_result.append("error")
        calc1+="error"
    print("phép tính thứ nhất",lst_result)
    #phép tính thứ 2
    calc2=""
    if math[1]=="-":
        if int(lst_num[0])<int(lst_result[0]):
            lst_result.append(abs(int(lst_result[-1])-int(lst_num[0])))
            calc2+=str(lst_result[0])+" - "+str(lst_num[0])+" = "+str(lst_result[-1])
        else:
            lst_result.append(abs(int(lst_num[0])-int(lst_result[-1])))
            calc2+=str(lst_num[0])+" - "+str(lst_result[0])+" = "+str(lst_result[-1])
    elif math[1]=="+":
        lst_result.append(abs(int(lst_num[0])+int(lst_result[-1])))
        calc2+=str(lst_num[0])+" + "+str(lst_result[0])+" = "+str(lst_result[-1])
    else:
        lst_result.append("error")
        calc2+="error"
    print("phép tính thứ 2",lst_result)



    #find a
    a=""
    a+=add_data_in_list_to_string( get_element_to_start(list2[0],find_index_of_element_in_list(list2[0],lst_num[0])))
    a+="= "+lst_num[0] +" "
    a+=add_data_in_list_to_string(get_element_to_end(list2[0],find_index_of_element_in_list(list2[0],lst_num[0])))
    #find b
    b=""
    b+= add_data_in_list_to_string(listTT[1])
    #find câu hỏi
    c=""
    try:       
        c+=add_data_in_list_to_string(get_element_to_start_for_az2(list2[2],find_index_by_list(list2[2],question_word)))
        c+="? "
        c+=add_data_in_list_to_string(get_element_to_end_for_az2(list2[2],find_index_by_list(list2[2],question_word)))
    except:
        c+="chưa thể tóm tắt câu hỏi cho bài toán này! =))"
    #find lời giải thứ nhất
    az1=""
    try:
        az1+=add_data_in_list_to_string(get_element_to_end_for_az2(list2[2],find_index_by_list(list2[2],question_word)))
        az1+=add_data_in_list_to_string( get_element_to_start_for_az1(list2[1],find_index_by_list(list2[1],buffer_word)))
        az1=find_exist_and_remove(az1)
        az1+=": "
    except:
        az1+="chưa thể tìm lời giải cho bài toán này! =))"
    #find lời giải thứ 2
    az2=""
    try:
        az2+=add_data_in_list_to_string(get_element_to_start_for_az2(list2[2],find_index_by_list(list2[2],question_word)))
        az2+=":"
    except:
        az2+="chưa thể tìm lời giải cho bài toán này! =))"   
    #find kết luận
    az3=""
    try:
        az3+=add_data_in_list_to_string(get_element_to_start_for_az2(list2[2],find_index_by_list(list2[2],question_word)))
        az3+=" "+str(lst_result[-1])+" "
        az3+=add_data_in_list_to_string(get_element_to_end_for_az2(list2[2],find_index_by_list(list2[2],question_word)))
    except:
        az3+="chưa thể tìm lời giải cho bài toán này! =))"




    return calc1,calc2,a,b,c,az1,az2,az3

if __name__ == "__main__":
    main2(data3)