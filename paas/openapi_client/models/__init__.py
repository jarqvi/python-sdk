# coding: utf-8

# flake8: noqa
"""
    PaaS

    Manage your apps using our API  [wss://api.iran.liara.ir?token=<api-token>&cmd=/bin/bash&project_id=<project-id>]( wss://api.iran.liara.ir?token=<api-token>&cmd=/bin/bash&project_id=<project-id>)  Parameters: - `token`: Your api token in liara - `cmd`: By default /bin/bash - `project_id`: The id of your project in liara  This `WebSocket` endpoint allows `real-time` communication with the projects service hosted at `Liara` You can use `WebSocket protocols` to send and receive data, enabling efficient and low-latency interactions with the projects

    The version of the OpenAPI document: 1.0.0
    Contact: info@liara.ir
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from openapi_client.models.applets import Applets
from openapi_client.models.applets_applets_inner import AppletsAppletsInner
from openapi_client.models.applets_applets_inner_release import AppletsAppletsInnerRelease
from openapi_client.models.change_plan_request import ChangePlanRequest
from openapi_client.models.check_domain import CheckDomain
from openapi_client.models.check_domain_domain import CheckDomainDomain
from openapi_client.models.check_domain_domain_project import CheckDomainDomainProject
from openapi_client.models.create_app import CreateApp
from openapi_client.models.create_app_domain201_response import CreateAppDomain201Response
from openapi_client.models.create_app_domain201_response_domain import CreateAppDomain201ResponseDomain
from openapi_client.models.create_app_domain_request import CreateAppDomainRequest
from openapi_client.models.create_disk_request import CreateDiskRequest
from openapi_client.models.create_ftp200_response import CreateFtp200Response
from openapi_client.models.create_ftp_request import CreateFtpRequest
from openapi_client.models.deploy_releases import DeployReleases
from openapi_client.models.domains import Domains
from openapi_client.models.domains_domains_inner import DomainsDomainsInner
from openapi_client.models.domains_domains_inner_project import DomainsDomainsInnerProject
from openapi_client.models.download_backup200_response import DownloadBackup200Response
from openapi_client.models.enable_ssl200_response import EnableSsl200Response
from openapi_client.models.enable_ssl_request import EnableSslRequest
from openapi_client.models.get_app_summary_reports200_response import GetAppSummaryReports200Response
from openapi_client.models.get_app_summary_reports200_response_cpu_usage_inner import GetAppSummaryReports200ResponseCpuUsageInner
from openapi_client.models.get_app_summary_reports200_response_cpu_usage_inner_value_inner import GetAppSummaryReports200ResponseCpuUsageInnerValueInner
from openapi_client.models.get_app_summary_reports200_response_disks_usage_inner import GetAppSummaryReports200ResponseDisksUsageInner
from openapi_client.models.get_disk_backup import GetDiskBackup
from openapi_client.models.get_disk_backup_backups_inner import GetDiskBackupBackupsInner
from openapi_client.models.get_disks import GetDisks
from openapi_client.models.get_disks_disks_inner import GetDisksDisksInner
from openapi_client.models.get_disks_mounts_inner import GetDisksMountsInner
from openapi_client.models.get_ftps200_response import GetFtps200Response
from openapi_client.models.get_ftps200_response_accesses_inner import GetFtps200ResponseAccessesInner
from openapi_client.models.ip_static200_response import IpStatic200Response
from openapi_client.models.logs_inner import LogsInner
from openapi_client.models.project_all_details import ProjectAllDetails
from openapi_client.models.project_all_details_project import ProjectAllDetailsProject
from openapi_client.models.project_all_details_project_envs_inner import ProjectAllDetailsProjectEnvsInner
from openapi_client.models.project_all_details_project_node import ProjectAllDetailsProjectNode
from openapi_client.models.projects import Projects
from openapi_client.models.projects_projects_inner import ProjectsProjectsInner
from openapi_client.models.redirect_domain_request import RedirectDomainRequest
from openapi_client.models.releases import Releases
from openapi_client.models.releases_deploy200_response import ReleasesDeploy200Response
from openapi_client.models.releases_releases_inner import ReleasesReleasesInner
from openapi_client.models.releases_releases_inner_git_info import ReleasesReleasesInnerGitInfo
from openapi_client.models.releases_releases_inner_git_info_author import ReleasesReleasesInnerGitInfoAuthor
from openapi_client.models.reports import Reports
from openapi_client.models.reports_result_inner import ReportsResultInner
from openapi_client.models.resize_disk_request import ResizeDiskRequest
from openapi_client.models.set_app_domain_request import SetAppDomainRequest
from openapi_client.models.sources_deploy200_response import SourcesDeploy200Response
from openapi_client.models.turn_app_request import TurnAppRequest
from openapi_client.models.update_envs import UpdateEnvs
from openapi_client.models.update_envs200_response import UpdateEnvs200Response
from openapi_client.models.update_envs_variables_inner import UpdateEnvsVariablesInner
