from subprocess import check_output


def get_revison():
    """
    Return the source revision (last commit id) of the project
    """

    try:
        revision = check_output(['git', 'rev-parse', '--short', 'HEAD']).strip()
    except OSError:
        revision = None

    return revision
