# Copyright (C) 2018 Intel Corporation
#
# SPDX-License-Identifier: MIT

from django.db import models
from cvat.apps.engine.models import Task


class GitData(models.Model):
    task = models.OneToOneField(Task, on_delete = models.CASCADE, primary_key = True)
    url = models.URLField(max_length = 2000)
