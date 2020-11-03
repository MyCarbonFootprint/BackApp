variable "mariadb_root_password" {
  type = string
}

variable "backapp_token" {
  type = string
}

variable "backapp_version" {
  type    = string
  default = "latest"
}

variable "app_name" {
    type = string
    default = "backapp"
}