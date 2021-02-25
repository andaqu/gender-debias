Project structure:

```
gender-debias
├── dataset (*)
│   ├── dataset-neutral
│   ├── dataset-original
│   └── dataset-raw
├── saved 
│   ├── neutral (*)
│   ├── original (*)
│   └── data
└── src
    ├── debiaswe
    ├── utils
    └── model.ipynb
```

> `(*)` not included in repository. Please refer to Google Drive link coming soon.

* `dataset-neutral`: Lemmatised pre-processed dataset.
* `dataset-original`: Pre-processed dataset.
* `dataset-raw`: Original obtained dataset.
* `saved/neutral`: Models trained from lemmatised pre-processed dataset (word2vec and fasttext).
* `saved/original`: Models trained from original pre-processed dataset (word2vec, fasttext and tf-idf vectorizer).
* `saved/data`: Saved data for gender bias observation and mitigation.
* `src/debiaswe`: Obtained and arranged debiaswe code from `[1]`. (*Note to self* :: A better approach would have been fork this project and have it as a submodule...)  
* `src/utils`: Utility scripts to pre-process and other tasks.
* `model.ipynb`: Jupyter notebook to train and test models.

`[1]`: https://github.com/tolga-b/debiaswe