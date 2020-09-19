"""empty message

Revision ID: 25fae54d082b
Revises: 2c3caebad7a1
Create Date: 2020-08-19 09:26:17.101170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25fae54d082b'
down_revision = '2c3caebad7a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('artistvenue')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artistvenue',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], name='artistvenue_artist_id_fkey'),
    sa.ForeignKeyConstraint(['venue_id'], ['venues.id'], name='artistvenue_venue_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='artistvenue_pkey')
    )
    # ### end Alembic commands ###