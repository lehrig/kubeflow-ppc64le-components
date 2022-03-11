#!/bin/bash -e

KFP_VERSION=1.7.0

image_name=quay.io/ibm/kubeflow-component-base-image-kfp
full_image_name=${image_name}:v${KFP_VERSION}

cd "$(dirname "$0")"
docker build --build-arg KFP_VERSION=$KFP_VERSION -t "${full_image_name}" .
docker push "${full_image_name}"

