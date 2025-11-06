"""seed din276 cost groups

Revision ID: ae3b1d2c3f4e
Revises: 39f07ae969c9
Create Date: 2025-11-06 20:10:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae3b1d2c3f4e'
down_revision: Union[str, Sequence[str], None] = '39f07ae969c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Insert DIN276 seed cost groups."""
    din276 = sa.table(
        'din276_cost_groups',
        sa.column('id', sa.Integer()),
        sa.column('code', sa.String()),
        sa.column('name', sa.String()),
        sa.column('description', sa.Text()),
        sa.column('parent_id', sa.Integer()),
        sa.column('level', sa.Integer()),
    )

    op.bulk_insert(
        din276,
        [
            {
                'id': 1,
                'code': '100',
                'name': 'Grundstück und Erschließung',
                'description': 'Kosten für Grundstück, Erschließung und Rechte am Grundstueck',
                'parent_id': None,
                'level': 1,
            },
            {
                'id': 2,
                'code': '200',
                'name': 'Vorbereitung des Bauvorhabens',
                'description': 'Planung, Gutachten, Bodenuntersuchungen etc.',
                'parent_id': None,
                'level': 1,
            },
            {
                'id': 3,
                'code': '300',
                'name': 'Bauwerk – Baukonstruktion',
                'description': 'Tragwerk, Wände, Decken, Dach',
                'parent_id': None,
                'level': 1,
            },
            {
                'id': 4,
                'code': '400',
                'name': 'Technische Anlagen',
                'description': 'HKL, Elektro, Förderanlagen',
                'parent_id': None,
                'level': 1,
            },
            {
                'id': 5,
                'code': '500',
                'name': 'Außenanlagen',
                'description': 'Parkanlagen, Wege, Zufahrten',
                'parent_id': None,
                'level': 1,
            },
            {
                'id': 6,
                'code': '600',
                'name': 'Ausstattung',
                'description': 'Einbaumöbel, spezielle Ausstattungen',
                'parent_id': None,
                'level': 1,
            },
            {
                'id': 7,
                'code': '700',
                'name': 'Baunebenkosten',
                'description': 'Honorare, Gebühren, Versicherungen',
                'parent_id': None,
                'level': 1,
            },
        ],
    )


def downgrade() -> None:
    """Remove DIN276 seed cost groups."""
    conn = op.get_bind()
    conn.execute(
        sa.text(
            "DELETE FROM din276_cost_groups WHERE code IN (:c1,:c2,:c3,:c4,:c5,:c6,:c7)"
        ),
        {"c1": '100', 'c2': '200', 'c3': '300', 'c4': '400', 'c5': '500', 'c6': '600', 'c7': '700'},
    )
