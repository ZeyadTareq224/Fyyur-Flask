"""empty message

Revision ID: 2c3caebad7a1
Revises: 2504e1b85fd0
Create Date: 2020-08-19 09:20:23.387786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c3caebad7a1'
down_revision = '2504e1b85fd0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artistvenue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venues.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('artists_venue_id_fkey', 'artists', type_='foreignkey')
    op.drop_column('artists', 'venue_id')
    op.drop_constraint('venues_artist_id_fkey', 'venues', type_='foreignkey')
    op.drop_column('venues', 'artist_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('venues_artist_id_fkey', 'venues', 'artists', ['artist_id'], ['id'])
    op.add_column('artists', sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('artists_venue_id_fkey', 'artists', 'venues', ['venue_id'], ['id'])
    op.drop_table('artistvenue')
    # ### end Alembic commands ###