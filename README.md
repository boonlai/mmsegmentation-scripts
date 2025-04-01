# MMSegmentation Scripts
To accompany COMP-6011 Task 1. All scripts are to be ran at the root of `mmsegmentation/`.

## Data Processing

- `crop.py`
  - For cropping SydneyScapes dataset to 2:1 ratio
  - Ensure that the dataset has been extracted to `data/sydneyscapes` before running this script

## Test and Benchmarking

- `test.py`
  - Batch test models for mIoU and mean accuracy
- `bench.py`
  - Batch benchmarks models for FPS
