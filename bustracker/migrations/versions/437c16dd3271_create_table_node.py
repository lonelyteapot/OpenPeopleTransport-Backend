"""Create table Node

Revision ID: 437c16dd3271
Revises: c3c4c2b0f62a
Create Date: 2022-06-21 18:46:15.823509

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '437c16dd3271'
down_revision = 'c3c4c2b0f62a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('node',
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('node')
    # ### end Alembic commands ###
