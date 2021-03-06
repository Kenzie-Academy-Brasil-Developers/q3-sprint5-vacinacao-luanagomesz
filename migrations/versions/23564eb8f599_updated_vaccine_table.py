"""updated vaccine table

Revision ID: 23564eb8f599
Revises: d78d0cefd731
Create Date: 2022-05-01 18:06:15.952786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23564eb8f599'
down_revision = 'd78d0cefd731'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('vaccine_cards_cpf_key', 'vaccine_cards', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('vaccine_cards_cpf_key', 'vaccine_cards', ['cpf'])
    # ### end Alembic commands ###
