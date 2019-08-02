#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from pandas import *
from tkinter import *
#import codecs
import csv
import copy
from collections import Counter
import random
from sklearn.cluster import KMeans
#TO FIND FACTOR K

datafile=open('test_test1.csv','r+')
datareader=csv.reader(datafile,delimiter=',')
datafile1=open('test_test1.csv','r+')
datareader1=csv.reader(datafile1,delimiter=',')
dataset = pd.read_csv('test_test1.csv')
X1 = dataset.iloc[:, [1,6]].values
data=[]
data1=[]
data2=[]
data3=[]
data4=[]
min_occuring=[]
count=0
for row in datareader:
    data.append(row)
for row in datareader1:
    data2.append(row)
    count+=1  
data2=data2[1:]
first=data[0]
data=data[1:]
gen_data=[]
sup_data=[]
micro_data=[]
micro_data=copy.deepcopy(data)
# Using the elbow method to find the optimal number of clusters
wcss = []
for i in range(1, 15):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X1)
    wcss.append(kmeans.inertia_)
"""plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
"""
# Fitting K-Means to the dataset
def ytd1():
    kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)
    y_kmeans = kmeans.fit_predict(X1)
# Visualising the clusters
    plt.scatter(X1[y_kmeans == 0, 0], X1[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
    plt.scatter(X1[y_kmeans == 1, 0], X1[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
    plt.scatter(X1[y_kmeans == 2, 0], X1[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
    plt.scatter(X1[y_kmeans == 3, 0], X1[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
    plt.scatter(X1[y_kmeans == 4, 0], X1[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
    plt.legend()
    plt.show()
    array1=[]
    sum1=[]
    for i in range(5):
        array1.append(0)
        sum1.append(0)
    for i in range(0,count-1):
         if(y_kmeans[i]==0):  
              array1[0]+=1
              sum1[0]+=X1[i][1]
         elif(y_kmeans[i]==1):  
              array1[1]+=1
              sum1[1]+=X1[i][1]
         elif(y_kmeans[i]==2):  
              array1[2]+=1
              sum1[2]+=X1[i][1]
         elif(y_kmeans[i]==3):  
              array1[3]+=1
              sum1[3]+=X1[i][1]
         elif(y_kmeans[i]==4):  
              array1[4]+=1
              sum1[4]+=X1[i][1]
    for i in range (5):
        sum1[i]/=array1[i]  
    for i in range (0,count-1):
         if(y_kmeans[i]==0):  
              X1[i][1]=sum1[0]
         elif(y_kmeans[i]==1):  
              X1[i][1]=sum1[1]
         elif(y_kmeans[i]==2):  
              X1[i][1]=sum1[2]
         elif(y_kmeans[i]==3):  
              X1[i][1]=sum1[3]
         elif(y_kmeans[i]==4):  
              X1[i][1]=sum1[4] 
      
    df=X1.tolist()
    for i in range (0,count-1):
             micro_data[i][1]=str(df[i][0])
             micro_data[i][6]=str(df[i][1]) 
    micro_data.sort(key=lambda x: x[6])         
# Visualising the clusters
    plt.scatter(X1[y_kmeans == 0, 0], X1[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
    plt.scatter(X1[y_kmeans == 1, 0], X1[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
    plt.scatter(X1[y_kmeans == 2, 0], X1[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
    plt.scatter(X1[y_kmeans == 3, 0], X1[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
    plt.scatter(X1[y_kmeans == 4, 0], X1[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
    plt.legend()
    plt.show()
    ytd(micro_data)

for i in range (0,count-1):
    temp1=data[i][6][:3]+"*"*(len(data[i][6])-3)
    temp2=data[i][9][:3]+"*"*(len(data[i][9])-3)
    data[i][6]=temp1
    data[i][9]=temp2
    min_occuring.append(temp1)
gen_data= copy.deepcopy(data)
    

for i in range (0,count-1):
    data[i][0]='*'
    data[i][3]='*'
    data[i][5]="INDIAN"
sup_data= copy.deepcopy(data)

for i in range (0,count-1):
    temp1=int(data[i][1])
    tex1=temp1-temp1%10
    tex2=temp1-temp1%10+10
    stri=str(tex1)+"-"+str(tex2)
    data[i][1]=stri
data.sort(key=lambda x: x[6])
min_occuring.sort()
min_occur=100000
for i in range(0,count-1):
    if(min_occuring.count(min_occuring[i])<min_occur):
        min_occur=min_occuring.count(min_occuring[i])
    i=i+min_occuring.count(min_occuring[i])
print(min_occur,"Anonymity")
data1=copy.deepcopy(data)

tempor=[]
k_data=[]
k_data=copy.deepcopy(data)

#TO FIND FACTOR L

for i in range (0,count-1):
    temp1=int(data2[i][1])
    if temp1>=50:
        tex=">=50"
    else:
        tex="<50"
    data[i][1]=tex


min_occuring.sort()
sum1=0
s=set(min_occuring)
k=[]
k=sorted(s)
sum1=0
i=0
s1=set()
s2=set()
min1=1000000
for e in k:
    temp1=min_occuring.count(e)
    tempor=data[i:i+temp1]
    for j in range(0,temp1-1):
        if (tempor[j][1]==">=50"):
            s1.add(tempor[j][7])
        else:
            s2.add(tempor[j][7])
    tempor.sort(key=lambda x: x[1])
    data[i:i+temp1]=tempor
    i=i+temp1
    min1=min(min1,len(s1),len(s2))
    s1=set()
    s2=set()
print(min1,"diversity")    
data3=copy.deepcopy(data)

t_data=[]
t_data=copy.deepcopy(data)
c1=0
c2=0
c3=0
c4=0
c5=0
t_factor=min_occur
for i in range (0,count-1):
    if(i%min_occur==0 and i!=0):
        if(max(c1,c2,c3,c4,c5) < t_factor):
            t_factor=max(c1,c2,c3,c4,c5)
        c1=0
        c2=0
        c3=0
        c4=0
        c5=0
    if(t_data[i][7]=="CANCER" or t_data[i][7]=="HYPERTENSION" or t_data[i][7]=="AIDS" or t_data[i][7]=="BRAIN TUMOUR" or t_data[i][7]=="ARTHRITIS" or t_data[i][7]=="RABIES" or t_data[i][7]=="EBOLA"):
        c1=c1+1
        t_data[i][7]="CHRONIC DISEASE"
    if(t_data[i][7]=="MALARIA" or t_data[i][7]=="DENGUE" or t_data[i][7]=="INFLUENZA"):
        c2=c2+1
        t_data[i][7]="MOSQUITO BITE"
    if(t_data[i][7]=="JAUNDICE" or t_data[i][7]=="HEPATITIS" or t_data[i][7]=="DIABETES" or t_data[i][7]=="DIARRHEA" or t_data[i][7]=="CHOLERA" or t_data[i][7]=="TYPHOID"):
        c3=c3+1
        t_data[i][7]="STOMACH INFECTION"  
    if(t_data[i][7]=="ASTHMA" or t_data[i][7]=="SWINE FLU" or t_data[i][7]=="STROKE" or t_data[i][7]=="HEART ATTACK"):
        c4=c4+1
        t_data[i][7]="LUNGS AND HEART DISEASE"  
    if(t_data[i][7]=="SMALL POX" or t_data[i][7]=="MEASLES" or t_data[i][7]=="CHICKEN POX" or t_data[i][7]=="TETANUS"):
        c5=c5+1
        t_data[i][7]="SKIN DISEASE"

print(t_factor,"Closeness")


#GUI USING TKINTER LIBRARY

top=Tk()
scrollbar = Scrollbar(top)
scrollbar.pack( side = RIGHT, fill=Y )
topFrame=Frame(top)
topFrame.pack()
frame=Frame(top)
frame.pack(side=BOTTOM)
text_font = ('Courier New','10','bold')
listbox = Listbox(frame,width=1000,height=100,fg="black",bg="lightblue",font=text_font)
listbox.pack(side=LEFT,fill=X)

# RSA (public key cryptography)

'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''


def multiplicative_inverse(e, phi):
    m0 = phi
    y = 0
    x = 1
  
    if (phi == 1) : 
        return 0
  
    while (e > 1) : 
  
        # q is quotient 
        q = e // phi 
  
        t = phi 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        phi = e % phi 
        e = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
  
    # Make x positive 
    if (x < 0) : 
        x = x + m0 
  
    return x 


'''
Tests to see if a number is prime.
'''


def is_prime(num):

    k=0
    for i in range(2,num//2+1):
        if(num%i==0):
            k=k+1
    if(k<=0):
        return True
    else:
        return False
'''Generate key pair'''

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    # n = pq
    n = p * q

    # Phi is the totient of n
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

message=[]
def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    message.append(cipher)
    str2 = ''.join(str(e) for e in cipher)

    return str2


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)
print ("RSA Encrypter/ Decrypter")
p = int(input("Enter a prime number between 17 & 30"))
q = int(input("Enter another prime number (Not one you entered above): "))
print ("Generating your public/private keypairs now . . .")
public, private = generate_keypair(p, q)
print ("Your public key is ", public, " and your private key is ", private)
for i in range (0,count-1):
    data3[i][7]=(encrypt(public, data3[i][7]))
data4=copy.deepcopy(data3)
for i in range (0,count-1):
    data4[i][7]=(decrypt(private, message[i]))
    
    
def ytd(dataa):
    listbox.delete(0,END)
    a=first[0]
    space=[18,10,8,8,14,15,10,50,18,18]
    for j in range(1,10,1):
            a=a+" "*(space[j-1]-len(first[j-1]))+first[j]
    listbox.insert(END,a)
    for row in dataa:
        str1=row[0]
        for j in range(1,10,1):
            str1=str1+" "*(space[j-1]-len(row[j-1]))+row[j]
        listbox.insert(END,str1)
    listbox.config(yscrollcommand=scrollbar.set,xscrollcommand=scrollbar.set)
    s1=scrollbar.config(command=listbox.xview)#.pack(side=BOTTOM,column=0)
    s2=scrollbar.config(command=listbox.yview)#.pack(side=LEFT,column=1)   
def ytd3():
    master2 = Tk()
    master2.geometry("200x100")
    master2.title("New Window")
    master2.configure(background='lightblue')
    L1 = Label(master2, text="Enter d:",fg='white',bg='steelblue',font=text_font)
    L2 = Label(master2, text="Enter n:",fg='white',bg='steelblue',font=text_font)
    E1 = Entry(master2, bd =5)
    E2 = Entry(master2, bd =5)
    newwindow1 = Button(master2, text="Ok",font=text_font, width=10 ,command=lambda:ytd4(E1.get(),private,E2.get()) )
    L1.grid(row=0,sticky=E)
    L2.grid(row=1,sticky=E)
    E1.grid(row=0,column=1)
    E2.grid(row=1,column=1)
    newwindow1.grid(row=3,column=1)
    master2.mainloop()   
def ytd4(E1,private,E2):
    key, n=private
    if(str(key)==str(E1) and str(n)==str(E2)):
        print("Success")
        ytd(data4)
    else:
        print ("THE KEY ENTERED IS INVALID ")    
B1=Button(topFrame, text ="K-anonymity",fg="white",bg="steelblue",width=20,command= lambda:ytd(k_data))
B5=Button(topFrame, text ="Generalization",fg="white",bg="steelblue",width=20,command= lambda:ytd(gen_data))
B6=Button(topFrame, text ="Suppression",fg="white",bg="steelblue",width=20,command= lambda:ytd(sup_data))
B2=Button(topFrame, text ="L-diversity",fg="white",bg="steelblue",width=20,command= lambda:ytd(data))
B3=Button(topFrame, text ="T-closeness",fg="white",bg="steelblue",width=20,command= lambda:ytd(t_data))
B4=Button(topFrame, text="Original Data",fg="white",bg="steelblue",width=20,command=lambda:ytd(data2))
B7=Button(topFrame, text="Encrypt",fg="white",bg="steelblue",width=20,command=lambda:ytd(data3))
B8=Button(topFrame, text="Decrypt",fg="white",bg="steelblue",width=20,command=lambda:ytd3())
B9=Button(topFrame, text="Micro-Aggregation",fg="white",bg="steelblue",width=20,command=lambda:ytd1())
B4.pack(side=LEFT)
B5.pack(side=LEFT)
B6.pack(side=LEFT)
B1.pack(side=LEFT)
B2.pack(side=LEFT)
B3.pack(side=LEFT)
B7.pack(side=LEFT)
B8.pack(side=LEFT)
B9.pack(side=LEFT)
top.mainloop()



with open('Cryptography.csv', 'w') as csvfile: 
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(first) 
    for i in range (0,count-1):
        csvwriter.writerow(data3[i]) 
        

with open('Micro Aggregation.csv', 'w') as csvfile: 
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(first) 
    for i in range (0,count-1):
        csvwriter.writerow(micro_data[i]) 

with open('Till_l.csv', 'w') as csvfile: 
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(first) 
    for i in range (0,count-1):
        csvwriter.writerow(data[i]) 
        
dataset1=pd.read_csv('test_test1.csv')
dataset2=pd.read_csv('Cryptography.csv')
dataset3=pd.read_csv('Micro Aggregation.csv')
dataset4=pd.read_csv('Till_l.csv')