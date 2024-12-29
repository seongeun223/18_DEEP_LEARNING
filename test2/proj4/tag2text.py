"""
 * The Tag2Text Model - Simplified
"""

# STEP 1: Import modules
import torch
from PIL import Image
from ram.models import tag2text
from ram import inference_tag2text as inference
from ram import get_transform

# STEP 2: Create inference object
image_path = "images/1641173_2291260800.jpg"
model_path = "pretrained/tag2text_swin_14m.pth"
image_size = 384
threshold = 0.68
specified_tags = "None"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
transform = get_transform(image_size=image_size)

# STEP 3: Load data
image = transform(Image.open(image_path)).unsqueeze(0).to(device)

# STEP 4: Inference
delete_tag_index = [127, 2961, 3351, 3265, 3338, 3355, 3359]
model = tag2text(
    pretrained=model_path,
    image_size=image_size,
    vit="swin_b",
    delete_tag_index=delete_tag_index,
)
model.threshold = threshold
model.eval()
model = model.to(device)
res = inference(image, model, specified_tags)

# STEP 5: Post-processing
print("Model Identified Tags: ", res[0])
print("User Specified Tags: ", res[1])
print("Image Caption: ", res[2])
