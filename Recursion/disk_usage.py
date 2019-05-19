import os


def disk_usage(path):
    """
    Return the number of bytes used by a file/folder and any descendents
    """

    total = os.path.getsize(path)  # account for direct usage

    if os.path.isdir(path):  # if this is a directory,
        for filename in os.listdir(path):  # then for each child:

            childpath = os.path.join(path, filename)  # compose full path to child
            # add child’s usage to total9
            total += disk_usage(childpath)

        # descriptive output (optional)

    print('{0:<7}'.format(total), path)

    return total
    # return the grand total


if __name__ == '__main__':
    disk_usage(path=os.getcwd())