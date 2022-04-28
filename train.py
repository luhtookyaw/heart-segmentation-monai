import torch
import argparse
from monai.networks.nets import UNet
from monai.networks.layers import Norm
from monai.losses import DiceLoss, DiceCELoss
from utilities import prepare, train


parser = argparse.ArgumentParser()
parser.add_argument("-d", "--data", type=str, help="Directory for Data")
parser.add_argument("-m", "--model", type=str, help="Directory for model")

data_dir = parser.parse_args().data
model_dir = parser.parse_args().model
data_in = prepare(data_dir, a_min=0, a_max=1435.2, cache=True)

device = torch.device("cuda:0")
model = UNet(
    dimensions=3,
    in_channels=1,
    out_channels=2,
    channels=(16, 32, 64, 128, 256), 
    strides=(2, 2, 2, 2),
    num_res_units=2,
    norm=Norm.BATCH,
).to(device)


#loss_function = DiceCELoss(to_onehot_y=True, sigmoid=True, squared_pred=True, ce_weight=calculate_weights(1792651250,2510860).to(device))
loss_function = DiceLoss(to_onehot_y=True, sigmoid=True, squared_pred=True)
optimizer = torch.optim.Adam(model.parameters(), 1e-5, weight_decay=1e-5, amsgrad=True)

if __name__ == '__main__':
    train(model, data_in, loss_function, optimizer, 600, model_dir)