import pytest

from eapp import app, db

@pytest.fixture
def db_session():

    app.config["SQLALCHEMY_DATABASE_URI"] = \
        "mysql+pymysql://root:root@localhost/saledb_test"

    app.config["TESTING"] = True

    with app.app_context():

        db.create_all()

        yield db.session

        db.session.rollback()
        db.drop_all()