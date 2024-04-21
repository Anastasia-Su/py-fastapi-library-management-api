"""'initial_migration3'

Revision ID: 208118c5a0af
Revises: 0502a48a8a05
Create Date: 2024-04-21 14:41:39.432592

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '208118c5a0af'
down_revision: Union[str, None] = '0502a48a8a05'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('book', 'publication_date',
               existing_type=sa.DATE(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('book', 'publication_date',
               existing_type=sa.DATE(),
               nullable=True)
    # ### end Alembic commands ###
