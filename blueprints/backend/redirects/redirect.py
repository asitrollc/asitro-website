from flask import Flask, request, render_template , jsonify, redirect, url_for, Blueprint

main_redirect = Blueprint('redirect', __name__)


@main_redirect.route('/redirect/discord/invite/')
def discord_invite():
  return redirect("https://discord.com/api/oauth2/authorize?client_id=954585884311818250&permissions=8&scope=bot%20applications.commands", code=302)


@main_redirect.route('/redirect/status/page/')
def status_page():
  return redirect("https://stats.uptimerobot.com/PWGqmu07Er", code=302)

