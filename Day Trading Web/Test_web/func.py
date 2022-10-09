from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user

#First layer of the website, it contains all journalling pages after login
func = Blueprint('func',__name__)

@func.route('/drc', methods=['GET','POST'])
def drc():
    return render_template('drc.html', user=current_user)

@func.route('/monthlystat', methods=['GET','POST'])
def monthlystat():
    return render_template('monthlystat.html', user=current_user)

@func.route('/journal', methods=['GET','POST'])
def journal():
    return render_template('journal.html', user=current_user)


@func.route('/playbook', methods=['GET','POST'])
def playbook():
    return render_template('playbook.html', user=current_user)