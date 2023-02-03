import torch
from transformers import (
    T5ForConditionalGeneration,
)
from pydantic import BaseModel

model = T5ForConditionalGeneration.from_pretrained("risolate/kcT5-purificate")