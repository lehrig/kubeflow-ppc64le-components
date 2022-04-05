FROM registry.access.redhat.com/ubi8/ubi-minimal:8.5

ARG KUBECTL_VERSION=v1.21.11 # highest kubeflow-supported release

RUN microdnf update && rm -rf /var/cache/yum && microdnf install -y \
  # Installs
  curl \ # for downloading k8s client
  jq \ # for kubectl output processing
  ##########
  && \
  microdnf clean all && \
  curl -LO https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/ppc64le/kubectl && \
  microdnf remove -y curl && \
  chmod +x ./kubectl && \
  mv ./kubectl /usr/local/bin/kubectl
