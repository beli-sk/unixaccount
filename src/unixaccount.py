# vim: set fileencoding=UTF-8 :
#
# Unix Account - python module to manipulate unix system accounts
# Copyright (C) 2014 Michal Belica <devel@beli.sk>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import os
import subprocess
import crypt
import random
import string
import logging
import pwd
import grp

logger = logging.getLogger(__name__)

SUDO = "/usr/bin/sudo"
TOOLSDIR = "/usr/sbin/"

class UnixAccountError(Exception): pass
class AlreadyExists(UnixAccountError): pass
class NotFound(UnixAccountError): pass
class Busy(UnixAccountError):
    """Object busy or locked. E.g. user logged in"""
    pass

def _crypt_pwd(password):
    salt = '$6$' + ''.join(random.choice('./' + string.ascii_lowercase \
            + string.ascii_uppercase + string.digits) for x in range(8))
    crpw = crypt.crypt(password, salt)
    return crpw

def modify_user(username, group=None, homedir=None, password=None,
        mkhome=False, shell=None):
    """Modify existing user account."""
    args = []
    if os.geteuid() != 0:
        args.append(SUDO)
    args.append('%susermod' % TOOLSDIR)
    group and args.extend(['-g', group])
    shell and args.extend(['-s', shell])
    homedir and args.extend(['-d', homedir])
    mkhome and args.append('-m')
    password and args.extend(['-p', _crypt_pwd(password)])
    args.append(username)
    try:
        subprocess.check_call(args, shell=False)
    except subprocess.CalledProcessError as e:
        code = e.returncode
        useradd_errors = {
                1: (logging.ERROR, "can't update password file"),
                2: (logging.ERROR, "invalid command syntax"),
                3: (logging.ERROR, "invalid argument to option"),
                4: (logging.ERROR, "UID already in use"),
                6: (logging.ERROR, "specified group doesn't exist"),
                9: (logging.ERROR, "username already in use"),
                10: (logging.ERROR, "can't update group file"),
                12: (logging.ERROR, "can't create home directory"),
                14: (logging.ERROR, "can't update SELinux user mapping"),
                }
        if code in useradd_errors:
            if code == 9 or code == 4:
                raise AlreadyExists("Specified user name or UID already in use")
            logger.log(useradd_errors[code][0], \
                    "useradd error: %s" % useradd_errors[code][1])
        raise

def create_user(username, group=None, homedir=None, password=None,
        mkhome=False, shell=None):
    """Create a new user account"""
    args = []
    if os.geteuid() != 0:
        args.append(SUDO)
    args.append('%suseradd' % TOOLSDIR)
    group and args.extend(['-g', group])
    shell and args.extend(['-s', shell])
    homedir and args.extend(['-d', homedir])
    mkhome and args.append('-m')
    password and args.extend(['-p', _crypt_pwd(password)])
    args.append(username)
    try:
        subprocess.check_call(args, shell=False)
    except subprocess.CalledProcessError as e:
        code = e.returncode
        useradd_errors = {
                1: (logging.ERROR, "can't update password file"),
                2: (logging.ERROR, "invalid command syntax"),
                3: (logging.ERROR, "invalid argument to option"),
                4: (logging.ERROR, "UID already in use"),
                6: (logging.ERROR, "specified group doesn't exist"),
                9: (logging.ERROR, "username already in use"),
                10: (logging.ERROR, "can't update group file"),
                12: (logging.ERROR, "can't create home directory"),
                14: (logging.ERROR, "can't update SELinux user mapping"),
                }
        if code in useradd_errors:
            if code == 9 or code == 4:
                raise AlreadyExists("Specified user name or UID already in use")
            logger.log(useradd_errors[code][0], \
                    "useradd error: %s" % useradd_errors[code][1])
        raise

def delete_user(username):
    """Delete user account."""
    args = []
    if os.geteuid() != 0:
        args.append(SUDO)
    args.append('%suserdel' % TOOLSDIR)
    args.append(username)
    try:
        subprocess.check_call(args, shell=False)
    except subprocess.CalledProcessError as e:
        code = e.returncode
        useradd_errors = {
                1: (logging.ERROR, "can't update password file"),
                2: (logging.ERROR, "invalid command syntax"),
                6: (logging.ERROR, "specified user doesn't exist"),
                8: (logging.ERROR, "user currently logged in"),
                10: (logging.ERROR, "can't update group file"),
                12: (logging.ERROR, "can't remove home directory"),
                }
        if code in useradd_errors:
            if code == 6:
                raise NotFound("Specified user doesn't exist")
            elif code == 8:
                raise Busy("User currently logged in")
            logger.log(useradd_errors[code][0], \
                    "useradd error: %s" % useradd_errors[code][1])
        raise

def get_uid(username):
    "Return numeric user ID for given username or raise NotFound exception."
    try:
        return pwd.getpwnam(username)[2]
    except KeyError:
        raise NotFound("Specified user doesn't exist")

def get_gid(groupname):
    "Return numeric group ID for given group name or raise NotFound exception."
    try:
        return grp.getgrnam(groupname)[2]
    except KeyError:
        raise NotFound("Specified group doesn't exist")

def get_username(uid):
    "Return user name for given numeric user ID or raise NotFound exception"
    try:
        return pwd.getpwuid(uid)[0]
    except KeyError:
        raise NotFound("Specified user doesn't exist")

