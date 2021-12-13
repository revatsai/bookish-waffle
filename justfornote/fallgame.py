import cv2
import numpy as np
import mediapipe as mp
import time

mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils # 畫圖工具
mpDraw = mp_drawing.DrawingSpec(thickness=1, circle_radius=0) # style

cap = cv2.VideoCapture(0)
fps = [0] * 30 # 顯示的fps為30個畫面的fps

class Object:
    def __init__(self, size=50):
        self.logo_org = cv2.imread('static/imgs/fallgame.jpeg')
        self.size = size
        self.logo = cv2.resize(self.logo_org, (size, size))
        img2gray = cv2.cvtColor(self.logo, cv2.COLOR_BGR2GRAY)
        _, logo_mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
        self.logo_mask = logo_mask
        self.speed = 15
        self.x = 100
        self.y = 0
        self.score = 0

    def insert_object(self, frame):
        roi = frame[self.y:self.y + self.size, self.x:self.x + self.size]
        roi[np.where(self.logo_mask)] = 0 # np.where(self.logo_mask)輸出滿足條件 (即非0) 元素的座標(logo的座標)
        roi += self.logo

    def update_position(self, tresh, pose_landmarks): # 丟進畫面相減的圖像
        h, w, _ = tresh.shape # 跟畫面一樣
        self.y += self.speed
        if self.y + self.size > h:
            self.y = 0
            self.x = np.random.randint(0, w - self.size - 1)
            self.score += 1
            self.speed += 1

        check = False
        for point in pose_landmarks:
            if int(point.x * w) >= self.x and int(point.x * w) <= (self.x + self.size) and (point.y * h) < (self.y+ self.size):
                self.y = 0
                self.x = np.random.randint(0, w - self.size - 1)
                check = True
                self.score -= 1
                break

        return check


obj = Object()

# This is where the game loop starts
with mp_holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) as holistic:
    while True:
        _, frame = cap.read()
        begin_time = time.time() # 計算FPS
        frame = cv2.flip(frame, 1)

        results = holistic.process(frame) # 模型識別

        try:
            hit = obj.update_position(frame, results.pose_landmarks.landmark)
            obj.insert_object(frame)

            if hit:
                frame[:, :, :] = 255

            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS, mpDraw, mpDraw)

            fps.append(1 / (time.time() - begin_time))
            fps = fps[1:]
            text = 'FPS:{:.2f}'.format(sum(fps) / len(fps)) # 計算設定畫面數的fps
            cv2.putText(frame, text, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1.4, (0, 255, 255), 1)

            text = f"Score: {obj.score}"
            cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
            cv2.imshow("Webcam", frame)
        except:continue

        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
