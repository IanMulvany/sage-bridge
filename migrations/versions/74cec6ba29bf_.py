"""empty message

Revision ID: 74cec6ba29bf
Revises: e2f70d3db407
Create Date: 2017-05-16 15:56:54.580271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74cec6ba29bf'
down_revision = 'e2f70d3db407'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ss_user', sa.Column('language', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ss_user', 'language')
    # ### end Alembic commands ###
