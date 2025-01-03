Final update
------------

This repository is archived and left online for historical reasons and
because someone might decide it's useful and fork it. Enjoy!

XMPP-OTR logging handler for Python
===================================

This is a Python library for logging to XMPP destinations using OTR
(`Off-the-Record Messaging`_) encryption.

Features
--------

-  OTRv2
-  Pure python (no libotr dependency)
-  Log to multiple destinations
-  Optionally check log destinations' OTR fingerprints

Installation
------------

::

    $ sudo pip install --pre xmpppy  # xmpppy is tagged as an "rc" version
    $ sudo pip install otrxmpplogger

Example
-------

::

    from otrxmpplogger import OTRXMPPLogger
    import logging
    import time
    log = logging.getLogger()
    privkey = open('.otrprivkey', 'r').read()
    handler = OTRXMPPLogger(
        'bradass87@jabber.ccc.de/datadiode',
        'supersecret',
        [
            (
                'mendax@jabber.wikileaks.org',
                '33eb6b01c97ceba92bd6b5e3777189c43f8d6f03'
            ),
            'esnowden@chat.nsa.gov'
        ],
        privkey
    )

    log.addHandler(handler)
    log.debug('setting up OTR')  # Trigger OTR setup
    time.sleep(3)  # Give OTR a little while to go active
    log.critical('@6 is a rat!')

Notes
-----

-  XMPP invitations are not handled
-  It seems to take roughly 3 seconds to set up an OTR session. Messages
   logged before the session is ready may be lost.

Dependencies
------------

-  `xmpppy`_ (>= 0.4.1)
-  `pure-python-otr`_ (>= 1.0.0)
-  `otrxmppchannel`_ (>= 1.0.3)

Author
------

-  Mike Gogulski - https://github.com/mikegogulski

License
-------

This is free and unencumbered public domain software. For more
information, see http://unlicense.org/ or the accompanying UNLICENSE
file.

.. _Off-the-Record Messaging: https://otr.cypherpunks.ca/
.. _xmpppy: http://xmpppy.sourceforge.net/
.. _pure-python-otr: https://github.com/afflux/pure-python-otr
.. _otrxmppchannel: https://github.com/mikegogulski/python-otrxmppchannel