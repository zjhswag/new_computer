import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

# 加载预训练的ResNet50模型，并移除最后的全连接层
model = models.resnet50(pretrained=True)
model = torch.nn.Sequential(*list(model.children())[:-1])  # 移除全连接层

# 图像预处理
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

i = 0


def extract_features(image_path):
    global i
    print(f'处理第{i}帧')
    i += 1
    image = Image.open(image_path)
    image = preprocess(image)
    image = image.unsqueeze(0)  # 添加批量维度
    with torch.no_grad():
        features = model(image)
    return features.squeeze().numpy()
