# -*- coding: utf-8 -*-

import logging
from otrxmppchannel import OTRXMPPChannel


class OTRXMPPLogger(logging.Handler):
    """
    OTR-XMPP logging handler
    ------------------------
    Uses Off-the-Record Messaging to send log entries to XMPP destinations
    See https://otr.cypherpunks.ca/

    Example::

    from otrxmpplogger import OTRXMPPLogger
    import logging
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
    log.critical('@6 is a rat!')

    NOTE: XMPP invitations are not handled
    NOTE: It seems to take roughly 3 seconds to set up an OTR session.
        Messages logged before the session is ready may be lost.

    :param jid: logger JID, e.g. 'myapplogger@jabber.riseup.net'
    :param password: XMPP server password
    :param recipients: a single recipient JID, a tuple of
        *(jid, OTRFingerprint/None)*, or a list of same
    :param privkey: base64-encoded DSA private key for OTR. If *None* is
        passed, a new key will be generated and dumped via a *ValueError*
        exception.
    """

    def __init__(self, jid, password, recipients, privkey=None):
        logging.Handler.__init__(self)
        self.is_logging = False
        self.channel = OTRXMPPChannel(jid, password, recipients, privkey)

    def emit(self, record):
        # prevent recursive logging
        if self.is_logging:
            return
        self.is_logging = True
        message = self.format(record)
        self.channel.send(message)
        self.is_logging = False
