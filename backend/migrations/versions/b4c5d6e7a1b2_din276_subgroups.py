"""add din276 subgroups

Revision ID: b4c5d6e7a1b2
Revises: ae3b1d2c3f4e
Create Date: 2025-11-06 20:20:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4c5d6e7a1b2'
down_revision: Union[str, Sequence[str], None] = 'ae3b1d2c3f4e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Insert finer DIN276 subgroups and link to parents."""
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
                'id': 8,
                'code': '100.1',
                'name': 'Grundstückskosten',
                'description': 'Kaufpreis, Vermessung, Erschließungskosten (Untergruppe 100)',
                'parent_id': 1,
                'level': 2,
            },
            {
                'id': 9,
                'code': '200.1',
                'name': 'Planung & Voruntersuchungen',
                'description': 'Architektur, Fachplanung, Gutachten (Untergruppe 200)',
                'parent_id': 2,
                'level': 2,
            },
            {
                'id': 10,
                'code': '300.1',
                'name': 'Gründung',
                'description': 'Fundamente, Pfähle, Bodenverbesserung',
                'parent_id': 3,
                'level': 2,
            },
            {
                'id': 11,
                'code': '300.2',
                'name': 'Rohbau',
                'description': 'Wände, Decken, Stützen, Betonarbeiten',
                'parent_id': 3,
                'level': 2,
            },
            {
                'id': 12,
                'code': '300.3',
                'name': 'Dach',
                'description': 'Dacheindeckung, Dachkonstruktion',
                'parent_id': 3,
                'level': 2,
            },
            {
                'id': 13,
                'code': '400.1',
                'name': 'Heizung',
                'description': 'Heizungsanlage und Verteilung',
                'parent_id': 4,
                'level': 2,
            },
            {
                'id': 14,
                'code': '400.2',
                'name': 'Sanitär',
                'description': 'Sanitärinstallationen, Abwasser',
                'parent_id': 4,
                'level': 2,
            },
            {
                'id': 15,
                'code': '400.3',
                'name': 'Elektro',
                'description': 'Elektroinstallation, Verteiler, Leitungen',
                'parent_id': 4,
                'level': 2,
            },
        ],
    )


def downgrade() -> None:
    """Remove the DIN276 subgroups added in upgrade."""
    conn = op.get_bind()
    conn.execute(
        sa.text(
            "DELETE FROM din276_cost_groups WHERE code IN (:a,:b,:c,:d,:e,:f,:g,:h)"
        ),
        {
            'a': '100.1',
            'b': '200.1',
            'c': '300.1',
            'd': '300.2',
            'e': '300.3',
            'f': '400.1',
            'g': '400.2',
            'h': '400.3',
        },
    )
