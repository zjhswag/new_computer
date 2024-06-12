import cv2
import numpy as np
import os

from 关键帧提取.提取帧的特征 import extract_features


def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2)


def extract_keyframes(feature_vectors, distance_threshold=0.05):
    keyframes = [0]  # 选择第一个帧作为关键帧
    accumulated_distance = 0
    for i in range(1, len(feature_vectors)):
        similarity = cosine_similarity(feature_vectors[i], feature_vectors[i - 1])
        distance = 1 - similarity
        accumulated_distance += distance
        if accumulated_distance >= distance_threshold:
            keyframes.append(i)
            accumulated_distance = 0  # 重置累积距离
    return keyframes


# 提取每一帧的特征向量
frame_dir = 'frames'
frame_paths = [os.path.join(frame_dir, f) for f in sorted(os.listdir(frame_dir))]
print(len(frame_paths))

feature_vectors = [extract_features(frame) for frame in frame_paths]

# 提取关键帧的索引
keyframe_indices = extract_keyframes(feature_vectors)

# 输出关键帧
for idx in keyframe_indices:
    print(f'Keyframe: {frame_paths[idx]}')

keyframe_dir = 'key_frames'
if not os.path.exists(keyframe_dir):
    os.makedirs(keyframe_dir)

# 保存关键帧
for idx in keyframe_indices:
    keyframe_path = frame_paths[idx]
    keyframe_img = cv2.imread(keyframe_path)
    keyframe_save_path = os.path.join(keyframe_dir, os.path.basename(keyframe_path))
    cv2.imwrite(keyframe_save_path, keyframe_img)
    print(f'Saved keyframe: {keyframe_save_path}')
print(f'从{len(frame_paths)}张照片里提取出来了{len(keyframe_indices)}张关键帧')
