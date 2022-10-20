"""YRAP commands."""

from bucket import Bucket
from projects import Project


def controller():
    """YRAP controller."""
    print('What would you like to do?')
    print('1: Create a new bucket item')
    print('2: Create a new project from a bucket item')
    print('3: Exit')
    choice = int(input())
    if choice == 1:
        create_bucket_item()
    elif choice == 2:
        create_project_from_bucket_item()
    elif choice == 3:
        exit()
    else:
        print('Invalid choice.')
    controller()

def create_bucket_item():
    """Create a new bucket item."""
    bucket = Bucket()
    bucket.add(input('What is the bucket item? '))
    bucket.save()


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
    print('What will indicate that the project is complete?')
    done_when = input()
    project = Project()
    project.add(item, done_when)
    project.save()
    bucket.remove(item)
    bucket.save()
    print(f'Created project {item}.')


if __name__ == '__main__':
    controller()
