## End to End Machine Learning Project


###  Set Up Prcoess for Jupyter Notebook

1. First we need to create new conda enviornment
```sh
conda create --p venv python==3.10 -y
```
2. Install the `ipykernel`
```sh
conda install ipykernel
```
3. Using the following command, we will now have this conda environment in the Jupyter notebook.
```sh
python -m ipykernel install --user --name=firstEnv
```
4. Open the jupyter lab
```bash
jupyter-lab
```
Then select the `kernel` 