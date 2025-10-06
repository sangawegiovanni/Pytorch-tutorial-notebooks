import torch
from torch.utils.data import DataLoader,Dataset

class MyDataset(Dataset):
    def __init__(self):
        self.x=torch.Tensor([[1.0],[2.0],[3.0],[4.0]])
        self.y=torch.Tensor([[1.0],[2.0],[3.0],[4.0]])

    def __len__(self):
        return len(self.x)    
    def __getitem__(self,idx):
        return self.x[idx],self.y[idx]
    
dataset=MyDataset()
dataloader=DataLoader(dataset,batch_size=2,shuffle=True)