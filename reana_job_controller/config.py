# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2017, 2018 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Flask application configuration."""

import os

from reana_job_controller.htcondorcern_job_manager import \
    HTCondorJobManagerCERN
from reana_job_controller.kubernetes_job_manager import KubernetesJobManager

MAX_JOB_RESTARTS = 3
"""Number of retries for a job before considering it as failed."""

SHARED_VOLUME_PATH_ROOT = os.getenv('SHARED_VOLUME_PATH_ROOT', '/var/reana')
"""Root path of the shared volume ."""

COMPUTE_BACKENDS = {
    'kubernetes': KubernetesJobManager,
    'htcondorcern': HTCondorJobManagerCERN
}
"""Supported job compute backends and corresponding management class."""

DEFAULT_COMPUTE_BACKEND = 'kubernetes'
"""Default job compute backend."""

MULTIPLE_COMPUTE_BACKENDS = os.getenv('MULTIPLE_COMPUTE_BACKENDS', False)
"""Allow multiple job compute backends."""
