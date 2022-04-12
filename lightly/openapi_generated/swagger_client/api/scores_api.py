# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@lightly.ai
    Generated by: https://openapi-generator.tech
"""

from lightly.openapi_generated.swagger_client.api_client import ApiClient
from lightly.openapi_generated.swagger_client.api.scores_api_endpoints.create_or_update_active_learning_score_by_tag_id import CreateOrUpdateActiveLearningScoreByTagId
from lightly.openapi_generated.swagger_client.api.scores_api_endpoints.get_active_learning_score_by_score_id import GetActiveLearningScoreByScoreId
from lightly.openapi_generated.swagger_client.api.scores_api_endpoints.get_active_learning_scores_by_tag_id import GetActiveLearningScoresByTagId


class ScoresApi(
    CreateOrUpdateActiveLearningScoreByTagId,
    GetActiveLearningScoreByScoreId,
    GetActiveLearningScoresByTagId,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
