Retinopathy_Detection/
│
├── data/
│   ├── raw/
│   │   ├── images/
│   │   └── data_all.csv
│   │
│   └── processed/
│       ├── train/
│       │   ├── class_1/
│       │   ├── class_2/
│       │   └── class_3/
│       ├── val/
│       │   ├── class_1/
│       │   ├── class_2/
│       │   └── class_3/
│       └── test/
│           ├── class_1/
│           ├── class_2/
│           └── class_3/
│
├── notebooks/
│   ├── 01_data_audit.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_densenet121_training.ipynb
│   ├── 04_mobilenetv2_training.ipynb
│   ├── 05_efficientnetb0_training.ipynb
│   └── 06_model_comparison.ipynb
│
├── models/
│   ├── densenet121_best.keras
│   ├── mobilenetv2_best.keras
│   ├── efficientnetb0_best.keras
│   └── final_best_model.keras
│
├── src/
│   ├── preprocessing/
│   │   ├── clahe.py
│   │   ├── crop_retina.py
│   │   └── image_loader.py
│   │
│   ├── training/
│   │   ├── train_densenet.py
│   │   ├── train_mobilenet.py
│   │   ├── train_efficientnet.py        ← NEW
│   │   ├── callbacks.py                 ← NEW (shared callbacks factory)
│   │   └── evaluate.py
│   │
│   └── inference/
│       ├── predict.py
│       ├── batch_predict.py             ← NEW (full test-set evaluation)
│       └── gradcam.py
│
├── app/
│   ├── app.py
│   ├── templates/
│   └── static/
│
├── rag/
│   ├── chroma_db/
│   ├── medical_docs/
│   ├── embedder.py                      ← NEW (PDF ingestion → ChromaDB)
│   └── chatbot.py                       ← now only handles Q&A chain
│
├── reports/
│   ├── confusion_matrix/
│   ├── plots/
│   └── final_metrics.csv
│
├── config.yaml                          ← NEW (single source of truth)
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md