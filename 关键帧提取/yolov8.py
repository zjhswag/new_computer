import cv2
from ultralytics import YOLO

# 加载预训练的YOLOv8模型
model = YOLO('yolov8n.pt')

# 打开摄像头
cap = cv2.VideoCapture(0)  # 参数0表示使用默认摄像头

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

window_name = 'YOLOv8 Real-Time Detection'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 1280, 720)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    # 对帧进行推理
    results = model(frame)

    # 在帧上绘制检测结果
    annotated_frame = results[0].plot()

    # 显示结果
    cv2.imshow('YOLOv8 Real-Time Detection', annotated_frame)

    # 按q键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
