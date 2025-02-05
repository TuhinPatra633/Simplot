# Simplot

Simplot is a chart-based question-answering system leveraging pre-trained models for extracting tables from charts and answering questions. The project is divided into multiple phases, including data preparation, model training, and inference.

------

## Dataset
Download the dataset from the following link:  
[ChartQA Dataset - HuggingFace Repository](https://huggingface.co/datasets/ahmed-masry/ChartQA/tree/main)

------

## File Descriptions

`dataset.py`: Prepares the dataset and generates positive and negative PNG samples.  
`preprocess.py`: Processes the dataset to create inputs for model training.  
`main.py`: Handles training of Phase 1 (Teacher Model) and Phase 2 (Student Model).  
`inference.py`: Extracts tables from charts and generates predictions (saved as `prediction.csv`).  
`QA.py`: Performs question answering using the Gemini model (results saved in `qa_results.csv`).  

----------

## Model Training

Follow these steps to train the models:

1. **Download the Dataset**  
   Download the full dataset from the [ChartQA repository](https://huggingface.co/datasets/ahmed-masry/ChartQA/tree/main).  

2. **Set Up the Environment**  
   Create a Python environment using the dependencies listed in `requirements.txt`.

3. **Run Preprocessing**  
   Execute the preprocessing script:  
   (python preprocess.py)


4. **Phase 1: Teacher Model Training**  
   Train the teacher model using the following command:  
   (python main.py --phase 1)
 

5. **Phase 2: Student Model Training**  
   Train the student model by loading the best Phase 1 model state:  
   (python main.py --phase 2 --state_path './state/phase_1_best_model.pth' --lr 1e-5)


---

## Inference

The pre-trained models are available in the `state/` folder. To perform inference:

1. **Set Up the Environment**  
   Create the environment using `requirements.txt`.

2. **Extract Tables from Charts**  
   Run the following command to generate predictions:  
   (python inference.py )
   Sample output can be found in `result/prediction.csv`.

3. **Question Answering**  
   Use the Gemini model for question answering:  
   (python QA.py --api_key 'your_api_key' --qa_type 'human')
   Results will be saved in `result/qa_results.csv`. A sample is already provided in the `result/` folder.

---

## Folder Structure


Simplot/
│
├── dataset.py
├── preprocess.py
├── main.py
├── inference.py
├── QA.py
├── requirements.txt
├── state/                     # Pre-trained model files
│   ├── phase_2_best_model.pth
│   ├── ...
├── result/                    # Output files
│   ├── prediction.csv         # Sample table extraction results
│   ├── qa_results.csv         # Sample QA results
└── data/                      # Dataset folder


---

## Notes

- Ensure you have a valid API key for Gemini when running the QA phase.  
- Modify paths in the commands if your directory structure differs. 
