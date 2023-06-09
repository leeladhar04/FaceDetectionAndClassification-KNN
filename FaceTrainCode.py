import cv2
import numpy as np

cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

skip=0
face_data=[]
# face_section=[]
dataset_path='data'

# file_name=input("Enter the file name ")
while True:

	ret,frame=cap.read()

	if ret==False:
		continue

	gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	cv2.imshow("Frame",frame)
	faces=face_cascade.detectMultiScale(frame,1.3,5)
	faces=sorted(faces,key=lambda f:f[2]*f[3])

	for face in faces[-1:]:
		x,y,w,h=face
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

		#Extract required part of the face
		offset=10
		face_section=frame[y-offset:y+h+offset,x-offset:x+w+offset]
		face_section=cv2.resize(face_section,(100,100))


		#store every 10th face
		skip+=1
		if(skip%10==0):
			face_data.append(face_section)
			print(len(face_data))

	cv2.imshow("Frame",frame)
	# cv2.imshow("face_section",face_section)

	key_pressed=cv2.waitKey(1) & 0xFF
	if key_pressed==ord('q'):
		break
face_data=np.asarray(face_data)
face_data=face_data.reshape((face_data.shape[0],-1))
print(face_data.shape)

np.save('name.npy',face_data)
print("Data successfully saved ")

cap.release()
cv2.destroyAllWindows()
