# num = 256*256
# print("the value of i is ", num)   # the value of i is  65536

# results = [x if x%2==0 else 'TEK' for x in range(10)]  # eğer else kısmı yoksa if li kısım range den sonra yazılır
# print(results)  # 'TEK' kısmı print e girdiği için break vs yazılamaz

# dictio={
#     "araba":
#         ("a":1,"b":2)
#         ("c":3,"d":4)
# }
# aa=[]
# listeler=("a",1),("c",3)
# for items in listeler:
#     aa.append(items[1])
#     # print(aa)
#     print(type(aa))
#     # print(items[1])
#     # cc=items[1]
#     # print(cc)

# print(aa[1])
# print(aa[0])

#----------
# faculty_codes={
#     "01":"Civil Engineering",
#     "02":"Architecture",

#     "13":"Textile Technologies and Design",
#     "14":"Computer and Informatics Engineering"

# }

# kimlikNo=input("ogrenci numaranizi girin: ")
# liste =kimlikNo.split()
# print(liste)


# laptops ={
#     "brand":"Lenovo", "CPU":"Intel Core i7","RAM":"16 GB","Storage":"512 GB"
# }

# marka=input("marka adi girin: ")
# for i in laptops.values():  # key ve value ları getirir
#     print(i)
# print(f"[]")


# kelime="34ZA5839"
# print(kelime[-1].isdecimal())
# print(kelime[-1])
# print(len(kelime))


# import pickle

# #Here's an example dict
# grades = { 'Alice': 89, 'Bob': 72, 'Charles': 87 }

# #Use dumps to convert the object to a serialized string
# serial_grades = pickle.dumps( grades )
# print(serial_grades)  #  b'\x80\x04\x95#\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x05Alice\x94KY\x8c\x03Bob\x94KH\x8c\x07Charles\x94KWu.'

# #Use loads to de-serialize an object
# received_grades = pickle.loads( serial_grades )

# isim = 'Zeynep'

# def fonk():
#     global isim
#     isim += ' Aslan'
#     return isim

# print(fonk())

# Ids = ["7","2","3","4","5"]
# Ids.sort()
# # latest = int(Ids[-1]) +1
# # Ids.append(str(latest))
# latest = str( int(Ids[-1]) + 1)
# Ids.append(latest)
# print(latest)
# print(Ids)

# liste = [3,13,5,2]
# names = ["ali","ayse","zeynep","hulya"]
# sayi = 13

# for number,name in zip(liste, names):
#     if sayi==number:
#         print(f"{number} id li {name} kisisinin veriler silindi.")

# secenek = 4
# liste = [1,2,3]
# temp = False
# for i in liste:
#     if i==secenek:
#         temp=True
#         break
#     if i == liste[-1]:


# while (secenek is ( 1 or 2 or 3)):
#     print("esit")
#     break

# print(secenek not in liste)
# while secenek not in [1,2,3]:
#     print("hatali tuslama yaptiniz. tekrar deneyin.")
#     secenek = input("kullaniciyi eklemek icin 1 i, silmek icin 2 yi , sifre degistirmek icin 3 u tuslayin: ")

# print("0")

# deneme = "  ,-  merHaBA BeN zEynEp. senin adin ne"
# deneme.strip().''.join(e for e in string if e.isalnum())
# print()
# new = deneme.strip()
# neww = new.''.join(e for e in string if e.isalnum())
# print(new)
# new = ''.join(e for e in deneme if e.isalnum())
# print(deneme.isalnum())
# print(new)

# secenek = input("kullaniciyi eklemek icin 1 i, silmek icin 2 yi , sifre degistirmek icin 3 u tuslayin: ")
# secenek_list = ["1","2","3"]
# while secenek not in secenek_list:
#     print("hatali tuslama yaptiniz. tekrar deneyin.")
#     secenek = input("kullaniciyi eklemek icin 1 i, silmek icin 2 yi , sifre degistirmek icin 3 u tuslayin: ")
# print("0")
# import re

# kelime = " selam"
# print(bool(re.search("\s", kelime)))
# print(kelime.isalnum())
# kelime=kelime.strip()
# print(kelime)


