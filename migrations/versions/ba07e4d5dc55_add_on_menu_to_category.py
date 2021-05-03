"""add on menu to Category

Revision ID: ba07e4d5dc55
Revises: 
Create Date: 2021-04-30 11:36:59.853778

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba07e4d5dc55'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('on_menu', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('category', 'on_menu')
    # ### end Alembic commands ###
