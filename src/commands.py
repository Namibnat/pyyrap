"""YRAP commands."""

from bucket import Bucket
from projects import Project


def create_project_from_bucket_item():
    """Review bucket items, and allow items to be turned into projects."""
    bucket = Bucket()
    bucket_df = bucket.read()
    if bucket_df is None:
        print('Bucket is empty.')
        return
    for index, row in bucket_df.iterrows():
        print(f'{index}: {row["item"]}')
    print('Which item would you like to turn into a project?')
    item_index = int(input())
    item = bucket_df['item'][item_index]
    project = Project()
    project.add(item)
    project.save()
    bucket.remove(item)
    bucket.save()
    print(f'Created project {item}.')


if __name__ == '__main__':
    create_project_from_bucket_item()
