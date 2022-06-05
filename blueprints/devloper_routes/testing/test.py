from flask import Flask, request, render_template , jsonify, redirect, url_for, Blueprint
tests = Blueprint('tests', __name__)

@tests.route('/test')
def test():
    return "This is an example app"

