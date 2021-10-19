FROM registry.access.redhat.com/ubi8/ubi-minimal:8.4-210

ARG KUBECTL_VERSION=v1.17.17

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
  mv ./kubectl /usr/local/bin/kubectl
