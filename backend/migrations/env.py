from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from app.models import Base
# Import all model modules so the metadata is populated for autogenerate
import app.models.project
import app.models.contract
import app.models.invoice
import app.models.user
import app.models.din276
import app.models.budget
import app.models.audit
import app.models.contract_cost
import app.models.invoice_line
import app.models.approval
import app.models.funding
from app.core.config import settings

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

def get_url():
    """Get database URL from settings"""
    # Prefer the configured DATABASE_URL (loaded via pydantic Settings).
    # If the app uses an async driver (e.g. postgresql+asyncpg) we convert it
    # to the sync driver expected by Alembic's Engine (postgresql+psycopg2).
    url = getattr(settings, "DATABASE_URL", None)
    if not url:
        # fallback to a short-lived sqlite file for offline/autogenerate
        return "sqlite:///./alembic_tmp.db"

    # If using SQLAlchemy async URL with asyncpg, Alembic's sync engine
    # needs a sync driver like psycopg2. Convert it automatically.
    if url.startswith("postgresql+asyncpg"):
        url = url.replace("+asyncpg", "+psycopg2")

    return url


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.
    """
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = get_url()
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
