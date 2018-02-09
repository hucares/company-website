"""empty message

Revision ID: 6c02555b4e3b
Revises: 77799c791f03
Create Date: 2018-02-09 12:49:19.173539

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6c02555b4e3b'
down_revision = '77799c791f03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fullcontact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('fullcontact_response', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('github_handle', sa.String(length=255), nullable=True),
    sa.Column('angellist_handle', sa.String(length=255), nullable=True),
    sa.Column('twitter_handle', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_fullcontact_email'), 'fullcontact', ['email'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_fullcontact_email'), table_name='fullcontact')
    op.drop_table('fullcontact')
    # ### end Alembic commands ###