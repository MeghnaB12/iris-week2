# Vertex AI ML Pipeline Setup & Model Training

## 1. Install Vertex AI SDK & Dependencies  
Installed the Google Cloud Vertex AI Python SDK for managing model deployment and cloud resources:

```bash
pip3 install --upgrade google-cloud-aiplatform
```

## 2. Configure Google Cloud Environment

Set project ID and region. Created a unique Cloud Storage bucket to store model artifacts and intermediate data:

```bash
PROJECT_ID = "articulate-run-461205-f7"
LOCATION = "us-central1"
BUCKET_URI = f"gs://mlops-course-articulate-run-461205-f7-week1"
```

## 3. Initialize Vertex AI SDK

Configured the SDK with project, location, and bucket:

```bash
from google.cloud import aiplatform
aiplatform.init(project=PROJECT_ID, location=LOCATION, staging_bucket=BUCKET_URI)
```
## 4. Prepare Model and Deployment Resource Names

Defined names for:

- Model artifact directory in Cloud Storage
- Artifact repository name
- Container image name
- Model display name for Vertex AI console

## 5. Train and Serialize Decision Tree Model

- Loaded Iris dataset (iris.csv)
- Split data into training and test sets (60/40 split, stratified)
- Trained a Decision Tree classifier with max depth=3
- Achieved accuracy: 0.983
- Serialized model to local artifacts/model.joblib using joblib

## 6. Upload Model Artifacts to Cloud Storage

Uploaded the serialized model to the configured Cloud Storage bucket for use in Vertex AI serving:

```bash
gsutil cp artifacts/model.joblib {BUCKET_URI}/{MODEL_ARTIFACT_DIR}/
```
