# Service
resource "kubernetes_service" "backapp" {
  metadata {
    name = var.app_name
  }
  spec {
    selector = {
      app = var.app_name
    }

    port {
      port        = 5000
      target_port = 5000
      protocol    = "TCP"
      name        = "http"
    }

    type = "NodePort"
  }
}

# Ingress
resource "kubernetes_ingress" "backapp" {
  metadata {
    name = var.app_name
  }

  spec {
    backend {
      service_name = var.app_name
      service_port = 5000
    }

    rule {
      host = "${var.app_name}${data.terraform_remote_state.kube_cluster.outputs.cluster_wildcard_dns}"
      http {
        path {
          backend {
            service_name = var.app_name
            service_port = 5000
          }

          path = "/*"
        }
      }
    }
  }
}

# Deployment
resource "kubernetes_deployment" "backapp" {
  metadata {
    name = var.app_name
    labels = {
      app = var.app_name
    }
  }

  spec {
    replicas = 2

    selector {
      match_labels = {
        app = var.app_name
      }
    }

    template {
      metadata {
        labels = {
          app = var.app_name
        }
      }

      spec {
        image_pull_secrets {
          name = "docker-cfg"
        }

        container {
          image             = "docker.pkg.github.com/mycarbonfootprint/backapp/backapp:${var.backapp_version}"
          name              = var.app_name
          image_pull_policy = "Always"

          port {
            container_port = 5000
          }

          env {
            name  = "API_TOKEN"
            value = var.backapp_token
          }
          env {
            name  = "FLASK_APP"
            value = "app"
          }
          env {
            name  = "FLASK_ENV"
            value = "production"
          }
          env {
            name  = "DATABASE_URI"
            value = "mysql+pymysql://root:${var.mariadb_root_password}@mariadb-release-primary.default:3306/my_database"
          }
        }
      }
    }
  }
}
