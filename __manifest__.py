{
    "name": "AISaleBot - AI Sales Chatbot",
    "version": "19.0.1.0.0",
    "category": "Website/Website",
    "summary": "Integrate AISaleBot AI Sales Chatbot into your Odoo Website",
    "description": """
AISaleBot helps you convert visitors into customers using AI-powered sales chat.

This module allows you to:
- Connect your Odoo Website with AISaleBot SaaS
- Embed AI Sales Chatbot into your website
- Manage connection via API Key

All AI processing, licensing, and usage limits are handled externally by AISaleBot servers.
""",
    "author": "AISaleBot",
    "website": "https://aisalebot.io/",
    "support": "support@aisalebot.com",
    "license": "OPL-1",
    "depends": ["base", "website"],
    "data": [
        "views/settings.xml",
        "views/website_templates.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "aisalebot_odoo/static/src/js/embed.js",
        ],
    },
    "installable": True,
    "application": False,
}
