# MMSegmentation Scripts
To accompany COMP-6011 Task 1. All scripts are to be ran at the root of `mmsegmentation/`.

## Helper Scripts

### Data Processing

- `crop.py`
  - For cropping SydneyScapes dataset to 2:1 ratio
  - Ensure that the dataset has been extracted to `data/sydneyscapes` before running this script

### Test and Benchmarking

- `test.py`
  - Batch test models for mIoU and mean accuracy
- `bench.py`
  - Batch benchmarks models for FPS

## Models

```shell
mkdir -p ./mmsegmentation/checkpoints

# ICNet
wget -O ./mmsegmentation/checkpoints/icnet_r18-d8_4xb2-80k_cityscapes-832x832.pth \
  https://download.openmmlab.com/mmsegmentation/v0.5/icnet/icnet_r18-d8_832x832_80k_cityscapes/icnet_r18-d8_832x832_80k_cityscapes_20210925_225521-2e36638d.pth

# BiSeNetV2
wget -O ./mmsegmentation/checkpoints/bisenetv2_fcn_4xb4-160k_cityscapes-1024x1024.pth \
  https://download.openmmlab.com/mmsegmentation/v0.5/bisenetv2/bisenetv2_fcn_4x4_1024x1024_160k_cityscapes/bisenetv2_fcn_4x4_1024x1024_160k_cityscapes_20210902_015551-bcf10f09.pth

# STDC (2)
wget -O ./mmsegmentation/checkpoints/stdc2_in1k-pre_4xb12-80k_cityscapes-512x1024.pth \
  https://download.openmmlab.com/mmsegmentation/v0.5/stdc/stdc2_in1k-pre_512x1024_80k_cityscapes/stdc2_in1k-pre_512x1024_80k_cityscapes_20220224_073048-1f8f0f6c.pth

# DDRNet (slim)
wget -O ./mmsegmentation/checkpoints/ddrnet_23-slim_in1k-pre_2xb6-120k_cityscapes-1024x1024.pth \
  https://download.openmmlab.com/mmsegmentation/v0.5/ddrnet/ddrnet_23-slim_in1k-pre_2xb6-120k_cityscapes-1024x1024/ddrnet_23-slim_in1k-pre_2xb6-120k_cityscapes-1024x1024_20230426_145312-6a5e5174.pth

# PIDNet (S)
wget -O ./mmsegmentation/checkpoints/pidnet-s_2xb6-120k_1024x1024-cityscapes.pth \
  https://download.openmmlab.com/mmsegmentation/v0.5/pidnet/pidnet-s_2xb6-120k_1024x1024-cityscapes/pidnet-s_2xb6-120k_1024x1024-cityscapes_20230302_191700-bb8e3bcc.pth
```