"""empty message

Revision ID: cb28efd08462
Revises: d783290accf9
Create Date: 2017-05-16 16:03:27.593579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb28efd08462'
down_revision = 'd783290accf9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ss_user', sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.add_column('ss_user', sa.Column('submitted', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ss_user', 'submitted')
    op.drop_column('ss_user', 'created')
    # ### end Alembic commands ###
