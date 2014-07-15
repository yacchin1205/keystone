# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 OpenStack LLC
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from keystone.common import wsgi
from keystone.token import controllers


class Router(wsgi.ComposableRouter):
    def add_routes(self, mapper):
        token_controller = controllers.Auth()
        mapper.connect('/tokens',
                       controller=token_controller,
                       action='authenticate',
                       conditions=dict(method=['POST']))
        mapper.connect('/tokens/revoked',
                       controller=token_controller,
                       action='revocation_list',
                       conditions=dict(method=['GET']))
        mapper.connect('/tokens/{token_id}',
                       controller=token_controller,
                       action='validate_token',
                       conditions=dict(method=['GET']))
        mapper.connect('/tokens/{token_id}',
                       controller=token_controller,
                       action='validate_token_head',
                       conditions=dict(method=['HEAD']))
        mapper.connect('/tokens/{token_id}',
                       controller=token_controller,
                       action='delete_token',
                       conditions=dict(method=['DELETE']))
        mapper.connect('/tokens/{token_id}/endpoints',
                       controller=token_controller,
                       action='endpoints',
                       conditions=dict(method=['GET']))

        # Certificates used to verify auth tokens
        mapper.connect('/certificates/ca',
                       controller=token_controller,
                       action='ca_cert',
                       conditions=dict(method=['GET']))

        mapper.connect('/certificates/signing',
                       controller=token_controller,
                       action='signing_cert',
                       conditions=dict(method=['GET']))

        # gakunin auth
        mapper.connect('/token_by/email',
                       controller=token_controller,
                       action='gakunin_email',
                       conditions=dict(method=['POST']))

        mapper.connect('/token_by/eppn',
                       controller=token_controller,
                       action='gakunin_eppn',
                       conditions=dict(method=['POST']))
