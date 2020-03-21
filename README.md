## Create 2D Dataset Interactively

![image](https://user-images.githubusercontent.com/6872080/77237182-4e3e5700-6b9c-11ea-97f1-70da935535c7.png)

* Installation

```
python -m pip install git+https://github.com/abhijeetdtu/intrdata
```

### Usage

* From Command line
```python
python -m intrdata.dataset.create -- --num-classes 3
```

* from Python code
```python
from intrdata.dataset.create import inputDataset
df = inputDataset(2)
```
