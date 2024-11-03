#CS YEAR-END PROJECT
#                       Customer Segmentation
'''-------------------------------------------------------------------'''

#Required Modules
from tkinter import *
import os
import csv
import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


#Pop-up 

#Commencing the Pop-up for wrong password
def delete3():
    #erasing the contents in screen 4
    screen4.destroy()

#Commencing the Pop-up for wrong username
def delete4():
    #erasing the contents in screen 5
    screen5.destroy()


def session():
    #creating a new screen
    #SCREEN 8 - dashboard
    global screen8
    screen8= Toplevel(screen)
    screen8.title('dashboard')
    screen8.geometry('400x400')
    Label(screen8,text='Welcome User',width='300',height='2',bg='grey').pack()
    Label(screen8,text='').pack()
    entry()

def entry():
    global cid
    global gender1
    global age1
    global income1
    global spending
    
    #for creating the values in csv file
    #setting the tkinter variable for all the labels
    Customer_id=StringVar()
    gender=StringVar()
    age=StringVar()
    income=StringVar()
    spending_score=StringVar()
    
    #customer id
    Label(screen8,text='Enter the customer ID:').pack()
    cid=Entry(screen8,textvariable=Customer_id)
    cid.pack()

    #gender
    Label(screen8,text='Enter the gender of the customer:').pack()
    gender1=Entry(screen8,textvariable=gender)
    gender1.pack()

    #age
    Label(screen8,text='Enter the age of the customer:').pack()
    age1=Entry(screen8,textvariable=age)
    age1.pack()


    #annual income
    Label(screen8,text='Enter the Annual Income of the customer:').pack()
    income1=Entry(screen8,textvariable=income)
    income1.pack()


    #spending score
    Label(screen8,text='Enter the spending score of the customer:').pack()
    spending=Entry(screen8,textvariable=spending_score)
    spending.pack()
 

    #button for data creation
    Button(screen8,text='Submit',width=10,height=1,command=confirm).pack()
        
    Label(screen8,text='').pack()
    Label(screen8,text='').pack()

    #button for plotting the graph in new screen
    Button(screen8,text='Plot Graph',command=graph_it).pack()
    
def confirm():
    #creating a new screen 
    #SCREEN 9-CONFIRMATION
    screen9=Toplevel(screen)
    screen9.title('Success')
    screen9.geometry('400x400')

    #UPDATING THE CONTENTS INTO THE CSV FILE
    create_file()

    #CLEARING THE RESPECTIVE FIELDS
    cid.delete(0,END)
    gender1.delete(0,END)
    age1.delete(0,END)
    income1.delete(0,END)
    spending.delete(0,END)
    Label(screen9, text='Data Entered').pack()
    
def create_file():
    #RECIEVING THE VALUES USING GET METHOD
    cid_info=cid.get()
    gender_info=gender1.get()
    age_info=age1.get()
    income_info=income1.get()
    spending_info=spending.get()

    #APPENDING THE CSV FILE WITH NEW INFO
    #CREATING THE LIST WITH THE GIVEN VALUES
    info=[cid_info,gender_info,age_info,income_info,spending_info]
    with open(username1+'.csv','a')as file3:
        writer = csv.writer(file3)
        writer.writerow(info)
    

