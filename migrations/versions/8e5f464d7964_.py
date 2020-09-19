"""empty message

Revision ID: 8e5f464d7964
Revises: 48c1de59d21f
Create Date: 2020-08-17 13:16:02.369153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e5f464d7964'
down_revision = '48c1de59d21f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('upcoming', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shows', 'upcoming')
    # ### end Alembic commands ###