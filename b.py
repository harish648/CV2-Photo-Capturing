import cv2
from tkinter import *
root = Tk()
root.title('Camera')

cap=cv2.VideoCapture(0)

while(True):
		ret,frame=cap.read() #ret is used for booleann whereas the frame is used for capturing the image 
		

		if cv2.waitKey(1) & 0xFF== ord('q'):
			break
		cv2.imshow("capture",frame)
cap.release()
cv2.destroyAllWindows()

def capture():
	cv2.imwrite('a.jpg',frame)

button_photo=Button(root,text='Photo',padx=40,pady=20,command=capture)
button_photo.grid(row=1,column=2)

root.mainloop()
