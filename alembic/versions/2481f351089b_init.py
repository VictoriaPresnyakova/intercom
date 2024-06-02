"""init

Revision ID: 2481f351089b
Revises: 
Create Date: 2024-06-01 15:20:37.985116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import ForeignKey

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
        sa.Column('auth_token', sa.String(), nullable=True),
        sa.Column('settings', sa.JSON, nullable=True, server_default='{"2factor": false}'),
    )

    notification = op.create_table(
        'notification',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('text', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer, ForeignKey("public.user.id"), nullable=False),
    )

    intercom = op.create_table(
        'intercom',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('settings',  sa.JSON, nullable=True, server_default='{}'),
    )

    request = op.create_table(
        'request',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('time', sa.DateTime, nullable=False),
        sa.Column('filename', sa.String(), nullable=True),
    )

    key = op.create_table(
        'key',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('is_active', sa.Boolean, nullable=False, default=False),
        )


def downgrade():
    pass
