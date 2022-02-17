"""creating the vaccine table

Revision ID: e80dc7696dc9
Revises: 
Create Date: 2022-02-16 11:34:19.162526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e80dc7696dc9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vaccine_cads',
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('first_shot_date', sa.DateTime(), nullable=True),
    sa.Column('second_shot_date', sa.DateTime(), nullable=True),
    sa.Column('vaccine_name', sa.String(length=50), nullable=False),
    sa.Column('health_unit_name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('cpf')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vaccine_cads')
    # ### end Alembic commands ###