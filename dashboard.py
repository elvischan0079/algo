from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config('SECRET_KEY')