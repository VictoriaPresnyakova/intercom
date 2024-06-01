"""init

Revision ID: 2481f351089b
Revises: 
Create Date: 2024-06-01 15:20:37.985116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.

revision = '2481f351089b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    from repositories.db.enums import UserRole
    op.execute("DROP TYPE IF EXISTS userrole;")
    user = op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('email', sa.String(), nullable=False, unique=True),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('role', sa.Enum(UserRole, values_callable=lambda obj: [e.value for e in obj]),
                  nullable=False),
        sa.Column('full_name', sa.String(), nullable=False),
        sa.Column('phone', sa.String(), nullable=False, unique=True),
        sa.Column('address', sa.Integer, nullable=False, unique=True),
        sa.Column('key', sa.String(), nullable=False, unique=True),
        #sa.Column('is_active', sa.Boolean, nullable=False, default=False),
        sa.Column('auth_token', sa.String(), nullable=True)
    )


def downgrade():
    pass
