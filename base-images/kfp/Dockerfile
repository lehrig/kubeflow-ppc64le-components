FROM registry.access.redhat.com/ubi8/python-38

ARG KFP_VERSION=1.7.0

ENV PIPELINE_SDK_PACKAGE=https://storage.googleapis.com/ml-pipeline/release/${KFP_VERSION}/kfp.tar.gz

RUN pip install --quiet --no-cache-dir \
    ${PIPELINE_SDK_PACKAGE}
