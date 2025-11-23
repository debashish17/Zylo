#!/usr/bin/env python3
"""
GPU Verification Script for TescoCreate AI
Tests CUDA availability and GPU performance
"""

import sys

def test_gpu():
    print("🔍 Testing GPU Configuration...")
    print("=" * 60)

    # Test 1: Check if PyTorch is installed
    try:
        import torch
        print("✅ PyTorch installed:", torch.__version__)
    except ImportError:
        print("❌ PyTorch not installed")
        print("   Install with: pip install torch torchvision")
        return False

    # Test 2: Check CUDA availability
    cuda_available = torch.cuda.is_available()
    print(f"{'✅' if cuda_available else '❌'} CUDA available:", cuda_available)

    if not cuda_available:
        print("\n⚠️  GPU not detected. Running on CPU.")
        print("   This is fine for development, but ML will be slower.")
        print("\nTo enable GPU:")
        print("   1. Install CUDA Toolkit 12.1 from NVIDIA")
        print("   2. Install cuDNN")
        print("   3. Reinstall PyTorch with CUDA support:")
        print("      pip install torch==2.2.0+cu121 torchvision==0.17.0+cu121 --index-url https://download.pytorch.org/whl/cu121")
        return True  # Not an error, just running on CPU

    # Test 3: Get GPU details
    print(f"✅ CUDA version: {torch.version.cuda}")
    print(f"✅ GPU device: {torch.cuda.get_device_name(0)}")
    print(f"✅ GPU memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB")

    # Test 4: Run simple GPU operation
    try:
        print("\n🧪 Testing GPU operation...")
        x = torch.rand(1000, 1000).cuda()
        y = torch.rand(1000, 1000).cuda()
        z = x @ y  # Matrix multiplication on GPU
        print("✅ GPU computation successful!")

        # Benchmark
        import time
        start = time.time()
        for _ in range(100):
            z = x @ y
        torch.cuda.synchronize()
        gpu_time = time.time() - start

        # CPU benchmark
        x_cpu = x.cpu()
        y_cpu = y.cpu()
        start = time.time()
        for _ in range(100):
            z_cpu = x_cpu @ y_cpu
        cpu_time = time.time() - start

        speedup = cpu_time / gpu_time
        print(f"✅ GPU speedup: {speedup:.1f}x faster than CPU")

    except Exception as e:
        print(f"❌ GPU operation failed: {e}")
        return False

    print("\n" + "=" * 60)
    print("🎉 GPU is ready for ML model inference!")
    print(f"   Expected performance improvements:")
    print(f"   - Background removal: ~{speedup:.0f}x faster")
    print(f"   - YOLO detection: ~{speedup:.0f}x faster")
    print(f"   - NLP inference: ~{speedup:.0f}x faster")

    return True

if __name__ == "__main__":
    success = test_gpu()
    sys.exit(0 if success else 1)
