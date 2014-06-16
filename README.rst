Unix Account
============

Python module to manipulate unix system accounts by calling standard unix
commands user{add,mod,del} which do the actual system files manipulation.

Uses ``sudo`` to run the commands if not root (EUID not 0).

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

Install
-------

::

    pip install unixaccount

Contents
--------

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

    create_user(username, group=None, homedir=None, password=None, mkhome=False, shell=None)
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


License
-------

Copyright 2014 Michal Belica <devel@beli.sk>

::

    Unix Account is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    Unix Account is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with Unix Account.  If not, see < http://www.gnu.org/licenses/ >.

