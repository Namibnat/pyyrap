"""Projects are the heart of GTD."""

import datetime
import os
from collections import namedtuple


class Project:
    def __init__(self, gtd_dir='.yrap', project_file='projects.csv', delimiter='|', logging=True):
        self.project = []
        self.project_headers = ['date_created', 'project', 'done_when', 'project_status', 'finished_date']
        self.item = namedtuple('Project', self.project_headers)
        self.gtd_dir = gtd_dir
        self.project_file = project_file
        self.delimiter = delimiter
        self.logging = logging
        self.home_directory = os.path.expanduser('~')
        self.project_path = os.path.join(self.home_directory, self.gtd_dir, self.project_file)


class Actions:
    pass
