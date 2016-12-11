import cv2
import numpy as np
import math
import copy

cap = cv2.VideoCapture(0)
traillist = []
pointlist = []
minyx = 0
drawlist = []
#Drawing setting variables
size = 5
red = 0
gre = 128
blu = 0
sel = 0
mode = 1
options = ["Size", "Red", "Green", "Blue"]
modes = ["Draw", "Trails"]
while(cap.isOpened()):
    miny = 99999
    ret, img = cap.read()
    cv2.rectangle(img,(300,300),(100,100),(0,255,0),0)
    crop_img = img[100:300, 100:300]
    grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    value = (35, 35)
    blurred = cv2.GaussianBlur(grey, value, 0)
    _, thresh1 = cv2.threshold(blurred, 127, 255,
                               cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    cv2.imshow('Thresholded', thresh1)

    version = 2

    #if version is '3':
        #image, contours, hierarchy = cv2.findContours(thresh1.copy(), \
               #cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #elif version is '2':
    contours, hierarchy = cv2.findContours(thresh1.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cnt = max(contours, key = lambda x: cv2.contourArea(x))
    
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(crop_img,(x,y),(x+w,y+h),(0,0,255),0)
    hull = cv2.convexHull(cnt)
    drawing = np.zeros(crop_img.shape,np.uint8)
    cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
    cv2.drawContours(drawing,[hull],0,(0,0,255),0)
    hull = cv2.convexHull(cnt,returnPoints = False)
    defects = cv2.convexityDefects(cnt,hull)
    count_defects = 0
    cv2.drawContours(thresh1, contours, -1, (0,255,0), 3)
  
  
    for i in range(defects.shape[0]):
	
        s,e,f,d = defects[i,0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
	pointlist.append(far)
        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
        if angle <= 90:
            count_defects += 1
            cv2.circle(crop_img,far,1,[0,0,255],-1)
        #dist = cv2.pointPolygonTest(cnt,far,True)
        cv2.line(crop_img,start,end,[0,255,0],2)
	#print(far, prevfar, prevfar2)
	#Main one cv2.circle(crop_img,far,5,[255,0,0],-1)

    
    for i in range (len(pointlist)):
    	miny = min(miny,pointlist[i][1])
	if miny == pointlist[i][1]:
	   	minyx = pointlist[i][0]
    holdtuple = (minyx, miny)
    traillist.append(pointlist[:])
    #Setting Keys:
    if cv2.waitKey(33) == ord('a'):
    	drawlist.append(holdtuple)
    if cv2.waitKey(33) == ord('s'):
    	del drawlist[:]
    if cv2.waitKey(33) == ord('i'):
    	if sel < 3:
		sel+=1
	else:
		sel=0
    if cv2.waitKey(33) == ord('k'):
   	if mode == 0: 
		mode = 1
	else:
	 	mode = 0
    if cv2.waitKey(33) == ord('j'):
    	if sel == 0:
		if size > 0:
			size-=1
	if sel == 1:
		if red > 0:
			red-=1
	if sel == 2:
		if gre > 0:
			gre-=1
	if sel == 3:
		if blu > 0:
			blu-=1
    if cv2.waitKey(33) == ord('l'):
   	if sel == 0:
		if size < 35:
			size+=1
	if sel == 1:
		if red < 255:
			red+=1
	if sel == 2:
		if gre < 255:
			gre+=1
	if sel == 3:
		if blu < 255:
			blu+=1

    #Draw data
    #print("Drawing points thus far", drawlist)

    #Trail data
    #print("Current trail points", traillist)

    #Drawing lopops for trails/painting:
    for i in range(len(drawlist)): #Loop for drawing 
		if mode == 0:
	   		cv2.circle(crop_img,drawlist[i],size,[blu,gre,red],-1)

    if(len(traillist)>25): #Regulates how many particles are left by trails
	traillist.pop(0)
    for i in range(len(traillist)): #Loops for trails 
    	for x in range(len(traillist[i])):
		hold = traillist[i][x]
		mod = i+1
		if mode == 1:
			cv2.circle(crop_img,hold,mod/size,[blu, gre, red],-1)
    for x in range(len(pointlist)):
		cv2.circle(crop_img,pointlist[x],size,[blu,gre,red],-1)
    del pointlist[:]
    #////////////////////////
    stats = "R: " + str(red) + " G: " + str(gre) + " B: " + str(blu) + " Size: " + str(size)
    selections = "Current option: " + options[sel] + " Current mode: " + modes[mode]
    cv2.putText(img, stats, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)
    cv2.putText(img, selections, (50,70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)
    
    #Explanation for the keys
    cv2.putText(img, "K - Switch Drawing&Trail modes", (50,340), cv2.FONT_HERSHEY_SIMPLEX, 0.6, 3)
    cv2.putText(img, "A - Draw", (50,360), cv2.FONT_HERSHEY_SIMPLEX, 0.6, 3)
    cv2.putText(img, "S - Erase the drawing", (50,380), cv2.FONT_HERSHEY_SIMPLEX, 0.6, 3)
    cv2.putText(img, "I - Change Size/ Color", (50,400), cv2.FONT_HERSHEY_SIMPLEX, 0.6, 3)
    cv2.putText(img, "J - Decrease Size/Color", (50,420), cv2.FONT_HERSHEY_SIMPLEX, 0.6, 3)
    cv2.putText(img, "L - Increase Size/Color", (50,440), cv2.FONT_HERSHEY_SIMPLEX, 0.6, 3)
 
    #////////////////////////
    #cv2.imshow('drawing', drawing)
    #cv2.imshow('end', crop_img)
    cv2.imshow('Gesture', img)
    all_img = np.hstack((drawing, crop_img))
    cv2.imshow('Contours', all_img)
    k = cv2.waitKey(10)
    if k == 27:
	break