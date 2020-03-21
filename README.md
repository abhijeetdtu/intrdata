## Create 2D Dataset Interactively


* From Command line
```python
python -m intrdata.dataset.create -- --num-classes 3
```

* from Python code
```python
from intrdata.dataset.create import inputDataset
df = inputDataset(2)
```
