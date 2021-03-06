import cv2
import numpy

#events =[i for i in dir(cv2) if 'EVENT' in i]
#print(events)
"""
['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 
'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 
'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 
'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 
'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 
'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']
"""

def clickEvent(event_name,x,y,flags,param):
	if(event_name==cv2.EVENT_LBUTTONDOWN):

		cv2.putText(img,str(x)+','+str(y),(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,100,100),3,cv2.LINE_AA)
		#frame,text,coordinate,font,fontscale,color,thickness,linetype
		cv2.imshow('FrameTitle',img)

	if(event_name==cv2.EVENT_RBUTTONDOWN):
		cv2.putText(img,str(img[y,x,0])+','+str(img[y,x,1])+','+str(img[y,x,2]),(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,100,100),1,cv2.LINE_AA)
		#puts blue green and red color
		cv2.imshow('FrameTitle',img)

img=numpy.zeros((512,512,3),numpy.uint8)
cv2.imshow('FrameTitle',img)
cv2.setMouseCallback('FrameTitle',clickEvent)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('/Users/newmac/Documents/GayatriBasude/Python/OpenCV/MouseEventImg.jpg',img)

