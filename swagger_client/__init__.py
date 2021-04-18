# coding: utf-8

# flake8: noqa

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.7.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.alliance_api import AllianceApi
from swagger_client.api.assets_api import AssetsApi
from swagger_client.api.bookmarks_api import BookmarksApi
from swagger_client.api.calendar_api import CalendarApi
from swagger_client.api.character_api import CharacterApi
from swagger_client.api.clones_api import ClonesApi
from swagger_client.api.contacts_api import ContactsApi
from swagger_client.api.contracts_api import ContractsApi
from swagger_client.api.corporation_api import CorporationApi
from swagger_client.api.dogma_api import DogmaApi
from swagger_client.api.faction_warfare_api import FactionWarfareApi
from swagger_client.api.fittings_api import FittingsApi
from swagger_client.api.fleets_api import FleetsApi
from swagger_client.api.incursions_api import IncursionsApi
from swagger_client.api.industry_api import IndustryApi
from swagger_client.api.insurance_api import InsuranceApi
from swagger_client.api.killmails_api import KillmailsApi
from swagger_client.api.location_api import LocationApi
from swagger_client.api.loyalty_api import LoyaltyApi
from swagger_client.api.mail_api import MailApi
from swagger_client.api.market_api import MarketApi
from swagger_client.api.opportunities_api import OpportunitiesApi
from swagger_client.api.planetary_interaction_api import PlanetaryInteractionApi
from swagger_client.api.routes_api import RoutesApi
from swagger_client.api.search_api import SearchApi
from swagger_client.api.skills_api import SkillsApi
from swagger_client.api.sovereignty_api import SovereigntyApi
from swagger_client.api.status_api import StatusApi
from swagger_client.api.universe_api import UniverseApi
from swagger_client.api.user_interface_api import UserInterfaceApi
from swagger_client.api.wallet_api import WalletApi
from swagger_client.api.wars_api import WarsApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.bad_request import BadRequest
from swagger_client.models.error_limited import ErrorLimited
from swagger_client.models.forbidden import Forbidden
from swagger_client.models.gateway_timeout import GatewayTimeout
from swagger_client.models.internal_server_error import InternalServerError
from swagger_client.models.service_unavailable import ServiceUnavailable
from swagger_client.models.unauthorized import Unauthorized