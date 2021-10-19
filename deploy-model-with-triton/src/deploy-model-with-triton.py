#!/usr/bin/env python3
import argparse
import kfp
import kfp.dsl as dsl
from kfp import compiler
from kfp import components
from yaml import safe_load

# Defining and parsing the command-line arguments
parser = argparse.ArgumentParser(description='Deploying an S3-stored model with Trition Inference Server.')
parser.add_argument('--name',
                    type=str,
                    required=True,
                    help='Name of the model. Example: my-model')
parser.add_argument('--s3-address',
                    type=str,
                    required=True,
                    help='S3 end point of the model. Example: s3://minio-service-kubeflow.apps:80/my-model-repository/my-model')
args = parser.parse_args()
print(f'Program arguments: {args}')


# Kubernetes Resources are manipulated using ResourceOps:
# https://www.kubeflow.org/docs/components/pipelines/sdk/manipulate-resources/
minio-credentials_resource = yaml.safe_load("secrets.yaml")
deploy-triton_resource = yaml.safe_load("deployment.yaml")
create-service_resource = yaml.safe_load("service.yaml")

deploy-triton_resource['metadata']['name'] = args.name+"-deployment"
deploy-triton_resource['metadata']['labels']['app'] = args.name
deploy-triton_resource['spec']['selector']['matchLabels']['app'] = args.name
deploy-triton_resource['spec']['template']['spec']['containers'][0]['name'] = args.name
deploy-triton_resource['spec']['template']['spec']['containers'][0]['args'] = ["tritonserver",
        "--model-store="+args.s3-address,
        "--model-control-mode=poll",
        "--repository-poll-secs=5"]

create-service_resource['metadata']['name'] = args.name+"-service"
create-service_resource['metadata']['labels']['app'] = args.name
create-service_resource['spec']['selector']['app'] = args.name

create-minio-credentials_op = dsl.ResourceOp(
    name="create-minio-credentials",
    k8s_resource=credentials_resource,
    action="create",
    attribute_outputs={"name": "{.metadata.name}"}
)

deploy-triton_op = dsl.ResourceOp(
    name="deploy-triton",
    k8s_resource=deploy-triton_resource,
    action="create",
    attribute_outputs={"name": "{.metadata.name}"}
)

create-service_op = dsl.ResourceOp(
    name="create-service",
    k8s_resource=create-service_resource,
    action="create",
    attribute_outputs={"name": "{.metadata.name}"}
)
