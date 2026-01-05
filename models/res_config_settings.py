from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    aisalebot_enabled = fields.Boolean(
        string="Enable AISaleBot",
        config_parameter="aisalebot.enabled",
        default=False
    )

    aisalebot_embed_script = fields.Char(
        string="AISaleBot Embed Script",
        config_parameter="aisalebot.embed_script",
        size=2000
    )
