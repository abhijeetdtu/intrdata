## Create 2D Dataset Interactively

* This tool allows to quickly create 2d datasets for trying different models
* The datasets are returned in form of Pandas Dataframe

<img src="https://user-images.githubusercontent.com/6872080/77237182-4e3e5700-6b9c-11ea-97f1-70da935535c7.png"  height="250x"/>

* Installation

```
python -m pip install git+https://github.com/abhijeetdtu/intrdata
```

### Usage

* Use the "DataFrame" button to end the creation and return the pandas DataFrame
* Use Class-* button to switch between classes

* From Command line
```python
python -m intrdata.dataset.create -- --num-classes 3
```

* from Python code
```python
from intrdata.dataset.create import inputDataset
df = inputDataset(2)
```
