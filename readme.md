![SIMPLOT Banner](assets/banner.png)

# SIMPLOT: Enhancing Chart Question Answering by Distilling Essentials

Official implementation of [**SIMPLOT: Enhancing Chart Question Answering by Distilling Essentials**](https://arxiv.org/abs/2405.00021), accepted at **NAACL 2025 (Findings)**.

---

## 🚀 Overview

Chart interpretation with logical reasoning is a growing challenge in vision-language models. **SIMPLOT** improves chart-to-table extraction by filtering essential elements, enhancing reasoning without additional datasets or annotations.

### 🔹 Key Contributions:
- Mimics a simplified plot retaining only essential information for reasoning.
- Overcomes limitations of previous SOTA methods like DePlot.
- Introduces a novel prompt addressing ignored visual attributes (e.g., color).

<p align="center">
  <img src="assets/architecture.png" width="85%">
</p>

---

## ⚙️ Environment Setup

```bash
conda create -n Simplot python=3.8 
conda activate Simplot 
pip install -r requirements.txt
```

---

## 📂 Dataset Preparation

Download the **ChartQA** dataset from: [Hugging Face](https://huggingface.co/datasets/ahmed-masry/ChartQA)

```bash
cd data/
unzip test.zip
cd ..
python preprocess.py
```

Ensure the directory structure is:

```
data/
├── train  
│   ├── train_augmented.json 
│   ├── train_human.json   
│   ├── annotations       
│   ├── png               
│   ├── tables            
│   ├── positive_png      
│   ├── negative_png      
│   ├── columns           
│   ├── indexes           
│
├── val  
│
└── test  
    ├── gpt_columns       
    ├── gpt_indexes       
```

---

## 🏋️ Training

### 🔹 Phase 1 (Chart Simplification Training)
```bash
python main.py --phase 1
```

### 🔹 Phase 2 (Chart-to-Table Extraction & Reasoning)
```bash
python main.py --phase 2 --state_path './state/phase_1_best_model.pth' --lr 1e-5 
```

---

## 🔍 Inference

### 📊 Evaluate RD
```bash
python inference.py
```

### 📝 ChartQA Question Answering
```bash
python QA.py --api_key 'your_api_key' --qa_type 'human or augmented'
```

---

## 📈 OpenCQA Evaluation

### 🔹 Dataset Setup
Download **OpenCQA** from: [GitHub](https://github.com/vis-nlp/OpenCQA)

```bash
cd data/opencqa/test/
unzip test.zip
cd ../../../
python preprocess_opencqa.py
```

### 🔹 Inference
```bash
python inference.py --img_path './data/opencqa/test/img/' --row_path './data/opencqa/test/gpt_indexes/' --col_path './data/opencqa/test/gpt_columns/' --inference_type 'opencqa/'
```

### 🔹 Open-ended Question Answering
```bash
python opencqa.py --api_key 'your_api_key'
```

---

## 🏆 Unichart Integration

### 🔹 Phase 1
```bash
python unichart/unichart_phase1.py
```

### 🔹 Phase 2
```bash
python unichart/unichart_phase2.py
```

### 🔹 Inference
```bash
python unichart/unichart_inference.py
```

Obtain `predicted.csv` and use it in the QA process.

---

## 🛠️ Citation
If you find this work useful, please cite:
```bibtex
@article{simplot2025,
  author    = {Your Name},
  title     = {SIMPLOT: Enhancing Chart Question Answering by Distilling Essentials},
  journal   = {NAACL 2025 Findings},
  year      = {2025},
  archivePrefix = {arXiv},
  eprint    = {2405.00021},
}
```

---

## 📬 Contact
For issues, feel free to open an [issue](https://github.com/your_repo/issues) or reach out!

---
