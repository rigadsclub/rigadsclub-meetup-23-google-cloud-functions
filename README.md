# Dependencies

## Python environment

Suggested: create a dedicated conda environment

```
conda create --name riga-ds-club
conda activate riga-ds-club
conda install --file requirements.txt
```

Alternative: feel free to use virtualenv or simply run:
```
pip install -r requirements.txt
```

Optional: Make your conda environments available for Jupiter Notebooks
```
conda install -c anaconda ipykernel
python3 -m ipykernel install --user --name=riga-ds-club
```

## Google Cloud

### 1. Install Google Cloud SDK

Follow the official Google Cloud Platform tutorial
```
https://cloud.google.com/sdk/docs/install
```

### 2. Authenticate
```
gcloud auth login
```

```
gcloud config set project riga-ds-club-workshop
```

```
gcloud functions deploy mnist --runtime python37 --trigger-http --memory 2048 --allow-unauthenticated
```