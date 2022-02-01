from app import app
from flask import render_template, request, redirect, url_for
from models import Kitiki


@app.route('/')
def index():
    q = request.args.get('q')
    if q:
        cats = Kitiki.query.filter(Kitiki.name.contains(q) | Kitiki.description.contains(q) | Kitiki.breed.contains(q))
        return redirect(f'/kitiki/?q={q}')
    return render_template('index.html')


@app.route('/kitiki/')
def kitiki():
    q = request.args.get('q')
    page = request.args.get('page')
    sort = request.args.get('sorted')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    if q:
        cats = Kitiki.query.filter(Kitiki.name.contains(q) | Kitiki.description.contains(q) | Kitiki.breed.contains(q))
    else:
        cats = Kitiki.query.order_by(Kitiki.name.asc())
    if sort == "breedasc":
        cats = Kitiki.query.order_by(Kitiki.breed.asc())
    elif sort == "breeddesc":
        cats = Kitiki.query.order_by(Kitiki.breed.desc())
    elif sort == "ageasc":
        cats = Kitiki.query.order_by(Kitiki.age.asc())
    elif sort == "agedesc":
        cats = Kitiki.query.order_by(Kitiki.age.desc())


    pages = cats.paginate(page=page, per_page=5)
    return render_template('kitiki.html', cats=cats, pages=pages)


@app.route('/about')
def about():
    q = request.args.get('q')
    if q:
        cats = Kitiki.query.filter(Kitiki.name.contains(q) | Kitiki.description.contains(q) | Kitiki.breed.contains(q))
        return redirect(f'/kitiki/?q={q}')
    return render_template('about.html')


@app.route('/<cat_name>')
def cat_detail(cat_name):
    cat = Kitiki.query.filter(Kitiki.name == cat_name).first()  # .first_or_404()
    q = request.args.get('q')
    if q:
        cats = Kitiki.query.filter(Kitiki.name.contains(q) | Kitiki.description.contains(q) | Kitiki.breed.contains(q))
        return redirect(f'/kitiki/?q={q}')
    return render_template('cat_detail.html', cat=cat)

