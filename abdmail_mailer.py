#!/usr/bin/env python
# encoding: utf-8


class Mailer(object):
    """Send mails to interested parties about pre-specified conditions."""

    def __init__(self, mail_sender, admin_emails, repository_name):
        """Initialise, simply store the supplied parameters.

        :mail_sender: supports send(to, cc, subject, message)
        :admin_emails: list of string, who to tell when no appropriate users
        :repository_name: the repository that is in context

        """
        self._mail_sender = mail_sender
        assert not isinstance(admin_emails, basestring), "admin_emails string"
        self._admin_emails = admin_emails
        self._repository_name = repository_name

    def userException(self, message, branch_name):
        msg = ""
        msg += "in repository: " + self._repository_name
        msg += "\nerror when processing branch: " + str(branch_name)
        msg += "\n" + message
        self._mail_sender.send(
            to=self._admin_emails,
            subject="user exception",
            message=msg)

    def initialCommitMessageParseException(self, e, branch_name):
        subject = ""
        subject += self._repository_name + ": "
        subject += branch_name + ": "
        subject += "missing info"
        msg = ""
        msg += "in repository: " + self._repository_name
        msg += "\nerror when processing branch: " + str(branch_name)
        msg += "\n" + e.message
        self._mail_sender.send(
            to=[e.email],
            subject="bad review branch",
            message=str(branch_name))

    def badBranchName(self, owner, branch_name):
        self._mail_sender.send(
            to=[owner],
            subject="bad review branch",
            message=str(branch_name))


#------------------------------------------------------------------------------
# Copyright (C) 2012 Bloomberg L.P.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#------------------------------- END-OF-FILE ----------------------------------