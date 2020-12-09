from tkinter import *
from firebase import firebase
from PIL import Image, ImageTk
fbconn = firebase.FirebaseApplication('https://samplefbtest-266bd.firebaseio.com/',None)

global crtans
crtans = 0
class FirstRound:
    print("Done")
        
    def __init__(self, master):


        global w,h,ws,hs,x,y

        w = 1000
        h = 650
        ws = root.winfo_screenwidth() # width of the screen
        hs = root.winfo_screenheight() # height of the screen
        x = (ws/4) - (w/4)
        y = (hs/4) - (h/4)

        global answer1,answer2,anslist
        anslist = []
        answer1 = '2'
        answer2 = '1'
        answer3 = '2'
        answer4 = '2'
        answer5 = '1'
        answer6 = '2'
        answer7 = '3'
        answer8 = '4'
        answer9 = '3'
        answer10 = '3'
        answer11 = '1'
        answer12 = '2'
        answer13 = '3'
        answer14 = '3'
        answer15 = '3'
        answer16 = '4'
        answer17 = '2'
        answer18 = '4'
        answer19 = '3'
        answer20 = '3'
        
        self.master=master
        master.title('First Round')

        self.frame = Frame(master,width=1000, height=600, bg='black')
        self.frame.pack()

        self.heading = Label(self.frame, text="Kalasalingam Institute of Technology", font=('arial 30 bold'), fg='black', bg='lightgreen')
        self.heading.place(x=180, y=20)

        self.title = Label(self.frame, text="Cybertron'20", font=('arial 30 bold'), fg='black', bg='lightgreen')
        self.title.place(x=350, y=100)

        self.name = Label(self.frame, text="Name :", font=('arial 13'), fg='black', bg='lightgreen')
        self.name.place(x=300, y=200)

        self.nameentry = Entry(self.frame,width=50)
        self.nameentry.place(x=400,y=200)

        self.clg = Label(self.frame, text="College :", font=('arial 13'), fg='black', bg='lightgreen')
        self.clg.place(x=300, y=250)

        self.clgentry = Entry(self.frame,width=50)
        self.clgentry.place(x=400,y=250)

        self.mail = Label(self.frame, text="Mail :", font=('arial 13'), fg='black', bg='lightgreen')
        self.mail.place(x=300, y=300)

        self.mailentry = Entry(self.frame,width=50)
        self.mailentry.place(x=400,y=300)

        self.start = Button(self.frame,width=10,text="Start",command = self.start)
        self.start.place(x=380,y=350)

        self.secondwin = Toplevel()

        self.secondwin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.frame1 = Frame(self.secondwin,width=1000, height=600, bg='black')
        self.frame1.pack()

        self.event = Label(self.secondwin, text="Capture The Flag", font=('arial 30 bold'), fg='black', bg='lightgreen')
        self.event.place(x=300, y=20)

        self.q1 = Image.open("images/q1-small.png")
        self.render = ImageTk.PhotoImage(self.q1)
        self.img = Label(self.secondwin, image=self.render)
        self.img.image = self.render
        self.img.place(x=50, y=100)
        
        def q1():
            global ans,crtans
            ans = str(var.get())
            if ans == answer1:
                crtans = crtans+1


        #Question 1
        var = IntVar()
        self.R1 = Radiobutton(self.secondwin, text="A) 6, 10, 8 ", variable=var, value=1,bg='lightgreen',
                  command=q1)
        self.R1.place(x=500,y=100)
        self.R2 = Radiobutton(self.secondwin, text="B) 4, 8, 4", variable=var, value=2,bg='lightgreen',
                  command=q1)
        self.R2.place(x=500,y=150)
        self.R3 = Radiobutton(self.secondwin, text="C) 2, 4, 4", variable=var, value=3,bg='lightgreen',
                  command=q1)
        self.R3.place(x=500,y=200)
        self.R4 = Radiobutton(self.secondwin, text="D) 2, 8, 4", variable=var, value=4,bg='lightgreen',
                  command=q1)
        self.R4.place(x=500,y=250)

        self.q2 = Image.open("images/q2-small.png")
        self.render = ImageTk.PhotoImage(self.q2)
        self.img = Label(self.secondwin, image=self.render)
        self.img.image = self.render
        self.img.place(x=50, y=350)

        '''self.q2 = Label(self.secondwin, text="2)How to declare a variable?", font=('arial 15'), fg='black',
                        bg='lightgreen')
        self.q2.place(x=20, y=300)'''

        def q2():
            global ans1,crtans
            ans1 = str(var1.get())
            print(ans1)
            if ans1 == answer2:
                crtans = crtans+1


        #Question 2
        var1 = IntVar()

        self.R5 = Radiobutton(self.secondwin, text="A) 101010", variable=var1, value=1,bg='lightgreen',
                  command=q2)
        self.R5.place(x=500,y=350)
        self.R6 = Radiobutton(self.secondwin, text="B) 0xxa5f1010", variable=var1, value=2,bg='lightgreen',
                  command=q2)
        self.R6.place(x=500,y=400)
        self.R7 = Radiobutton(self.secondwin, text="C) Run time error", variable=var1, value=3,bg='lightgreen',
                  command=q2)
        self.R7.place(x=500,y=450)

        self.R8 = Radiobutton(self.secondwin, text="D) No Output", variable=var1, value=4,bg='lightgreen',
                  command=q2)
        self.R8.place(x=500,y=500)

        self.secondnext = Button(self.secondwin,width=10,text="NEXT",command = self.secondnext)
        self.secondnext.place(x=800,y=550)

        self.secondback = Button(self.secondwin,width=10,text="BACK",command = self.secondback)
        self.secondback.place(x=700,y=550)

        self.secondwin.withdraw()

        self.thirdwin = Toplevel()

        self.thirdwin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.frame2 = Frame(self.thirdwin,width=1000, height=600, bg='black')
        self.frame2.pack()


        self.q3 = Image.open("images/q3-small.png")
        self.render = ImageTk.PhotoImage(self.q3)
        self.img = Label(self.thirdwin, image=self.render)
        self.img.image = self.render
        self.img.place(x=50, y=100)

        
        
        def q3():
            global ans2,crtans
            ans2 = str(var2.get())
            if ans2 == answer3:
                crtans = crtans+1
        #Question 3
        var2 = IntVar()
        self.R9 = Radiobutton(self.thirdwin, text="A) 0", variable=var2, value=1,bg='lightgreen',
                  command=q3)
        self.R9.place(x=500,y=100)
        self.R10 = Radiobutton(self.thirdwin, text="B) Error because of incorrect line-1 only.", variable=var2, value=2,bg='lightgreen',
                  command=q3)
        self.R10.place(x=500,y=150)
        self.R11 = Radiobutton(self.thirdwin, text="C) Error because of incorrect line-1 and line-2.", variable=var2, value=3,bg='lightgreen',
                  command=q3)
        self.R11.place(x=500,y=200)
        self.R12 = Radiobutton(self.thirdwin, text="D) Error because of incorrect line-2 only.", variable=var2, value=4,bg='lightgreen',
                  command=q3)
        self.R12.place(x=500,y=250)

        self.q4 = Image.open("images/q4-small.png")
        self.render = ImageTk.PhotoImage(self.q4)
        self.img = Label(self.thirdwin, image=self.render)
        self.img.image = self.render
        self.img.place(x=50, y=350)

        '''self.q2 = Label(self.secondwin, text="2)How to declare a variable?", font=('arial 15'), fg='black',
                        bg='lightgreen')
        self.q2.place(x=20, y=300)'''

        def q4():
            global ans3,crtans
            ans3 = str(var3.get())
            print(ans3)
            if ans3 == answer4:
                crtans = crtans+1


        #Question 4
        var3 = IntVar()

        self.R13 = Radiobutton(self.thirdwin, text="A) 0", variable=var3, value=1,bg='lightgreen',
                  command=q4)
        self.R13.place(x=500,y=350)
        self.R14 = Radiobutton(self.thirdwin, text="B) Runtime error", variable=var3, value=2,bg='lightgreen',
                  command=q4)
        self.R14.place(x=500,y=400)
        self.R15 = Radiobutton(self.thirdwin, text="C) 5", variable=var3, value=3,bg='lightgreen',
                  command=q4)
        self.R15.place(x=500,y=450)

        self.R16 = Radiobutton(self.thirdwin, text="D) compilation error", variable=var3, value=4,bg='lightgreen',
                  command=q4)
        self.R16.place(x=500,y=500)

        

        self.thirdnext = Button(self.thirdwin,width=10,text="NEXT",command = self.thirdnext)
        self.thirdnext.place(x=800,y=550)

        self.thirdback = Button(self.thirdwin,width=10,text="BACK",command = self.thirdback)
        self.thirdback.place(x=700,y=550)

        self.thirdwin.withdraw()

        self.forthwin = Toplevel()

        self.forthwin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.frame3 = Frame(self.forthwin,width=1000, height=600, bg='black')
        self.frame3.pack()


        self.q5 = Image.open("images/q5-small.png")
        self.render = ImageTk.PhotoImage(self.q5)
        self.img = Label(self.forthwin, image=self.render)
        self.img.image = self.render
        self.img.place(x=50, y=100)

        def q5():
            global ans4,crtans
            ans4 = str(var4.get())
            print(ans4)
            if ans4 == answer5:
                crtans = crtans+1

        #Question 5
        var4 = IntVar()

        self.R17 = Radiobutton(self.forthwin, text="A) address address value", variable=var4, value=1,bg='lightgreen',
                  command=q5)
        self.R17.place(x=500,y=100)
        self.R18 = Radiobutton(self.forthwin, text="B) address value value", variable=var4, value=2,bg='lightgreen',
                  command=q5)
        self.R18.place(x=500,y=150)
        self.R19 = Radiobutton(self.forthwin, text="C) address address address", variable=var4, value=3,bg='lightgreen',
                  command=q5)
        self.R19.place(x=500,y=200)

        self.R20 = Radiobutton(self.forthwin, text="D) compilation error", variable=var4, value=4,bg='lightgreen',
                  command=q5)
        self.R20.place(x=500,y=250)

        self.q6 = Image.open("images/q6-small.png")
        self.render = ImageTk.PhotoImage(self.q6)
        self.img = Label(self.forthwin, image=self.render)
        self.img.image = self.render
        self.img.place(x=50, y=350)

        def q6():
            global ans5,crtans
            ans5 = str(var5.get())
            print(ans5)
            if ans5 == answer6:
                crtans = crtans+1


        #Question 6
        var5 = IntVar()

        self.R21 = Radiobutton(self.forthwin, text="A) No output", variable=var5, value=1,bg='lightgreen',
                  command=q6)
        self.R21.place(x=500,y=350)
        self.R22 = Radiobutton(self.forthwin, text="B) compile time error", variable=var5, value=2,bg='lightgreen',
                  command=q6)
        self.R22.place(x=500,y=400)
        self.R23 = Radiobutton(self.forthwin, text="C) 1", variable=var5, value=3,bg='lightgreen',
                  command=q6)
        self.R23.place(x=500,y=450)

        self.R24 = Radiobutton(self.forthwin, text="D) 4", variable=var5, value=4,bg='lightgreen',
                  command=q6)
        self.R24.place(x=500,y=500)

        self.forthnext = Button(self.forthwin,width=10,text="NEXT",command = self.forthnext)
        self.forthnext.place(x=800,y=550)

        self.forthback = Button(self.forthwin,width=10,text="BACK",command = self.forthback)
        self.forthback.place(x=700,y=550)

        self.forthwin.withdraw()

        self.fifthwin = Toplevel()

        self.fifthwin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.frame3 = Frame(self.fifthwin,width=1000, height=600, bg='black')
        self.frame3.pack()

        self.q7 = Image.open("images/q7-small.png")
        self.render = ImageTk.PhotoImage(self.q7)
        self.img = Label(self.fifthwin, image=self.render)
        self.img.image = self.render
        self.img.place(x=50, y=100)

        def q7():
            global ans6,crtans
            ans6 = str(var6.get())
            print(ans6)
            if ans6 == answer7:
                crtans = crtans+1

        #Question 7
        var6 = IntVar()

        self.R25 = Radiobutton(self.fifthwin, text="A) The control won’t fall into the for loop", variable=var6, value=1,bg='lightgreen',
                  command=q7)
        self.R25.place(x=500,y=100)
        self.R26 = Radiobutton(self.fifthwin, text="B) Numbers will be displayed until the signed limit of short and throw a run time error", variable=var6, value=2,bg='lightgreen',
                  command=q7)
        self.R26.place(x=500,y=150)
        self.R27 = Radiobutton(self.fifthwin, text="C) ) Numbers will be displayed until the signed limit of short and program will \nsuccessfully terminate", variable=var6, value=3,bg='lightgreen',
                  command=q7)
        self.R27.place(x=500,y=200)

        self.R28 = Radiobutton(self.fifthwin, text="D) This program will get into an infinite loop and keep printing numbers with no errors", variable=var6, value=4,bg='lightgreen',
                  command=q7)
        self.R28.place(x=500,y=250)

        self.q8 = Image.open("images/q8-small.png")
        self.render = ImageTk.PhotoImage(self.q8)
        self.img = Label(self.fifthwin, image=self.render)
        self.img.image = self.render
        self.img.place(x=50, y=350)

        def q8():
            global ans7,crtans
            ans7 = str(var7.get())
            print(ans7)
            if ans7 == answer8:
                crtans = crtans+1


        #Question 8
        var7 = IntVar()

        self.R21 = Radiobutton(self.fifthwin, text="A) 0.000000 1.000000 2.000000", variable=var7, value=1,bg='lightgreen',
                  command=q8)
        self.R21.place(x=500,y=350)
        self.R22 = Radiobutton(self.fifthwin, text="B) 2.000000", variable=var7, value=2,bg='lightgreen',
                  command=q8)
        self.R22.place(x=500,y=400)
        self.R23 = Radiobutton(self.fifthwin, text="C) Compile time error", variable=var7, value=3,bg='lightgreen',
                  command=q8)
        self.R23.place(x=500,y=450)

        self.R24 = Radiobutton(self.fifthwin, text="D) 3.000000", variable=var7, value=4,bg='lightgreen',
                  command=q8)
        self.R24.place(x=500,y=500)

        self.fifthnext = Button(self.fifthwin,width=10,text="NEXT",command = self.fifthnext)
        self.fifthnext.place(x=800,y=550)

        self.fifthback = Button(self.fifthwin,width=10,text="BACK",command = self.fifthback)
        self.fifthback.place(x=700,y=550)

        self.fifthwin.withdraw()

        self.sixthwin = Toplevel()

        self.sixthwin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.frame4 = Frame(self.sixthwin,width=1000, height=600, bg='black')
        self.frame4.pack()

        self.q9 = Image.open("images/q9-small.png")
        self.render = ImageTk.PhotoImage(self.q9)
        self.img = Label(self.sixthwin, image=self.render)
        self.img.image = self.render
        self.img.place(x=50, y=100)

        def q9():
            global ans8,crtans
            ans8 = str(var8.get())
            print(ans8)
            if ans8 == answer9:
                crtans = crtans+1

        #Question 9
        var8 = IntVar()

        self.R29 = Radiobutton(self.sixthwin, text="A) 5", variable=var8, value=1,bg='lightgreen',
                  command=q9)
        self.R29.place(x=500,y=100)
        self.R30 = Radiobutton(self.sixthwin, text="B) 0", variable=var8, value=2,bg='lightgreen',
                  command=q9)
        self.R30.place(x=500,y=150)
        self.R31 = Radiobutton(self.sixthwin, text="C) Syntax Error", variable=var8, value=3,bg='lightgreen',
                  command=q9)
        self.R31.place(x=500,y=200)

        self.R32 = Radiobutton(self.sixthwin, text="D) 05", variable=var8, value=4,bg='lightgreen',
                  command=q9)
        self.R32.place(x=500,y=250)

        self.q10 = Image.open("images/q10-small.png")
        self.render = ImageTk.PhotoImage(self.q10)
        self.img = Label(self.sixthwin, image=self.render)
        self.img.image = self.render
        self.img.place(x=50, y=350)

        def q10():
            global ans9,crtans
            ans9 = str(var9.get())
            print(ans9)
            if ans9 == answer10:
                crtans = crtans+1


        #Question 10
        var9 = IntVar()

        self.R33 = Radiobutton(self.sixthwin, text="A) 11 33", variable=var9, value=1,bg='lightgreen',
                  command=q10)
        self.R33.place(x=500,y=350)
        self.R34 = Radiobutton(self.sixthwin, text="B) Error", variable=var9, value=2,bg='lightgreen',
                  command=q10)
        self.R34.place(x=500,y=400)
        self.R35 = Radiobutton(self.sixthwin, text="C) exception", variable=var9, value=3,bg='lightgreen',
                  command=q10)
        self.R35.place(x=500,y=450)

        self.R36 = Radiobutton(self.sixthwin, text="D) 11 -33", variable=var9, value=4,bg='lightgreen',
                  command=q10)
        self.R36.place(x=500,y=500)

        self.fifthnext = Button(self.sixthwin,width=10,text="NEXT",command = self.sixthnext)
        self.fifthnext.place(x=800,y=550)

        self.sixthback = Button(self.sixthwin,width=10,text="BACK",command = self.sixthback)
        self.sixthback.place(x=700,y=550)
        
        self.sixthwin.withdraw()


        self.seventhwin = Toplevel()

        self.seventhwin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.frame5 = Frame(self.seventhwin,width=1000, height=600, bg='black')
        self.frame5.pack()

        self.q11 = Image.open("images/q11-small.png")
        self.render = ImageTk.PhotoImage(self.q11)
        self.img = Label(self.seventhwin, image=self.render)
        self.img.image = self.render
        self.img.place(x=50, y=100)

        def q11():
            global ans10,crtans
            ans10 = str(var10.get())
            print(ans10)
            if ans10 == answer11:
                crtans = crtans+1

        #Question 11
        var10 = IntVar()

        self.R37 = Radiobutton(self.seventhwin, text="A) Garbage value", variable=var10, value=1,bg='lightgreen',
                  command=q11)
        self.R37.place(x=500,y=100)
        self.R38 = Radiobutton(self.seventhwin, text="B) 1", variable=var10, value=2,bg='lightgreen',
                  command=q11)
        self.R38.place(x=500,y=150)
        self.R39 = Radiobutton(self.seventhwin, text="C) 0", variable=var10, value=3,bg='lightgreen',
                  command=q11)
        self.R39.place(x=500,y=200)

        self.R40 = Radiobutton(self.seventhwin, text="D) Error", variable=var10, value=4,bg='lightgreen',
                  command=q11)
        self.R40.place(x=500,y=250)

        self.q12 = Image.open("images/q12-small.png")
        self.render = ImageTk.PhotoImage(self.q12)
        self.img = Label(self.seventhwin, image=self.render)
        self.img.image = self.render
        self.img.place(x=50, y=350)

        def q12():
            global ans11,crtans
            ans11 = str(var11.get())
            print(ans11)
            if ans11 == answer12:
                crtans = crtans+1

        #Question 12
        var11 = IntVar()

        self.R41 = Radiobutton(self.seventhwin, text="A) 5", variable=var11, value=1,bg='lightgreen',
                  command=q12)
        self.R41.place(x=500,y=350)
        self.R42 = Radiobutton(self.seventhwin, text="B) 6", variable=var11, value=2,bg='lightgreen',
                  command=q12)
        self.R42.place(x=500,y=400)
        self.R43 = Radiobutton(self.seventhwin, text="C) 14", variable=var11, value=3,bg='lightgreen',
                  command=q12)
        self.R43.place(x=500,y=450)

        self.R44 = Radiobutton(self.seventhwin, text="D) Compilation Error", variable=var11, value=4,bg='lightgreen',
                  command=q12)
        self.R44.place(x=500,y=500)

        self.seventhnext = Button(self.seventhwin,width=10,text="NEXT",command = self.seventhnext)
        self.seventhnext.place(x=800,y=550)

        self.seventhback = Button(self.seventhwin,width=10,text="BACK",command = self.seventhback)
        self.seventhback.place(x=700,y=550)


        self.seventhwin.withdraw()



        #----------------------------------------------------------------------#


        self.eighthwin = Toplevel()

        self.eighthwin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.frame6 = Frame(self.eighthwin,width=1000, height=600, bg='black')
        self.frame6.pack()

        self.q13 = Image.open("images/q13-small.png")
        self.render = ImageTk.PhotoImage(self.q13)
        self.img = Label(self.eighthwin, image=self.render)
        self.img.image = self.render
        self.img.place(x=50, y=100)

        def q13():
            global ans12,crtans
            ans12 = str(var12.get())
            print(ans12)
            if ans12 == answer13:
                crtans = crtans+1

        #Question 13
        var12 = IntVar()

        self.R45 = Radiobutton(self.eighthwin, text="A) The program has a compile error because the size of the array \nwasn’t specified when declaring the array.", variable=var12, value=1,bg='lightgreen',
                  command=q13)
        self.R45.place(x=500,y=100)
        self.R46 = Radiobutton(self.eighthwin, text="B) The program has a runtime error because the array elements are not initialized.", variable=var12, value=2,bg='lightgreen',
                  command=q13)
        self.R46.place(x=500,y=150)
        self.R47 = Radiobutton(self.eighthwin, text="C) The program runs fine and displays x[0] is 0.", variable=var12, value=3,bg='lightgreen',
                  command=q13)
        self.R47.place(x=500,y=200)

        self.R48 = Radiobutton(self.eighthwin, text="D) The program has a runtime error because the array element x[0] is not defined.", variable=var12, value=4,bg='lightgreen',
                  command=q13)
        self.R48.place(x=500,y=250)

        self.q14 = Image.open("images/q14-small.png")
        self.render = ImageTk.PhotoImage(self.q14)
        self.img = Label(self.eighthwin, image=self.render)
        self.img.image = self.render
        self.img.place(x=50, y=350)

        def q14():
            global ans13,crtans
            ans13 = str(var13.get())
            print(ans13)
            if ans13 == answer14:
                crtans = crtans+1

        #Question 14
        var13 = IntVar()

        self.R49 = Radiobutton(self.eighthwin, text="A) 0", variable=var13, value=1,bg='lightgreen',
                  command=q14)
        self.R49.place(x=500,y=350)
        self.R50 = Radiobutton(self.eighthwin, text="B) 5", variable=var13, value=2,bg='lightgreen',
                  command=q14)
        self.R50.place(x=500,y=400)
        self.R51 = Radiobutton(self.eighthwin, text="C) Exception is thrown", variable=var13, value=3,bg='lightgreen',
                  command=q14)
        self.R51.place(x=500,y=450)

        self.R52 = Radiobutton(self.eighthwin, text="D) Returns the index of “Hari”", variable=var13, value=4,bg='lightgreen',
                  command=q14)
        self.R52.place(x=500,y=500)

        self.eighthnext = Button(self.eighthwin,width=10,text="NEXT",command = self.eighthnext)
        self.eighthnext.place(x=800,y=550)

        self.eighthback = Button(self.eighthwin,width=10,text="BACK",command = self.eighthback)
        self.eighthback.place(x=700,y=550)


        self.eighthwin.withdraw()

        #=======================================================================================#


        self.ninthwin = Toplevel()

        self.ninthwin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.frame7 = Frame(self.ninthwin,width=1000, height=600, bg='black')
        self.frame7.pack()

        self.q15 = Image.open("images/q15-small.png")
        self.render = ImageTk.PhotoImage(self.q15)
        self.img = Label(self.ninthwin, image=self.render)
        self.img.image = self.render
        self.img.place(x=50, y=100)

        def q15():
            global ans14,crtans
            ans14 = str(var14.get())
            print(ans14)
            if ans14 == answer15:
                crtans = crtans+1

        #Question 15
        var14 = IntVar()

        self.R53 = Radiobutton(self.ninthwin, text="A) 123", variable=var14, value=1,bg='lightgreen',
                  command=q15)
        self.R53.place(x=500,y=100)
        self.R54 = Radiobutton(self.ninthwin, text="B) 1", variable=var14, value=2,bg='lightgreen',
                  command=q15)
        self.R54.place(x=500,y=150)
        self.R55 = Radiobutton(self.ninthwin, text="C) Error", variable=var14, value=3,bg='lightgreen',
                  command=q15)
        self.R55.place(x=500,y=200)

        self.R56 = Radiobutton(self.ninthwin, text="D) 1 2 3", variable=var14, value=4,bg='lightgreen',
                  command=q15)
        self.R56.place(x=500,y=250)

        self.q16 = Image.open("images/q16-small.png")
        self.render = ImageTk.PhotoImage(self.q16)
        self.img = Label(self.ninthwin, image=self.render)
        self.img.image = self.render
        self.img.place(x=50, y=350)

        def q16():
            global ans15,crtans
            ans15 = str(var15.get())
            print(ans15)
            if ans15 == answer16:
                crtans = crtans+1

        #Question 16
        var15 = IntVar()

        self.R57 = Radiobutton(self.ninthwin, text="A) Cybertron", variable=var15, value=1,bg='lightgreen',
                  command=q16)
        self.R57.place(x=500,y=350)
        self.R58 = Radiobutton(self.ninthwin, text="B) CYBERTRON", variable=var15, value=2,bg='lightgreen',
                  command=q16)
        self.R58.place(x=500,y=400)
        self.R59 = Radiobutton(self.ninthwin, text="C) False", variable=var15, value=3,bg='lightgreen',
                  command=q16)
        self.R59.place(x=500,y=450)

        self.R60 = Radiobutton(self.ninthwin, text="D) True", variable=var15, value=4,bg='lightgreen',
                  command=q16)
        self.R60.place(x=500,y=500)

        self.ninthnext = Button(self.ninthwin,width=10,text="NEXT",command = self.ninthnext)
        self.ninthnext.place(x=800,y=550)

        self.ninthback = Button(self.ninthwin,width=10,text="BACK",command = self.ninthback)
        self.ninthback.place(x=700,y=550)


        self.ninthwin.withdraw()

        #______________________________________________________________________________________________#

        self.tenthwin = Toplevel()

        self.tenthwin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.frame8 = Frame(self.tenthwin,width=1000, height=600, bg='black')
        self.frame8.pack()

        self.q17 = Image.open("images/q17-small.png")
        self.render = ImageTk.PhotoImage(self.q17)
        self.img = Label(self.tenthwin, image=self.render)
        self.img.image = self.render
        self.img.place(x=50, y=100)

        def q17():
            global ans16,crtans
            ans16 = str(var16.get())
            print(ans16)
            if ans16 == answer17:
                crtans = crtans+1

        #Question 17
        var16 = IntVar()

        self.R61 = Radiobutton(self.tenthwin, text="A) Type Error: can only concatenate list (not “int”) to list", variable=var16, value=1,bg='lightgreen',
                  command=q17)
        self.R61.place(x=500,y=100)
        self.R62 = Radiobutton(self.tenthwin, text="B) 11", variable=var16, value=2,bg='lightgreen',
                  command=q17)
        self.R62.place(x=500,y=150)
        self.R63 = Radiobutton(self.tenthwin, text="C) 12", variable=var16, value=3,bg='lightgreen',
                  command=q17)
        self.R63.place(x=500,y=200)

        self.R64 = Radiobutton(self.tenthwin, text="D) 38", variable=var16, value=4,bg='lightgreen',
                  command=q17)
        self.R64.place(x=500,y=250)

        self.q18 = Image.open("images/q18-small.png")
        self.render = ImageTk.PhotoImage(self.q18)
        self.img = Label(self.tenthwin, image=self.render)
        self.img.image = self.render
        self.img.place(x=50, y=350)

        def q18():
            global ans17,crtans
            ans17 = str(var17.get())
            print(ans17)
            if ans17 == answer18:
                crtans = crtans+1

        #Question 18
        var17 = IntVar()

        self.R65 = Radiobutton(self.tenthwin, text="A)  [5, 2, 3, 4] [5, 2, 3, 4] [1, 2, 3, 4] [1, 2, 3, 4]", variable=var17, value=1,bg='lightgreen',
                  command=q18)
        self.R65.place(x=500,y=350)
        self.R66 = Radiobutton(self.tenthwin, text="B) [[5], 2, 3, 4] [[5], 2, 3, 4] [[5], 2, 3, 4] [1, 2, 3, 4]", variable=var17, value=2,bg='lightgreen',
                  command=q18)
        self.R66.place(x=500,y=400)
        self.R67 = Radiobutton(self.tenthwin, text="C) [5, 2, 3, 4] [5, 2, 3, 4] [5, 2, 3, 4] [1, 2, 3, 4]", variable=var17, value=3,bg='lightgreen',
                  command=q18)
        self.R67.place(x=500,y=450)

        self.R68 = Radiobutton(self.tenthwin, text="D) [[5], 2, 3, 4] [[5], 2, 3, 4] [1, 2, 3, 4] [1, 2, 3, 4]", variable=var17, value=4,bg='lightgreen',
                  command=q18)
        self.R68.place(x=500,y=500)

        self.tenthnext = Button(self.tenthwin,width=10,text="NEXT",command = self.tenthnext)
        self.tenthnext.place(x=800,y=550)

        self.tenthback = Button(self.tenthwin,width=10,text="BACK",command = self.tenthback)
        self.tenthback.place(x=700,y=550)


        self.tenthwin.withdraw()

        #____________________________________________---------------------------------------------#


        self.lastwin = Toplevel()

        self.lastwin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.frame9 = Frame(self.lastwin,width=1000, height=600, bg='black')
        self.frame9.pack()

        self.q19 = Image.open("images/q19-small.png")
        self.render = ImageTk.PhotoImage(self.q19)
        self.img = Label(self.lastwin, image=self.render)
        self.img.image = self.render
        self.img.place(x=50, y=100)

        def q19():
            global ans18,crtans
            ans18 = str(var18.get())
            print(ans18)
            if ans18 == answer19:
                crtans = crtans+1

        #Question 19
        var18 = IntVar()

        self.R69 = Radiobutton(self.lastwin, text="A) KeyError", variable=var18, value=1,bg='lightgreen',
                  command=q19)
        self.R69.place(x=500,y=100)
        self.R70 = Radiobutton(self.lastwin, text="B) {0: 1, 7: 0, 1: 1, 8: 0}", variable=var18, value=2,bg='lightgreen',
                  command=q19)
        self.R70.place(x=500,y=150)
        self.R71 = Radiobutton(self.lastwin, text="C) {0: 0, 7: 0, 1: 1, 8: 1}", variable=var18, value=3,bg='lightgreen',
                  command=q19)
        self.R71.place(x=500,y=200)

        self.R72 = Radiobutton(self.lastwin, text="D) {1: 1, 7: 2, 0: 1, 8: 1}", variable=var18, value=4,bg='lightgreen',
                  command=q19)
        self.R72.place(x=500,y=250)

        self.q20 = Image.open("images/q20-small.png")
        self.render = ImageTk.PhotoImage(self.q20)
        self.img = Label(self.lastwin, image=self.render)
        self.img.image = self.render
        self.img.place(x=50, y=350)

        def q20():
            global ans19,crtans
            ans19 = str(var19.get())
            print(ans19)
            if ans19 == answer20:
                crtans = crtans+1

        #Question 20
        var19 = IntVar()

        self.R73 = Radiobutton(self.lastwin, text="A) 100", variable=var19, value=1,bg='lightgreen',
                  command=q20)
        self.R73.place(x=500,y=350)
        self.R74 = Radiobutton(self.lastwin, text="B) Compilation error", variable=var19, value=2,bg='lightgreen',
                  command=q20)
        self.R74.place(x=500,y=400)
        self.R75 = Radiobutton(self.lastwin, text="C) Runtime error", variable=var19, value=3,bg='lightgreen',
                  command=q20)
        self.R75.place(x=500,y=450)

        self.R76 = Radiobutton(self.lastwin, text="D) None of these", variable=var19, value=4,bg='lightgreen',
                  command=q20)
        self.R76.place(x=500,y=500)

        self.save = Button(self.lastwin,width=10,text="Save",command = self.save)
        self.save.place(x=800,y=550)

        self.lastback = Button(self.lastwin,width=10,text="BACK",command = self.lastback)
        self.lastback.place(x=700,y=550)

        self.lastwin.withdraw()

        
    def save(self):
        print("Done")
        self.name = self.nameentry.get()
        self.clg = self.clgentry.get()
        self.mail = self.mailentry.get()
        data_to_upload = {'Name' : self.name,
                          'College' : self.clg,
                          'Mail' : self.mail,
                          'Correct' : crtans}
        result = fbconn.post('/candidate/',data_to_upload)
        self.save.config(state="disabled")
        self.answer()
    def answer(self):
        if answer1==ans:
            anslist.append('1')
        else:
            anslist.append('0')
        if answer2==ans1:
            anslist.append('1')
        else:
            anslist.append('0')
        print(anslist)
    def start(self):
        self.master.withdraw()
        self.secondwin.deiconify()
    def secondnext(self):
        print("Done")
        self.secondwin.withdraw()
        self.thirdwin.deiconify()
    def thirdnext(self):
        print("Third Next")
        self.thirdwin.withdraw()
        self.forthwin.deiconify()
    def forthnext(self):
        print("Forth Next")
        self.forthwin.withdraw()
        self.fifthwin.deiconify()
    def fifthnext(self):
        print("Fifth Next")
        self.fifthwin.withdraw()
        self.sixthwin.deiconify()
    def sixthnext(self):
        print("Sixth Next")
        self.sixthwin.withdraw()
        self.seventhwin.deiconify()
    def seventhnext(self):
        print("Seventh Next")
        self.seventhwin.withdraw()
        self.eighthwin.deiconify()
    def eighthnext(self):
        print("Eighth Next")
        self.eighthwin.withdraw()
        self.ninthwin.deiconify()
    def ninthnext(self):
        print("Ninth Next")
        self.ninthwin.withdraw()
        self.tenthwin.deiconify()
    def tenthnext(self):
        print("Tentn Next")
        self.tenthwin.withdraw()
        self.lastwin.deiconify()
    def lastnext(self):
        print("Last Next")
    def secondback(self):
        print("Back")
        self.secondwin.withdraw()
        self.master.deiconify()
    def thirdback(self):
        self.thirdwin.withdraw()
        self.secondwin.deiconify()
    def forthback(self):
        self.forthwin.withdraw()
        self.thirdwin.deiconify()
    def fifthback(self):
        self.fifthwin.withdraw()
        self.forthwin.deiconify()
    def sixthback(self):
        self.sixthwin.withdraw()
        self.fifthwin.deiconify()
    def seventhback(self):
        self.seventhwin.withdraw()
        self.sixthwin.deiconify()
    def eighthback(self):
        self.eighthwin.withdraw()
        self.seventhwin.deiconify()
    def ninthback(self):
        self.ninthwin.withdraw()
        self.eighthwin.deiconify()
    def tenthback(self):
        self.tenthwin.withdraw()
        self.ninthwin.deiconify()
    def lastback(self):
        self.lastwin.withdraw()
        self.tenthwin.deiconify()
      
root =  Tk()
obj = FirstRound(root)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.mainloop()
