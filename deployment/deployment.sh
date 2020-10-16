#!/bin/bash

set -e

BASEDIR=$(dirname "$(readlink -f -- "$0")")
cd "${BASEDIR}" || exit

if [ -f "${BASEDIR}"/.env ]; then
    source "${BASEDIR}"/.env
fi

if [ -f "${BASEDIR}"/../.env ]; then
    source "${BASEDIR}"/../.env
fi

# Define Kubernetes cluster directory
KUBERNETES_CLUSTER_DIRECTORY="${BASEDIR}"/kubernetes-cluster

printf 'Clone Kubernetes cluster repository.\n'
rm -rf "${KUBERNETES_CLUSTER_DIRECTORY}"
if [ ${GH_TOKEN} ]; then
    git clone https://paretl:${GH_TOKEN}@github.com/MyCarbonFootprint/kubernetes-cluster.git "${KUBERNETES_CLUSTER_DIRECTORY}"
else
    git clone git@github.com:MyCarbonFootprint/kubernetes-cluster.git "${KUBERNETES_CLUSTER_DIRECTORY}"
fi

printf 'Get Kube config file.\n'
cd "${KUBERNETES_CLUSTER_DIRECTORY}"
terraform init
terraform apply -target local_file.kubeconfig -auto-approve
mv "${KUBERNETES_CLUSTER_DIRECTORY}"/kubeconfig "${BASEDIR}"/kubeconfig
export KUBECONFIG="${BASEDIR}"/kubeconfig
rm -rf "${KUBERNETES_CLUSTER_DIRECTORY}"

# Check cluster connexion
kubectl cluster-info

# Define kube files location
KUBE_FILE="${BASEDIR}"/app.yaml
KUBE_TEMPLATE_FILE="${BASEDIR}"/app-template.yaml

if [ ! ${VERSION_TO_DEPLOY} ]; then
    VERSION_TO_DEPLOY=latest
fi

BACKEND_IMAGE_NAME=docker.pkg.github.com/mycarbonfootprint/backapp/backapp:"${VERSION_TO_DEPLOY}"

# Change values in kube file
sed \
    "s|BACKEND_IMAGE_NAME|$BACKEND_IMAGE_NAME|g; \
    s|TOKEN_VALUE|$API_TOKEN|g" \
    "${KUBE_TEMPLATE_FILE}" > ${KUBE_FILE}

printf 'Deploy kube environment.\n'
kubectl apply -f ${KUBE_FILE}
