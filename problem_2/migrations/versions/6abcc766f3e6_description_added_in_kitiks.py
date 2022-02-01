"""description added in kitiks

Revision ID: 6abcc766f3e6
Revises: c889df1d1017
Create Date: 2022-01-23 21:31:38.127005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6abcc766f3e6'
down_revision = 'c889df1d1017'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('kitiki', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('kitiki', 'description')
    # ### end Alembic commands ###
