# 
# This script is to be ran at the root of mmsegmentation/
#

import re
import subprocess

models = [
    ["icnet", "icnet_r18-d8_4xb2-80k_cityscapes-832x832"],
    ["bisenetv2", "bisenetv2_fcn_4xb4-160k_cityscapes-1024x1024"],
    ["stdc", "stdc2_in1k-pre_4xb12-80k_cityscapes-512x1024"],
    ["ddrnet", "ddrnet_23-slim_in1k-pre_2xb6-120k_cityscapes-1024x1024"],
    ["pidnet", "pidnet-s_2xb6-120k_1024x1024-cityscapes"],
]

# e.g. INFO - Iter(test) [500/500]    aAcc: 95.6000  mIoU: 73.2100  mAcc: 81.8100  data_time: 0.0263  time: 0.0540"
test_pattern = re.compile(r"aAcc:\s*([\d\.]+)\s+mIoU:\s*([\d\.]+)\s+mAcc:\s*([\d\.]+)")

for model_folder, model_name in models:
    config_path = f"configs/{model_folder}/{model_name}.py"
    checkpoint_path = f"checkpoints/{model_name}.pth"

    # test.py
    test_cmd = [
        "python",
        "tools/test.py",
        config_path,
        checkpoint_path
    ]
    test_result = subprocess.run(test_cmd, capture_output=True, text=True)
    
    # Parse iMoU and accuracy metrics
    match_test = test_pattern.search(test_result.stdout)
    if not match_test:
      raise Exception(f"Failed to parse test results on {model_folder}: {test_result.stdout}") 
        
    aAcc, mIoU, mAcc = match_test.groups()

    # Print the summarised metrics
    print(f"{model_folder} | mIoU: {mIoU} | mAcc: {mAcc}")
