import numpy as np
import pandas as pd
import sklearn
import torch
import transformers 
import datasets

def main():
    print("NumPy:", np.__version__)
    print("Pandas:", pd.__version__)
    print("Sklearn:", sklearn.__version__)
    print("Torch:", torch.__version__)
    print("transformers:", transformers.__version__)
    print("datasets:", datasets.__version__)

    print()
    print("CUDA available:", torch.cuda.is_available())

    if torch.cuda.is_available():
        print("GPU:", torch.cuda.get_device_name(0))
if __name__ == "__main__":
    main()
