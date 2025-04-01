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

# e.g. Overall fps: 62.39 img / s
benchmark_pattern = re.compile(r"Overall fps:\s*([\d\.]+)")

for model_folder, model_name in models:
    config_path = f"configs/{model_folder}/{model_name}.py"
    checkpoint_path = f"checkpoints/{model_name}.pth"

    # benchmark.py
    benchmark_cmd = [
        "python",
        "tools/analysis_tools/benchmark.py",
        config_path,
        checkpoint_path
    ]
    benchmark_result = subprocess.run(benchmark_cmd, capture_output=True, text=True)
    
    # Parse FPS
    match_bench = benchmark_pattern.search(benchmark_result.stdout)
    if not match_bench:
      raise Exception(f"Failed to parse benchmark results on {model_folder}: {benchmark_result.stdout}") 
    
    fps = match_bench.group(1)

    # Print the summarised metrics
    print(f"{model_folder} | fps: {fps}")
