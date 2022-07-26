"""empty message

Revision ID: 07b13434c3c1
Revises: 9c153b94d76c
Create Date: 2022-07-25 12:44:01.034028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07b13434c3c1'
down_revision = '9c153b94d76c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('upcoming_shows', sa.PickleType(), nullable=True))
    op.add_column('Artist', sa.Column('past_shows', sa.PickleType(), nullable=True))
    op.add_column('Artist', sa.Column('past_shows_count', sa.Integer(), nullable=True))
    op.add_column('Artist', sa.Column('upcoming_shows_count', sa.Integer(), nullable=True))
    op.add_column('Venue', sa.Column('upcoming_shows', sa.PickleType(), nullable=True))
    op.add_column('Venue', sa.Column('past_shows', sa.PickleType(), nullable=True))
    op.add_column('Venue', sa.Column('past_shows_count', sa.Integer(), nullable=True))
    op.add_column('Venue', sa.Column('upcoming_shows_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'upcoming_shows_count')
    op.drop_column('Venue', 'past_shows_count')
    op.drop_column('Venue', 'past_shows')
    op.drop_column('Venue', 'upcoming_shows')
    op.drop_column('Artist', 'upcoming_shows_count')
    op.drop_column('Artist', 'past_shows_count')
    op.drop_column('Artist', 'past_shows')
    op.drop_column('Artist', 'upcoming_shows')
    # ### end Alembic commands ###