# deneme = input("sifrenizi girin[4-12 karakter uzunlugunda, ozel karakter bulundurmamali, bosluk icermemelidir]: ")
#             deneme.strip()
#             if not deneme.isalnum():
#                 print("sifrenizde bosluk karakteri bulunmamalidir. lutfen talimatlara uygun sifre girisi yapin.")
#                 print(f"kalan yanlis girme hakkiniz {count-i-1}")
#                 continue
#             # if bool(re.search("\s", deneme)):
#             #     print("sifredeniz tek kelimeden olusmalidir. lutfen talimatlara uygun sifre girisi yapin.")
#             #     continue
#             if len(deneme)<4 or len(deneme)>12:
#                 print("sifre belirtilen karakter uzunlugunda olmalidir. lutfen talimatlara uygun sifre girisi yapin.")
#                 print(f"kalan yanlis girme hakkiniz {count-i-1}")
#                 continue
#             if deneme == password:
#                 temp = True
#                 break
#             if i == count - 1:
#                 print(f"{count} basarisiz giris yaptiniz. ana menuye yonlendiriliyorsunuz..")
#                 time.sleep(1)
#                 break

# import os
# filename = "mkmk-0.1.jpeg"

# # name = os.path.split(filename)[1].split(".")[0].split("-")[0]
# name = os.path.split(filename)[1].split("-")[0]
# print(name)

# Ids = ['1','10','3','9']
# Idss = ["1","10","3","9"]
# list_int = map(int, Idss)
# list_int = list(list_int)
# list_int = sorted(list_int)
# biggest_id = list_int[-1]
# print(list_int)
# print(biggest_id)

# name = input("isim girin: ")
# if " " in name:
#     print("isimde bosluk bulunmamalidir")
#     print(name)
# if any(char.isdigit() for char in name):  # sayi iceriyor mu
#     print("isimde sayi bulunmamalidir")
#     print(name)

# face_locations = [(1,2,3),(3,5,6)]
# print(len(face_locations))


# t=int(input()) #number of test cases
# t=[1, 53, 44, 2, 5, 53]
# for _ in range(t):
#     n=int(input()) # no. of array elements
#     l=[int(x) for x in input().split()]  #array elements
#     for i in range(1,n-1):
#         if l.count(i)==2:  # using count function to count the elements
#             print(i,end=' ')
#     print()


# list1 = [1,2,3,2,1,5,6,5,5,5]
# list2=[]
# import collections
# print([item for item, count in collections.Counter(a).items() if count > 1])
# # print()
# tekrar
# a.remove(2)
# print(a)
# for i in range(len(list1)):
#     if list1[i] not in list2:
#         list2.append(list1[i])


# names = ["ali", "veli", "selami", "ali"]
# isim = "ali"
# # for name in names:
# names.remove(isim)
# print(names)



# from collections import OrderedDict

# my_list = ["ali", "veli", "selami", "ali", "veli", "asadasd"]
# name = "ali"
# my_final_list = list(OrderedDict.fromkeys(my_list))
# print(my_final_list)
# print(list(my_final_list))

# for i in my_list:
#     if i == name:
#         my_list.remove(i)

# print(my_list)

# list1 = [1,2,3,4]
# list4 = [5,6,7,8]
# list1 += list4
# print(list1)

# num = "a"
# print(num.isnumeric())

# import tkinter as tk
# # from PyQt4 import QtGui    # or PySide

# def center(toplevel):
#     toplevel.update_idletasks()

#     # Tkinter way to find the screen resolution
#     screen_width = toplevel.winfo_screenwidth()
#     screen_height = toplevel.winfo_screenheight()

#     # PyQt way to find the screen resolution
#     # app = QtGui.QApplication([])
#     # screen_width = app.desktop().screenGeometry().width()
#     # screen_height = app.desktop().screenGeometry().height()

#     size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
#     x = screen_width/2 - size[0]/2
#     y = screen_height/2 - size[1]/2

#     toplevel.geometry("+%d+%d" % (x, y))
#     toplevel.title("Centered!")

# if __name__ == '__main__':
#     root = tk.Tk()
#     root.title("Not centered")

#     win = tk.Toplevel(root)
#     center(win)

#     root.mainloop()

