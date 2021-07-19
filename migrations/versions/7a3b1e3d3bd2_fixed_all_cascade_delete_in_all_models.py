"""Fixed all cascade delete in all models

Revision ID: 7a3b1e3d3bd2
Revises: 567f7ab58feb
Create Date: 2021-07-19 10:41:41.119074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a3b1e3d3bd2'
down_revision = '567f7ab58feb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('colunateste', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'colunateste')
    # ### end Alembic commands ###
