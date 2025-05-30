# MLOps Week 2 - DVC Tracking for iris.csv

This project demonstrates how to use Git and DVC (Data Version Control) to manage and version the `iris.csv` dataset in a reproducible machine learning workflow.

---

##  Project Setup

### 1. Create Project Directory and Virtual Environment

```bash
mkdir MLOps-week2
cd MLOps-week2
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Initialize Git and Clone Repository

```bash
git init
git clone https://github.com/MeghnaB12/iris-week2.git
cd iris-week2
```

### 3. Install Dependencies and Initialize DVC

```bash
pip install -r requirements.txt
pip install dvc
dvc init
```

### 4. Track Dataset Only with DVC

```bash
dvc add data/iris.csv
```

### 5. Prevent Git from Tracking the Dataset

```bash
git rm --cached data/iris.csv
echo "data/iris.csv" >> .gitignore
git add .gitignore
git commit -m "Stop tracking iris.csv in Git and add to .gitignore"
```

### 6. Commit DVC Setup and Tag Initial Version

```bash
git add data/iris.csv.dvc .dvc .dvcignore
git commit -m "Initialize DVC tracking for iris.csv"
git tag V0
git push --tags
```

### 7. Modify and Version the Data
Simulate Data Update: Remove Last 20 Rows

```bash
head -n -20 data/iris.csv > temp.csv && mv temp.csv data/iris.csv
```

### 8. Re-track and Commit Changes with DVC

```bash
dvc add data/iris.csv
git add data/iris.csv.dvc
git commit -m "Update iris.csv by removing last 20 rows"
git tag V1
git push --tags
```

### Compare Versions

9. Save Copies of Each Version

```bash
# Version V0
git checkout V0
dvc checkout
cp data/iris.csv iris_V0.csv

# Version V1
git checkout V1
dvc checkout
cp data/iris.csv iris_V1.csv

```

### 10. Compare Data Changes
 Unix file-level diff

```bash
diff -u iris_V0.csv iris_V1.csv
```

DVC-level structured diff

```bash
dvc diff V0 V1
```
