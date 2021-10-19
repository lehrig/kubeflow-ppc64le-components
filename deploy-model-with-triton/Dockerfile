FROM registry.access.redhat.com/ubi8/ubi-minimal:8.4-210

ARG KUBECTL_VERSION=v1.17.17
ARG YQ_VERSION=v4.13.4
ARG YQ_BINARY=yq_linux_ppc64le

COPY ./src .

RUN microdnf update && microdnf install -y \
  ca-certificates \
  curl \
  gzip \
  jq \
  
  procps \
  tar \
  wget \
  && \
  curl -LO https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/ppc64le/kubectl && \
  chmod +x ./kubectl && \
  mv ./kubectl /usr/local/bin/kubectl && \
  curl -LO https://github.com/mikefarah/yq/releases/download/${YQ_VERSION}/${YQ_BINARY} && \
  chmod +x ./${YQ_BINARY} && \
  mv ./${YQ_BINARY} /usr/local/bin/yq