def graph_it():
    #creating a new screen for presenting the graph
    #SCREEN 10
    screen10=Toplevel(screen)
    screen10.title('Graph')
    screen10.geometry('400x400')

    #Plotting a graph using the csv file
    #loading the data from the csv file for the pandas dataframe
    dataset=pd.read_csv(username1+'.csv')

    #choosing the annual income column and spending score column
    dataset_new=dataset[['Annual Income','Spending Score']].values

    #determining the maximum number of clusters
    #using the simple method
    limit=int((dataset_new.shape[0]//2)**0.5)

    #creating a list for all posible clusters pairs
    fields=[]
    values=[]

    #determining the number of clusters
    #using silhoutte score method
    for k in range(2,limit+1):
        model=KMeans(n_clusters=k)
        model.fit(dataset_new)
        pred=model.predict(dataset_new)
        score=silhoette_score(dataset_new, pred)
        print(score)
        fields.append(k)
        values.append(score)

    #creating a dictionary to find the clusters
    _cluster_=dict(zip(fields, values))
    

    #clustering the data using kmeans
    #the maximum number of clusters is k
    a=max(values)
    k=fields[values.index(a)]
    model=KMeans(n_clusters=k)

    #predicting the clusters
    pred=model.fit_predict(dataset_new)

    #plotting all the clusters
    colours=['red','blue','green','yellow','orange']

    for j in np.unique(model.labels_):
        plt.scatter(dataset_new[pred==j, 0],
        dataset_new[pred==j, 1],
        c=colours[j])

    #plotting the cluster centroids
    plt.scatter(model.cluster_centers_[:, 0],
    model.cluster_centers_[:, 1],
    s=200,#marker size
    c='black')

    #Plotting and marking the graph
    plt.title('K Means clustering')
    plt.xlabel('Annual Income')
    plt.ylabel('Spending Score')
    plt.show()

    #exiting the graph page
    Label(screen10, text='').pack()
    Label(screen10, text='').pack()
    Button(screen10, text='End', width=10, height=1, command=screen10.destroy).pack()

    
def login_success():
    #creating a csv file for the purpose of database
    header=['CID','Gender','Age','Annual Income','Spending Score']
    
    file2=open(username1+'.csv','w')
    writer1=csv.writer(file2)
    writer1.writerow(header)
    file2.close()
    session()


#GUI of the pop-up of wrong password
def password_not_recognised():
    #CREATING A NEW SCREEN
    #SCREEN 4- PASSWROD ERROR
    global screen4
    screen4=Toplevel(screen)
    screen4.title('ERROR')
    screen4.geometry('400x400')
    Label(screen4, text='Password Not Recognised').pack()
    Button(screen4, text='OK', command=delete3).pack()

#GUI of the pop-up of the wrong username
def user_not_found():
    #CREATING A NEW SCREEN
    #SCREEN 5- USER ERROR
    global screen5
    screen5=Toplevel(screen)
    screen5.title('ERROR')
    screen5.geometry('400x400')
    Label(screen5, text='User Not Found').pack()
    Button(screen5, text='OK', command=delete4).pack()

#creating a file for the user info
def register_user():
    #GETTING THE VALUES FOR THE USER INFO USING GET METHOD
    global username_info
    username_info=username.get()
    password_info=password.get()

    #CHECKING IF THE USER IS ALREADY PRESENT OR NOT
    if username_info in users:
        #deleting the entries given by the user
        username_entry.delete(0,END)
        password_entry.delete(0,END)

        #informing the user that the username has already been registered
        Label(screen1,text='Username Already Present', fg='red' ,font=('calibri', 11)).pack()
    else:
        #INCLUDING THE USER TO THE LIST
        users.append(username_info)

        #CREATING A FILE WHICH CONTAINS THE USER AND THE PASSWORD IN A DISTINCT FILE
        file=open(username_info,"w")
        file.write(username_info+'\n')
        file.write(password_info)
        file.close()
          
        #deleting the entries given by the user
        username_entry.delete(0,END)
        password_entry.delete(0,END)
          
        #confirming the registration
        Label(screen1,text='Registration Succesful', fg='green' ,font=('calibri', 11)).pack()

 #User info verification   
def login_verify():

    #GETTING THE INFO FOR VERIFICATION USING GET METHOD
    global username1
    username1=username_verify.get()
    password1=password_verify.get()

    #CLEARING THE RESPECTIVE FIELDS
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)
    
    #using the os module to access the entire files in the directory(folder)
    list_of_files=os.listdir()
    #SEARCHING FOR THE USER NAMES IN ALL FILES IN THE DIRECTORY
    if username1 in list_of_files:
        file1=open(username1,'r')
        #ignore blank spaces
        verify=file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()

#New User Registration    
def register():
    #CREATING A NEW SCREEN
    #SCREEN1 - REGISTER
    global screen1
    global users
    screen1=Toplevel(screen)
    screen1.title('Register')
    screen1.geometry('400x400')
    users=[]

    global username
    global password
    global username_entry
    global password_entry
    username=StringVar()
    password=StringVar()

    Label(screen1,text='Please enter details below',bg='grey',width='300',height='2', font=('Calibri',13)).pack()
    Label(screen1,text='').pack()

    Label(screen1,text='New Username:').pack()
    global username_entry
    global password_entry
    username_entry=Entry(screen1,textvariable=username)
    username_entry.pack()
    Label(screen1,text='New Password :').pack()
    password_entry=Entry(screen1,textvariable=password)
    password_entry.pack()
    Label(screen1,text='').pack()
    Button(screen1,text='Register',width=10,height=1,command=register_user).pack()
    
#Login Page    
def login():
    global screen2
    screen2=Toplevel(screen)
    screen2.title('login')
    screen2.geometry('400x400')
    Label(screen2,text='Please enter details below to login',bg='grey',width='300',height='2', font=('Calibri',13)).pack()
    Label(screen2,text='').pack()

    global username_verify
    global password_verify
    
    username_verify=StringVar()
    password_verify=StringVar()
    
    global username_entry1
    global password_entry1
    Label(screen2,text='Username:').pack()
    username_entry1= Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text='').pack()
    Label(screen2,text='Password :').pack()
    password_entry1= Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text='').pack()
    Button(screen2, text='Login', width=10, height=1, command=login_verify).pack()
    
  #INTRO SCREEN  
def main_screen():
    global screen
    screen = Tk()
    screen.geometry('400x400')
    Label(text='').pack()
    Label(text='').pack()
    Label(text='').pack()
    Label(text='').pack()
    screen.title('Customer Segmentation')
    Label(text = 'Customer Segmentation',bg ='grey',width='300',height='2', font=('Calibri',13)).pack()
    Label(text='').pack()#empty line
    Button(text='  Login ',width='300',height='2',command=login).pack()
    Label(text='').pack()
    Button(text='Register',width='300',height='2',command=register).pack()
    screen.mainloop()#to avoid buffer
    
#Calling the function to start the program
main_screen()
    
