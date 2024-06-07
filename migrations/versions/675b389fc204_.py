"""empty message.

Revision ID: 675b389fc204
Revises: 958a22329222
Create Date: 2024-06-06 12:04:22.460433
"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "675b389fc204"
down_revision = "958a22329222"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("orders", schema=None) as batch_op:
        batch_op.alter_column(
            "ship_postal_code", existing_type=sa.VARCHAR(length=64), nullable=True
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("orders", schema=None) as batch_op:
        batch_op.alter_column(
            "ship_postal_code", existing_type=sa.VARCHAR(length=64), nullable=False
        )

    # ### end Alembic commands ###
