import cv2
import numpy as np
import mediapipe as mp
import time

def flash():
    mp_holistic = mp.solutions.holistic
    mp_drawing = mp.solutions.drawing_utils # 畫圖工具
    mpDraw = mp_drawing.DrawingSpec(thickness=1, circle_radius=0) # style

    cap = cv2.VideoCapture(0)
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    class Object:
        def __init__(self, size=50, init=1, score = 0):
            if not init: # 初始化框
                gc = np.zeros((100, 100, 3), np.uint8)
                self.rectangle = cv2.rectangle(gc, (3, 3), (97, 97), (255, 0, 0), 2)
                self.size = size
                self.rec_resize = cv2.resize(self.rectangle, (size, 2*size)) # resize長寬比例
                img2gray = cv2.cvtColor(self.rec_resize, cv2.COLOR_BGR2GRAY)
                success, rec_mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
                self.rec_mask = rec_mask      
                self.x = int(0.5*w-0.5*self.size)
                self.y = int(0.5*h-0.75*self.size)
                self.score = score

            else: # 遊戲logo框
                self.logo_org = cv2.imread('static/imgs/logo_flash.png')
                self.size = size
                self.logo = cv2.resize(self.logo_org, (size, size))
                img2gray = cv2.cvtColor(self.logo, cv2.COLOR_BGR2GRAY)
                _, logo_mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
                self.logo_mask = logo_mask
                self.speed = 20
                self.x = 100
                self.y = 0
                self.score = 0

        def insert_object(self, frame, init=1):
            if not init:
                roi = frame[self.y: self.y + 2*self.size, self.x: self.x + self.size] # 調整長寬比例要跟著調
                roi[np.where(self.rec_mask)] = 0
                roi += self.rec_resize
            else:
                roi = frame[self.y:self.y + self.size, self.x:self.x + self.size]
                roi[np.where(self.logo_mask)] = 0 # np.where(self.logo_mask)輸出滿足條件 (即非0) 元素的座標(logo的座標)
                roi += self.logo

        def update_position(self, frame, pose_landmarks, init=1): # 丟進畫面相減的圖像
            if init:
                h, w, _ = frame.shape # 跟畫面一樣
                self.y += self.speed
                if self.y + self.size > h:
                    self.y = 0
                    self.x = np.random.randint(self.size, w - 2*self.size - 1) # (0, w - self.size - 1)
                    self.score += 1

                # Check for collision
                roi = frame[self.y:self.y + self.size, self.x:self.x + self.size]
                check = np.any(roi[np.where(self.logo_mask)]) # np.any()陣列中皆為0回傳False，有一個不為0就True
                check = False
                for point in pose_landmarks:
                    if int(point.x * w) >= self.x and int(point.x * w) <= (self.x + self.size) and (point.y * h) < (self.y+ self.size):
                        self.y = 0
                        self.x = np.random.randint(self.size, w - 2*self.size - 1)
                        check = True
                        self.score -= 1
                        break

                return check

    flashscore = 0
    box_w = int(0.3*w) # 校準框寬
    obj = Object(size=box_w, init=0) # 初始化物件
    time_it = time.time()
    init_time = 3 # 校準時間
    init_done = 0
    game_over = 0
    reset = 0
    score = 0 # 會不斷更新，最後要回傳這個出去

    with mp_holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) as holistic:
        while True:
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)

            results = holistic.process(frame) # 模型識別

            game_time = 60 + init_time
            second = (game_time+2) - float(time.time() - time_it)
            if second > 0 and init_done == 1: # 遊戲中顯示
                game_over = 0
                cv2.putText(frame, "Game Start", (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                m,s = divmod(int(second), 60)
                time_left = str(m).zfill(2) + ":" + str(s).zfill(2)
                cv2.putText(frame, time_left, (500, 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                score = obj.score
            elif second <= 0 : # 遊戲結束，物件轉初始化(顯示分數等於最後分數)、新增結束遊戲物件
                obj = Object(size=box_w, init=0, score=score)
                obj.x = 0
                obj.y = int(0.5*h-0.75*obj.size)
                obj_re = Object(size=box_w, init=0)
                obj_re.x = int(w-obj_re.size)
                obj_re.y = int(0.5*h-0.75*obj_re.size)
                x3, y3, x4, y4 = obj_re.x, obj_re.y, (obj_re.x + obj_re.size), (obj_re.y + obj_re.size)
                reset = 1
                game_over = 1

            try: # 用try是因為results沒有偵測到點會結束程式
                if init_done == 1 and game_over == 0: # 主遊戲
                    hit = obj.update_position(frame, results.pose_landmarks.landmark)
                    obj.insert_object(frame)
                    if hit:
                        frame[:, :, :] = 255
                elif game_over == 1: # 結束後重新計時、初始化
                    time_it = time.time()
                    init_done = 0
                    game_over = 0

                if init_done == 0 and results.pose_landmarks.landmark: # 初始化偵測
                    x1, y1, x2, y2 = obj.x, obj.y, (obj.x + obj.size), (obj.y + 2*obj.size) # 調整長寬比例要跟著調
                    x_max, y_max, x_min, y_min = 0, 0, w, h
                    for point in results.pose_landmarks.landmark:
                        x, y = int(point.x * w), int(point.y * h)
                        if x > x_max: x_max = x
                        if x < x_min: x_min = x
                        if y > y_max: y_max = y
                        if y < y_min: y_min = y
                    cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 0, 255), 2)
                    #mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS, mpDraw, mpDraw)

                    if x_min > x1 and y_min > y1 and x_max < x2 : # 不判定右下角y

                        second = (init_time +1) - float(time.time()-time_it)
                        if second > 0 and init_done == 0: # 倒數3秒的顯示
                            m,s = divmod(int(second),60)
                            time_left = 'Game start in : '+ str(s).zfill(2)
                            cv2.putText(frame, time_left, (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

                        else: # 3秒後的瞬間
                            init_done = 1
                            obj = Object()
                            continue
                    elif init_done == 0: # 結束時再顯示
                        obj.insert_object(frame, init=0)
                        if reset:
                            obj_re.insert_object(frame, init=0)
                            cv2.putText(frame, "Time's up!", (int(0.25*w), int(0.5*h)), cv2.FONT_HERSHEY_PLAIN, 4, (0, 255, 0), 3)
                            cv2.putText(frame, "Restart", (10, int(0.5*h-0.5*obj.size)), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)
                            cv2.putText(frame, "Stop", (10+int(w-obj_re.size), int(0.5*h-0.5*obj.size)), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)
                            if x_min > x3 and y_min > y3 and x_max < x4 :
                                print('game stop')
                                break
                        time_it = time.time()
                        cv2.putText(frame, "Please stand in the frame", (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                    else:
                        pass

            except:pass
            finally:
                text = f"Score: {obj.score}"
                flashscore = obj.score
                # if flashscore < 0:
                #     flashscore = 0
                cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                cv2.imshow("frame", frame)

            if cv2.waitKey(5) & 0xFF == 27:
                break

    cap.release()
    cv2.destroyAllWindows()
    return flashscore