import cv2
from fer import FER

# 初始化摄像头
cap = cv2.VideoCapture(0)

# 初始化 FER 情绪识别
detector = FER(mtcnn=True)

while True:
    # 读取摄像头画面
    ret, frame = cap.read()
    if not ret:
        break

    # 进行情绪识别
    result = detector.detect_emotions(frame)

    # 在画面中绘制情绪识别结果
    for face in result:
        (x, y, w, h) = face["box"]
        emotions = face["emotions"]
        dominant_emotion = max(emotions, key=emotions.get)

        # 绘制面部矩形框
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # 在面部矩形框上方绘制情绪标签
        cv2.putText(frame, dominant_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

    # 显示结果
    cv2.imshow('Real-time Emotion Recognition', frame)

    # 按下 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头并关闭所有窗口
cap.release()
cv2.destroyAllWindows()
