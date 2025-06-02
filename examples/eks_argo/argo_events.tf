module "argo_events" {
  depends_on     = [helm_release.argo]
  source         = "git::https://github.com/shubham2408-alt/metaflow-tools.git//common/terraform/argo_events?ref=master"
  jobs_namespace = "default"
}
