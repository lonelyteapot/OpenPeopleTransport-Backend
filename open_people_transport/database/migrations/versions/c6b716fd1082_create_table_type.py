"""Create table Type

Revision ID: c6b716fd1082
Revises:
Create Date: 2022-06-21 14:03:25.631844

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'c6b716fd1082'
down_revision = 'c62ab13a7632'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('type',
    sa.Column('name', sa.String(length=12), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('type')
    # ### end Alembic commands ###