import gradio as gr
import os
import torch

from model import create_model
from timeit import default_timer as timer
from typing import Tuple, Dict

with open('class_names.txt','r') as f:
    class_names = [food.strip() for food in f.readlines()]
    
effnetb2_model, efficientnet_b2_transforms = create_model()

effnetb2_model.load_state_dict(
    torch.load(f='effnetb2_model.pth'),
    map_location=torch.device('cpu'),
)

def predict(img) -> Tuple[Dict,float]:
    start_time = timer()
    
    img = efficientnet_b2_transforms(img).unsqueeze(0)
    
    effnetb2_model.eval()
    with torch.inference_mode():
        pred_probs = torch.softmax(effnetb2_model(img), dim=1)
        
    pred_labels_and_probs = {class_names[i]: float(pred_probs[0][i] for i in range(len(class_names)))}
    
    end_time = timer()
    pred_time = round(end_time - start_time, 3)
    
    return pred_labels_and_probs, pred_time

title = 'FoodEye'
description = "Worried about what's on the plate, worry no more with this application!"
article = "Create using PyTorch"

example_list = [['example/' + example ] for example in os.listdir('examples/')]

gradio_app = gr.Interface(fn=predict,
                          inputs=gr.Image(type='pil'),
                          outputs=[gr.Label(num_top_classes=5, label='Predictions'),
                                   gr.Number(label='Prediction Time in seconds')],
                          examples=example_list,
                          title=title,
                          description=description,
                          article=article)

gradio_app.launch()