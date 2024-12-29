# step0 : prepare
# 1. install git
# 2. install package : pip install git+https://github.com/xinyu1205/recognize-anything.git
# 3. model download : https://huggingface.co/xinyu1205/recognize-anything-plus-model/resolve/main/ram_plus_swin_large_14m.pth

# STEP 1: Import modules
import numpy as np
import random
import torch
from PIL import Image
from ram.models import ram_plus
from ram import inference_ram as inference
from ram import get_transform

image_path = "images/demo/demo1.jpg"
model_path = "ram_plus_swin_large_14m.pth"

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
transform = get_transform(image_size=384)

# STEP 2: Create inference object
model = ram_plus(pretrained=model_path,
                            image_size=384,
                            vit='swin_l')
model.eval()
model = model.to(device)

image_path = 'images/demo/demo1.jpg'
transform = get_transform(image_size=384)
image = transform(Image.open(image_path)).unsqueeze(0).to(device)

# step4 : inference
res = inference(image, model)

# step5 : 
print("Image Tags: ", res[0])
print("图像标签: ", res[1])