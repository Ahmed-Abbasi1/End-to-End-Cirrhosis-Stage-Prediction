import boto3
import os

bucket_name = 'cirrhosis-ml-project'
local_model_path = 'models/best_model.pkl'  # 🔁 FIXED
s3_key = 'models/best_model.pkl'

s3 = boto3.client('s3')

if os.path.exists(local_model_path):
    s3.upload_file(local_model_path, bucket_name, s3_key)
    print(f"✅ Model uploaded to s3://{bucket_name}/{s3_key}")
else:
    print("❌ Local model file not found at:", local_model_path)
