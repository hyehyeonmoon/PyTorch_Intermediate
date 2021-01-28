import torch
import torch.nn as nn


class ConvolutionBlock(nn.Module):

    def __init__(self, in_channels, out_channels):
        self.in_channels = in_channels
        self.out_channels = out_channels

        super().__init__()

        self.layers = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, (3, 3), padding=1),
            #(N, C=in_channels, H, W)->filter (N, FN=out_channels, FH=3, FW)=3 ->(N, FN, OH, OW)
            nn.ReLU(),
            nn.BatchNorm2d(out_channels), #FC layer는 out_shape이 들어갔다면, Convolutional latey는 out_channels가 들어가야 함
            nn.Conv2d(out_channels, out_channels, (3, 3), stride=2, padding=1),
            #(N, FN=out_channels, OH, OW)->filter (N, FN=out_channels, 3, 3)->(N, FN=out_channels, OH/2, OW/2)
            nn.ReLU(),
            nn.BatchNorm2d(out_channels),
        )

    def forward(self, x):
        # |x| = (batch_size, in_channels, h, w)

        y = self.layers(x)
        #|y|=(batch_size, out_channels, oh/2, ow/2)

        return y


class ConvolutionalClassifier(nn.Module):

    def __init__(self, output_size):
        self.output_size = output_size

        super().__init__()

        self.blocks = nn.Sequential( # |x| = (n, 1, 28, 28) #CNN은 이미지의 입력 크기를 미리 지정해야 하고, 이미지의 입력이 달라지면 sequential도 수동적으로 고쳐줘야 함
            ConvolutionBlock(1, 32), # (n, 32, 14, 14)
            ConvolutionBlock(32, 64), # (n, 64, 7, 7)
            ConvolutionBlock(64, 128), # (n, 128, 4, 4)
            ConvolutionBlock(128, 256), # (n, 256, 2, 2) #4에서 2가 되는 것은 직접 계산해 보면 알 수 있음
            ConvolutionBlock(256, 512), # (n, 512, 1, 1)
        )
        self.layers = nn.Sequential(
            nn.Linear(512, 50),
            nn.ReLU(),
            nn.BatchNorm1d(50),
            nn.Linear(50, output_size),
            nn.LogSoftmax(dim=-1),
        )

    def forward(self, x):
        assert x.dim() > 2 #convolution layer에 들어가므로 dimension이 2차원이면 안됨

        if x.dim() == 3:
            # |x| = (batch_size, h, w)
            x = x.view(-1, 1, x.size(-2), x.size(-1))
        # |x| = (batch_size, 1, h, w)

        z = self.blocks(x)
        # |z| = (batch_size, 512, 1, 1)

        y = self.layers(z.squeeze())
        # |y| = (batch_size, output_size)=(n, 512)

        return y
