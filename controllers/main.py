from odoo import http
from odoo.http import request
import re


class AISaleBotController(http.Controller):

    @http.route(
        "/aisalebot/embed.js",
        type="http",
        auth="public",
        website=True,
        csrf=False,
    )
    def aisalebot_embed(self):
        ICP = request.env["ir.config_parameter"].sudo()

        if ICP.get_param("aisalebot.enabled") != "True":
            return request.make_response(
                "",
                headers=[("Content-Type", "application/javascript")]
            )

        raw = ICP.get_param("aisalebot.embed_script") or ""
        if not raw:
            return request.make_response(
                "",
                headers=[("Content-Type", "application/javascript")]
            )

        m = re.search(
            r'<script[^>]+src="([^"]+)"([^>]*)></script>',
            raw,
            re.IGNORECASE
        )
        if not m:
            return request.make_response(
                "",
                headers=[("Content-Type", "application/javascript")]
            )

        src = m.group(1)
        attrs = m.group(2)

        lines = []
        for k, v in re.findall(r'([\w\-]+)="([^"]+)"', attrs):
            lines.append(f's.setAttribute("{k}", "{v}");')

        attr_js = "\n".join(lines)

        js = (
            "(function(){\n"
            "  function loadBot(){\n"
            f'    var s=document.createElement("script");\n'
            f'    s.src="{src}";\n'
            f'    {attr_js}\n'
            "    document.body.appendChild(s);\n"
            "  }\n"
            "  if(document.readyState==='loading'){\n"
            "    document.addEventListener('DOMContentLoaded',loadBot);\n"
            "  }else{loadBot();}\n"
            "})();"
        )

        return request.make_response(
            js,
            headers=[("Content-Type", "application/javascript")]
        )
