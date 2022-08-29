locals {
  # Having issues with forwardslash and terraform interpolation at the service selector
  appname_label = "app.kubernetes.io/name"
}

resource "kubernetes_deployment" "fastapipoc" {
  metadata {
    name = "fastapipoc"
    labels = {
      "${local.appname_label}"    = "fastapipoc"
      "app.kubernetes.io/version" = "v0.3.0"
    }
    namespace = "default"
  }

  spec {
    replicas = 1

    selector {
      match_labels = {
        "app.kubernetes.io/name" = "fastapipoc"
      }
    }

    template {
      metadata {
        labels = {
          "app.kubernetes.io/name" = "fastapipoc"
        }
      }

      spec {
        container {
          image = "brunoevonah/fastapipoc:v0.3.0"
          name  = "fastapipoc"

          resources {
            limits = {
              cpu    = "250m"
              memory = "128Mi"
            }
            requests = {
              cpu    = "100m"
              memory = "64Mi"
            }
          }

          port {
            container_port = 8000
          }

          env {
            name  = "LOG_LEVEL"
            value = "INFO"
          }

          liveness_probe {
            http_get {
              path = "/health"
              port = 8000
            }

            initial_delay_seconds = 30
            period_seconds        = 15
          }

          readiness_probe {
            http_get {
              path = "/health"
              port = 8000
            }

            initial_delay_seconds = 30
            period_seconds        = 15
          }
        }
      }
    }
  }
}


resource "kubernetes_service" "fastapipoc" {
  metadata {
    name = "fastapipoc"
    labels = {
      "app.kubernetes.io/name"    = "fastapipoc"
      "app.kubernetes.io/version" = "v0.3.0"
    }
    namespace = "default"
  }

  spec {
    selector = {
      app = "${local.appname_label}"
    }

    port {
      port = 8000
    }

    type = "ClusterIP"
  }
}
