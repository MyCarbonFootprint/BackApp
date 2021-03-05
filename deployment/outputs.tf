output "app_dns" {
    value = "${var.app_name}${data.terraform_remote_state.kube_cluster.outputs.cluster_wildcard_dns}"
}
