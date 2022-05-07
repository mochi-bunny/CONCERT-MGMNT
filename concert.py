''' 

CONCEPTS APPLIED:
1.TRIGGER
2.CONSTRAINTS: NOT NULL, CHECK, PRIMARY KEY, FOREIGN KEY, UNIQUE
3.VIEW
4.SUBQUERY
5.PYTHON GUI TKINTER
6.INNER JOIN
7.SQL CONNECTOR
8.FUNCTION AND CLASS
9.WHILE LOOP

'''


import mysql.connector
import pandas as pd
from tkinter import *

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)
print("WELCOME TO EXA EVENTS")

c=mydb.cursor()
#c.execute("create database event_inc")
'''
c.execute("show databases")
for x in c:
    print(x)
    '''
c.execute("use event_inc")




'''
 
c.execute("drop trigger artist_hired")
c.execute("drop table artist")
c.execute("drop table hires")
c.execute("drop table employee")


c.execute("drop table time_")
c.execute('drop table arena')
c.execute("drop table performs")

c.execute("drop trigger BOOKING_DETAILS")
c.execute("drop procedure ticket_entry")
c.execute('drop table booking')
c.execute("drop table ticket")
'''

#employee -------------------------------------------------------------------------------------------------------------------------------------------

'''
c.execute("create table employee(eid varchar(4) not null,ename char(25),company char(30),primary key(eid))")

c.execute("insert into employee(eid, ename, company) values('A12','CHRISTOPHER CHAN','JYP'),('A13','FELIX LEE','JYP'),('A15','JEONGIN YANG','JYP'),('A30','IRENE SEL','SM'),('A82','JAY PARK','BIGHIT LAB'),('M23','SILVIA KELP','MG SERVICES'),('T82','JAKE KIM','MGTECH'),('T21','KELLY HAN','Y TECHNO'),('A45','HAN JISUNG','JYP'),('M67','HARRY POTTS','K MGMT')")
'''  

#print(p1)
#print("created      ") 

#HIRES-------------------------------------------------------------------------------------------------------------------------------------------
 
#c.execute("drop table hires")
'''
c.execute("create table hires( eid varchar(4) not null unique,primary key(eid),foreign key(eid) references employee(eid), check (eid like 'A%')  )")
c.execute("insert into hires(eid) values ('A12'),('A13'), ('A15'),('A30'), ('A82'),('A45')")
'''


#print(p2)
#print("created      ")

#ARTIST-------------------------------------------------------------------------------------------------------------------------------------------
#c.execute("drop table artist")
'''
c.execute("create table artist(artist_id varchar(4) not null unique , artist_name char(25) not null,foreign key(artist_id) references hires(eid))")
c.execute("insert into artist(artist_id, artist_name) values('A12','STRAY KIDS'),('A13','STRAY KIDS'),('A15','STRAY KIDS'),('A45','STRAY KIDS'),('A30','IRENE'),('A82','JAY')")

'''

#print(p3)
#print("created      ")

#TRIGGER TO INSERT ARTIST ID INTO HIRES-------------------------------------------------------------------------------------------------------------------------------------------
#c.execute("CREATE TRIGGER artist_hired AFTER INSERT ON employee FOR EACH ROW BEGIN if (new.eid like'A%') then insert into hires values(new.eid); end if;END ")
#print("trigger")

#ARENA-------------------------------------------------------------------------------------------------------------------------------------------
'''
c.execute("CREATE TABLE arena(	pid varchar(5) not null,arena_no varchar(4) not null,primary key(pid))")
c.execute("insert into arena values('S9213', 'EG13'),('X902','DF21'),('J872','EG13'),('D452','BA89'),('G481','DF21')")

'''
#print(p4)
#print("created      ")



#performs-------------------------------------------------------------------------------------------------------------------------------------------
'''
c.execute("CREATE TABLE performs(pno int(4),pname  char(25),artist_name CHAR(25) not null,primary key(pno))")

c.execute("insert into performs(pno, pname, artist_name) values(2132,'GODS MENU','STRAY KIDS'),(2534,'MONSTER','IRENE'),(3421,'BACK DOOR', 'STRAY KIDS'),(5642,'GOBLIN: MUSICAL', 'IRENE'),(7639,'MIRACLE IN THE WOOD','JAY')")
'''
#print(p5)
 
 
#time_-------------------------------------------------------------------------------------------------------------------------------------------
#c.execute("drop table time_")
'''
c.execute("create table time_(pid  varchar(5) not null,pno int(4),ptime datetime,foreign key(pno) references performs(pno),foreign key(pid) references arena(pid))")
c.execute("insert into time_(pid,pno, ptime) values('S9213', 2132, '22-10-05 16:04' ),('X902', 2534 ,'22-10-05 18:30'),('J872',3421,'22-10-05 16:45'),('D452', 5642,'22-10-04 21:15' ),('G481', 7639, '22-10-06 17:22')")
'''

#print(p6)
 

#ticket-------------------------------------------------------------------------------------------------------------------------------------------
#c.execute("drop table ticket")
'''
c.execute("create table ticket(t_no int(5),seat varchar(4) unique ,e_date date, primary key(t_no))")
c.execute("insert into ticket(t_no, seat ,e_date) values(30085, 'E009','22-10-05' ),(30087,  'E049','22-10-05'),(30089, 'A453', '22-10-04'),(30030, 'D039','22-10-06')")
'''
#print(p7)

