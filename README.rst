Unix Account
============

Python module to manipulate unix system accounts

Locations
---------

Unix Account packages are available from Cheese shop (PyPI)
at https://pypi.python.org/pypi/unixaccount

The `project page <https://github.com/beli-sk/unixaccount>`_ is hosted on Github.

If you've never worked with *git* or contributed to a project on Github,
there is a `quick start guide <https://help.github.com/articles/fork-a-repo>`_.

If you find something wrong or know of a missing feature, please
`create an issue <https://github.com/beli-sk/unixaccount/issues>`_ on the project
page. If you find that inconvenient or have some security concerns, you could
also drop me a line at <devel@beli.sk>.

Usage
-----

CLASSES
~~~~~~~

* exceptions.Exception(exceptions.BaseException)

   * UnixAccountError

      * AlreadyExists
      * Busy
      * NotFound

FUNCTIONS
~~~~~~~~~

::

    create_user(username, group=None, homedir=None, password=None, mkhome=False, shell='/bin/false')
        Create a new user account
        
    delete_user(username)
        Delete user account.
        
    modify_user(username, group=None, homedir=None, password=None, mkhome=False, shell=None)
        Modify existing user account.
        
    get_gid(groupname)
        Return numeric group ID for given group name or raise NotFound exception.
        
    get_uid(username)
        Return numeric user ID for given username or raise NotFound exception.
        
    get_username(uid)
        Return user name for given numeric user ID or raise NotFound exception

