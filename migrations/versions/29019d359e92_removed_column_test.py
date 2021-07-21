"""removed column test

Revision ID: 29019d359e92
Revises: f9a13071e68a
Create Date: 2021-07-20 20:45:49.846037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29019d359e92'
down_revision = 'f9a13071e68a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('addresses', 'tabelateste')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('addresses', sa.Column('tabelateste', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
