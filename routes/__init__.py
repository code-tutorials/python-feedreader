from flask import abort, redirect, request, render_template
from app import app
from db import db
from models.article import Article
from models.source import Source
import feed

@app.route('/', methods=['GET'])
def index_get():
    query = Article.query
    query = query.filter(Article.unread == True)
    query = query.order_by(Article.date_added.desc())
    articles = query.all()
    return render_template('index.html', articles=articles)

@app.route('/read/<int:article_id>', methods=['GET'])
def read_article_get(article_id):
    article = Article.query.get(article_id)
    article.unread = False
    db.session.commit()
    return redirect(article.link)

@app.route('/sources', methods=['GET'])
def sources_get():
    query = Source.query
    query = query.order_by(Source.title)
    sources = query.all()
    return render_template('sources.html', sources=sources)

@app.route('/sources', methods=['POST'])
def sources_post():
    feed_url = request.form['feed']
    parsed = feed.parse(feed_url)
    feed_source = feed.get_source(parsed)
    source = Source.insert_from_feed(feed_url, feed_source)
    return redirect('/sources')
