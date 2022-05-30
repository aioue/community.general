#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2017, Eike Frost <ei@kefro.st>
# Copyright (c) 2021, Christophe Gilles <christophe.gilles54@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = '''
---
module: keycloak_realm

short_description: Allows administration of Keycloak realm via Keycloak API

version_added: 3.0.0


description:
    - This module allows the administration of Keycloak realm via the Keycloak REST API. It
      requires access to the REST API via OpenID Connect; the user connecting and the realm being
      used must have the requisite access rights. In a default Keycloak installation, admin-cli
      and an admin user would work, as would a separate realm definition with the scope tailored
      to your needs and a user having the expected roles.

    - The names of module options are snake_cased versions of the camelCase ones found in the
      Keycloak API and its documentation at U(https://www.keycloak.org/docs-api/8.0/rest-api/index.html).
      Aliases are provided so camelCased versions can be used as well.

    - The Keycloak API does not always sanity check inputs e.g. you can set
      SAML-specific settings on an OpenID Connect client for instance and vice versa. Be careful.
      If you do not specify a setting, usually a sensible default is chosen.

options:
    state:
        description:
            - State of the realm.
            - On C(present), the realm will be created (or updated if it exists already).
            - On C(absent), the realm will be removed if it exists.
        choices: ['present', 'absent']
        default: 'present'
        type: str

    id:
        description:
            - The realm to create.
        type: str
    realm:
        description:
            - The realm name.
        type: str
    access_code_lifespan:
        description:
            - The realm access code lifespan.
        aliases:
            - accessCodeLifespan
        type: int
    access_code_lifespan_login:
        description:
            - The realm access code lifespan login.
        aliases:
            - accessCodeLifespanLogin
        type: int
    access_code_lifespan_user_action:
        description:
            - The realm access code lifespan user action.
        aliases:
            - accessCodeLifespanUserAction
        type: int
    access_token_lifespan:
        description:
            - The realm access token lifespan.
        aliases:
            - accessTokenLifespan
        type: int
    access_token_lifespan_for_implicit_flow:
        description:
            - The realm access token lifespan for implicit flow.
        aliases:
            - accessTokenLifespanForImplicitFlow
        type: int
    account_theme:
        description:
            - The realm account theme.
        aliases:
            - accountTheme
        type: str
    action_token_generated_by_admin_lifespan:
        description:
            - The realm action token generated by admin lifespan.
        aliases:
            - actionTokenGeneratedByAdminLifespan
        type: int
    action_token_generated_by_user_lifespan:
        description:
            - The realm action token generated by user lifespan.
        aliases:
            - actionTokenGeneratedByUserLifespan
        type: int
    admin_events_details_enabled:
        description:
            - The realm admin events details enabled.
        aliases:
            - adminEventsDetailsEnabled
        type: bool
    admin_events_enabled:
        description:
            - The realm admin events enabled.
        aliases:
            - adminEventsEnabled
        type: bool
    admin_theme:
        description:
            - The realm admin theme.
        aliases:
            - adminTheme
        type: str
    attributes:
        description:
            - The realm attributes.
        type: dict
    browser_flow:
        description:
            - The realm browser flow.
        aliases:
            - browserFlow
        type: str
    browser_security_headers:
        description:
            - The realm browser security headers.
        aliases:
            - browserSecurityHeaders
        type: dict
    brute_force_protected:
        description:
            - The realm brute force protected.
        aliases:
            - bruteForceProtected
        type: bool
    client_authentication_flow:
        description:
            - The realm client authentication flow.
        aliases:
            - clientAuthenticationFlow
        type: str
    client_scope_mappings:
        description:
            - The realm client scope mappings.
        aliases:
            - clientScopeMappings
        type: dict
    default_default_client_scopes:
        description:
            - The realm default default client scopes.
        aliases:
            - defaultDefaultClientScopes
        type: list
        elements: str
    default_groups:
        description:
            - The realm default groups.
        aliases:
            - defaultGroups
        type: list
        elements: str
    default_locale:
        description:
            - The realm default locale.
        aliases:
            - defaultLocale
        type: str
    default_optional_client_scopes:
        description:
            - The realm default optional client scopes.
        aliases:
            - defaultOptionalClientScopes
        type: list
        elements: str
    default_roles:
        description:
            - The realm default roles.
        aliases:
            - defaultRoles
        type: list
        elements: str
    default_signature_algorithm:
        description:
            - The realm default signature algorithm.
        aliases:
            - defaultSignatureAlgorithm
        type: str
    direct_grant_flow:
        description:
            - The realm direct grant flow.
        aliases:
            - directGrantFlow
        type: str
    display_name:
        description:
            - The realm display name.
        aliases:
            - displayName
        type: str
    display_name_html:
        description:
            - The realm display name HTML.
        aliases:
            - displayNameHtml
        type: str
    docker_authentication_flow:
        description:
            - The realm docker authentication flow.
        aliases:
            - dockerAuthenticationFlow
        type: str
    duplicate_emails_allowed:
        description:
            - The realm duplicate emails allowed option.
        aliases:
            - duplicateEmailsAllowed
        type: bool
    edit_username_allowed:
        description:
            - The realm edit username allowed option.
        aliases:
            - editUsernameAllowed
        type: bool
    email_theme:
        description:
            - The realm email theme.
        aliases:
            - emailTheme
        type: str
    enabled:
        description:
            - The realm enabled option.
        type: bool
    enabled_event_types:
        description:
            - The realm enabled event types.
        aliases:
            - enabledEventTypes
        type: list
        elements: str
    events_enabled:
        description:
            - Enables or disables login events for this realm.
        aliases:
            - eventsEnabled
        type: bool
        version_added: 3.6.0
    events_expiration:
        description:
            - The realm events expiration.
        aliases:
            - eventsExpiration
        type: int
    events_listeners:
        description:
            - The realm events listeners.
        aliases:
            - eventsListeners
        type: list
        elements: str
    failure_factor:
        description:
            - The realm failure factor.
        aliases:
            - failureFactor
        type: int
    internationalization_enabled:
        description:
            - The realm internationalization enabled option.
        aliases:
            - internationalizationEnabled
        type: bool
    login_theme:
        description:
            - The realm login theme.
        aliases:
            - loginTheme
        type: str
    login_with_email_allowed:
        description:
            - The realm login with email allowed option.
        aliases:
            - loginWithEmailAllowed
        type: bool
    max_delta_time_seconds:
        description:
            - The realm max delta time in seconds.
        aliases:
            - maxDeltaTimeSeconds
        type: int
    max_failure_wait_seconds:
        description:
            - The realm max failure wait in seconds.
        aliases:
            - maxFailureWaitSeconds
        type: int
    minimum_quick_login_wait_seconds:
        description:
            - The realm minimum quick login wait in seconds.
        aliases:
            - minimumQuickLoginWaitSeconds
        type: int
    not_before:
        description:
            - The realm not before.
        aliases:
            - notBefore
        type: int
    offline_session_idle_timeout:
        description:
            - The realm offline session idle timeout.
        aliases:
            - offlineSessionIdleTimeout
        type: int
    offline_session_max_lifespan:
        description:
            - The realm offline session max lifespan.
        aliases:
            - offlineSessionMaxLifespan
        type: int
    offline_session_max_lifespan_enabled:
        description:
            - The realm offline session max lifespan enabled option.
        aliases:
            - offlineSessionMaxLifespanEnabled
        type: bool
    otp_policy_algorithm:
        description:
            - The realm otp policy algorithm.
        aliases:
            - otpPolicyAlgorithm
        type: str
    otp_policy_digits:
        description:
            - The realm otp policy digits.
        aliases:
            - otpPolicyDigits
        type: int
    otp_policy_initial_counter:
        description:
            - The realm otp policy initial counter.
        aliases:
            - otpPolicyInitialCounter
        type: int
    otp_policy_look_ahead_window:
        description:
            - The realm otp policy look ahead window.
        aliases:
            - otpPolicyLookAheadWindow
        type: int
    otp_policy_period:
        description:
            - The realm otp policy period.
        aliases:
            - otpPolicyPeriod
        type: int
    otp_policy_type:
        description:
            - The realm otp policy type.
        aliases:
            - otpPolicyType
        type: str
    otp_supported_applications:
        description:
            - The realm otp supported applications.
        aliases:
            - otpSupportedApplications
        type: list
        elements: str
    password_policy:
        description:
            - The realm password policy.
        aliases:
            - passwordPolicy
        type: str
    permanent_lockout:
        description:
            - The realm permanent lockout.
        aliases:
            - permanentLockout
        type: bool
    quick_login_check_milli_seconds:
        description:
            - The realm quick login check in milliseconds.
        aliases:
            - quickLoginCheckMilliSeconds
        type: int
    refresh_token_max_reuse:
        description:
            - The realm refresh token max reuse.
        aliases:
            - refreshTokenMaxReuse
        type: int
    registration_allowed:
        description:
            - The realm registration allowed option.
        aliases:
            - registrationAllowed
        type: bool
    registration_email_as_username:
        description:
            - The realm registration email as username option.
        aliases:
            - registrationEmailAsUsername
        type: bool
    registration_flow:
        description:
            - The realm registration flow.
        aliases:
            - registrationFlow
        type: str
    remember_me:
        description:
            - The realm remember me option.
        aliases:
            - rememberMe
        type: bool
    reset_credentials_flow:
        description:
            - The realm reset credentials flow.
        aliases:
            - resetCredentialsFlow
        type: str
    reset_password_allowed:
        description:
            - The realm reset password allowed option.
        aliases:
            - resetPasswordAllowed
        type: bool
    revoke_refresh_token:
        description:
            - The realm revoke refresh token option.
        aliases:
            - revokeRefreshToken
        type: bool
    smtp_server:
        description:
            - The realm smtp server.
        aliases:
            - smtpServer
        type: dict
    ssl_required:
        description:
            - The realm ssl required option.
        choices: ['all', 'external', 'none']
        aliases:
            - sslRequired
        type: str
    sso_session_idle_timeout:
        description:
            - The realm sso session idle timeout.
        aliases:
            - ssoSessionIdleTimeout
        type: int
    sso_session_idle_timeout_remember_me:
        description:
            - The realm sso session idle timeout remember me.
        aliases:
            - ssoSessionIdleTimeoutRememberMe
        type: int
    sso_session_max_lifespan:
        description:
            - The realm sso session max lifespan.
        aliases:
            - ssoSessionMaxLifespan
        type: int
    sso_session_max_lifespan_remember_me:
        description:
            - The realm sso session max lifespan remember me.
        aliases:
            - ssoSessionMaxLifespanRememberMe
        type: int
    supported_locales:
        description:
            - The realm supported locales.
        aliases:
            - supportedLocales
        type: list
        elements: str
    user_managed_access_allowed:
        description:
            - The realm user managed access allowed option.
        aliases:
            - userManagedAccessAllowed
        type: bool
    verify_email:
        description:
            - The realm verify email option.
        aliases:
            - verifyEmail
        type: bool
    wait_increment_seconds:
        description:
            - The realm wait increment in seconds.
        aliases:
            - waitIncrementSeconds
        type: int

extends_documentation_fragment:
- community.general.keycloak


author:
    - Christophe Gilles (@kris2kris)
'''

EXAMPLES = '''
- name: Create or update Keycloak realm (minimal example)
  community.general.keycloak_realm:
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
    id: realm
    state: present

- name: Delete a Keycloak realm
  community.general.keycloak_realm:
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
    id: test
    state: absent

'''

RETURN = '''
msg:
    description: Message as to what action was taken.
    returned: always
    type: str
    sample: "Realm testrealm has been updated"

proposed:
    description: Representation of proposed realm.
    returned: always
    type: dict
    sample: {
      id: "test"
    }

existing:
    description: Representation of existing realm (sample is truncated).
    returned: always
    type: dict
    sample: {
        "adminUrl": "http://www.example.com/admin_url",
        "attributes": {
            "request.object.signature.alg": "RS256",
        }
    }

end_state:
    description: Representation of realm after module execution (sample is truncated).
    returned: on success
    type: dict
    sample: {
        "adminUrl": "http://www.example.com/admin_url",
        "attributes": {
            "request.object.signature.alg": "RS256",
        }
    }
'''

from ansible_collections.community.general.plugins.module_utils.identity.keycloak.keycloak import KeycloakAPI, camel, \
    keycloak_argument_spec, get_token, KeycloakError
from ansible.module_utils.basic import AnsibleModule


def sanitize_cr(realmrep):
    """ Removes probably sensitive details from a realm representation.

    :param realmrep: the realmrep dict to be sanitized
    :return: sanitized realmrep dict
    """
    result = realmrep.copy()
    if 'secret' in result:
        result['secret'] = '********'
    if 'attributes' in result:
        if 'saml.signing.private.key' in result['attributes']:
            result['attributes'] = result['attributes'].copy()
            result['attributes']['saml.signing.private.key'] = '********'
    return result


def main():
    """
    Module execution

    :return:
    """
    argument_spec = keycloak_argument_spec()

    meta_args = dict(
        state=dict(default='present', choices=['present', 'absent']),

        id=dict(type='str'),
        realm=dict(type='str'),
        access_code_lifespan=dict(type='int', aliases=['accessCodeLifespan']),
        access_code_lifespan_login=dict(type='int', aliases=['accessCodeLifespanLogin']),
        access_code_lifespan_user_action=dict(type='int', aliases=['accessCodeLifespanUserAction']),
        access_token_lifespan=dict(type='int', aliases=['accessTokenLifespan'], no_log=False),
        access_token_lifespan_for_implicit_flow=dict(type='int', aliases=['accessTokenLifespanForImplicitFlow'], no_log=False),
        account_theme=dict(type='str', aliases=['accountTheme']),
        action_token_generated_by_admin_lifespan=dict(type='int', aliases=['actionTokenGeneratedByAdminLifespan'], no_log=False),
        action_token_generated_by_user_lifespan=dict(type='int', aliases=['actionTokenGeneratedByUserLifespan'], no_log=False),
        admin_events_details_enabled=dict(type='bool', aliases=['adminEventsDetailsEnabled']),
        admin_events_enabled=dict(type='bool', aliases=['adminEventsEnabled']),
        admin_theme=dict(type='str', aliases=['adminTheme']),
        attributes=dict(type='dict'),
        browser_flow=dict(type='str', aliases=['browserFlow']),
        browser_security_headers=dict(type='dict', aliases=['browserSecurityHeaders']),
        brute_force_protected=dict(type='bool', aliases=['bruteForceProtected']),
        client_authentication_flow=dict(type='str', aliases=['clientAuthenticationFlow']),
        client_scope_mappings=dict(type='dict', aliases=['clientScopeMappings']),
        default_default_client_scopes=dict(type='list', elements='str', aliases=['defaultDefaultClientScopes']),
        default_groups=dict(type='list', elements='str', aliases=['defaultGroups']),
        default_locale=dict(type='str', aliases=['defaultLocale']),
        default_optional_client_scopes=dict(type='list', elements='str', aliases=['defaultOptionalClientScopes']),
        default_roles=dict(type='list', elements='str', aliases=['defaultRoles']),
        default_signature_algorithm=dict(type='str', aliases=['defaultSignatureAlgorithm']),
        direct_grant_flow=dict(type='str', aliases=['directGrantFlow']),
        display_name=dict(type='str', aliases=['displayName']),
        display_name_html=dict(type='str', aliases=['displayNameHtml']),
        docker_authentication_flow=dict(type='str', aliases=['dockerAuthenticationFlow']),
        duplicate_emails_allowed=dict(type='bool', aliases=['duplicateEmailsAllowed']),
        edit_username_allowed=dict(type='bool', aliases=['editUsernameAllowed']),
        email_theme=dict(type='str', aliases=['emailTheme']),
        enabled=dict(type='bool'),
        enabled_event_types=dict(type='list', elements='str', aliases=['enabledEventTypes']),
        events_enabled=dict(type='bool', aliases=['eventsEnabled']),
        events_expiration=dict(type='int', aliases=['eventsExpiration']),
        events_listeners=dict(type='list', elements='str', aliases=['eventsListeners']),
        failure_factor=dict(type='int', aliases=['failureFactor']),
        internationalization_enabled=dict(type='bool', aliases=['internationalizationEnabled']),
        login_theme=dict(type='str', aliases=['loginTheme']),
        login_with_email_allowed=dict(type='bool', aliases=['loginWithEmailAllowed']),
        max_delta_time_seconds=dict(type='int', aliases=['maxDeltaTimeSeconds']),
        max_failure_wait_seconds=dict(type='int', aliases=['maxFailureWaitSeconds']),
        minimum_quick_login_wait_seconds=dict(type='int', aliases=['minimumQuickLoginWaitSeconds']),
        not_before=dict(type='int', aliases=['notBefore']),
        offline_session_idle_timeout=dict(type='int', aliases=['offlineSessionIdleTimeout']),
        offline_session_max_lifespan=dict(type='int', aliases=['offlineSessionMaxLifespan']),
        offline_session_max_lifespan_enabled=dict(type='bool', aliases=['offlineSessionMaxLifespanEnabled']),
        otp_policy_algorithm=dict(type='str', aliases=['otpPolicyAlgorithm']),
        otp_policy_digits=dict(type='int', aliases=['otpPolicyDigits']),
        otp_policy_initial_counter=dict(type='int', aliases=['otpPolicyInitialCounter']),
        otp_policy_look_ahead_window=dict(type='int', aliases=['otpPolicyLookAheadWindow']),
        otp_policy_period=dict(type='int', aliases=['otpPolicyPeriod']),
        otp_policy_type=dict(type='str', aliases=['otpPolicyType']),
        otp_supported_applications=dict(type='list', elements='str', aliases=['otpSupportedApplications']),
        password_policy=dict(type='str', aliases=['passwordPolicy'], no_log=False),
        permanent_lockout=dict(type='bool', aliases=['permanentLockout']),
        quick_login_check_milli_seconds=dict(type='int', aliases=['quickLoginCheckMilliSeconds']),
        refresh_token_max_reuse=dict(type='int', aliases=['refreshTokenMaxReuse'], no_log=False),
        registration_allowed=dict(type='bool', aliases=['registrationAllowed']),
        registration_email_as_username=dict(type='bool', aliases=['registrationEmailAsUsername']),
        registration_flow=dict(type='str', aliases=['registrationFlow']),
        remember_me=dict(type='bool', aliases=['rememberMe']),
        reset_credentials_flow=dict(type='str', aliases=['resetCredentialsFlow']),
        reset_password_allowed=dict(type='bool', aliases=['resetPasswordAllowed'], no_log=False),
        revoke_refresh_token=dict(type='bool', aliases=['revokeRefreshToken']),
        smtp_server=dict(type='dict', aliases=['smtpServer']),
        ssl_required=dict(choices=["external", "all", "none"], aliases=['sslRequired']),
        sso_session_idle_timeout=dict(type='int', aliases=['ssoSessionIdleTimeout']),
        sso_session_idle_timeout_remember_me=dict(type='int', aliases=['ssoSessionIdleTimeoutRememberMe']),
        sso_session_max_lifespan=dict(type='int', aliases=['ssoSessionMaxLifespan']),
        sso_session_max_lifespan_remember_me=dict(type='int', aliases=['ssoSessionMaxLifespanRememberMe']),
        supported_locales=dict(type='list', elements='str', aliases=['supportedLocales']),
        user_managed_access_allowed=dict(type='bool', aliases=['userManagedAccessAllowed']),
        verify_email=dict(type='bool', aliases=['verifyEmail']),
        wait_increment_seconds=dict(type='int', aliases=['waitIncrementSeconds']),
    )

    argument_spec.update(meta_args)

    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True,
                           required_one_of=([['id', 'realm', 'enabled'],
                                             ['token', 'auth_realm', 'auth_username', 'auth_password']]),
                           required_together=([['auth_realm', 'auth_username', 'auth_password']]))

    result = dict(changed=False, msg='', diff={}, proposed={}, existing={}, end_state={})

    # Obtain access token, initialize API
    try:
        connection_header = get_token(module.params)
    except KeycloakError as e:
        module.fail_json(msg=str(e))

    kc = KeycloakAPI(module, connection_header)

    realm = module.params.get('realm')
    state = module.params.get('state')

    # convert module parameters to realm representation parameters (if they belong in there)
    params_to_ignore = list(keycloak_argument_spec().keys()) + ['state']

    # Filter and map the parameters names that apply to the role
    realm_params = [x for x in module.params
                    if x not in params_to_ignore and
                    module.params.get(x) is not None]

    # See whether the realm already exists in Keycloak
    before_realm = kc.get_realm_by_id(realm=realm)

    if before_realm is None:
        before_realm = {}

    # Build a proposed changeset from parameters given to this module
    changeset = {}

    for realm_param in realm_params:
        new_param_value = module.params.get(realm_param)
        changeset[camel(realm_param)] = new_param_value

    # Prepare the desired values using the existing values (non-existence results in a dict that is save to use as a basis)
    desired_realm = before_realm.copy()
    desired_realm.update(changeset)

    result['proposed'] = sanitize_cr(changeset)
    before_realm_sanitized = sanitize_cr(before_realm)
    result['existing'] = before_realm_sanitized

    # Cater for when it doesn't exist (an empty dict)
    if not before_realm:
        if state == 'absent':
            # Do nothing and exit
            if module._diff:
                result['diff'] = dict(before='', after='')
            result['changed'] = False
            result['end_state'] = {}
            result['msg'] = 'Realm does not exist, doing nothing.'
            module.exit_json(**result)

        # Process a creation
        result['changed'] = True

        if 'id' not in desired_realm:
            module.fail_json(msg='id needs to be specified when creating a new realm')

        if module._diff:
            result['diff'] = dict(before='', after=sanitize_cr(desired_realm))

        if module.check_mode:
            module.exit_json(**result)

        # create it
        kc.create_realm(desired_realm)
        after_realm = kc.get_realm_by_id(desired_realm['id'])

        result['end_state'] = sanitize_cr(after_realm)

        result['msg'] = 'Realm %s has been created.' % desired_realm['id']
        module.exit_json(**result)

    else:
        if state == 'present':
            # Process an update

            # doing an update
            result['changed'] = True
            if module.check_mode:
                # We can only compare the current realm with the proposed updates we have
                if module._diff:
                    result['diff'] = dict(before=before_realm_sanitized,
                                          after=sanitize_cr(desired_realm))
                result['changed'] = (before_realm != desired_realm)

                module.exit_json(**result)

            # do the update
            kc.update_realm(desired_realm, realm=realm)

            after_realm = kc.get_realm_by_id(realm=realm)

            if before_realm == after_realm:
                result['changed'] = False

            result['end_state'] = sanitize_cr(after_realm)

            if module._diff:
                result['diff'] = dict(before=before_realm_sanitized,
                                      after=sanitize_cr(after_realm))

            result['msg'] = 'Realm %s has been updated.' % desired_realm['id']
            module.exit_json(**result)

        else:
            # Process a deletion (because state was not 'present')
            result['changed'] = True

            if module._diff:
                result['diff'] = dict(before=before_realm_sanitized, after='')

            if module.check_mode:
                module.exit_json(**result)

            # delete it
            kc.delete_realm(realm=realm)

            result['proposed'] = {}
            result['end_state'] = {}

            result['msg'] = 'Realm %s has been deleted.' % before_realm['id']

    module.exit_json(**result)


if __name__ == '__main__':
    main()
