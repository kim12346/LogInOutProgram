from tkinter import *
import tkinter.messagebox as msgbox
from tkinter import ttk

dict = {}
list = []

root = Tk()
root.geometry("300x265+600+140")  # 창 크기: 500x500, 창 위치: 500+140
root.resizable(False, False)# x너비, y높이 값 변경 불가
root.title("LOGIN PAGE")  # 창 제목: LOGIN

id_label = Label(root, text="ID: ")
id_label.pack()

id_entry = Entry(root, width=30)
id_entry.pack()

pw_label = Label(root, text="PW: ")
pw_label.pack()

pw_entry = Entry(root, width=30, show="*")
pw_entry.pack()

# 회원가입창 함수
def join():
    global new_id_en, new_pw_en, confirm_btn, canc_btn, new_id_label, new_pw_label, grid, button_frame

    grid = ttk.Separator(root, orient="horizontal")
    grid.pack(fill="both")

    new_id_label = Label(root, text="New ID: ")
    new_id_label.pack()
    
    new_id_en = Entry(root, width=30)
    new_id_en.pack()
    
    new_pw_label = Label(root, text="New PW: ")
    new_pw_label.pack()
    
    new_pw_en = Entry(root, width=30, show="*")
    new_pw_en.pack()

    # Frame for buttons
    button_frame = Frame(root)
    button_frame.pack(padx=1)

    confirm_btn = Button(button_frame, width=8, height=1, text="확인", command=confirm)
    confirm_btn.pack(side=LEFT)

    canc_btn = Button(button_frame, width=8, height=1, text='취소', command=cancel)
    canc_btn.pack(side=LEFT)

# 회원가입창 취소버튼함수(회원가입창 사라짐)
def cancel():
    new_id_en.destroy() #입력 창 등 삭제
    new_pw_en.destroy()
    new_id_label.destroy()
    new_pw_label.destroy()
    confirm_btn.destroy()
    canc_btn.destroy()
    grid.destroy()
    button_frame.destroy()


# 회원가입 창에서 아이디와 비번을 입력하고 확인 버튼을 눌렀을 때의 이벤트
def confirm():
    global line
    dict_id = new_id_en.get()
    dict_pw = new_pw_en.get()
    new_id_en.delete(0, END)
    new_pw_en.delete(0, END)
    inf_file = open("IDPW.txt", "r", encoding="utf8")
    line = inf_file.readline()

    #만약 파일안에 입력한 아이디가 있으면
    if dict_id in line:
        msgbox.showinfo("알림", "이미 아이디가 존재합니다.")

    elif dict_id and dict_pw:
        new_id_en.destroy() #입력 창 등 삭제
        new_pw_en.destroy()
        new_id_label.destroy()
        new_pw_label.destroy()
        confirm_btn.destroy()
        canc_btn.destroy()
        grid.destroy()

        msgbox.showinfo("알림", "회원가입이 완료되었습니다.")
        list.append("{} {}".format(dict_id, dict_pw))
        inf_file = open("IDPW.txt", "a", encoding="utf8")
        inf_file.write("{} {}\n".format(dict_id, dict_pw))

    else:
        msgbox.showinfo("알림", "아이디 또는 패스워드를 입력하세요.")

# 로그인 확인 함수
def chk_login():
    global input_id, input_pw

    input_id = id_entry.get()
    input_pw = pw_entry.get()

    try:
        with open("IDPW.txt", "r", encoding="utf8") as chkfile:
            for line in chkfile:
                tmp = line.rstrip().split()

                d_id = tmp[0]
                d_pw = tmp[1]

                dict[d_id] = d_pw

    except FileNotFoundError:
        msgbox.showinfo("알림", "회원가입 기록이 없습니다.")
        return

    if input_id in dict and dict[input_id] == input_pw:
        print("로그인 성공!")
        infor_user()
    elif input_id not in dict:
        msgbox.showinfo("알림", "아이디가 존재하지 않습니다.")
    elif dict[input_id] != input_pw:
        msgbox.showinfo("알림", "비밀번호가 틀립니다.")
    else:
        msgbox.showinfo("알림", "로그인 실패.")

# 사용자 정보(사용자사진, 로그아웃버튼, 회원탈퇴버튼 포함)
# 사용자 사진 안나올시 -> 파일 경로 수정
def infor_user():
    global user, profile, pro_lable, grid, pro_out, logoutbtn
    grid = ttk.Separator(root, orient="horizontal")
    grid.pack(fill="both")

    profile = PhotoImage(file="파이썬/userimg.png")
    pro_lable = Label(root, image=profile)
    pro_lable.image = profile  # Keep a reference to avoid garbage collection
    pro_lable.pack()
    user = Label(root, width=20, height=1, text=f"회원 아이디: {input_id}")
    user.pack()
    logoutbtn = Button(root, text="로그아웃", command=logout)#로그아웃버튼
    logoutbtn.pack()
    pro_out = Button(root, text="회원탈퇴", command=proout) #회원탈퇴버튼
    pro_out.pack()

# 로그아웃 함수
def logout():
    pro_lable.destroy()
    user.destroy()
    logoutbtn.destroy()
    pro_out.destroy()
    grid.destroy()

    id_entry.delete(0, END)
    pw_entry.delete(0, END)

# 회원탈퇴 함수
def proout():
    global lines, chk_id, chk_pw, newlines, line

    chk_id = id_entry.get()
    chk_pw = pw_entry.get()
    id_entry.delete(0, END)
    pw_entry.delete(0, END)
    pro_lable.destroy()
    user.destroy()
    logoutbtn.destroy()
    pro_out.destroy()
    grid.destroy()

    with open("IDPW.txt", "r", encoding="utf8") as chkfile:
        lines = chkfile.readlines()

    newlines = []
    for line in lines:
        if not line.startswith(chk_id):
            newlines.append(line)
    
    with open("IDPW.txt", "w", encoding='utf8') as chkfile:
        chkfile.writelines(newlines)
    msgbox.showinfo("알림", "회원탈퇴되었습니다.")

# 메인

button_frame2 = Frame(root)
button_frame2.pack(padx=1)

log_btn = Button(button_frame2, width=8, height=1, text="로그인", command=chk_login)  # 로그인 버튼
log_btn.pack(side=LEFT)

join_btn = Button(button_frame2, width=8, height=1, text="가입하기", command=join)  # 회원가입 버튼
join_btn.pack(side=LEFT)


root.mainloop()