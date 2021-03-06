"""empty message

Revision ID: 3249f734ed2e
Revises: 8e5f464d7964
Create Date: 2020-08-17 14:58:16.512967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3249f734ed2e'
down_revision = '8e5f464d7964'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('seeking_description', sa.String(length=2000), nullable=True))
    op.add_column('artists', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artists', 'seeking_venue')
    op.drop_column('artists', 'seeking_description')
    # ### end Alembic commands ###
