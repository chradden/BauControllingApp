"""add din276 level-3 subgroups

Revision ID: c7d8e9f0a1b2
Revises: b4c5d6e7a1b2
Create Date: 2025-11-06 20:35:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c7d8e9f0a1b2'
down_revision: Union[str, Sequence[str], None] = 'b4c5d6e7a1b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Insert DIN276 level-3 subgroups and link to level-2 parents."""
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
                'id': 16,
                'code': '300.2.1',
                'name': 'Innenwände - Trockenbau/Stein',
                'description': 'Innenwände, Trennwände, nicht-tragend',
                'parent_id': 11,  # 300.2 (Rohbau)
                'level': 3,
            },
            {
                'id': 17,
                'code': '300.2.2',
                'name': 'Außenwände - Verblendung/Isolation',
                'description': 'Außenwandaufbauten, Wärmeverbundsysteme',
                'parent_id': 11,
                'level': 3,
            },
            {
                'id': 18,
                'code': '300.3.1',
                'name': 'Dacheindeckung - Material',
                'description': 'Dacheindeckung, Abdichtung, Unterkonstruktion',
                'parent_id': 12,  # 300.3 (Dach)
                'level': 3,
            },
            {
                'id': 19,
                'code': '400.3.1',
                'name': 'Beleuchtung',
                'description': 'Allgemeinbeleuchtung, Notbeleuchtung',
                'parent_id': 15,  # 400.3 (Elektro)
                'level': 3,
            },
            {
                'id': 20,
                'code': '400.3.2',
                'name': 'Stromversorgung & Verteiler',
                'description': 'Versorgungsleitungen, Hauptverteiler',
                'parent_id': 15,
                'level': 3,
            },
            {
                'id': 21,
                'code': '100.1.1',
                'name': 'Anschluss- und Erschließungskosten',
                'description': 'Anschlussleitungen, Aufschließungskosten',
                'parent_id': 8,  # 100.1 (Grundstückskosten)
                'level': 3,
            },
            {
                'id': 22,
                'code': '200.1.1',
                'name': 'Genehmigungsplanung',
                'description': 'Genehmigungen, Baugenehmigungen, Behördenwege',
                'parent_id': 9,  # 200.1 (Planung & Voruntersuchungen)
                'level': 3,
            },
        ],
    )


def downgrade() -> None:
    """Remove the inserted level-3 subgroups."""
    conn = op.get_bind()
    conn.execute(
        sa.text(
            "DELETE FROM din276_cost_groups WHERE code IN (:a,:b,:c,:d,:e,:f,:g)"
        ),
        {
            'a': '300.2.1',
            'b': '300.2.2',
            'c': '300.3.1',
            'd': '400.3.1',
            'e': '400.3.2',
            'f': '100.1.1',
            'g': '200.1.1',
        },
    )
