#!/usr/bin/env python3
"""
    This module defines the API routes for the Information
"""
from flask import jsonify
from api.v1.views import app_views
from datetime import datetime, timezone
from os import getenv
from dotenv import load_dotenv

load_dotenv()


@app_views.route("/information", methods=["GET"], strict_slashes=False)
def information() -> str:
    """ GET /api/v1/information
    Description:
        This function returns the information of the API
    Parameters:
        None
    Return:
        - A JSON Representation the information of the API
          [email, current_datetime, github-url]
        - Status Code: 200
    """
    information = {
        "email": getenv("EMAIL"),
        "current_datetime": datetime.now(timezone.utc).isoformat(),
        "github-url": getenv("GITHUB_URL"),
    }
    return jsonify(information), 200
