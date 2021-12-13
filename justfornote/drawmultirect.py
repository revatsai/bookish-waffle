# -*- coding: utf-8 -*-

import cv2
import numpy as np
import mediapipe as mp
import time

mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils
mpDraw = mp_drawing.DrawingSpec(thickness=1, circle_radius=0)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

class Object:
	def __init__(self, size = 200):
		gc = np.zeros((100, 100, 3), np.uint8)
		# gc.fill(0)
		self.rectangle = cv2.rectangle(gc, (3, 3), (97, 97), (255, 0, 0), 3)
		self.size = size
		self.rec_resize = cv2.resize(self.rectangle, (size, size))
		img2gray = cv2.cvtColor(self.rec_resize, cv2.COLOR_BGR2GRAY)
		success, rec_mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
		self.rec_mask = rec_mask      
		self.init_x = np.random.randint(0, width - self.size -1)
		self.init_y = np.random.randint(0, height - self.size -1)
		self.score = 0
		
	def insert_object(self, myRectangle):
		roi = myRectangle[self.init_y: self.init_y + self.size, self.init_x: self.init_x + self.size]
		roi[np.where(self.rec_mask)] = 0
		roi += self.rec_resize

	
	

obj = Object()
time_it = time.time()

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
	while True:
		success, frame = cap.read()
		h, w, c = frame.shape
		x1, y1, x2, y2 = obj.init_x, obj.init_y, (obj.init_x + obj.size), (obj.init_y + obj.size)


		frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
		results = holistic.process(frame)
		
		
		obj.insert_object(frame)
		game_time = 15
		second = (game_time+2) - float(time.time() - time_it)
		if second > 0:
			m,s = divmod(int(second), 60)
			time_left = str(m).zfill(2) + ":" + str(s).zfill(2)
			cv2.putText(frame, time_left, (500, 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
			
			if results.right_hand_landmarks:
				x_max = 0
				y_max = 0
				x_min = w
				y_min = h
				for point in results.right_hand_landmarks.landmark:
					x, y = int(point.x * w), int(point.y * h)
					if x > x_max:
						x_max = x
					if x < x_min:
						x_min = x
					if y > y_max:
						y_max = y
					if y < y_min:
						y_min = y
				cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 0, 255), 2) # RGB
				mp_drawing.draw_landmarks(frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

				if x_min > x1 and y_min > y1 and x_max < x2 and  y_max < y2:
					obj.score += 1
					obj.init_x = np.random.randint(0, width - obj.size -1)
					obj.init_y = np.random.randint(0, height - obj.size -1)
		else:
			cv2.putText(frame, "Time's up!", (180, 220), cv2.FONT_HERSHEY_PLAIN, 4, (0, 255, 0), 2)

		frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

		

		text = f"Score: {obj.score}"
		cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)	


		cv2.imshow("Webcam", frame)

		if cv2.waitKey(1) == 27:
			break



cap.release()
cv2.destroyAllWindows()