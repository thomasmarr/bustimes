"""add stop letter aka platform name to db

Revision ID: 5e409e4576b6
Revises: 17372e4bde0b
Create Date: 2019-11-03 20:48:19.602836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e409e4576b6'
down_revision = '17372e4bde0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('requests', sa.Column('platform_name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('requests', 'platform_name')
    # ### end Alembic commands ###
