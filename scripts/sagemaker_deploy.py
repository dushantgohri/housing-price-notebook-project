import boto3
import sagemaker
from sagemaker import get_execution_role
from sagemaker.model import Model

def deploy_model(model_artifact, role, endpoint_name):
    sagemaker_session = sagemaker.Session()
    
    # Create a model object
    model = Model(
        model_data=model_artifact,
        role=role,
        image_uri=sagemaker.image_uris.retrieve('linear-learner', sagemaker_session.boto_region_name),
        sagemaker_session=sagemaker_session
    )
    
    # Deploy the model to an endpoint
    predictor = model.deploy(
        initial_instance_count=1,
        instance_type='ml.m5.large',
        endpoint_name=endpoint_name
    )
    
    return predictor

if __name__ == "__main__":
    # Specify the model artifact location and endpoint name
    model_artifact = 's3://your-bucket/path/to/model.tar.gz'  # Update with your model path
    role = get_execution_role()
    endpoint_name = 'housing-price-prediction-endpoint'  # Update with your desired endpoint name
    
    predictor = deploy_model(model_artifact, role, endpoint_name)
    print(f'Model deployed to endpoint: {endpoint_name}')