#booking-------------------------------------------------------------------------------------------------------------------------------------------
#c.execute("drop table booking")
'''
c.execute("create table booking(t_no int(5),arena_no varchar(4) not null, foreign key(t_no) references ticket(t_no) )")
c.execute(" insert into booking values(30085, 'EG13'),(30087, 'EG13' ),(30089, 'BA89'),(30030, 'DF21')")
'''
#print(p8)

#booking_Trigger-------------------------------------------------------------------------------------------------------------------------------------------
#c.execute("CREATE TRIGGER BOOKING_DETAILS AFTER INSERT ON ticket FOR EACH ROW BEGIN declare ar varchar(4) ; if (new.seat like 'E%') then set ar='EG13'; ELSE IF (new.seat like 'A%') then set ar='BA89'; ELSE IF (new.seat like 'D%') then set ar='DF21';	END IF; END IF; END IF; insert into booking values(new.t_no, ar); END")
#print("trigger created")


#procedure-------------------------------------------------------------------------------------------------------------------------------------------
#c.execute("create procedure ticket_entry(in tno int(5), seat varchar(4), edate date) begin  insert into ticket values(tno,seat, edate); end")

#print("proc made")
#MENU-------------------------------------------------------------------------------------------------------------------------------------------

#c.execute("insert into ticket values(30034, 'A119','22-10-05' )")


x="y" 
while(x=="y"):
    
    print("1- RECENT EVENTS")
    print("2-MEMBERS OF EACH GROUP")
    print("3-EVENT LOCATION AND TICKET DETAILS")
    print("4-VIEW TABLES")
    print("5-INSERT NEW TICKET DETAILS")
    print("0-EXIT")
    n=int(input("choice? "))

    if n==2:
        #subquery
        c.execute("select a.artist_name, e.ename from employee e , artist a where a.artist_id=e.eid and e.eid in (select * from hires) order by a.artist_name")
        e=c.fetchall()
        print(pd.DataFrame(e,columns=["artist name", "member name"]))
         
    elif n==1:
        #select query as view
         #c.execute("create view even_ as select p.pname, p.artist_name, t.ptime from performs p, time_ t where p.pno=t.pno group by p.pname")
         c.execute("select * from even_")
         e=c.fetchall()
         print(pd.DataFrame(e,columns=["artist name", "performance name","performance time"]))
        
    elif n==3:
        #inner join
         c.execute(" select t.t_no, t.seat ,t.e_date, b.arena_no from ticket t inner join booking b on t.t_no=b.t_no group by t.t_no ")
         
         e=c.fetchall()
         print(pd.DataFrame(e,columns=["t_no", "seat" ,"e_date", "arena_no" ]))
    elif n==4:
        #display tables
        print("TABLES:\n1-EMPLOYEE\n2-HIRES\n3-ARTIST\n4-ARENA\n5-PERFORMS\n6-TIME\n7-TICKET\n8-BOOKING\n")
        
        a=int(input("enter table no. -"))

        if a==1:
            c.execute("select * from employee")
            res=c.fetchall()
            p1=pd.DataFrame(res,columns=["eid","ename","company"])
             
            print(p1)
            

        elif a==2:            
            c.execute("select * from hires")
            res2=c.fetchall()
            p2=pd.DataFrame(res2,columns=["eid"])
            print(p2)
            
        elif a==3:
            c.execute("select * from artist")
            res3=c.fetchall()
            p3=pd.DataFrame(res3,columns=["artist_id", "artist_name"])
            print(p3)
            
        elif a==4:
            c.execute("select * from arena")
            res4=c.fetchall()
            p4=pd.DataFrame(res4,columns=["pid", "arena_no"])
            print(p4)

        elif a==5:
            c.execute("select * from performs")
            res5=c.fetchall()
            p5=pd.DataFrame(res5,columns=["pno", "pname", "artist_name"])
            print(p5)
            
        elif a==6:
            c.execute("select * from time_")
            res6=c.fetchall()
            p6=pd.DataFrame(res6,columns=["pid","pno", "ptime"])
            print(p6)

        elif a==7:
            c.execute("select * from ticket")
            res7=c.fetchall()
            p7=pd.DataFrame(res7,columns=["t_no", "seat" ,"e_date"])
            print(p7)
            
        elif a==8:
            c.execute("select * from booking")
            res8=c.fetchall()
            p8=pd.DataFrame(res8,columns=["t_no", "arena_no"])
            print(p8)
    elif n==5:
        class Window:
            def __init__(self, win):
                self.l1= Label(w, text='TICKET NO.: ')
                self.l2= Label(w, text='SEAT NO:')
                self.l3= Label(w, text='DATE:')
                self.t1=Entry()
                self.t2=Entry()
                self.t3=Entry()

                self.btn=Button(w, text='submit')


                self.l1.place(x=100, y=50)
                self.t1.place(x=200, y=50)
                self.l2.place(x=100, y=150)
                self.t2.place(x=200, y=150)
                self.l3.place(x=100, y=250)
                self.t3.place(x=200, y=250)
                self.b1=Button(win, text='SUBMIT', command=self.submit)
                self.b1.place(x=300, y=300)

            def submit(self):
                s1=int(self.t1.get())
                s2=self.t2.get()
                s3=self.t3.get()
                self.t1.delete(0, 'end')
                self.t2.delete(0, 'end')
                self.t3.delete(0, 'end')
                args=(s1,s2,s3)
                
                c.callproc("ticket_entry", args)
                print("inserted")
        w=Tk()
        mywin=Window(w)
        w.title('INSERT TICKET DETAILS')
        w.geometry("500x500+10+10")
        w.mainloop()
        
           
    elif n==0: break    
    x=input("continue viewing? y/n:")
    
