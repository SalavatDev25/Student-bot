from aiogram import Bot
from dependency_injector import containers, providers

from app.infrastructure.db import SessionContext, Database
from app.repositories.uow import UnitOfWork
from app.settings import Settings
from app.use_case.create_statement import CreateStatementUseCase
from app.utils.converter import MessageFormatter
from app.view.get_departament import GetDepartamentView
from app.view.get_statement import GetStatementView


class WebAppContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["app.telegram", __name__])
    config = providers.Configuration()

    settings = providers.Singleton(Settings)
    bot = providers.Singleton(Bot, token=settings.provided.telegram.bot_token)

    # db
    database: providers.Provider[Database] = providers.Singleton(
        Database, settings.provided.database
    )
    session_context: providers.Provider[SessionContext] = providers.Factory(
        SessionContext
    )

    unit_of_work: providers.ContextLocalSingleton[
        UnitOfWork
    ] = providers.ContextLocalSingleton(
        UnitOfWork, session_context=session_context, database=database
    )

    message_formatter: providers.Singleton[MessageFormatter] = providers.Singleton(
        MessageFormatter
    )

    # use case
    create_statement_use_case: providers.Factory[
        CreateStatementUseCase
    ] = providers.Factory(
        CreateStatementUseCase,
        formatter=message_formatter,
        uow=unit_of_work,
    )

    # view
    get_departament_view: providers.Factory[GetDepartamentView] = providers.Factory(
        GetDepartamentView,
        uow=unit_of_work,
    )
    get_statement_view: providers.Factory[GetStatementView] = providers.Factory(
        GetStatementView,
        uow=unit_of_work,
    )
