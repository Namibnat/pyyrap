"""Projects are the heart of GTD."""

import datetime
import os
from collections import namedtuple

import pandas as pd


class GTDDefines:
    """GTD defines for the project module."""

    # File
    PROJECT_FILE = 'projects.csv'
    ACTION_FILE = 'actions.csv'
    GTD_DIR = '.yrap'
    HOME_DIR = os.path.expanduser('~')

    # Project states
    PROJECT_STATE_ACTIVE = 'active'
    PROJECT_STATE_COMPLETE = 'complete'
    PROJECT_STATE_HOLD = 'hold'
    PROJECT_STATE_CANCELLED = 'cancelled'
    PROJECT_STATE_DELETED = 'deleted'


class Project:
    def __init__(self, project_file=GTDDefines.PROJECT_FILE, delimiter='|', logging=True):
        self.project = []
        self.project_headers = ['date_created', 'project', 'done_when', 'project_status', 'finished_date']
        self.item = namedtuple('Project', self.project_headers)
        self.project_file = project_file
        self.delimiter = delimiter
        self.logging = logging
        self.home_directory = os.path.expanduser('~')
        self.project_path = os.path.join(self.home_directory, GTDDefines.GTD_DIR, self.project_file)

    def create_project_file(self):
        if not os.path.exists(self.project_path):
            os.makedirs(os.path.dirname(self.project_path), exist_ok=True)
            with open(self.project_path, 'w') as f:
                f.write(self.delimiter.join(self.project_headers))

    def add(self, project, done_when, project_status=GTDDefines.PROJECT_STATE_ACTIVE):
        self.project.append(self.item(date_created=datetime.datetime.now(), project=project, done_when=done_when,
                                      project_status=project_status, finished_date=None))

    def read(self):
        """Read the project from a csv file"""
        try:
            project_df = pd.read_csv(self.project_path, sep=self.delimiter)
        except pd.errors.EmptyDataError:
            project_df = None
        except FileNotFoundError:
            project_df = None
        return project_df

    def save(self):
        """Save the project to a csv file"""
        self.create_project_file()
        project_df = pd.DataFrame(self.project)
        existing_dg = self.read()
        if existing_dg is not None:
            project_df = project_df.append(existing_dg)
        project_df.to_csv(self.project_path, index=False, sep=self.delimiter)


class Actions:
    def __init__(self, action_file=GTDDefines.ACTION_FILE, delimiter='|', logging=True):
        self.action = []
        self.action_headers = [
            'date_created', 'action_name', 'project', 'action_status', 'finished_date', 'this_week']
        self.item = namedtuple('Action', self.action_headers)
        self.action_file = action_file
        self.delimiter = delimiter
        self.logging = logging
        self.home_directory = os.path.expanduser('~')
        self.action_path = os.path.join(self.home_directory, GTDDefines.GTD_DIR, self.action_file)

    def create_action_file(self):
        if not os.path.exists(self.action_path):
            os.makedirs(os.path.dirname(self.action_path), exist_ok=True)
            with open(self.action_path, 'w') as f:
                f.write(self.delimiter.join(self.action_headers))
