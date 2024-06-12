import cv2
import os

# 视频文件路径
video_path = 'test2.mp4'
# 帧保存目录
frame_dir = 'frames'

# 创建保存帧的目录
if not os.path.exists(frame_dir):
    os.makedirs(frame_dir)

# 打开视频文件
cap = cv2.VideoCapture(video_path)
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_path = os.path.join(frame_dir, f'frame_{frame_count:04d}.jpg')
    cv2.imwrite(frame_path, frame)
    frame_count += 1

cap.release()
print(f'Total frames: {frame_count}')
