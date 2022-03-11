FROM registry.access.redhat.com/ubi8/python-38

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
