# Authors:
#   Jason Gerard DeRose <jderose@redhat.com>
#
# Copyright (C) 2008  Red Hat
# see file 'COPYING' for use and warranty contextrmation
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; version 2 only
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

"""
Test the `ipalib.request` module.
"""

import locale
from tests.util import raises
from ipalib.constants import OVERRIDE_ERROR
from ipalib import request


def test_set_languages():
    """
    Test the `ipalib.request.set_languages` function.
    """
    f = request.set_languages
    c = request.context
    langs = ('ru', 'en')

    # Test that StandardError is raised if languages has already been set:
    assert not hasattr(c, 'languages')
    c.languages = None
    e = raises(StandardError, f, *langs)
    assert str(e) == OVERRIDE_ERROR % ('context.languages', None, langs)
    del c.languages

    # Test setting the languages:
    assert not hasattr(c, 'languages')
    f(*langs)
    assert c.languages == langs
    del c.languages

    # Test setting language from locale.getdefaultlocale()
    assert not hasattr(c, 'languages')
    f()
    assert c.languages == locale.getdefaultlocale()[:1]
    del c.languages
    assert not hasattr(c, 'languages')
