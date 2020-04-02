# Bayesian generic text classifier

In a directory called categories we create one directory per category we want to classify.
For example if we want to classify types of e-mail, we create two directories named ham and spam.
Inside those directories we save text documents accordingly.

## To install

```
git clone https://github.com/kostaslazaros/bayesian_classifier.git
cd bayesian_classifier
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

### From command line

From command line run in python interpreter:

```python
import bayesian_multi_classifier as bmc
predictor = bmc.Predict('./categories/')
predictor.predict('Enter text to classify')
```

### From web interface

To start the rest api server

```bash
python flaskapp.py
```

In your browser of choice open index.html
