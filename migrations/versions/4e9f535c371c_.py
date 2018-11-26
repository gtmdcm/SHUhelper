"""empty message

Revision ID: 4e9f535c371c
Revises: c9efdb662890
Create Date: 2018-04-30 20:47:53.874431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e9f535c371c'
down_revision = 'c9efdb662890'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teacher',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('degree', sa.String(), nullable=True),
    sa.Column('sex', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('education', sa.String(), nullable=True),
    sa.Column('dept', sa.String(), nullable=True),
    sa.Column('cs', sa.String(), nullable=True),
    sa.Column('intro', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('user_type', sa.String(), nullable=True))
    op.drop_column('user', 'degree')
    op.drop_column('user', 'education')
    op.drop_column('user', 'cs')
    op.drop_column('user', 'intro')
    op.drop_column('user', 'sex')
    op.drop_column('user', 'title')
    op.drop_column('user', 'type')
    op.drop_column('user', 'dept')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('dept', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('sex', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('intro', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('cs', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('education', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('degree', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('user', 'user_type')
    op.drop_table('teacher')
    # ### end Alembic commands ###
