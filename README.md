# AffectNet Facial Emotion Recognition (EfficientNet-B0)

This repo contains a Google Colab notebook that trains a **Facial Emotion Recognition (FER)** model on the **AffectNet** dataset using **transfer learning with EfficientNet-B0**.

> Note: AffectNet is **not redistributed** in this repository. You must obtain it through the official channels and place it in the expected folder structure.

---

## What’s inside

- EfficientNet-B0 (ImageNet pretrained) backbone
- Transfer learning (freeze → train head → optional fine-tuning)
- Train / validation / test pipeline
- Metrics (accuracy) + training curves
- Model saving for later inference

Main notebook:
- `affectnet_efficientnet_b0.ipynb`

---

## Dataset (AffectNet)

AffectNet is a large-scale facial expression dataset.  
You must download it separately and organize it in one of the supported formats below.

### Supported dataset formats

#### Format A: Folder-per-class (recommended)
