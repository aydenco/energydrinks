"""empty message

Revision ID: 2a748d822728
Revises: 0438bb8e1999
Create Date: 2022-12-06 21:00:30.242791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a748d822728'
down_revision = '0438bb8e1999'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('drink', schema=None) as batch_op:
        batch_op.alter_column('brand',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=250),
               existing_nullable=False)
        batch_op.alter_column('flavor',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=250),
               existing_nullable=True)
        batch_op.alter_column('caffeine',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=10),
               existing_nullable=True)
        batch_op.alter_column('sugar',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=10),
               existing_nullable=True)
        batch_op.alter_column('calories',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.String(length=10),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('drink', schema=None) as batch_op:
        batch_op.alter_column('calories',
               existing_type=sa.String(length=10),
               type_=sa.VARCHAR(length=4),
               existing_nullable=True)
        batch_op.alter_column('sugar',
               existing_type=sa.String(length=10),
               type_=sa.VARCHAR(length=4),
               existing_nullable=True)
        batch_op.alter_column('caffeine',
               existing_type=sa.String(length=10),
               type_=sa.VARCHAR(length=4),
               existing_nullable=True)
        batch_op.alter_column('flavor',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)
        batch_op.alter_column('brand',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)

    # ### end Alembic commands ###