# x,y,z,t=1,2,3,4
# myTuple=[(x,y,z,t)]
# # myTuple=[myTuple]
# print(myTuple)


# val = "12"
# print(val.isnumeric())

# info_add = "* ekranın karşında 1 kişi olmalı *\n* isimde sayı olmamalı *\n* 3 adet resim çekilecektir *"
# print(info_add)

# from collections import OrderedDict

# known_face_names = ['zeynep', 'zeynep', 'zeynep', 'ali', 'ali', 'ali']
# name_list = []
# name_list = list(OrderedDict.fromkeys(known_face_names))
# print(name_list)



# import cv2
# import time

# if __name__ == '__main__' :

#     # Start default camera
#     video = cv2.VideoCapture(0)

#     # Find OpenCV version
#     (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

#     # With webcam get(CV_CAP_PROP_FPS) does not work.
#     # Let's see for ourselves.

#     if int(major_ver)  < 3 :
#         fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
#         print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
#     else :
#         fps = video.get(cv2.CAP_PROP_FPS)
#         print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

#     # Number of frames to capture
#     num_frames = 120

#     print("Capturing {0} frames".format(num_frames))

#     # Start time
#     start = time.time()

#     # Grab a few frames
#     for i in range(0, num_frames) :
#         ret, frame = video.read()

#     # End time
#     end = time.time()

#     # Time elapsed
#     seconds = end - start
#     print ("Time taken : {0} seconds".format(seconds))

#     # Calculate frames per second
#     fps  = num_frames / seconds
#     print("Estimated frames per second : {0}".format(fps))

#     # Release video
#     video.release()

# import time

# start = time.time()
# for i in range(10000):
#     print("#######")
#     if (time.time()-start)>3:
#         print("bitti")
#         break
# print(start)
# seconds = time.time()-start
# print(seconds)


# import numpy as np

# A = np.array([[90, 80, 40],
#               [90, 60, 80],
#               [60, 50, 70],
#               [30, 40, 70],
#               [30, 20, 90]])

# ones = np.ones([5, 5])
# deviation = A - (ones.dot(A) / len(A))
# covariance = deviation.T.dot(deviation)
# print(covariance)

# matrix = np.eye(3, dtype=int)
# print(matrix)


# liste = [1,2,3,4,5,6,7,8]

# tuplee = (x for x in liste)
# # tupleee = ()
# tupleee = liste[3], liste[4], liste[5]
# print(tupleee)

# from numpy import array
# from numpy.linalg import norm
# arr = array([-1, -2, 3, 4, -5])
# print(arr)
# norm_l1 = norm(arr, 1)
# print(norm_l1)



# Str = "this is string example....wow!!!"
# Str = Str.encode('base64')

# print("Encoded String: ", Str)
# print("Decoded String: " + Str.decode('base64','strict'))

# x = 5
# print(callable(x))  #  False

# def testFunction():
#   print("Test")

# y = testFunction
# print(callable(y))  #  True



# class Foo:
#   def __call__(self):
#     print('Print Something')

# print(callable(Foo))  #  True

# import numpy as np
# # import matplotlib.pyplot as plt

# zline = np.linspace(0, 15, 1000)
# # print(zline)
# xline = np.sin(zline)
# print(xline)

# str_list = ["", "sdgf","sfdgvs","sdf"]
# isthere = filter("", str_list)
# print(isthere.__next__())
# for f in isthere:
#     print(f)
# isThereEmptyValue = [True if x != "" else False for x in str_list]    

# print(isThereEmptyValue)

# keypoints=[_ for _ in range(17)]
# rightCommonList = keypoints[2:5]
# print(rightCommonList)
# leftCommonList = keypoints[9:12]
# print(leftCommonList)
# otherCommonList = [x for x in keypoints if x not in rightCommonList or leftCommonList]
# otherCommonList = [x if x not in rightCommonList or x not in leftCommonList else "q" for x in keypoints]
# results = [x if x % 2 == 0 else 'TEK' for x in range(10)]

# otherCommonList = []
# for fruit in keypoints:
#     if fruit not in rightCommonList:
#         if fruit not in leftCommonList:
#             otherCommonList.append(fruit)
# otherCommonList=rightCommonList+leftCommonList
# print(otherCommonList)

