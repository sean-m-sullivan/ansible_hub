# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Herve Quatremain <hquatrem@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class ModuleDocFragment(object):

    # Ansible Galaxy documentation fragment
    DOCUMENTATION = r"""
options:
  ah_host:
    description:
    - URL to Ansible Automation Hub instance.
    - If value not set, will try environment variable E(AH_HOST), or E(AAP_HOSTNAME).
    - If value not specified by any means, the value of C(127.0.0.1) will be used.
    type: str
    aliases: [ ah_hostname, aap_hostname ]
  ah_username:
    description:
    - Username for your Ansible Automation Hub instance.
    - If value not set, will try environment variable E(AH_USERNAME), or E(AAP_USERNAME).
    type: str
    aliases: [ aap_username ]
  ah_password:
    description:
    - Password for your Ansible Automation Hub instance.
    - If value not set, will try environment variable E(AH_PASSWORD), or E(AAP_PASSWORD).
    type: str
    aliases: [ aap_password ]
  validate_certs:
    description:
    - Whether to allow insecure connections to Automation Hub Server.
    - If V(no), SSL certificates will not be validated.
    - This should only be used on personally controlled sites using self-signed certificates.
    - If value not set, will try environment variable E(AH_VERIFY_SSL), or E(AAP_VALIDATE_CERTS).
    type: bool
    aliases: [ ah_verify_ssl, aap_validate_certs ]
  request_timeout:
    description:
    - Specify the timeout Ansible should use in requests to the Automation Hub host.
    - Defaults to 10 seconds, but this is handled by the shared module_utils code.
    - If value not set, will try environment variable E(AAP_REQUEST_TIMEOUT)
    type: float
    aliases: [ aap_request_timeout ]
  ah_path_prefix:
    description:
    - API path used to access the api.
    - For galaxy_ng this is either V(automation-hub) or the custom prefix used on install with E(GALAXY_API_PATH_PREFIX).
    - For Automation Hub this is V(galaxy).
    type: str
    default: 'galaxy'
"""
