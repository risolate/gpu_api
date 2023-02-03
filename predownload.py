import torch
from transformers import (
    T5ForConditionalGeneration,
)

model = T5ForConditionalGeneration.from_pretrained("risolate/kcT5-purificate")