# a = ['apple', 'carrot', 'lemon']
# b = ['pineapple', 'apple', 'tomato']

# # This gives us: new_list = ['carrot' , 'lemon']
# new_list = [fruit for fruit in a if fruit not in b]
# print(new_list)


"""
# Python3 program for the above approach
import math

# Function to find the angle
# between the two lines
def calculateAngle(x1, y1, z1,
				x2, y2, z2,
				x3, y3, z3):
						
	# Find direction ratio of line AB
	ABx = x1 - x2
	ABy = y1 - y2
	ABz = z1 - z2

	# Find direction ratio of line BC
	BCx = x3 - x2
	BCy = y3 - y2
	BCz = z3 - z2

	# Find the dotProduct
	# of lines AB & BC
	dotProduct = (ABx * BCx +
				ABy * BCy +
				ABz * BCz)

	# Find magnitude of
	# line AB and BC
	magnitudeAB = (ABx * ABx +
				ABy * ABy +
				ABz * ABz)
	magnitudeBC = (BCx * BCx +
				BCy * BCy +
				BCz * BCz)

	# Find the cosine of
	# the angle formed
	# by line AB and BC
	angle = dotProduct
	angle /= math.sqrt(magnitudeAB *
					magnitudeBC)

	# Find angle in radian
	angle = (angle * 180) / 3.14

	# Print angle
	print(round(abs(angle), 4))

# Driver Code
if __name__=='__main__':

	# Given coordinates
	# Points A
	x1, y1, z1 = 1, 3, 3

	# Points B
	x2, y2, z2 = 3, 4, 5

	# Points C
	x3, y3, z3 = 5, 6, 9

	# Function Call
	calculateAngle(x1, y1, z1,
				x2, y2, z2,
				x3, y3, z3)
"""
# import numpy as np
# B = np.arange(2*3*4).reshape((2,3,4))
# A = np.arange(2*3*4).reshape((2,3,4))
# c=A+B
# print(c[0][0][1])


# import pyqtgraph.opengl as gl
# from PyQt4.Qt import QApplication

# class MyGLView(gl.GLViewWidget):
#     def __init__(self, text):
#         super(MyGLView, self).__init__()
#         self.text = text

#     def setText(self, text):
#         self.text = text
#         self.update()

#     def paintGL(self, *args, **kwds):
#         gl.GLViewWidget.paintGL(self, *args, **kwds)
#         self.renderText(0, 0, 0, self.text)


# app = QApplication([])
# w = MyGLView(text="O HAI World")
# w.show()


# from pyqtgraph.Qt import QtGui, QtCore
# import sys
 
 
# class Second(QtGui.QMainWindow):
#     def __init__(self, parent=None):
#         super(Second, self).__init__(parent)
 
 
# class First(QtGui.QMainWindow):
#     def __init__(self, parent=None):
#         super(First, self).__init__(parent)
#         self.pushButton = QtGui.QPushButton("click me")
 
#         self.setCentralWidget(self.pushButton)
 
#         self.pushButton.clicked.connect(self.on_pushButton_clicked)
#         self.dialog = Second(self)
 
#     def on_pushButton_clicked(self):
#         self.dialog.show()
 
 
# def main():
#     app = QtGui.QApplication(sys.argv)
#     main = First()
#     main.show()
#     sys.exit(app.exec_())
 
# if __name__ == '__main__':
#     main()

# import numpy as np

# a = np.array([32.49, -39.96,-3.86])
# b = np.array([31.39, -39.28, -4.66])
# c = np.array([31.14, -38.09,-4.49])
# print(type(a))
# ba = a - b
# bc = c - b

# cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
# angle = np.arccos(cosine_angle)

# print(np.degrees(angle))

# x = namedTuple()


# Python3 program for the above approach
# import math


# def calculateAngle(rightArmPoint, leftArmPoint):
						
# 	rABx = rightArmPoint[0][0] - rightArmPoint[1][0]
# 	rABy = rightArmPoint[0][1] - rightArmPoint[1][1]
# 	rABz = rightArmPoint[0][2] - rightArmPoint[1][2]

