"""teste

Revision ID: 19eff8c62c83
Revises: 9d19192b708b
Create Date: 2021-07-19 14:39:43.132357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19eff8c62c83'
down_revision = '9d19192b708b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('colunatest', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'colunatest')
    # ### end Alembic commands ###