# 	rBCx = rightArmPoint[2][0] - rightArmPoint[1][0]
# 	rBCy = rightArmPoint[2][1] - rightArmPoint[1][1]
# 	rBCz = rightArmPoint[2][2] - rightArmPoint[1][2]

# 	rdotProduct = (rABx * rBCx +
# 				rABy * rBCy +
# 				rABz * rBCz)

# 	rmagnitudeAB = (rABx * rABx +
# 				rABy * rABy +
# 				rABz * rABz)
# 	rmagnitudeBC = (rBCx * rBCx +
# 				rBCy * rBCy +
# 				rBCz * rBCz)

# 	rangle = rdotProduct
# 	rangle /= math.sqrt(rmagnitudeAB *
# 					rmagnitudeBC)

# 	rangle = (rangle * 180) / 3.14


# 	ranglee = "SAĞ KOL ACISI: %.2f" % (round(abs(Rangle), 4))

# 	# -----------------------------------------------

# 	lABx = leftArmPoint[0][0] - leftArmPoint[1][0]
# 	lABy = leftArmPoint[0][1] - leftArmPoint[1][1]
# 	lABz = leftArmPoint[0][2] - leftArmPoint[1][2]

# 	lBCx = leftArmPoint[2][0] - leftArmPoint[1][0]
# 	lBCy = leftArmPoint[2][1] - leftArmPoint[1][1]
# 	lBCz = leftArmPoint[2][2] - leftArmPoint[1][2]

# 	ldotProduct = (lABx * lBCx +
# 				lABy * lBCy +
# 				lABz * lBCz)

# 	lmagnitudeAB = (lABx * lABx +
# 				lABy * lABy +
# 				lABz * lABz)
# 	lmagnitudeBC = (lBCx * lBCx +
# 				lBCy * lBCy +
# 				lBCz * lBCz)

# 	langle = ldotProduct
# 	langle /= math.sqrt(lmagnitudeAB * lmagnitudeBC)

# 	langle = (langle * 180) / 3.14

# 	langlee = "SOL KOL ACISI: %.2f" % (round(abs(langle), 4))

# 	return ranglee, langlee


# if __name__=='__main__':

# 	rangle, langle = calculateAngle(rightArmPoint, leftArmPoint)

# import numpy as np

# import arcpy
# import math

# def GetAngle (p1, p2):
#     x1, y1 = p1
#     x2, y2 = p2
#     dX = x2 - x1
#     dY = y2 - y1
#     rads = math.atan2 (-dY, dX) #wrong for finding angle/declination?
#     return math.degrees (rads)

# def LineToXYs (line): #return first and last coordinates
#     firstX, firstY = (line.firstPoint.X, line.firstPoint.Y)
#     lastX, lastY = (line.lastPoint.X, line.lastPoint.Y)
#     return [(firstX, firstY), (lastX, lastY)]

# def AngleFromLines (lines):
#     #lines is a python list of line geometries that share a vertex
#     for line1 in lines:
#         for line2 in lines:
#             if line1 == line2:
#                 continue
#             line1StPnt, line1EndPnt = LineToXYs (line1) #get start and end xys for first line
#             line2StPnt, line2EndPnt  = LineToXYs (line2) #get start and end xys for second line
#             angle1 = GetAngle (line1StPnt, line1EndPnt) #calc angle - Doesn't work
#             angle2 = GetAngle (line2StPnt, line2EndPnt) #calc angle - Doesn't work
#             print("first line start and end coordinates:", line1StPnt, line1EndPnt)
#             print("second line start and end coordinates:", line2StPnt, line2EndPnt)
#             # print "angle 1:", angle1
#             # print "angle 2:", angle2
#             # print "length 1:", line1.length
#             # print "length 2:", line2.length
#             angle = abs (angle1 - angle2)
#             print("angle between lines:", angle)

# AngleFromLines ([lineGeom1, lineGeom2]) #lineGeom* = arcpy polyline geometry object

import numpy as np

a = np.array([356, 83])
b = np.array([356, 177])
c = np.array([356, 240])

ba = a - b
bc = c - b

cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
angle = np.arccos(cosine_angle)

print(np.degrees(angle))